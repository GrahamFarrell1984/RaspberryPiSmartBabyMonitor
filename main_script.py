import grovepi # Import the grovepi module
from grovepi import * # Import everything from the grovepi module
import dweepy # Import the dweepy module
from threading import Thread # Import the Thread class from the threading module
import time # Import the time module

from config import thingName # Import thingName from the config.py configuration file

dht_sensor = 7 # Connect the DHT sensor to digital port D7
dht_sensor_type = 0 # Use 0 for the blue-colored sensor

light_sensor = 0 # Connect the Grove Light Sensor to analog port A0
grovepi.pinMode(light_sensor,"INPUT") # Set pin mode for port A0 as an input

sound_sensor = 1 # Connect the Grove Sound Sensor to analog port A1
grovepi.pinMode(sound_sensor,"INPUT") # Set pin mode for port A1 as an input

pir_sensor = 8 # Connect the Grove PIR Motion Sensor to digital port D8
grovepi.pinMode(pir_sensor,"INPUT") # Set pin mode for port D8 as an input

# Functions / Methods

# Method to read from temperature sensor
def read_temperature():
    [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
    temperature = str(temp_sensor_value) # Convert temperature sensor value to a String and store in a variable called temperature
    return temperature # Return the temperature value from the dht sensor

# Method to read from humidity sensor
def read_humidity():
    [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
    humidity = str(hum_sensor_value) # Convert humidity sensor value to a String and store in a variable called humidity
    return humidity # Return the humidity value from the dht sensor

# Method to read from light sensor
def read_light():
    light_sensor_value = grovepi.analogRead(light_sensor) # Read the light sensor value and store it in a variable called light_sensor_value
    return light_sensor_value # Return the value from the light sensor

# Method to read from sound sensor
def read_sound():
    sound_sensor_value = grovepi.analogRead(sound_sensor) # Read the sound sensor value and store it in a variable called sound_sensor_value
    return sound_sensor_value # Return the value from the sound sensor

# Method to read from pir sensor
def read_pir():
    pir_sensor_value = grovepi.digitalRead(pir_sensor) # Read the pir sensor value and store it in a variable called pir_sensor_value
    return pir_sensor_value # Return the value from the pir sensor

try:
    counter = 0
    while True:
        counter += 1
        temperature = read_temperature() # Call the read_temperature() function / method and store result in a variable called temperature
        humidity = read_humidity() # Call the read_humidity() function / method and store result in a variable called humidity
        light = read_light() # Call the read_light() function / method and store result in a variable called light
        sound = read_sound() # Call the read_sound() function / method and store result in a variable called sound
        motion = read_pir() # Call the read_pir() function / method and store result in a variable called motion
        print("While loop has run " + str(counter) + " times" if counter > 1 else "While loop has run " + str(counter) + " time")
        print("Reading from: " + str(thingName))
        print("Temperature: " + str(temperature))
        print("Humidity: " + str(humidity))
        print("Light: " + str(light))
        print("Sound: " + str(sound))
        print("Motion detected" if motion else "No motion detected")
        time.sleep(2) # Call the sleep() method from the time module and pass in 2 second as a parameter
except Exception as e:
    print(e)

# Method to listen for dweets from a specific thing called Raspberry Pi Smart Baby Monitor
# def listen(publisher_thread): # The listen() method takes the publisher thread as a parameter
#     print(listener_thread_name + " is Listening!") # Print Starting Listening!
#     global publisher_state # Set publisher state as a global variable
#     publisher_state = True # Set publisher state to true
#     # global button_clicked
#     if not publisher_thread.is_alive(): # If publisher thread is not running execute the following code
#         publisher_thread.start() # Start publisher thread
#     for dweet in dweepy.listen_for_dweets_from(thingTwoName): # For loop listens for dweets from a specific thing called GrahamThingTwo
#         content = dweet["content"] # Store the content from each dweet into a variable called content
#         print(str(content)) # Print content
#         try:
#             button_clicked = content["ButtonClicked"]
#         except:
#             print("Button not clicked yet!")
#         thing = dweet["thing"] # Store the thing from each dweet into a variable called thing
#         print("Reading from " + str(thing) + ": " + str(content))
#         print("") # Adds an empty line in the terminal below our output above
#
#         # try:
#         #     if int(button_clicked) == 1: # Check if the button has been pressed
#         #         brightness = 255 # Set maximum brightness
#         #         grovepi.analogWrite(led,brightness) # Give PWM output to LED
#         #     else:
#         #         brightness = 0 # Set minimum brightness
#         #         grovepi.analogWrite(led,brightness) # Give PWM output to LED
#         # except:
#         #     print("Button still not clicked yet!")
#     print("Listening Ending!") # Print Listening Ending!

# # Method to publish dweets from a specific thing called Raspberry Pi Smart Baby Monitor
# def publish(): # The publish() method takes no parameters
#     print(publisher_thread_name + " is Publishing!") # Print Starting Publishing!
#     while True: # While true execute the following code
#     # while publisher_state: # While publisher state is true execute the following code
#         temperature = read_temperature() # Call the read_temperature() function / method and store result in a variable called temperature
#         humidity = read_humidity() # Call the read_humidity() function / method and store result in a variable called humidity
#         light = read_light() # Call the read_light() function / method and store result in a variable called light
#         sound = read_sound() # Call the read_sound() function / method and store result in a variable called sound
#         motion = read_pir() # Call the read_pir() function / method and store result in a variable called motion
#         result = dweepy.dweet_for(thingName, {"Temperature": temperature, "Humidity": humidity, "Light": light, "Sound": sound, "Motion": motion}) # Send a dweet from a specific thing called Raspberry Pi Smart Baby Monitor
#         print(str(thingName) + " published: " + str(result)) # Print the variable called result
#         time.sleep(2) # Call the sleep() method from the time module and pass in 2 second as a parameter
#         print("") # Adds an empty line in the terminal below our output above
#     print("Publishing Ending!") # Print Publishing Ending!
#
# publisher_thread = Thread(target=publish) # Create a new publisher thread passing in the publish() method as a parameter
# # listener_thread = Thread(target=listen, args=(publisher_thread,)) # Create a new listener thread passing in the listen() method and publisher_thread
#
# publisher_thread_name = publisher_thread.getName() # Get publisher thread name
# # listener_thread_name = listener_thread.getName() # Get listener thread name
#
# # listener_thread.start() # Start listener thread
# publisher_thread.start() # Start publisher thread
