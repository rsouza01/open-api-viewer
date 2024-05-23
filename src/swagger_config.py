swagger_template ={
    "swagger": "2.0",
    "info": {
      "title": "Open API Viewer",
      "description": "Open API Viewer Script",
      "contact": {
        "name": "Rodrigo",
        "email": "rsouza01@gmail.com",
        "url": "https://www.rodrigosouza.net.br",
        },
      "termsOfService": "Terms of services",
      "version": "1.0",
      "host":"",
      "basePath":"http://localhost:5000",
      "license":{
        "name":"MIT",
        "url":"https://opensource.org/license/mit"
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
            "endpoint": 'Open_API_Viewer',
            "route": '/Open_API_Viewer.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/",
}
