Freq=433000000
SampleRate=2500000
NbSamples=25000000
sudo rtl_sdr -f $Freq -g 0 -s $SampleRate -n $NbSamples capture.iq8
