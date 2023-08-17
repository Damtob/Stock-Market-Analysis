import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

def fetch_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def perform_analysis(stock_data):
    max_price = stock_data['High'].max()
    min_price = stock_data['Low'].min()
    avg_price = stock_data['Close'].mean()
    total_volume = stock_data['Volume'].sum()

    print("Stock Analysis:")
    print(f"Maximum Price: {max_price:.2f}")
    print(f"Minimum Price: {min_price:.2f}")
    print(f"Average Closing Price: {avg_price:.2f}")
    print(f"Total Volume: {total_volume:.0f}")

def plot_stock_data(stock_data):
    plt.figure(figsize=(10, 6))
    stock_data['Close'].plot(label='Closing Price', color='pink')
    plt.title('Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

def forecast_future_prices(stock_data, forecast_steps):
    closing_prices = stock_data['Close']
    model = ARIMA(closing_prices, order=(5,1,0))  # Example ARIMA order, you can adjust these parameters
    model_fit = model.fit(disp=0)
    forecast, stderr, conf_int = model_fit.forecast(steps=forecast_steps)

    return forecast

if __name__ == "__main__":
    symbol = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-08-11"
    forecast_steps = 30  # Number of days to forecast

    stock_data = fetch_stock_data(symbol, start_date, end_date)
    perform_analysis(stock_data)
    plot_stock_data(stock_data)

    forecast = forecast_future_prices(stock_data, forecast_steps)
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(stock_data)), stock_data['Close'], label='Historical Data', color='pink')
    plt.plot(range(len(stock_data), len(stock_data) + forecast_steps), forecast, label='Forecast', color='blue')
    plt.title('Stock Price Forecast')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
