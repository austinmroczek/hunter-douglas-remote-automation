from gpiozero import LED
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer


class HD():
    def __init__(self):
        self.isTraveling = False  # flag to ensure not triggering motion while already in motion
        self.isUp = False
        self.Button1 = LED(4, active_high=False)
        self.ButtonDown = LED(6, active_high=False)
        self.ButtonUp = LED(5, active_high=False)
        self.ButtonSetup()
        
    def ButtonSetup(self):
        self.Button1.off()
        self.ButtonDown.off()
        self.ButtonUp.off()

    def Group1Down(self): # tell Group1 to go down using Radio Control
        # returns an appropriate message

        if self.isUp == False: 
            return "Blinds are already down.  Doing nothing."
  
        if self.isTraveling == True:
            return "Blinds are already traveling.  Cannot take request."

        self.isTraveling = True
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
        self.isTraveling = False
        self.isUp = False
        return "Request accepted.  Blinds moved down."
  
    def Group1Up(): # tell Group1 to go Up using Radio Control

        if self.isUp == True: 
            return "Blinds are already up.  Doing nothing."
  
        if self.isTraveling == True:
            return "Blinds are already traveling.  Cannot take request."

        self.isTraveling = True 
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
        self.isTraveling = False
        self.isUp = True
        return "Request accepted.  Blinds moved up."

# HTTPRequestHandler class
class myHTTPServer_RequestHandler(BaseHTTPRequestHandler):
   
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        if self.path=="/up":
            message = myHD.Group1Up()
            self.wfile.write(bytes(message, "utf8"))
            
        elif self.path=="/down":
            message = myHD.Group1Down()
            self.wfile.write(bytes(message, "utf8"))
            
        else:
            message = "Error.  Bad URL/request"
            self.wfile.write(bytes(message, "utf8"))
 
        return

def runHTTP():
    print("Starting HTTP server...")
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, myHTTPServer_RequestHandler)
    print("Server started...")
    httpd.serve_forever()
    

myHD = HD()
runHTTP()