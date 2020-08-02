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

time.sleep(3)