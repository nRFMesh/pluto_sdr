import time
import json
import os
from array import array

prm = json.load(open("../config.json"))

os.system(f'iio_attr -q -u "{prm["uri"]}" -c ad9361-phy altvoltage0 frequency {prm["frequency"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 rf_bandwidth {prm["rf_bandwidth"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 sampling_frequency {prm["sampling_frequency"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 gain_control_mode {prm["gain_control_mode"]}')

tmp_file_name = "../"+prm["capture_file"]+".tmp"

print("Start Capture")
start = time.time()
os.system(f'iio_readdev -u "{prm["uri"]}" -b {prm["buffer_size"]} -s {prm["nb_samples"]} cf-ad9361-lpc > {tmp_file_name}')
capture_time = round((time.time() - start) * 1000)
print(f"Capture finish in {capture_time} ms")

print(f"converting file {tmp_file_name}")
input_file = open(tmp_file_name, 'rb')

short_array = array('h')
short_array.fromstring(input_file.read())
input_file.close()
print("loaded %d shorts"%(len(short_array)))
os.system("rm "+tmp_file_name)
#print(f"({short_array[0]} , {short_array[1]}),")

output_file = open("../"+prm["capture_file"], 'wb')
float_array = array('f', short_array)
print("converting %d floats"%(len(float_array)))
#print(f"({float_array[0]} , {float_array[1]}),")
float_array.tofile(output_file)
output_file.close()
