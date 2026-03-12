# Prowiz Analytics – Technical Assignment

This repository contains the solutions for the tasks assigned by Prowiz Analytics.
The assignment focuses on demonstrating practical skills in Python programming, API development, web scraping, database querying, and data analysis.

---

## Technologies Used

- Python
- Requests
- Pandas
- BeautifulSoup
- FastAPI
- SQLite
- Matplotlib
- Seaborn

---

## Repository Structure
```
Prowiz_Assignment
│
├── Task1.py
├── Task2.py
├── Task3.py
├── Task4.ipynb
├── Task5.py
├── requirements.txt
└── README.md
```

Each file corresponds to the implementation of a specific task from the assignment.

---

## Task 1 – API Data Extraction and Analysis

**File:** `Task1.py`

### Approach

For this task, the first step was to retrieve data from a public API. I used the `Requests` library to send a GET request and obtain the response in JSON format. After retrieving the data, it was converted into a Pandas DataFrame so that further analysis could be performed easily.

The analysis included:

- Printing the API response and checking its structure
- Counting the number of records returned
- Identifying the number of distinct users
- Determining which user has posted the maximum number of posts
- Calculating the average word count of post titles

Using Pandas made it easier to perform these calculations efficiently and analyze the dataset.

---

## Task 2 – HTML Parsing and Data Extraction

**File:** `Task2.py`

### Approach

In this task, the objective was to extract specific information from an HTML document.

I used `BeautifulSoup` to parse the HTML content and extract elements from the `<a>` tags. The following operations were performed:

- Extracting all `href` links
- Extracting `class` attributes from the `<a>` tags

To further demonstrate another approach, I also implemented a **regular expression based recursive function** to extract the same information from the HTML text. This shows two different ways to solve the same problem: using an HTML parser and using pattern matching.

---

## Task 3 – FastAPI Development

**File:** `Task3.py`

### Approach

For this task, I created a simple REST API using **FastAPI**.

Two endpoints were implemented:

### 1. Sum of Two Numbers

**Endpoint:** `POST /sum`

This endpoint accepts two numbers as input and returns their sum.
Input validation was added using a `try-except` block so that if non-numeric values are provided, the API returns an appropriate error message.

**Example output:**
```json
{"sum": 15}
```

### 2. Lowercase to Uppercase Conversion

**Endpoint:** `GET /uppercase`

This endpoint accepts a string and converts it to uppercase.
A validation check ensures that the input string is lowercase; otherwise, an error message is returned.

**Example:**
```
/uppercase?text=hello
```

**Response:**
```json
{"uppercase": "HELLO"}
```

---

## Task 4 – Data Analysis and Visualization

**File:** `Task4.ipynb`

### Approach

In this task, exploratory data analysis was performed on the dataset using Pandas.

The steps followed were:

- Loading the datasets
- Inspecting the structure and identifying missing values
- Cleaning the data where necessary
- Calculating important business metrics such as:
  - Revenue
  - Profit
- Aggregating the data based on store, region, or category
- Creating visualizations to identify trends and patterns

**Libraries used:**
- `Pandas` for data manipulation
- `Matplotlib` and `Seaborn` for visualization

The analysis helped identify patterns in sales performance and store-level metrics.

---

## Task 5 – SQL Database Operations

**File:** `Task5.py`

### Approach

For this task, I used **SQLite** in Python to create and query a database.

The steps performed were:

- Creating a database connection using the `sqlite3` module
- Creating a table named `student`
- Inserting sample student records
- Writing SQL queries to solve the following cases:
  - Finding the second topper in the class
  - Handling cases where multiple students may have equal marks
  - Using `DENSE_RANK()` to correctly determine the second rank when students share the same score

This task demonstrates how SQL queries can be executed directly from Python.

---

## Running the FastAPI Application

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the API server:**
```bash
uvicorn Task3:app --reload
```

Once the server starts, open:
```
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.
