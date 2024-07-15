import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset's CSV file into a Pandas DataFrame
df = pd.read_csv('vehicles_us.csv')  # Adjust the path if necessary

# Display the first few rows of the dataframe (optional)
st.write(df.head())

# Header
st.header('Car Sales Dashboard')

# Histogram using Plotly Express
hist_fig = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(hist_fig)

# Scatter plot using Plotly Express
scatter_fig = px.scatter(df, x='odometer', y='price', title='Car Price vs. Odometer')
st.plotly_chart(scatter_fig)

# Checkbox to toggle histogram/scatter plot display
show_plot = st.checkbox('Show Scatter Plot')

if show_plot:
    st.plotly_chart(scatter_fig)
else:
    st.plotly_chart(hist_fig)

