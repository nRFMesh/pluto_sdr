import json
import os

prm = json.load(open("params.json"))

os.system(f'iio_attr -q -u "{prm["uri"]}" -c ad9361-phy altvoltage0 frequency {prm["frequency"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 rf_bandwidth {prm["rf_bandwidth"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 sampling_frequency {prm["sampling_frequency"]}')
os.system(f'iio_attr -q -i -u "{prm["uri"]}" -c ad9361-phy voltage0 gain_control_mode {prm["gain_control_mode"]}')

os.system(f'iio_readdev -u "{prm["uri"]}" -b {prm["buffer_size"]} -s {prm["nb_samples"]} cf-ad9361-lpc > {prm["out_file"]}')
