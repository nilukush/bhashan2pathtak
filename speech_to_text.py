import speech_recognition as sr


def main():
    # Create a Recognizer instance
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        while True:  # Infinite loop to keep listening
            try:
                # Listen for the first phrase and extract it into audio data
                print("Speak now...")
                audio_data = r.record(source, duration=10)  # adjust the duration as needed
                # Convert speech to text
                text = r.recognize_google(audio_data, language='en-GB')
                print(text)
            except sr.UnknownValueError:
                # Google Speech Recognition could not understand the audio
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                # Could not request results from Google Speech Recognition service
                print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
    main()
