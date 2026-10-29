from werkzeug.serving import make_server
from main import app

server = make_server("127.0.0.1", 5000, app)

print("AI DevOps application server is running at http://127.0.0.1:5000", flush=True)

server.serve_forever()
