import time
import random
import logging

class RetryManager:
    def __init__(self, max_retries=5, base_delay=1.0, max_delay=60.0, failure_threshold=3):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.failure_threshold = failure_threshold
        self.failure_count = 0
        self.circuit_open = False

    def exponential_backoff(self, attempt):
        delay = min(self.base_delay * (2 ** attempt) + random.uniform(0, 1), self.max_delay)
        return delay

    def execute_with_retry(self, func):
        retries = 0
        last_exception = None

        if self.circuit_open:
            logging.warning("Circuit breaker is OPEN. Aborting execution.")
            raise Exception("Circuit breaker is open. Skipping execution.")

        while retries < self.max_retries:
            try:
                result = func()
                self.failure_count = 0  # Reset on success
                return result, retries
            except Exception as e:
                retries += 1
                last_exception = e
                self.failure_count += 1
                logging.warning(f"Attempt {retries}/{self.max_retries} failed: {e}")

                if self.failure_count >= self.failure_threshold:
                    self.circuit_open = True
                    logging.error("Circuit breaker TRIGGERED after repeated failures.")
                    break

                delay = self.exponential_backoff(retries)
                logging.info(f"Retrying after {delay:.2f}s...")
                time.sleep(delay)

        raise last_exception


# Test the retry logic
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    state = {"attempt_counter": 0}

    def flaky_function():
        state["attempt_counter"] += 1
        if state["attempt_counter"] < 3:
            raise Exception("Simulated failure")
        return {"ticket_id": "MOCK-123456", "processing_time_ms": 250}

    retry_manager = RetryManager(max_retries=5)
    try:
        result, attempts = retry_manager.execute_with_retry(flaky_function)
        logging.info(f"Success after {attempts} attempts: {result}")
    except Exception as e:
        logging.error(f"Final failure: {str(e)}")
