classdef Action
    %ACTION Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        price;
        mad;
        tma;
        actionTaken;
        actionValue;
        quantityTraded;
        currentBalance;
        stocksHeld;
    end
    
    methods
        function obj = Action(price, mad, tma, actionTaken, actionValue, ...
                                quantity, currentBalance, stocksHeld)
            %ACTION Construct an instance of this class
            %   Detailed explanation goes here
            obj.price = price;
            obj.mad = mad;
            obj.tma = tma;
            obj.actionTaken = actionTaken;
            obj.actionValue = actionValue; 
            obj.quantityTraded = quantity;
            obj.currentBalance = currentBalance;
            obj.stocksHeld = stocksHeld;
        end
        
        function print(obj)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            fprintf("%0.2f, %0.2f, %0.2f, %s, %0.2f, %0.2f, %0.2f, %0.2f, %0.2f\n", ...
                    obj.price, ...
                    obj.mad, ...
                    obj.tma, ...
                    obj.actionTaken, ...
                    obj.actionValue, ...
                    obj.quantityTraded, ...
                    obj.currentBalance, ...
                    obj.stocksHeld, ...
                    obj.currentBalance + (obj.stocksHeld*obj.price));
        end
    end
end

