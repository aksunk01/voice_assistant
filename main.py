#Python libraries
import pyttsx3
import pvporcupine
import pyaudio
import speech_recognition as sr
import struct
from AppOpener import open
from datetime import datetime

#My files
import file_search as fs
import gemini as chat
import app_opener as ao
import weather

#Access key for porcupine
access_key = #enter your own access key for porcupine listening command

#Wake word detection
def main():
    porcupine = pvporcupine.create(access_key = access_key, keywords=['computer'])

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate = porcupine.sample_rate,
        channels =1,
        format = pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listenning for wake word...")

    try:
        while True:
            
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow = False)
            pcm_unpacked = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm_unpacked)
            
            if keyword_index >= 0:
                speech = capture_speech()
                print("You said: " + speech[0])
                print("This is speech[1]", speech[1])
                
                if (speech[1] == "exit"):
                    speak("Shutting Down")
                    print("Program terminated")
                    exit()
                else:
                    speak(speech[1])
                    print(speech[1])
                print("Listening for wake word...")

    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
        


#This captures speech
def capture_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio)

            
            return([response, decision(response)])
            
        except sr.UnknownValueError:
            print("Sorry couldn't understand audio")
        except sr.RequestError as e:
            print(f"could not request results; {e}")


def decision(response):

    decisions=["search", "find", "time is it", "weather", "open", "exit"]
    decision = 6

    for choice in range(len(decisions)):
        if response.lower().find(decisions[choice]) != -1:
            decision = choice

    if decision == 0 or decision == 1:
        fs.main()
        return([response,"search"])
    elif decision == 2:

        return([response, datetime.now().time().strftime("%H:%M:%S")])
    elif decision == 3:
        return(weather.weather(response))
    elif decision == 4:
        open(ao.opener(response))
        speak(response)
    elif decision == 5:
        return("exit")
    else:
        return(chat.general(response))
        


def onStart(name):
    print('starting', name)

def onWord(name, location, length):
    print('word', name, location, length)


def onEnd(name, completed):
    print("Finishing", name, completed)


def speak(response):
        
    engine = pyttsx3.init()

    engine.connect("started-utterance", onStart)
    engine.connect("started-word", onWord)
    engine.connect("finish-utterance", onEnd)

    engine.say(response)

    engine.runAndWait()


if __name__ == "__main__":
    while True:
        main()
    










