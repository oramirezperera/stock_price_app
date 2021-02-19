# stock_price_app
A stock price web app made in Python and Streamlit

This simple web app using Python, Streamlit, yfinance and pandas to show the prices of certain stock market.

## Streamlit

Is a library to create custom web apps, it's focused on data apps. 

Streamlit is compatible with:
### - Scikit learn
### - Bokeh
### - LaTex
### - Pandas
### - OpenCV
### - Numpy
### - Matplotlib

## Yfinance 

Started as a workaround for Yahoo! Finance but now is independent. 

It's a way to download historical market data from Yahoo! finance.

## Pandas 

Is used to manipulate data and do data analysis.

## App

In st.write we use markdown language and the title of the app

The charts are interactive

You can change the stock by changing the ticker symbol with the ticker symbol of your choice

These are the valid periods of the tickers valid = 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max. The default is 1mo

## Starting

To start this app in your local environment you have to clone this repository.

### Prerequirements:

- You need Python 3.6 or superior
- Pandas
- Streamlit

## Installation:

All the prerequisites can be installed using pip3 install -r requirements.txt.

Once you have all the prerequisites you can run the app in your local environment using 

```
$ streamlit run stock_price.py
```

That will start out local server and give us two urls like this

```
  You can now view your Streamlit app in your browser.

  Network URL: http://
  External URL: http://
```

You can copy and paste the Network URL into your browser and see displayed the web application.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Thank You

- Thanks for visiting this GitHub repository tell me if you like it.
- If there any problem with the app just contact me.
- Hope is useful and you can check out a lot of stock tickers.
