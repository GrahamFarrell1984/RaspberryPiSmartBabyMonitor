# {"Publish": True}
# {"Publish": False}
# {"Terminate": True}
# {"Terminate": False}

import grovepi # Import the grovepi module
from grovepi import * # Import everything from the grovepi module
import paho.mqtt.client as mqtt
import time
from threading import Thread # Import the Thread class from the threading module
import json

BROKER_ADDRESS = "broker.mqttdashboard.com"
LISTEN_CLIENT_ID = "clientId-6y4TIkvtpM"
PUBLISH_CLIENT_ID = "clientId-B8UdQna4HB"

publishing = False

# dht_sensor = 7 # Connect the DHT sensor to digital port D7
# dht_sensor_type = 0 # Use 0 for the blue-colored sensor
#
light_sensor = 0 # Connect the Grove Light Sensor to analog port A0
grovepi.pinMode(light_sensor,"INPUT") # Set pin mode for port A0 as an input

sound_sensor = 1 # Connect the Grove Sound Sensor to analog port A1
grovepi.pinMode(sound_sensor,"INPUT") # Set pin mode for port A1 as an input

# pir_sensor = 8 # Connect the Grove PIR Motion Sensor to digital port D8
# grovepi.pinMode(pir_sensor,"INPUT") # Set pin mode for port D8 as an input

# Functions / Methods

# Method to read from temperature sensor
def read_temperature():
    # [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
    # temperature = str(temp_sensor_value) # Convert temperature sensor value to a String and store in a variable called temperature
    # return temperature # Return the temperature value from the dht sensor
    return 10

# Method to read from humidity sensor
def read_humidity():
    # [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
    # humidity = str(hum_sensor_value) # Convert humidity sensor value to a String and store in a variable called humidity
    # return humidity # Return the humidity value from the dht sensor
    return 20

# Method to read from light sensor
def read_light():
    light_sensor_value = grovepi.analogRead(light_sensor) # Read the light sensor value and store it in a variable called light_sensor_value
    return light_sensor_value # Return the value from the light sensor
    # return 30

# Method to read from sound sensor
def read_sound():
    sound_sensor_value = grovepi.analogRead(sound_sensor) # Read the sound sensor value and store it in a variable called sound_sensor_value
    return sound_sensor_value # Return the value from the sound sensor
    # return 40

# Method to read from pir sensor
def read_pir():
    # pir_sensor_value = grovepi.digitalRead(pir_sensor) # Read the pir sensor value and store it in a variable called pir_sensor_value
    # return pir_sensor_value # Return the value from the pir sensor
    return 1

# Method to read from temperature sensor
# def read_temperature():
#     [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
#     temperature = str(temp_sensor_value) # Convert temperature sensor value to a String and store in a variable called temperature
#     return temperature # Return the temperature value from the dht sensor
#
# # Method to read from humidity sensor
# def read_humidity():
#     [ temp_sensor_value, hum_sensor_value ] = dht(dht_sensor, dht_sensor_type) # Read the temperature and humidity sensor values
#     humidity = str(hum_sensor_value) # Convert humidity sensor value to a String and store in a variable called humidity
#     return humidity # Return the humidity value from the dht sensor

# Method to read from light sensor
# def read_light():
#     light_sensor_value = grovepi.analogRead(light_sensor) # Read the light sensor value and store it in a variable called light_sensor_value
#     return light_sensor_value # Return the value from the light sensor

# # Method to read from sound sensor
# def read_sound():
#     sound_sensor_value = grovepi.analogRead(sound_sensor) # Read the sound sensor value and store it in a variable called sound_sensor_value
#     return sound_sensor_value # Return the value from the sound sensor
#
# # Method to read from pir sensor
# def read_pir():
#     pir_sensor_value = grovepi.digitalRead(pir_sensor) # Read the pir sensor value and store it in a variable called pir_sensor_value
#     return pir_sensor_value # Return the value from the pir sensor

def on_message(client, userdata, message):
    print("Message received!")
    global publishing # Setting the publishing variable as global here gives access to the publishing variable on line 10
    string_message = str(message.payload.decode('utf-8'))
    print("Message received: " + string_message)
    if string_message == '{"Publish": True}':
        publishing = True
        print(publishing)
    publish(publishing)

def publish(publish):
    print("Publish method called!")
    counter = 0
    client = start_client(PUBLISH_CLIENT_ID)
    while publish:
        print(publishing)
        counter += 1
        print("Publishing!")
        temperature = read_temperature() # Call the read_temperature() function / method and store result in a variable called temperature
        humidity = read_humidity() # Call the read_humidity() function / method and store result in a variable called humidity
        light = read_light() # Call the read_light() function / method and store result in a variable called light
        sound = read_sound() # Call the read_sound() function / method and store result in a variable called sound
        motion = read_pir() # Call the read_pir() function / method and store result in a variable called motion
        print("While loop has run " + str(counter) + " times" if counter > 1 else "While loop has run " + str(counter) + " time")
        print("Temperature: " + str(temperature))
        print("Humidity: " + str(humidity))
        print("Light: " + str(light))
        print("Sound: " + str(sound))
        print("Motion detected" if motion else "No motion detected")
        readings = {
            'temperature': temperature,
            'humidity': humidity,
            'light': light,
            'sound': sound,
            'motion': motion
        }
        client.publish("GFNCI/PUBLISH", json.dumps(readings))
        time.sleep(1)

def start_client(client_id):
    client = mqtt.Client(client_id)
    client.connect(BROKER_ADDRESS)
    client.on_message = on_message
    return client

def listen(publisher_thread):
    print("Listen method called!")
    client = start_client(LISTEN_CLIENT_ID)
    client.subscribe("GFNCI/LISTEN")
    while True:
        client.loop_start()

def main_method():
    try:
        print("Main method called!")
        publisher_thread = Thread(target=publish) # Create a new publisher thread passing in the publish() method as a parameter
        listener_thread = Thread(target=listen, args=(publisher_thread,)) # Create a new listener thread passing in the listen() method and publisher_thread
        listener_thread.start() # Start listener thread
    except Exception as e:
        print("Main method not called!")

if __name__ == '__main__':
    try:
        main_method() # Call the main_method()
    except KeyboardInterrupt:
        sys.exit(0)
