# Fuzzy-Stock-Trader

# General
The program is designed to run a simulation of a stock trader over 360 days. The stock trading simulation uses fuzzy logic inference to determine whether we should buy few/many, sell few/many, or not trade at all.

The inputs to the fuzzy system are:
- TMA(i) - ten day moving average on day i
- MAD(i) - mean average divergence on day i
- XYZ(i) - price of stock XYZ on day i

There is a general correlation in MAD such that if MAD(i) is positive, then the XYZ(i+1) > XYZ(i). If MAD(i) is negative, then XYZ(i+1) < XYZ(i). Otherwise, there is no likely change.  This doesn't necessarily always hold.

## Note:
Both XYZ and MAD depend on a random integer based on the day. Therefore, they are both seeded with the day to make sure they have the same random value.

# Usage
1. open the ./src folder as the project in matlab
2. type `main` into the command window
3. view output
4. (Optional) copy the output to data/data.csv
5. (Optional) run scripting/plot.py to generate the plots

# Output
Each day has one line of output. The output for each day is comma delimited and is formatted as follows:
```
XYZ_Price, MAD, TMA, Action, Action_Value, Stocks_Traded, Current_Balance, Stocks_Held, Net_Worth
```
For example, the last day of data looks like:
```
9.94, 1.32, 8.78, DT, 0.50, 0.00, 106284.59, 300.00, 109267.21
```

# Folder Structure
- src - Contains the fuzzy inference system as well as the simulation logic.
- data - Contains the data output of our inference system (daily TMA, XYZ price, MAD, etc). Also contains the plots generated.
- scripting - Contains the script needed to plot the daily data for easy visualiztion.
