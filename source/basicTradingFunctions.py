import pandas as pd
import matplotlib.pyplot as plt

def normalize_data(df):
    """Normalize stock prices using the first row of the DF"""
    return df / df.iloc[0,:]

def plot_data(df, title="Stock Prices"):
     """Plot stock prices with a custom title and meaningful axis labels."""
     ax=df.plot(title=title, fontsize=12)
     ax.set_xlabel("Date")
     ax.set_ylabel("Price")
     ax.legend(loc='upper left')
     plt.show()

def rollingMean(df,symbol):
    ax=df[symbol].plot(title='Rolling Mean', label=symbol)
    df=pd.rolling_mean(df[symbol],window=50)
    df.plot(label='Rolling Mean',ax=ax)
    plt.show()
    
def get_rolling_mean(df,window):
    return df.rolling(window=window).mean()

def get_rolling_std(df,window):
    return df.rolling(window=window).std()

def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    # TODO: Compute upper_band and lower_band
    upper_band = rm+rstd*2
    lower_band = rm-rstd*2
    return upper_band, lower_band

def compute_daily_returns(df):
    daily_return = df.copy() # copy given DF to match size and column names
    #daily_return[1:] = (df[1:] / df[:-1].values) - 1
    daily_return = (df / df.shift(1)) - 1 #much easier with Pandas
    daily_return.iloc[0,:] = 0 # set dail return for row 0 to 0
    return daily_return

def test_norm(startDate,endDate,symbol):
    df1=getStockClosePrice(startDate,endDate,symbol)
    dates=pd.date_range(startDate,endDate)
    symbols = ['X','AAL','TEX']
    df=getStocksPriceDF(df1,symbols,dates[0])
    #print(df)    
    dfNorm=normalize_data(df)
    plot_data(dfNorm)

def test_rolling_mean(df,symbol):
    #rollingMean(df,symbol)
    ax=df[symbol].plot(title='Rolling Mean', label=symbol)
    dfRolling=get_rolling_mean(df,50)
    dfRolling=dfRolling.rename(columns={symbol : 'Rolling Mean'})
    dfRolling.plot(label='Rolling Mean',ax=ax)
    plt.show()
    plt.clf()

def test_rolling_std(df,symbol):
    ax=df[symbol].plot(title='Rolling STD', label=symbol)
    dfSTD=get_rolling_std(df,50)
    dfSTD.plot(label='Rolling Mean',ax=ax)
    plt.show()
    plt.clf()
    
def test_bollinger(df,symbol):
    
    dfRolling=get_rolling_mean(df,50)
    dfSTD=get_rolling_std(df,50)
    #Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(dfRolling, dfSTD)
    
    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax=df.plot(title="Bollinger Bands", label=symbol)
    dfRolling.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

def test_daily_return(df):
    # Compute daily returns
    plot_data(df)
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns")