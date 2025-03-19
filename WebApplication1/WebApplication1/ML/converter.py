import soundfile as sf

data, samplerate = sf.read('Try.mp3')

sf.write('output_file.wav', data, samplerate)
