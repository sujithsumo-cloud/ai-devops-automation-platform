from werkzeug.serving import make_server
from main import app

server = make_server("0.0.0.0", 5000, app)

print("AI DevOps Docker server is running on port 5000", flush=True)

server.serve_forever()
