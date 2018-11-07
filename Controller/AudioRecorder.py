import pyaudio
import wave
import re
import glob
import os
import shutil


CHUNK = 1024
FORMAT = pyaudio.paInt16 #paInt8
CHANNELS = 2
RATE = 44100 #sample rate
RECORD_SECONDS = 20

if not os.path.exists("../Database/Audio"):
    os.makedirs("../Database/Audio")
    print("Created 'Audio' directory")

if len(os.listdir("../Database/Audio") ) == 0:
    print("empty directory")
    CURRENT_FILE_NAME = "output0"+ ".wav"
else:
    LIST_OF_FILES = glob.glob('../Database/Audio/*.wav')  # * means all if need specific format then *.csv
    LATEST_FILE = max(LIST_OF_FILES, key=os.path.getctime)
    LIST_FILENAME = re.findall('\d+', LATEST_FILE)

    FILE_NUMBER = int(LIST_FILENAME[0])
    CURRENT_FILE_NUMBER = FILE_NUMBER + 1
    CON_CURRENT_FILE_NUMBER = str(CURRENT_FILE_NUMBER)
    CURRENT_FILE_NAME = "output" + CON_CURRENT_FILE_NUMBER + ".wav"


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data) # 2 bytes(16 bits) per channel

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(CURRENT_FILE_NAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
#Audio file not saving in the Audio directory so moved the audio file to the Audio directory
shutil.move(CURRENT_FILE_NAME,"../Database/Audio")
print("Moved "+CURRENT_FILE_NAME+" to Audio directory.")

passedParaName = CURRENT_FILE_NAME

