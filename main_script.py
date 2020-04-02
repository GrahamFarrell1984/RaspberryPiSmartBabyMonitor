import grovepi # Import the grovepi module
from grovepi import * # Import everything from the grovepi module
import time # Import the time module

from config import thingName # Import thingName from the config.py configuration file

dht_sensor = 7 # Connect the DHT sensor to digital port D7
dht_sensor_type = 0 # Use 0 for the blue-colored sensor

light_sensor = 0 # Connect the Grove Light Sensor to analog port A0
grovepi.pinMode(light_sensor,"INPUT") # Set pin mode for port A0 as an input

sound_sensor = 1 # Connect the Grove Sound Sensor to analog port A1
grovepi.pinMode(sound_sensor,"INPUT") # Set pin mode for port A1 as an input

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

while True:
    temperature = read_temperature() # Call the read_temperature() function / method and store result in a variable called temperature
    humidity = read_humidity() # Call the read_humidity() function / method and store result in a variable called humidity
    light = read_light() # Call the read_light() function / method and store result in a variable called light_sensor
    sound = read_sound() # Call the read_sound() function / method and store result in a variable called sound
    print("Reading from: " + str(thingName))
    print("Temperature: " + str(temperature))
    print("Humidity: " + str(humidity))
    print("Light: " + str(light))
    print("Sound: " + str(sound))
    time.sleep(1) # Call the sleep() method from the time module and pass in 1 second as a parameter
