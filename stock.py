import yfinance as yf
import matplotlib.pyplot as plt


def fetch_stock_data(symbol, start_date, end_date):
    # Fetch stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def perform_analysis(stock_data):
    # Calculate basic analysis metrics
    max_price = stock_data['High'].max()
    min_price = stock_data['Low'].min()
    avg_price = stock_data['Close'].mean()
    total_volume = stock_data['Volume'].sum()

    print("Stock Analysis:")
    print(f"Maximum Price: {max_price:.2f}")
    print(f"Minimum Price: {min_price:.2f}")
    print(f"Average Closing Price: {avg_price:.2f}")
    print(f"Total Volume: {total_volume:.0f}")


if __name__ == "__main__":
    symbol = "Googl"  # Replace with the stock symbol you want to analyze AAPL, Googl etc
    start_date = "2023-01-01"
    end_date = "2023-08-11"

    stock_data = fetch_stock_data(symbol, start_date, end_date)
    perform_analysis(stock_data)

    def plot_stock_data(stock_data):
        # Plotting the closing prices
        plt.figure(figsize=(10, 6))
        stock_data['Close'].plot(label='Closing Price', color='pink')
        plt.title('Stock Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.show()
    plot_stock_data(stock_data)




