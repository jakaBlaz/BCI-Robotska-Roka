"""Example program that shows how to attach meta-data to a stream, and how to
later on retrieve the meta-data again at the receiver side."""

import time

from pylsl import StreamInlet, resolve_stream


# first we resolve a stream
stream1 = resolve_stream('name', 'obci_eeg1')

# create a new inlet to read from the stream
inlet = StreamInlet(stream1[0])

# get the full stream info (including custom meta-data) and dissect it
info = inlet.info()
print("The stream's XML meta-data is: ")
print(info.as_xml()) 

print(info.nominal_srate()) #Nominal sampling rate

# first resolve an EEG stream on the lab network
info = stream1[0]
print('Connected to outlet ' + info.name() + '@' + info.hostname())
while True:
    offset = inlet.time_correction() #Retrieve an estimated time correction offset for the given stream.
    print('Offset: ' + str(offset))
    time.sleep(1)

    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    chunk, timestamps = inlet.pull_sample()
    

