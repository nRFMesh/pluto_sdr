#!/bin/sh

# the default directory the script runs in is /dev
cd /root

# create a file in the ram file system
touch capture.dat
touch capture.info


#switch off the led for 1 sec to make sure the capture pulse is visible off->on->off
echo 0 > /sys/class/leds/led0\:green/brightness
sleep 1

#configure the capture parameters
iio_attr -q -u "local:" -c ad9361-phy altvoltage0 frequency 2402000000
iio_attr -q -i -u "local:" -c ad9361-phy voltage0 rf_bandwidth 2000000
iio_attr -q -i -u "local:" -c ad9361-phy voltage0 sampling_frequency 10000000
iio_attr -q -i -u "local:" -c ad9361-phy voltage0 gain_control_mode fast_attack

echo 1 > /sys/class/leds/led0\:green/brightness
echo "capture start @ $(date +"%T")" > capture.info

#capture command
iio_readdev -b 1048576 -s 1000000 cf-ad9361-lpc > capture.dat

echo 0 > /sys/class/leds/led0\:green/brightness
echo "capture stop @ $(date +"%T")" >> capture.info

#leave an off break of 1 sec to space the capture and the copy on pulses
echo 0 > /sys/class/leds/led0\:green/brightness
sleep 1
echo 1 > /sys/class/leds/led0\:green/brightness

echo "copy start @ $(date +"%T")" >> capture.info

mv /root/capture.dat /media/sda1/capture.dat

echo 0 > /sys/class/leds/led0\:green/brightness
echo "copy stop @ $(date +"%T")" >> capture.info

#move the info file only after it is updated with the copy stop time
mv /root/capture.info /media/sda1/capture.info

#unmount
ACTION=remove_all /lib/mdev/automounter.sh
