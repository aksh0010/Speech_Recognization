import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()
# Get the current list of available voices
# voices = engine.getProperty('voices')

# Print the available voices
# for voice in voices:
#     print("Voice:")
#     print(" - ID: ", voice.id)
#     print(" - Name: ", voice.name)
#     print(" - Languages: ", voice.languages)
#     print(" - Gender: ", voice.gender)
#     print(" - Age: ", voice.age)
    
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'  # Replace 'your_voice_id_here' with the ID of the desired voice
engine.setProperty('voice', voice_id)

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    # engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source2:
    SpeakText("What can I do for you?")

    while True:
        try:
            # Adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Listen for the user's input
            audio2 = r.listen(source2)

            # Use Google to recognize audio
            MyText = r.recognize_google(audio2, language="en-US")

            MyText = MyText.lower()

            print("Did you say:", MyText)
            # Add a condition to terminate the loop if desired
            if MyText == "stop":
                SpeakText("All right I will go. Bye now !")

                break
            else :
                 SpeakText(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")
