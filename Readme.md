📈 Telegram Bot for Stock Monitoring
A Telegram bot built using aiogram that allows users to track stock prices of major companies. The bot integrates with Alpha Vantage to fetch stock data, stores the information in a PostgreSQL database, and provides users with daily updates, including stock price charts generated with matplotlib.

🛠 Features
User Registration

Users can register via the bot and manage their profile.
Company Selection

Users can select the companies they are interested in tracking from a predefined list of major companies.
Daily Stock Updates

The bot sends daily stock price charts for the selected companies directly to users.
Dynamic Chart Generation

Generates daily stock price charts using matplotlib with data fetched from PostgreSQL.
Automated Data Collection

An Airflow DAG periodically fetches stock price data from Alpha Vantage and loads it into a PostgreSQL database.
🚀 How It Works
Data Pipeline

An Airflow DAG collects data from the Alpha Vantage API and updates the PostgreSQL database.
Telegram Bot

The bot uses aiogram for handling user interactions.
Users can select and manage their preferred companies via simple commands.
Chart Generation

The bot queries the database for stock data and generates charts using matplotlib.
These charts are sent daily to users via Telegram.
🧩 Tech Stack
Programming Language: Python
Telegram Bot Framework: aiogram
Task Scheduler: Apache Airflow
Database: PostgreSQL
Charting Library: matplotlib
API for Stock Data: Alpha Vantage
📚 Installation & Setup
Prerequisites
Python 3.8 or higher.
PostgreSQL database.
Airflow installed and configured.
Steps
Clone the repository:

bash
Копировать код
git clone https://github.com/yourusername/telegram-stock-bot.git
cd telegram-stock-bot
Install dependencies:

bash
Копировать код
pip install -r requirements.txt
Set up the database:

Create a PostgreSQL database.
Apply migrations or set up tables as defined in the project.
Configure environment variables:

Create a .env file in the root directory and add the following variables:
makefile
Копировать код
TELEGRAM_TOKEN=your_telegram_bot_token
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
DATABASE_URL=postgresql://username:password@localhost/dbname
Start Airflow for data collection:

Place the provided DAG file in the Airflow dags folder.
Start the Airflow scheduler:
bash
Копировать код
airflow scheduler
airflow webserver
Run the Telegram bot:

bash
Копировать код
python bot.py
🎯 Usage
Start the Bot:
Open Telegram and start the bot using the link provided after registering it with BotFather.

Register and Select Companies:
Use the bot's commands to register, view available companies, and select the ones you want to track.

Receive Daily Updates:
The bot will send daily updates with stock price charts for your selected companies.

📂 Project Structure
bash
Копировать код
telegram-stock-bot/
├── bot.py                # Main script for the Telegram bot
├── dags/                 # Airflow DAG for fetching stock data
│   └── stock_data_dag.py
├── database/             # Database models and migrations
├── charts/               # Scripts for generating stock charts
├── config/               # Configuration files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
If you have any questions or feedback, please feel free to reach out:

Email: your_email@example.com
GitHub: yourusername
