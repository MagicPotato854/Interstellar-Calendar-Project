from vercel_wsgi import handle_wsgi
from api.index import app

def handler(event, context):
    return handle_wsgi(event, context, app)
