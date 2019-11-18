# Citatos

[![image size](https://img.shields.io/badge/image%20size-336MB-blue.svg)](https://hub.docker.com/r/maslick/citatos)

### Using dummy wsgi server (BaseHTTPServer):
```
pip3 install -r requirements.txt
python3 run.py
open http://localhost:8000
```

### Using gunicorn:
```
pip3 install -r requirements.txt
gunicorn run:app -c gunicorn.config.py
open http://localhost:5000
```

### Docker:
```
docker build . -t citatos
docker run -d -p 8080:5000 -e BACKEND_URL=goo.gl citatos
open http://`docker-machine ip`:8080
```

```
docker run -d -p 8081:5000 -e BACKEND_URL=maslick.io maslick/citatos
open http://`docker-machine ip`:8081
```

### k8s:
```
kubectl apply -f k8s
k set env deploy citatos BACKEND_URL=www.goog.li
open http://citatos.maslick.ru
```