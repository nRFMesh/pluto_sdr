from array import array
import json
import os

prm = json.load(open("params.json"))

#output from the capture is used as input for the conversion
input_file = open(prm["out_file"], 'rb')
filename, file_extension = os.path.splitext(prm["out_file"])
print(file_extension)
if(file_extension == '.iq16'):
    short_array = array('h')
elif(file_extension == '.iq8'):
    short_array = array('B')

short_array.fromstring(input_file.read())
input_file.close()

print("loaded %d shorts"%(len(short_array)))

#output of the conversion is the conv file
output_file = open(prm["conv_file"], 'wb')
float_array = array('f', short_array)
print("converting %d floats"%(len(float_array)))
float_array.tofile(output_file)
output_file.close()
