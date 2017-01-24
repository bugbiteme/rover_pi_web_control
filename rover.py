import web
import RPi.GPIO as GPIO 
from web import form
import time

PIN_IN1 = 8
PIN_IN2 = 10
PIN_IN3 = 24
PIN_IN4 = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## setting GPIO pin numbering to Board format
#GPIO.setup(7, GPIO.OUT) ## Setting GPIO Pin 7 to Output mode

#  Motor 1
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)

# Motor 2
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)

#Defining the index page
urls = ('/', 'index')
render = web.template.render('templates') #index.html is stored in '/templates' folder
app = web.application(urls, globals())

""" Defining the buttons. 'id' stands for HTML id of the element. 'value' is the value of the button as perceived by Python. 'html' is the text displayed in HTML page. 'class_' is HTML class"""
my_form = form.Form(
 form.Button("btn", id="btnR", value="forward", html="forward", class_="forward"),
 form.Button("btn", id="btnG", value="stop", html="stop", class_="stop"),
 form.Button("btn", id="btnG", value="reverse", html="reverse", class_="reverse"),
 form.Button("btn", id="btnG", value="left", html="left", class_="left"),
 form.Button("btn", id="btnG", value="right", html="right", class_="right"),
 
)

# define the task of index page
class index:
    # rendering the HTML page
    def GET(self):
        form = my_form()
        return render.index(form, "Raspberry Pi Motor Control")

    # posting the data from the webpage to Pi
    def POST(self):
        # get the data submitted from the web form
        userData = web.input()
        if userData.btn == "forward":
            GPIO.output(PIN_IN1, True)
            GPIO.output(PIN_IN2, False)
            
            GPIO.output(PIN_IN3, True)
            GPIO.output(PIN_IN4, False)
            print "MOVING FORWARD"  #prints the status in Pi's Terminal
        elif userData.btn == "stop":
            
            GPIO.output(PIN_IN1, False)
            GPIO.output(PIN_IN2, False)
            
            GPIO.output(PIN_IN3, False)
            GPIO.output(PIN_IN4, False)
            print "STOP" #prints the status in Pi's Terminal
        elif userData.btn == "reverse":
            
            GPIO.output(PIN_IN1, False)
            GPIO.output(PIN_IN2, True)
            
            GPIO.output(PIN_IN3, False)
            GPIO.output(PIN_IN4, True)
            print "REVERSE" #prints the status in Pi's Terminal
            
        elif userData.btn == "right":
            
            GPIO.output(PIN_IN1, True)
            GPIO.output(PIN_IN2, False)
            
            GPIO.output(PIN_IN3, False)
            GPIO.output(PIN_IN4, True)
            print "RIGHT" #prints the status in Pi's Terminal
        elif userData.btn == "left":
            
            GPIO.output(PIN_IN1, False)
            GPIO.output(PIN_IN2, True)
            
            GPIO.output(PIN_IN3, True)
            GPIO.output(PIN_IN4, False)
            print "RIGHT" #prints the status in Pi's Terminal
        raise web.seeother('/')
# run
if __name__ == '__main__':
    app.run()

