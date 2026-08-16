# 📊 Automated Data Quality & Profiling Dashboard

An interactive **data profiling and quality analysis dashboard** built with Python and Streamlit.

The application automatically examines a dataset and provides an overview of its structure, data quality, descriptive statistics, distributions, potential outliers, and correlations between numerical variables.

## 🚀 Features

### 📋 Dataset Overview

* Total number of records
* Total number of features
* Missing values
* Duplicate rows

### 🔍 Data Quality Analysis

* Data types
* Missing values per column
* Missing value percentage
* Number of unique values

### 📊 Descriptive Statistics

Automatically generates statistical summaries for numerical variables, including:

* Mean
* Standard deviation
* Minimum and maximum values
* Quartiles

### 🎨 Visual Analytics

* Interactive numerical variable selection
* Distribution histograms with KDE
* Boxplots for potential outlier detection
* Correlation heatmap

### 👀 Raw Data Preview

Provides an interactive preview of the dataset for quick inspection.

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**

## 📂 Dataset

The dashboard currently uses a UK housing prices dataset hosted on GitHub.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/abosharkia/Data-Quality-Profiler.git
cd Data-Quality-Profiler
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

### 3. Run the application

```bash
streamlit run 1.py
```

The dashboard will open in your browser.

## 🎯 Project Purpose

This project was created as part of my Statistics & Data Science portfolio to practice applying statistical concepts and Python-based data analysis to a real-world dataset.

It demonstrates how automated profiling can help identify data quality issues and provide an initial understanding of a dataset before deeper analysis.

