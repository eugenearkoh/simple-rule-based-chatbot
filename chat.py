import json
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from chatbot import ObedAI

bot = ObedAI()

ROOT = Path(__file__).resolve().parent

class handler(BaseHTTPRequestHandler):

    def send_response_data(self, status, content, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        path = self.path.split("?")[0]

        files = {
            "/": "index.html",
            "/index.html": "index.html",
            "/style.css": "style.css",
            "/script.js": "script.js"
        }

        filename = files.get(path)

        if filename:
            try:
                content = (ROOT / filename).read_bytes()

                content_type = (
                    "text/html" if filename.endswith(".html")
                    else "text/css" if filename.endswith(".css")
                    else "application/javascript"
                )

                self.send_response_data(
                    200, content, content_type
                )
            except FileNotFoundError:
                self.send_response_data(
                    404, b"File not found", "text/plain"
                )
        elif path == "/api/chat":
            data = json.dumps({
                "success": True,
                "message": "OBED AI is online!"
            }).encode()

            self.send_response_data(
                200, data, "application/json"
            )
        else:
            self.send_response_data(
                404, b"Not found", "text/plain"
            )

    def do_POST(self):
        if self.path.split("?")[0] != "/api/chat":
            self.send_response_data(
                404, b"Not found", "text/plain"
            )
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            message = body.get("message", "").strip()

            if not message:
                raise ValueError("Message cannot be empty")

            if hasattr(bot, "get_response"):
                reply = bot.get_response(message)
            elif hasattr(bot, "respond"):
                reply = bot.respond(message)
            elif hasattr(bot, "chat"):
                reply = bot.chat(message)
            else:
                raise AttributeError(
                    "No recognized response method in ObedAI"
                )

            response = json.dumps({
                "success": True,
                "reply": str(reply)
            }).encode()

            self.send_response_data(
                200, response, "application/json"
            )

        except Exception as error:
            response = json.dumps({
                "success": False,
                "error": str(error)
            }).encode()

            self.send_response_data(
                500, response, "application/json"
            )
