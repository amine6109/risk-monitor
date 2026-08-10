import logging

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from risk import calculate_pnl, calculate_exposure, calculate_var

logging.basicConfig(
    filename="../logs/application.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)
class RiskMonitorHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        logger.info("Received GET request: %s", self.path)

        if self.path == "/health":
            response = {
                "status": "UP"
            }

        elif self.path == "/risk":

            price = 1.10
            initial_price = 1.08
            quantity = 1_000_000
            volatility = 0.02

            pnl = calculate_pnl(
                price,
                initial_price,
                quantity
            )

            exposure = calculate_exposure(
                price,
                quantity
            )

            var = calculate_var(
                exposure,
                volatility
            )
            logger.info(
                "Risk calculated: instrument=EURUSD pnl=%s exposure=%s var=%s",
                pnl,
                exposure,
                var
            )

            response = {
                "instrument": "EURUSD",
                "pnl": pnl,
                "exposure": exposure,
                "var": var
            }

        else:
            logger.warning(
                "Unknown endpoint requested: %s",
                self.path
            )

            response = {
                "error": "Endpoint not found"
            }

        body = json.dumps(response).encode()

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json"
        )
        self.send_header(
            "Content-Length",
            str(len(body))
        )
        self.end_headers()

        self.wfile.write(body)


server = HTTPServer(
    ("0.0.0.0", 8080),
    RiskMonitorHandler
)

logger.info("RiskMonitor started on port 8080")

server.serve_forever()