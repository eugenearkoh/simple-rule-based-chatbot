import json
from http.server import BaseHTTPRequestHandler
from chatbot import ObedAI


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(
            json.dumps({
                "success": True,
                "message": "OBED AI is online!"
            }).encode()
        )

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))

            if length <= 0 or length > 10000:
                raise ValueError("Invalid message size")

            data = json.loads(
                self.rfile.read(length).decode("utf-8")
            )

            message = data.get("message", "")

            if not isinstance(message, str) or not message.strip():
                raise ValueError("Please enter a message.")

            chatbot = ObedAI()
            reply = chatbot.get_response(message)

            response = {
                "success": True,
                "reply": reply
            }

            self.send_response(200)

        except (ValueError, json.JSONDecodeError) as error:
            response = {
                "success": False,
                "error": str(error)
            }
            self.send_response(400)

        except Exception:
            response = {
                "success": False,
                "error": "Something went wrong."
            }
            self.send_response(500)

        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(response, ensure_ascii=False).encode("utf-8")
        )
