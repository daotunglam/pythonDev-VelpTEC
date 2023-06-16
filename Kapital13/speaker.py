import win32com.client
text = """Hello, my friend.
            Ich muss lachen."""
speaker = win32com.client.Dispatch('Sapi.SpVoice')
voices = speaker.GetVoices() #1
for voice in voices: #2
    print(voice.GetDescription()) #3
    speaker.Voice = voice #4
    speaker.Speak(text)