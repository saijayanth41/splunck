

## ** TECHNICAL ARCHITECTURE**

### **CORE PLATFORM SPECIFICATIONS**

```
 TA-AutoTriageOne-Supreme/
├──  bin/                              
│   ├──  alert_orchestrator.py        
│   ├──  universal_api_client.py      
│   ├──  payload_template_engine.py   
│   ├──  retry_circuit_breaker.py    
│   ├──  mock_api_simulator.py       
│   ├──  credential_manager.py       
│   ├──  metrics_collector.py        
│   ├──  test_harness.py             
│   └──  config_validator.py         
│
├──  default/                        
│   ├──  alert_actions.conf          
│   ├──  app.conf                     
│   ├──  inputs.conf                  
│   ├──  props.conf                   
│   ├──  transforms.conf              
│   ├──  macros.conf                  
│   ├──  savedsearches.conf           
│   ├──  collections.conf             
│   └──  server.conf                  
│
├──  appserver/                       
│   ├──  static/
│   │   ├──  css/
│   │   │   ├── auto_triage_main.css   
│   │   │   ├── dashboard_theme.css    
│   │   │   └── mobile_responsive.css  
│   │   ├──  js/
│   │   │   ├── config_wizard.js       
│   │   │   ├── template_builder.js    
│   │   │   ├── api_tester.js          
│   │   │   ├── dashboard_controller.js
│   │   │   └── validation_engine.js   
│   │   └──  images/
│   │       ├── logo_variants/         
│   │       ├── integration_icons/      
│   │       └── workflow_diagrams/      
│   │
│   └──  templates/                        
│       ├── setup_wizard.html           
│       ├── dashboard_template.html     
│       └── template_builder.html       
│
├──  default_ui/data/ui/                
│   ├──  views/
│   │   ├── auto_triage_dashboard.xml   
│   │   ├── performance_analytics.xml   
│   │   ├── error_analysis.xml          
│   │   ├── template_gallery.xml       
│   │   └── system_health.xml          
│   │
│   ├──  manager/
│   │   ├── auto_triage_endpoints.xml   
│   │   ├── template_management.xml     
│   │   ├── credential_storage.xml      
│   │   └── system_settings.xml        
│   │
│   └──  nav/
│       └── default.xml                
│
├──  lookups/                          
│   ├──  vendor_api_specs.csv        
│   ├──  priority_mappings.csv       
│   ├──  response_code_actions.csv   
│   ├──  tenant_configurations.csv   
│   └──  mock_response_templates.csv  
│
├── samples/                          
│   ├──  sample_searches/             
│   ├──  template_library/              
│   ├──  configuration_examples/      
│   └──  test_scenarios/              
│
├──  tests/                           
   ├──  unit_tests/                 
   ├──  integration_tests/          
   ├──  performance_tests/          
   ├──  security_tests/             
   └──  test_reports/               
```

---

