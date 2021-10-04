flite -voice slt -t "Please say the number 69"
arecord -D hw:2,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.
python3 test_words.py recorded_mono.wav
flite -voice slt -t "Nice"
