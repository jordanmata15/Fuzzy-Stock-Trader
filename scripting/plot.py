"""
Script for plotting the daily data of the fuzzy stock trading system.

@Author: Jordan Mata
@Date: October 6, 2022
"""

import matplotlib.pyplot as plt
import os
import pandas as pd

PACKAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
SCRIPTING_DIR = os.path.join(PACKAGE_DIR, "scripts")
DATA_DIR = os.path.join(PACKAGE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.csv")

# allows us to be consistent with the colors of our variables in the plots
COLOR_DICT = {'XYZ_Price': 'orange',#'fuchsia', 
                'MAD': 'seagreen',#'lime', 
                'TMA': 'darkcyan', 
                'Stocks_Traded': 'pink',
                'Current_Balance': 'cornflowerblue',
                'Stocks_Held': 'red',
                'Stocks_Held_Value': 'orange',
                'Net_Worth': 'black'}



def plot_balances_and_net_worth(df):
    """Plot the Current balance, value of stocks held, and net worth (sum of previous two)
    for every day in our simulation.

    :param: df - dataframe containing one record for each day. Each day should contain columns
                    Current_Balance, Stocks_Held_Value, and Net_Worth   
    """
    net_worth_df = df[['Net_Worth']]
    # net worth is being plotted skewed, not sure why yet. Move it left 10 spaces
    net_worth_df.index = net_worth_df.index-10 
    balance_stocks_df = df[['Current_Balance', 'Stocks_Held_Value']]

    _, ax = plt.subplots()
    net_worth_df.plot(linestyle='dashed',
                        linewidth=2,
                        color=[COLOR_DICT.get(x, '#333333') for x in net_worth_df.columns], 
                        ax=ax)  
    balance_stocks_df.plot.bar(stacked=True, 
                                color=[COLOR_DICT.get(x, '#333333') for x in balance_stocks_df.columns], 
                                width=1, 
                                ax=ax)  
    plt.setp(ax.get_xticklabels()[::2], visible=False)
    plt.xlabel("Day")
    plt.ylabel("Dollar Value")
    plt.grid(linewidth=0.3)
    plt.show()



def plot_normalized_lines(df):
    """Plot a subset of the numeric columns. Each will be normalized so trends can be analyzed
    between multiple columns. 

    :param: df - dataframe containing a subset of the columns to plot. There should be one 
                    record for each day.
    """
    normalized_df = (df-df.min())/(df.max()-df.min())
    normalized_df.plot(color=[COLOR_DICT.get(x, '#333333') for x in df.columns])

    plt.xlabel("Day")
    plt.ylabel("Value (normalized to [0,1])")
    plt.grid(linewidth=0.3)
    plt.show()



if __name__=='__main__':
    col_names = ['XYZ_Price', 'MAD', 'TMA', 'Action', 'Action_Value', 'Stocks_Traded', 'Current_Balance', 'Stocks_Held', 'Net_Worth']
    results_df = pd.read_csv(DATA_FILE, header=None, names=col_names, index_col=False)
    results_df['Stocks_Held_Value'] = results_df['XYZ_Price'] * results_df['Stocks_Held']
    results_df.index = results_df.index+10
    
    plot_balances_and_net_worth(results_df)
    plot_normalized_lines(results_df[['TMA', 'XYZ_Price']])
    plot_normalized_lines(results_df[['Stocks_Held', 'TMA']])
    plot_normalized_lines(results_df[['MAD', 'XYZ_Price']])