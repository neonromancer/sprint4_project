**Streamlit Car Sales Dashboard**

**Project Overview**

This project provides a web-based dashboard using Streamlit to visualize car sales data from a CSV dataset. Users can interact with histograms and scatter plots to explore various aspects of the dataset.

**Methods and Libraries Used**

- Streamlit: Used to create the interactive web application.
- Pandas: Used for data manipulation and analysis.
- Plotly Express: Used for creating interactive visualizations.

**Dataset**

The dataset (vehicles_us.csv) contains car sales advertisements data and is included in the project's root directory for local testing and deployment.

**How to Run Locally**

To run this project locally, follow these steps:

1. Clone the repository to your local machine: git clone https://github.com/yourusername/your-repository.git
cd your-repository

2. Set up a Python virtual environment and install dependencies: python -m venv car-sales-env
.\car-sales-env\Scripts\activate  # On Windows
source car-sales-env/bin/activate  # On macOS/Linux
pip install -r requirements.txt

3. Run the Streamlit application: streamlit run app.py

4. Open a browser and go to http://localhost:8501 to view the application.

**Deployment on Render**

This project is deployed on Render for online access. To access the deployed application, visit [App URL](https://sprint4-project-wmm9.onrender.com/).

**Files Included**

- app.py: Main Streamlit application file.
- vehicles_us.csv: Dataset containing car sales data.
- requirements.txt: List of Python packages required for the project.
- .streamlit/config.toml: Configuration file for Streamlit on Render.

Credits
This project was created as part of a Streamlit application development tutorial.