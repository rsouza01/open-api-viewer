swagger_template ={
    "swagger": "2.0",
    "info": {
      "title": "Wine Quality Prediction",
      "description": "API Documentation for Wine Quality Prediction",
      "contact": {
        "name": "Admin",
        "email": "dinithi@axiatadigitallabs.com",
        "url": "http://www.axiatadigitallabs.com",
        },
      "termsOfService": "Terms of services",
      "version": "1.0",
      "host":"Wine_Quality_Prediction",
      "basePath":"http://localhost:5000",
      "license":{
        "name":"License of API",
        "url":"API license URL"
      }
              },
    "schemes": [
        "http",
        "https"
    ],
      }

swagger_config = {
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST"),
    ],
    "specs": [
        {
            "endpoint": 'Wine_Quality_Prediction',
            "route": '/Wine_Quality_Prediction.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",
    
}
