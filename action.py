import text_to_speech
import Speech_to_text
import datetime
import webbrowser
import weather


def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey,how I can help you")
        return "Hey,how I can help you"

    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning!")
        return "Good Morning!"

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = str(current_time.hour) +"Hour: "  + str(current_time.minute) +" Minute: "
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("ok")
        return "ok"
    
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is now ready for you")
        return "Spotify is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://www.google.co.in/")
        text_to_speech.text_to_speech("Google is now ready for you")
        return "Google is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Youtube is now ready for you")
        return "Youtube is now ready for you"
    
    elif "weather" in user_data:
        ans  =  weather.get_weather("Banglore")
        text_to_speech.text_to_speech(ans)
        return ans
        

    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"
    

        
