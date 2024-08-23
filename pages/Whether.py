import streamlit as st
import requests

def fetch_weather(api_key, city, locality):
    # Combine city and locality to form the query
    query = f"{locality}, {city}, IN"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    st.title("Live Weather Information")

    api_key = "2476fce804dd99ff0fbe78869e48db3c"
    if not api_key:
        st.warning("Please enter your API key above.")
        return

    # Input field for user to enter their locality
    locality = st.text_input("Enter your locality in Jaipur (e.g., Jagatpura, Vaishali Nagar):")

    if st.button("Fetch Weather"):
        if locality:
            weather_data = fetch_weather(api_key, "Jaipur", locality)

            if weather_data.get("cod") == 200:
                st.subheader(f"Weather in {locality}, Jaipur:")
                temp = weather_data["main"]["temp"]
                weather_description = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]

                st.write(f"Temperature: {temp}°C")
                st.write(f"Description: {weather_description}")
                st.write(f"Humidity: {humidity}%")
                st.write(f"Wind Speed: {wind_speed} m/s")
            else:
                st.error("Failed to fetch weather data. Please check your input and try again.")
        else:
            st.warning("Please enter a locality in Jaipur.")

if __name__ == "__main__":
    main()
