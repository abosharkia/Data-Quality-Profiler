import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration and styling
st.set_page_config(page_title="Data Quality Profiler", layout="wide")
st.title("📊 Automated Data Quality & Profiling Dashboard")
st.markdown("Created by **Adan** | Statistics & Data Science Portfolio")

# Load real estate dataset directly from GitHub
url = "https://raw.githubusercontent.com/datasets/house-prices-uk/master/data/data.csv"
df = pd.read_csv(url)

# Display Key Performance Indicators (KPIs) using metrics cards
c1, c2 = st.columns(2)
c1.metric("Total Records (Rows)", f"{df.shape[0]:,}")
c2.metric("Total Features (Columns)", df.shape[1])

# Interactive raw data preview (First 10 rows)
st.subheader("👀 Raw Data Preview")
st.dataframe(df.head(10))

# Descriptive statistics matrix for data profiling
st.subheader("📊 Descriptive Statistics Matrix")
st.dataframe(df.describe().T.round(2))

# Visualizing price distribution using a Seaborn histogram with KDE
st.subheader("🎨 Visual Analytics Hub")
fig, ax = plt.subplots(figsize=(10, 4))
sns.histplot(df['Price (All)'], kde=True, color='royalblue', bins=30, ax=ax)
st.pyplot(fig)
