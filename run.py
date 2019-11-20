import os
import random

from quote import quote

backend_url = os.getenv("BACKEND_URL", "ya.ru")


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    url = '<h1>Hello, world!</h1><div>BACKEND_URL: {0}</div><hr>'.format(backend_url)

    citations = ""
    authors = ["pushkin", "chekhov", "lermontov", "azimov", "pasternak", "bulgakov", "lenin", "strugatsky", "gumilyov",
               "akhmatova"]
    for q in quote(random.choice(authors), limit=5):
        citations += "<p>{0}: {1}</p>".format(q["author"], q["quote"])
    return [url.encode('utf-8'), citations.encode('utf-8')]


app = hello_world
port = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    print("Starting server on port %s..." % port)
    from wsgiref.simple_server import make_server

    httpd = make_server('', port, app)
    httpd.serve_forever()
