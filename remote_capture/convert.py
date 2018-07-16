import time
import json
import os
from array import array

input_filename = "../capture.iq16"

print(f"converting file {input_filename}")
input_file = open(input_filename, 'rb')

short_array = array('h')
short_array.fromstring(input_file.read())
input_file.close()
print("loaded %d shorts"%(len(short_array)))
#print(f"({short_array[0]} , {short_array[1]}),")

output_file = open("../capture.iqf32", 'wb')
float_array = array('f', short_array)
print("converting %d floats"%(len(float_array)))
#print(f"({float_array[0]} , {float_array[1]}),")
float_array.tofile(output_file)
output_file.close()
