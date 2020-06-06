"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream, resolve_streams, ContinuousResolver
import time

#continuious resolver
r = ContinuousResolver(prop='name', value='x')
time.sleep(3)
streams = r.results()
print('Streams >>', streams)
for stream in streams:
    print('results >>', stream)
    print("stream_name", stream.name())
    print("/--------------/")



# first resolve an EEG stream on the lab network
print("looking for an EEG stream...")
name1 = 'obci_eeg'
name2 = 'obci_aux'
mac1 = 'EEG'
mac2 = 'AUX'
stream1 = resolve_stream('name', name1)
#stream2 = resolve_stream('type', mac2)

# create a new inlet to read from the stream
inlet1 = StreamInlet(stream1[0])
#inlet2 = StreamInlet(stream2[0])
stream_info = inlet1.info()
stream_name = stream_info.name()
stream_mac = stream_info.type()
stream_host = stream_info.hostname() 
stream_n_channels = stream_info.channel_count()
print(stream_info)
print(stream_name)
print(stream_mac)
print(stream_host)
print(stream_n_channels)

#wait before streaming
time.sleep(10)
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet1.pull_sample()
    print()
    print(sample)
