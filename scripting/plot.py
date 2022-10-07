import matplotlib.pyplot as plt
import os
import pandas as pd

PACKAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
SCRIPTING_DIR = os.path.join(PACKAGE_DIR, "scripts")
DATA_DIR = os.path.join(PACKAGE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "data.csv")



def plot_balances_and_net_worth(df):
    df_value_columns = df[['Current_Balance', 'Stocks_Held_Value', 'Net_Worth']]
    df_value_columns.plot()
    plt.xlabel("Day")
    plt.ylabel("Dollar Value")
    plt.grid(linewidth=0.3)
    plt.show()


def plot_stock_held_and_price(df):
    df_value_columns = df[['Stocks_Held', 'XYZ_Price']]
    normalized_df = (df_value_columns-df_value_columns.min())/(df_value_columns.max()-df_value_columns.min())
    normalized_df.plot()
    plt.xlabel("Day")
    plt.ylabel("Value (normalized)")
    plt.grid(linewidth=0.3)
    plt.show()


def plot_stock_held_and_mad(df):
    df_value_columns = df[['Stocks_Held', 'MAD']]
    normalized_df = (df_value_columns-df_value_columns.min())/(df_value_columns.max()-df_value_columns.min())
    normalized_df.plot()
    plt.ylabel("Value (normalized)")
    plt.grid(linewidth=0.3)
    plt.show()


def plot_stock_held_and_tma(df):
    df_value_columns = df[['Stocks_Held', 'TMA']]
    normalized_df = (df_value_columns-df_value_columns.min())/(df_value_columns.max()-df_value_columns.min())
    normalized_df.plot()
    plt.xlabel("Day")
    plt.ylabel("Value (normalized)")
    plt.grid(linewidth=0.3)
    plt.show()


if __name__=='__main__':
    col_names = ['XYZ_Price', 'MAD', 'TMA', 'Action', 'Action_Value', 'Stocks_Traded', 'Current_Balance', 'Stocks_Held', 'Net_Worth']
    results_df = pd.read_csv(DATA_FILE, header=None, names=col_names, index_col=False)
    results_df['Stocks_Held_Value'] = results_df['XYZ_Price'] * results_df['Stocks_Held']
    plot_balances_and_net_worth(results_df)
    plot_stock_held_and_price(results_df)
    plot_stock_held_and_mad(results_df)
    plot_stock_held_and_tma(results_df)