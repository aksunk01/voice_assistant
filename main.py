import pyttsx3
import pvporcupine
import pyaudio
import speech_recognition as sr
import struct

access_key = "AGs3waMEvcfn0ATEEt/NL8sjZaoGY4hT64aeKQYHn4Lnp7XV3GjoNA=="





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
                capture_speech()
                
    except KeyboardInterrupt:
        print("Stopping")

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
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry couldn't understand audio")
        except sr.RequestError as e:
            print(f"could not request results; {e}")

if __name__ == "__main__":
    main()










'''
# text to speech
def onStart(name):
    print('starting', name)

def onWord(name, location, length):
    print('word', name, location, length)


def onEnd(name, completed):
    print("Finishing", name, completed)




engine = pyttsx3.init()

engine.connect("started-utterance", onStart)
engine.connect("started-word", onWord)
engine.connect("finish-utterance", onEnd)

engine.say("The quick brown fox jumped over the lazy dog.")

engine.runAndWait()'''