from gtts import gTTS
import speech_recognition as sr
import os

def text_to_speech():
    text = input("Enter the text you want to convert to speech: ")
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("output.mp3")
    os.system("start output.mp3")  # Use "start" for Windows, "open" for macOS, and "xdg-open" for Linux

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak now.")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")

def main():
    print("Select an option:")
    print("1. Text-to-Speech")
    print("2. Speech-to-Text")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        text_to_speech()
    elif choice == '2':
        speech_to_text()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
