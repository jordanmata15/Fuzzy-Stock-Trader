classdef StockTrader < handle
    %STOCKTRADER Fuzzy system to simulate a stock trader
    % 
    % The stock price on day 'i' is given by the static method XYZ(i)
    % The moving average divergence on day 'i' is given by MAD(i)
    % The 10 day moving average on day 'i' is given by TMA(i, 10)
    % We assume there is a correlation between MAD(i) and XYZ(i+1)
    % such that if MAD(i) is positive, XYZ(i+1) will generally increase
    % and if MAD(i) is negative, XYZ(i+1) will generally decrease.
    % Otherwise, there is no change.
    
    properties
        currentBalance;
        stocksHeld;
        fuzzySystem;
    end
    
    methods
        
        function obj = StockTrader(funding, fuzzySystemFile)
            %STOCKTRADER Construct an instance of this class
            obj.currentBalance = funding;
            obj.stocksHeld = 0;
            obj.fuzzySystem = readfis(fuzzySystemFile);
        end



        function [endingValue] = RunTradeSimulation(obj)
            %RUNTRADESIMULATION Runs the simulation over 100 days
            
            nDayAverage = 10;
            xyzMin = inf;
            xyzMax = -inf;
            madMin = inf;
            madMax = -inf;
            tmaMin = inf;
            tmaMax = -inf;
            
            for i = 1:100
                % calculate MAD and then normalize it between 0-1 
                % (based on what we've seen so far)
                mad = StockTrader.MAD(i);
                madMin = min(madMin, mad);
                madMax = max(madMax, mad);
                mad = StockTrader.Normalize(mad, madMin, madMax);
            
                % calculate XYZ and then normalize it between 0-1 
                % (based on what we've seen so far)
                xyz = StockTrader.XYZ(i);
                xyzMin = min(xyzMin, xyz);
                xyzMax = max(xyzMax, xyz);
                xyz = StockTrader.Normalize(xyz, xyzMin, xyzMax);
            
                % calculate TMA and then normalize it between 0-1 
                % (based on what we've seen so far)
                tma = StockTrader.TMA(i, nDayAverage);
                tmaMin = min(tmaMin, tma);
                tmaMax = max(tmaMax, tma);
                tma = StockTrader.Normalize(tma, tmaMin, tmaMax);
                
                % do not trade until we have a full set to average
                if i < nDayAverage
                    continue
                else
                    actionCrispValue = evalfis(obj.fuzzySystem, ...
                                               [mad, xyz, tma]);
                    obj.Trade(actionCrispValue, xyz);
                    fprintf("%0.2f\n", obj.currentBalance + xyz*obj.stocksHeld);
                end
            end

            stockValue = xyz*obj.stocksHeld;
            endingValue = obj.currentBalance + stockValue;
        end



        function Trade(obj, actionValue, xyz)
        %TRADE Executes a trade action based on the crisp value from the
        %fuzzy system output (actionValue between [0,1])
            
            fewPercent = 0.5;    
            manyPercent = 1;

            if actionValue < 0.20
                % SM
                if obj.stocksHeld > 0
                    unitsToSell = obj.stocksHeld * manyPercent;
                    obj.stocksHeld = obj.stocksHeld - unitsToSell;
                    obj.currentBalance = obj.currentBalance ...
                                            + (unitsToSell * xyz);
                end

            elseif actionValue < 0.40
                % SF
                if obj.stocksHeld > 0
                    unitsToSell = obj.stocksHeld * fewPercent;
                    obj.stocksHeld = obj.stocksHeld - unitsToSell;
                    obj.currentBalance = obj.currentBalance ...
                                            + (unitsToSell * xyz);
                end
            
            elseif actionValue < 0.60
                % DT
                % do nothing
            
            elseif actionValue < 0.80
                % BF
                if obj.currentBalance > 0
                    unitsToBuy = obj.currentBalance * fewPercent;
                    obj.stocksHeld = obj.stocksHeld + unitsToBuy;
                    obj.currentBalance = obj.currentBalance ...
                                            - (unitsToBuy * xyz);
                end
            
            else
                % BM
                if obj.currentBalance > 0
                    unitsToBuy = obj.currentBalance * manyPercent;
                    obj.stocksHeld = obj.stocksHeld + unitsToBuy;
                    obj.currentBalance = obj.currentBalance ...
                                            - (unitsToBuy * xyz);
                end
            end
        end

    end

  
    methods(Static)

        function [tma] = TMA(day, n)
        %TMA Calculates the moving average of XYZ stock over the past
        % 'n' days, starting on day 'day'
        %
        % If n>day then we take the average of the last 'day' days
        % Eg. TMA(10, 20) will take the moving average of the last 10
        % days only
            lower_bound = max(1, day-n+1);
            if lower_bound == 1
                n = day;
            end
            tma = 0;
            for i = lower_bound:day
                tma = tma + StockTrader.XYZ(i);
            end
            tma = tma/n;
        end


        function [mad] = MAD(i)
        %MAD Calculates the moving average divergence on day i
            rng(i); % ensure MAD and XYZ have same seed for given day
            r_i = -1+2*rand(1,1);
            eta_i = 0.5*r_i*mod(i,3);
            mad = 0.6*cos(0.4*i) - sin(0.5*i) + eta_i;
        end



        function [xyz] = XYZ(i)
        %XYZ Calculates the stock price of XYZ on day i
            rng(i); % ensure MAD and XYZ have same seed for given day
            r_i    = -1 + 2*rand(1,1);
            zeta_i = 0.6*r_i*mod(i,3);
            xyz    = 10 + 2.8*sin((2*pi*i)/19) ...
                        + 0.9*cos((2*pi*i)/19) ...
                        + zeta_i*0.014*i;
        end


        function [normalizedValue] = Normalize(val, min, max)
        %NORMALIZE Normalizes a value between a range of [min, max]
            range = max - min;
            normalizedValue = (val-min)/range;
        end

    end
end

