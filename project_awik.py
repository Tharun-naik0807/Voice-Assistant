import pyttsx3  # Text-to-speech
import speech_recognition as sr  # Speech recognition
import datetime  # Date and time 
import webbrowser  # Web browsing

# Initialize  or start the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text into speech"""
    engine.say(text)
    engine.runAndWait()

def greet_user():
    """Greet the user based on the current time,morning ,afternoon or evening"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning Master!")
    elif 12 <= hour < 18:
        speak("Good afternoon master!")
    else:
        speak("Good evening Master!")
    speak("Hello, I am Awik. How can I help you today?")
    print("hello I,am Awik..")
def take_command():
    """Fetch master's voice command and return as the text"""
    recognizer = sr.Recognizer()
    command = ""  # Default value to avoid UnboundLocalError
    
    try:
        with sr.Microphone() as source:
            print("Listening to master!....")
            recognizer.adjust_for_ambient_noise(source)  # Adjust background noise
            audio = recognizer.listen(source)  # Capture the audio from the master or user
        
        command = recognizer.recognize_google(audio)  # Convert the masters or users speech to text 
        command = command.lower()  # Convert to lowercase 
        print(f"You said: {command}")
    
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        speak("Sorry, I did not understand please say it again")
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        speak("Could not request results, please check your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred while trying to recognize your speech.")
    
    return command  # Always return the 'command' variable

def run_awik():
    """Main function to run the awik-style voice assistant."""
    greet_user()  # Greet the user
    
    while True:
        command = take_command()  # Fetch the user's command
        
        if "hello" in command:
            speak("Hi Their! How can I help you?")
            print("hello I,am Awik..")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"The current time is {current_time}")
            speak(f"The current time is {current_time}")
        
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif "open linkedin" in command:
            speak("Opening linkdin")
            webbrowser.open("https://www.linkedin.com/login/in")
        
        elif "open whatsapp" in command:
            speak("Opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif "open instagram" in command:
            speak("Opening instagram")
            webbrowser.open("https://www.instagram.com/")

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            print("Exiting awik...")
            break
# Run the awik assistant
if __name__ == "__main__":
    run_awik()
