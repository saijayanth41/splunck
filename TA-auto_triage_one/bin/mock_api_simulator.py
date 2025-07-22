from flask import Flask, request, jsonify
import random
import time
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

#  Configurable test behavior
SIMULATED_LATENCY_MS = (100, 500)  # Between 100ms and 500ms
FAILURE_RATE = 0.2  # 20% of requests fail

@app.route('/mock/incident', methods=['POST'])
def create_mock_ticket():
    start_time = time.time() * 1000
    payload = request.get_json()

    # Simulate processing delay
    delay = random.randint(*SIMULATED_LATENCY_MS) / 1000
    time.sleep(delay)

    # Simulate occasional failure
    if random.random() < FAILURE_RATE:
        logging.warning("Simulated 503 Service Unavailable")
        return jsonify({"error": "Service temporarily unavailable"}), 503

    # Simulated successful response
    ticket_id = f"MOCK-{random.randint(100000, 999999)}"
    processing_time = round(time.time() * 1000 - start_time)

    response = {
        "ticket_id": ticket_id,
        "status": "created",
        "processing_time_ms": processing_time
    }
    logging.info(f"Mock ticket created: {response}")
    return jsonify(response), 201

if __name__ == '__main__':
    print("Mock API server running on http://localhost:5000/mock/incident")
    app.run(port=5000)
