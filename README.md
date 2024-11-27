# 📈 Telegram Bot for Stock Monitoring

A Telegram bot built using `aiogram` that allows users to track stock prices of major companies. The bot integrates with [Alpha Vantage](https://www.alphavantage.co/) to fetch stock data, stores the information in a PostgreSQL database, and provides users with daily updates, including stock price charts generated with `matplotlib`.

---

## 🛠 Features

1. **User Registration**  
   - Users can register via the bot and manage their profile.
   
2. **Company Selection**  
   - Users can select the companies they are interested in tracking from a predefined list of major companies.

3. **Daily Stock Updates**  
   - The bot sends daily stock price charts for the selected companies directly to users.

4. **Dynamic Chart Generation**  
   - Generates daily stock price charts using `matplotlib` with data fetched from PostgreSQL.

5. **Automated Data Collection**  
   - An `Airflow DAG` periodically fetches stock price data from Alpha Vantage and loads it into a PostgreSQL database.

---

## 🚀 How It Works

1. **Data Pipeline**  
   - An Airflow DAG collects data from the Alpha Vantage API and updates the PostgreSQL database.

2. **Telegram Bot**  
   - The bot uses `aiogram` for handling user interactions.
   - Users can select and manage their preferred companies via simple commands.

3. **Chart Generation**  
   - The bot queries the database for stock data and generates charts using `matplotlib`.
   - These charts are sent daily to users via Telegram.

---

## 🧩 Tech Stack

- **Programming Language:** Python  
- **Telegram Bot Framework:** [aiogram](https://docs.aiogram.dev/)  
- **Task Scheduler:** [Apache Airflow](https://airflow.apache.org/)  
- **Database:** PostgreSQL  
- **Charting Library:** matplotlib  
- **API for Stock Data:** [Alpha Vantage](https://www.alphavantage.co/)  

---

## 📚 Installation & Setup

### Prerequisites
1. Python 3.8 or higher.
2. PostgreSQL database.
3. Airflow installed and configured.

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shmoki-molla/Stock_Project.git
   cd Stock_Project

   
