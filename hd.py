from gpiozero import LED
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer


Button1 = LED(4, active_high=False)
ButtonDown = LED(6, active_high=False)
ButtonUp = LED(5, active_high=False)

def ButtonSetup():
  Button1.off()
  ButtonDown.off()
  ButtonUp.off()

def Group1Down(): # tell Group1 to go down using Radio Control
  # activate group 1
  Button1.on()
  sleep(1)
  Button1.off()
  sleep(1)
  ButtonDown.on()
  sleep(2)
  ButtonDown.off()
  # wait a long time so the motion can finish
  sleep(10)
  
def Group1Up(): # tell Group1 to go Up using Radio Control
  # activate group 1
  Button1.on()
  sleep(1)
  Button1.off()
  sleep(1)
  ButtonUp.on()
  sleep(2)
  ButtonUp.off()
  # wait a long time so the motion can finish
  sleep(10)


# HTTPRequestHandler class
class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):
   
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        if self.path=="up":
            message = "up"
            self.wfile.write(bytes(message, "utf8"))
            Group1Up()
        elif self.path=="down":
            message = "down"
            self.wfile.write(bytes(message, "utf8"))
            Group1Down()
        else:
            message = "unknown"
            self.wfile.write(bytes(message, "utf8"))
 
        return

def runHTTP():
    print("Starting HTTP server...")
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("Server started...")
    httpd.serve_forever()
    

ButtonSetup()
runHTTP()