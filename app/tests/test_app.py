import socket
import subprocess
import sys
import time
import unittest
from pathlib import Path


class AppStartupTest(unittest.TestCase):
    def test_app_starts_and_serves_requests(self):
        app_path = Path(__file__).resolve().parents[1] / "app.py"
        proc = subprocess.Popen(
            [sys.executable, str(app_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(app_path.parent),
        )

        try:
            time.sleep(2)
            self.assertIsNotNone(proc.poll(), "app.py should keep running when started")
            with socket.create_connection(("127.0.0.1", 5000), timeout=2):
                pass
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)


if __name__ == "__main__":
    unittest.main()
