"""
Script for plotting the daily data of the fuzzy stock trading system.

@Author: Jordan Mata
@Date: October 6, 2022
"""

from cycler import cycler
import matplotlib.pyplot as plt
import os
import pandas as pd
from sklearn.metrics import jaccard_score

PACKAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
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
    plt.locator_params(nbins=4)
    plt.locator_params(axis='x', nbins=20)
    plt.xlabel("Day")
    plt.ylabel("Dollar Value")
    plt.grid(linewidth=0.3)
    plt.show()



def plot_normalized_lines_subplots(df_list):
    """Plot a list of dataframes as normalized line plots. Each dataframe is a separate plot. To plot
    all lines on the same chart, pass in a single dataframe with all desired columns.

    :param: df - list of dataframes, each containing the columns to plot. There should be one 
                    record for each day.
    """
    df_size = len(df_list)
    fig, ax = plt.subplots(df_size)
    fig.tight_layout()
    for i, df in enumerate(df_list):
        normalized_df = (df-df.min())/(df.max()-df.min())
        ax[i].set_prop_cycle(cycler(color=[COLOR_DICT.get(x, '#333333') for x in df.columns]))
        ax[i].plot(normalized_df)
        ax[i].locator_params(nbins=4)
        ax[i].locator_params(axis='x', nbins=20)
        ax[i].locator_params(axis='y', nbins=10)
        ax[i].set_xlabel("Day")
        ax[i].set_ylabel("Value (normalized to [0,1])")
        ax[i].grid(linewidth=0.3)
        ax[i].legend([col for col in df.columns.tolist()], loc="upper left")
    plt.show()



if __name__=='__main__':
    col_names = ['XYZ_Price', 'MAD', 'TMA', 'Action', 'Action_Value', 'Stocks_Traded', 'Current_Balance', 'Stocks_Held', 'Net_Worth']
    results_df = pd.read_csv(DATA_FILE, header=None, names=col_names, index_col=False)
    results_df['Stocks_Held_Value'] = results_df['XYZ_Price'] * results_df['Stocks_Held']
    results_df.index = results_df.index+10
    
    plot_balances_and_net_worth(results_df)
    plot_normalized_lines_subplots([results_df[['XYZ_Price']],
                                        results_df[['TMA']],
                                        results_df[['MAD']],
                                        results_df[['Stocks_Held']],])