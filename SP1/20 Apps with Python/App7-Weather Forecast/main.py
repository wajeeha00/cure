import streamlit as st
import plotly.express as px

from backend import get_data


st.title("Weather forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days you want to forecast")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [data["main"]["temp"] for data in filtered_data]
        temperatures = [temperatures/10 for temperatures in temperatures]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png","Snow": "images/snow.png"}
        sky_conditions = [data["weather"][0]["main"] for data in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)