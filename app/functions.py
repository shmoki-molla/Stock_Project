import matplotlib.pyplot as plt
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import app.requests as rq
import asyncio
import io


def get_company_name2(ticker):
    companies = {
        "stock_prices": "Apple",
        "stock_msft": "Microsoft",
        "stock_amzn": "Amazon.com",
        "stock_googl": "Google",
        "stock_tsla": "Tesla"
    }
    return companies.get(ticker, "Unknown Ticker")


async def create_plot(table_name):
    df = await rq.get_prices(table_name)
    if df.empty:
        print("DataFrame is empty!")
        return None

    df['date'] = pd.to_datetime(df['date'])

    plt.figure(figsize=(12, 8))
    plt.plot(df['date'], df['close'], color='mediumspringgreen', marker='o', markersize=5, linestyle='-', linewidth=2,
             label='Цена закрытия')

    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.gcf().autofmt_xdate()

    plt.title(f'Закрытые цены акций {get_company_name2(table_name)}', fontsize=16, fontweight='bold')
    plt.xlabel('Дата', fontsize=12)
    plt.ylabel('Цена закрытия (USD)', fontsize=12)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.ylim(df['close'].min() * 0.95, df['close'].max() * 1.05)  # Добавление 5% запаса сверху и снизу

    plt.fill_between(df['date'], df['close'], color='mediumaquamarine', alpha=0.3)

    plt.legend(loc='upper left')

    plt.tight_layout()

    plot_image = io.BytesIO()
    plt.savefig(plot_image, format='png')
    plot_image.seek(0)
    plt.close()

    with open(f"{table_name}.png", "wb") as f:
        f.write(plot_image.read())
    plot_image.seek(0)
    print(f"График сохранён как {table_name}t.png для отладки.")

    return plot_image


def get_company_name(ticker):
    companies = {
        "AAPL": "Apple",
        "MSFT": "Microsoft",
        "AMZN": "Amazon.com",
        "GOOGL": "Google",
        "TSLA": "Tesla"
    }

    return companies.get(ticker.upper(), "Unknown Ticker")


async def get_companies2():
    result = await rq.get_companies()
    result2 = []
    for comp in result:
        result2.append(str(comp[0]))
    return result2
