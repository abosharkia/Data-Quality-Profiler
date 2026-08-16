import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Data Quality Profiler",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Automated Data Quality & Profiling Dashboard")
st.markdown(
    "Created by **Adan** | Statistics & Data Science Portfolio"
)

# ============================================================
# Load Dataset
# ============================================================

url = "https://raw.githubusercontent.com/datasets/house-prices-uk/master/data/data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

# ============================================================
# Dataset Overview
# ============================================================

st.header("📋 Dataset Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Records",
    f"{df.shape[0]:,}"
)

c2.metric(
    "Total Features",
    f"{df.shape[1]:,}"
)

missing_values = df.isnull().sum().sum()

c3.metric(
    "Missing Values",
    f"{missing_values:,}"
)

duplicate_rows = df.duplicated().sum()

c4.metric(
    "Duplicate Rows",
    f"{duplicate_rows:,}"
)

# ============================================================
# Raw Data Preview
# ============================================================

st.header("👀 Raw Data Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# ============================================================
# Data Quality Analysis
# ============================================================

st.header("🔍 Data Quality Analysis")

quality_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Missing %": (
        df.isnull().sum().values / len(df) * 100
    ).round(2),
    "Unique Values": df.nunique().values
})

st.dataframe(
    quality_df,
    use_container_width=True
)

# ============================================================
# Descriptive Statistics
# ============================================================

st.header("📊 Descriptive Statistics")

numeric_df = df.select_dtypes(include=np.number)

if not numeric_df.empty:

    descriptive_stats = numeric_df.describe().T.round(2)

    st.dataframe(
        descriptive_stats,
        use_container_width=True
    )

else:
    st.info("No numerical columns were found in the dataset.")

# ============================================================
# Interactive Visualization
# ============================================================

st.header("🎨 Visual Analytics Hub")

if not numeric_df.empty:

    selected_column = st.selectbox(
        "Select a numerical variable:",
        numeric_df.columns
    )

    # --------------------------------------------------------
    # Distribution
    # --------------------------------------------------------

    st.subheader("📈 Distribution")

    fig, ax = plt.subplots(figsize=(10, 4))

    sns.histplot(
        df[selected_column].dropna(),
        kde=True,
        bins=30,
        ax=ax
    )

    ax.set_title(
        f"Distribution of {selected_column}"
    )

    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

    # --------------------------------------------------------
    # Boxplot
    # --------------------------------------------------------

    st.subheader("📦 Outlier Detection")

    fig, ax = plt.subplots(figsize=(10, 3))

    sns.boxplot(
        x=df[selected_column].dropna(),
        ax=ax
    )

    ax.set_title(
        f"Boxplot of {selected_column}"
    )

    ax.set_xlabel(selected_column)

    st.pyplot(fig)

# ============================================================
# Correlation Analysis
# ============================================================

st.header("🔗 Correlation Analysis")

if numeric_df.shape[1] >= 2:

    correlation = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(12, 7))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        ax=ax
    )

    ax.set_title("Correlation Matrix")

    st.pyplot(fig)

else:
    st.info(
        "At least two numerical variables are required "
        "for correlation analysis."
    )

# ============================================================
# Summary
# ============================================================

st.header("📝 Profiling Summary")

st.write(
    f"""
    This dataset contains **{df.shape[0]:,} records**
    and **{df.shape[1]:,} features**.

    The dashboard automatically analyzes data quality,
    descriptive statistics, variable distributions,
    potential outliers, and correlations between numerical
    variables.
    """
)

st.success(
    "✅ Data profiling completed successfully!"
)
