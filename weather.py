from requests_html import HTMLSession

def get_weather(city):
    session = HTMLSession()
    url = f"https://wttr.in/{city}?format=%t+%C"
    response = session.get(url)
    
    if response.status_code == 200:
        weather = response.text.strip()
        ans = (f"Weather in {city}: {weather}")
        return ans
    else:
        print("Failed to fetch weather data.")


