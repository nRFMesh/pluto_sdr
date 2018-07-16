REM ssh-keygen -R 192.168.2.1
scp ./target.sh root@192.168.2.1:/root
ssh root@192.168.2.1

cd /root
chmod a+x target.sh
./target.sh

scp root@192.168.2.1:/root/capture.iq16 .

scp root@192.168.2.1:/root/capture.info .


