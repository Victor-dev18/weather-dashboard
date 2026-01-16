import streamlit as st
import requests

def get_weather(city):
    api_key = st.secrets["OPENWEATHER_API_KEY"]  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except:
        return None

# --- UI Layout ---
st.title("🌤️ Weather Dashboard")
st.write("Check current weather conditions anywhere in the world.")

# 1. Input
city_input = st.text_input("Enter city name:", "Vijayawada")

# 2. Button
if st.button("Get Weather"):
    # 3. Logic
    data = get_weather(city_input)
    
    if data:
        # Extract data
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        location = data['name']
        
        # 4. Display nicely using Columns
        st.success(f"Weather data for **{location}** loaded!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Temperature", f"{temp}°C")
            
        with col2:
            st.metric("Humidity", f"{humidity}%")
            
        with col3:
            st.metric("Condition", condition.title())
            
    else:
        st.error("City not found! Please check the spelling.")