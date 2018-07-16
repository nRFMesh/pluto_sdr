from array import array

input_file = open('capture.iq16', 'rb')
short_array = array('i')
short_array.fromstring(input_file.read())

print("loaded %d shorts"%(len(short_array)))

output_file = open('capture.complex', 'wb')
float_array = array('f', short_array)
float_array.tofile(output_file)
output_file.close()
