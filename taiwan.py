from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Download seismic data
network = 'IU'
station = 'TATO'
channel = 'BH*'
starttime = UTCDateTime('2024-04-22T23:58:11')
endtime = starttime + 60*15 # 15 mins

#Client
client = Client('IRIS')

# Get waveforms
st = client.get_waveforms(network=network, station=station, location='00',channel=channel, 
                          starttime=starttime, endtime=endtime, attach_response = True )

# Convert to velocity
st.remove_response(output='VEL')


# de-trend is to put trend out
# Pre-processing
st.merge(fill_value='interpolate') # Merge traces if we have gaps
st.detrend(type = 'linear') # Remove linear trend
st.taper(max_percentage=0.05) # Apply taper -> apply to T
print(st)
st[2].plot()
