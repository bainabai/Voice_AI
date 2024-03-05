import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print("User said:", query)
        return query
    except Exception as e:
        print("Error:", str(e))
        return ""


def handle_command(command):
    if "hello" in command.lower():
        speak("Hello! How can I help you?")
    elif "time" in command.lower():
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command.lower():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "search" in command.lower():
        speak("What do you want me to search for?")
        query = recognize_speech()
        if query:
            search_url = "https://www.google.com/search?q=" + query
            webbrowser.open(search_url)
    elif "exit" in command.lower():
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")


def main():
    speak("Hello! How can I help you?")
    while True:
        command = recognize_speech()
        handle_command(command)

if __name__ == "__main__":
    main()


















