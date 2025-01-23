import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_data_overview(df):
    """Provide an overview of the dataset."""
    overview = {
        "Shape": df.shape,
        "Data Types": df.dtypes.to_dict(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Sample Data": df.head().to_dict()
    }
    return overview

def plot_numerical_distributions(df, numerical_columns):
    """Plot histograms and boxplots for numerical columns."""
    for column in numerical_columns:
        if column in df.columns:
            plt.figure(figsize=(10, 5))
            sns.histplot(df[column], kde=True, bins=20)
            plt.title(f"Distribution of {column}")
            plt.show()

            sns.boxplot(x=df[column])
            plt.title(f"Boxplot of {column}")
            plt.show()

def plot_categorical_distributions(df, categorical_columns):
    """Plot bar charts for categorical columns."""
    for column in categorical_columns:
        if column in df.columns:
            plt.figure(figsize=(10, 5))
            sns.countplot(y=column, data=df, order=df[column].value_counts().index)
            plt.title(f"Distribution of {column}")
            plt.show()

def plot_correlation_matrix(df):
    """Plot a heatmap of the correlation matrix."""
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()

def identify_missing_values(df):
    """Identify missing values in the dataset."""
    missing = df.isnull().sum()
    print("Missing Values by Column:")
    print(missing[missing > 0])

def detect_outliers(df, numerical_columns):
    """Detect outliers using boxplots."""
    for column in numerical_columns:
        if column in df.columns:
            sns.boxplot(df[column])
            plt.title(f"Outliers in {column}")
            plt.show()
