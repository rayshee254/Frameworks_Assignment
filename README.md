
## 🎯 Project Overview

This project analyzes a sample of 500 rows from the massive CORD-19 dataset to demonstrate research trends during the COVID-19 pandemic. By working with a sample, the analysis remains fast and efficient, perfect for prototyping visualizations and building an interactive dashboard without the overhead of processing a multi-gigabyte file.

## ✨ Key Features

-   **Lightweight Analysis:** Uses a sample of the first 500 rows for quick processing and iteration.
-   **Interactive Dashboard:** A clean, web-based interface built with Streamlit to explore the data.
-   **Sample Insights:** Shows publication trends, top journals, and common keywords within the sample.
-   **Efficient Workflow:** Avoids the complexity of chunking and memory management.

## 📊 Dataset & Sample

-   **Source:** [CORD-19 dataset on Kaggle](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)
-   **Full File:** `metadata.csv` (~1 GB+)
-   **File Used:** **First 500 rows** of `metadata.csv`.
-   **Note:** The full `metadata.csv` file is not included in this repo. The analysis is performed on a sample loaded directly from the local file.

## 💻 Installation & Setup

### Prerequisites
Ensure you have Python 3.8 or newer installed on your system.

### Steps
1.  **Download the project files:** Clone or download the `answers.ipynb`, `covid-app.py`, and this README file into a single project folder.

2.  **Install required Python packages:**
    ```bash
    pip install pandas matplotlib seaborn streamlit wordcloud
    ```

3.  **Download the data:**
    -   Visit the [CORD-19 dataset page on Kaggle](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge).
    -   Download the `metadata.csv` file.
    -   Place it in your project folder.

## 🚀 Usage

### Running the Jupyter Notebook
1.  Open `answers.ipynb` in Jupyter Notebook/Lab or VS Code.
2.  Run the cells to see the step-by-step analysis and visualizations.

### Running the Streamlit Dashboard
1.  Open a terminal and navigate to your project directory.
2.  Launch the application:
    ```bash
    streamlit run covid-app.py
    ```
3.  Your browser will open, displaying the interactive dashboard. The app will load the first 500 rows of your local `metadata.csv` file.


## ⚙️ Methodology

1.  **Data Loading:** The Python scripts use `pandas.read_csv()` with the `nrows=500` parameter to quickly load only the first 500 rows of the metadata file.
2.  **Data Cleaning:**
    -   Handling missing values in critical columns like `publish_time` and `journal`.
    -   Basic text cleaning on titles for word cloud generation.
3.  **Analysis:** Generating summary statistics, value counts, and simple time-series aggregations.
4.  **Visualization:** Creating plots with Matplotlib/Seaborn in the notebook and interactive elements in the Streamlit app.

## 🔍 Key Findings (Based on Sample)

*Analysis is based on the first 500 entries of the dataset and may not represent the full corpus.*

-   **Publication Dates:** The sample shows a concentration of papers from [Your Finding, e.g., 'early 2020'].
-   **Top Journals in Sample:** The most frequent journals in this sample are [Your Finding, e.g., 'BMJ, Lancet, JAMA'].
-   **Common Title Keywords:** Prominent words in paper titles include [Your Finding, e.g., 'COVID, coronavirus, pandemic, clinical'].

## 🔮 Future Work & Scaling Up

-   **Full Dataset Analysis:** Modify `covid-app.py` and `answers.ipynb` to use the full dataset by implementing chunking with `pandas` or using a database like SQLite.

---
**Disclaimer:** This analysis is performed on a non-random sample (the first 500 rows) for demonstration purposes. Conclusions are indicative of trends within this sample and should not be generalized to the entire CORD-19 dataset without further analysis.
