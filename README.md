# Scraping and Analyzing Femicide Data in Kenya (2016–2024)

A project focused on web scraping and preliminary data structuring of publicly available femicide records from the Africa Data Hub. The project recreates user interactions with a dynamic site to extract over 700 records of reported female killings in Kenya between 2016 and 2024.

## Project Overview

- **Objective:** Automatically extract detailed femicide records from a card-based, interactive website and structure the data for further analysis.
- **Motivation:** With increasing public discussion around femicide in Kenya, I wanted to explore the actual data behind the headlines and uncover any patterns.
- **Outcome:** A cleaned, structured CSV file containing over 700 complete femicide records, with key details such as names, dates, locations, suspects, and source links.

## Tools and Libraries
- **Python –** Programming language
- **Selenium –** Browser automation for dynamic web scraping
- **Pandas –** Data structuring and storage
- **CSV module –** Appending records in real time
- **VS Code –** Code editor used during development
- **Git & GitHub –** Version control and project hosting

## Scraping Strategy

Each femicide record on the source website is presented as a clickable card. Clicking opens a modal with detailed information such as the victim’s name, age, location, and source article.

Due to this dynamic structure, Selenium was the appropriate tool to simulate these interactions and extract data.

The scraper:
1. Loads the site and closes the cookie modal.
2. Scrolls to the bottom to ensure all records are loaded.
3. Iteratively clicks each card, extracts data from the modal, and closes it.
4. Writes each extracted record to a CSV file immediately.

## Next Steps (Not Yet Implemented)
- Load data from CSV into a DataFrame
- Clean and standardize columns (e.g. age formatting, missing fields)
- Perform EDA to uncover patterns (e.g. most common locations, suspect relationships)
- Visualize the data using a dashboard (Power BI or Streamlit)

## Future Improvements
- Refactor scraper into modular functions or a class
- Add structured error handling and retry logic
- Enable automatic scraping on schedule
- Track and extract new records

## Project Structure

- `scrape/` - Virtual environment folder (not tracked in Git)
- `.gitignore` - Ignores venv, cache, and other unnecessary files
- `femicide_data.csv` - Final CSV output with all 702 valid records
- `Femicide-data-extraction-report.md` - Detailed project write-up and documentation
- `requirements.txt` - All dependencies used (e.g. selenium, pandas)
- `scraper.py` - Original scraper script for records 0–690
- `scraper2.py` - Second script to append last 11 records (691–701)
- `README.md` - Project overview and usage instructions

📎 Source

All data is sourced from the publicly available <a href="https://www.africadatahub.org/femicide-kenya">Africa Data Hub</a>, compiled from news reports and court records between 2016 and 2024.
