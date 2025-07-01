from obspy import read

st = read()
#st.plot()
st[1].plot()
st[1].spectrogram(log=True) #create spectrogram

#Filter the wavefrom, tr -> trace (line)
tr = st[1].copy()
tr.filter('bandpass', freqmin = 1.0, freqmax = 5.0, corners = 4, zerophase = True)
tr.plot()

tr.write('demo_eq.mseed', format='MSEED')

fig = tr.plot(show=True)
fig.savefig('demo_Waveform.png', dpi=300)
