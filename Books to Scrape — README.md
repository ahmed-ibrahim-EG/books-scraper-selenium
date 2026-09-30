# 📚 Books to Scrape — Automated Data Pipeline

An automated web scraping and ETL pipeline built with **Python, Selenium, and Pandas** to extract, transform, and structure book catalog data from [Books to Scrape](https://books.toscrape.com/).

The project demonstrates a simple end-to-end data pipeline: **Web Scraping → Data Transformation → Structured CSV Output**.

---

## 📌 Project Overview

The pipeline automates browser-based data extraction across multiple paginated catalog pages.

It collects relevant book information, cleans and transforms the extracted values, and stores the final dataset in a structured CSV file ready for further analysis or ingestion into a data pipeline.

### Key Capabilities

- 🔄 **Automated Pagination**  
  Navigates through multiple catalog pages using Selenium.

- 🎯 **Targeted Data Extraction**  
  Extracts relevant book attributes such as title, price, and availability status.

- 🧹 **Data Cleaning & Transformation**
  - Removes unnecessary UI text and labels.
  - Strips the `£` currency symbol from prices.
  - Converts price values from strings to `float`.
  - Structures the extracted records into a consistent tabular format.

- 📦 **Structured Data Export**  
  Saves the transformed dataset as a UTF-8 encoded CSV file using Pandas.

---

## 🔄 Pipeline Flow

```text
Books to Scrape
       │
       ▼
 Selenium Web Scraping
       │
       ▼
 Raw Book Data
       │
       ▼
 Data Cleaning & Transformation
       │
       ▼
 Pandas DataFrame
       │
       ▼
 books_data.csv
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Selenium** | Browser automation and web scraping |
| **Pandas** | Data transformation and structured data handling |
| **CSV** | Final data storage format |

---

## 📂 Project Structure

```text
books-to-scrape-pipeline/
│
├── scraper.py          # Main scraping and ETL script
├── books_data.csv      # Processed dataset output
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<YOUR-USERNAME>/books-to-scrape-pipeline.git
cd books-to-scrape-pipeline
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Make sure Google Chrome is installed. Modern Selenium versions can manage the required ChromeDriver automatically.

### 4. Run the Pipeline

```bash
python scraper.py
```

The script will launch a browser session, navigate through the catalog pages, extract the book data, perform the required transformations, and generate:

```text
books_data.csv
```

in the project root directory.

---

## 📊 Dataset Schema

| Column | Data Type | Description | Example |
|--------|-----------|-------------|---------|
| `Book` | `string` | Full title of the book | `A Light in the Attic` |
| `price` | `float` | Book price after removing the GBP symbol | `51.77` |
| `status` | `string` | Current inventory availability | `In stock` |

---

## 🎯 Learning Objectives

This project was built to practice practical Data Engineering concepts, including:

- Web data extraction
- Browser automation with Selenium
- Data cleaning and transformation
- Type conversion
- Tabular data processing with Pandas
- Building a simple ETL workflow
- Exporting structured datasets

---

## 👤 Author

**Ahmed Ibrahim**

**Focus:** Data Engineering & Data Pipeline Development

- GitHub: [Ahmed Ibrahim](https://github.com/<YOUR-USERNAME>)
- Portfolio: [Portfolio](https://ahmed-portfolio-nine-nu.vercel.app/)

---

## 📌 Project Status

**Completed — Beginner Data Engineering Project**

Future improvements may include loading the processed data into a database and adding additional validation and logging steps.