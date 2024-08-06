# Fama-French and Momentum Analysis of Apple Stock

This code conducts a financial analysis of Apple (AAPL) stock returns using the Fama-French factors and momentum factor. It demonstrates how to fetch financial data, process it, and perform regression analysis to understand the relationship between these factors and stock returns.

## Features

- Fetches Fama-French factors and momentum data using `pandas_datareader`
- Downloads Apple stock data using `yfinance`
- Merges and processes data for analysis
- Performs OLS regression to analyze the relationship between factors and stock returns

## Requirements

- Python 3.x
- pandas
- pandas_datareader
- matplotlib
- yfinance
- statsmodels

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install pandas pandas_datareader matplotlib yfinance statsmodels
   ```

## Usage

1. Run the Jupyter notebook or Python script to execute the analysis.
2. The script will:
   - Fetch Fama-French factors and momentum data
   - Download Apple stock data
   - Merge and process the data
   - Perform regression analysis
   - Display results and plots

## Key Components

1. Data Fetching:
   - Fama-French factors and momentum data from Ken French's data library
   - Apple stock data from Yahoo Finance

2. Data Processing:
   - Resampling and merging datasets
   - Calculating excess returns

3. Analysis:
   - OLS regression of Apple's excess returns against Fama-French factors and momentum

## Results

The project provides:
- Visualizations of Fama-French factors and momentum over time
- Regression results showing the relationship between these factors and Apple's stock returns

## Future Improvements

- Extend the analysis to multiple stocks or portfolios
- Implement a more sophisticated asset pricing model
- Add functionality to backtest trading strategies based on these factors


## Acknowledgments

- Fama-French data provided by Kenneth French's data library
- Stock data provided by Yahoo Finance through yfinance
