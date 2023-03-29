from email.headerregistry import ContentTypeHeader
from importlib.util import resolve_name
import json
import logging
import socket

import azure.functions as func


def main(req: func.HttpRequest, readdb: func.DocumentList, updatedb: func.Out[func.Document]) -> func.HttpResponse:
    client_ip = req.headers.get("X-Forwarded-For") or req.headers.get("X-Real-IP") or socket.gethostbyname(socket.gethostname())
    
    currentrow = readdb[0].data
    
    
    currentrow['count'] += 1
    updatedb.set(func.Document.from_dict(currentrow))
    
    # write to the cosmos DB the new count
    response = func.HttpResponse(
        body=json.dumps(currentrow),
        status_code=200,
        headers={'Content-Type':'application/json'}
    )   
    updatedb.set(func.Document.from_dict(currentrow))

    return response

 
