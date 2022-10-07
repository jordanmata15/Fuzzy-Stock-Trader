classdef Action
    %ACTION Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        actionTaken;
        actionValue;
        price;
        quantity;
        currentBalance;
        stocksHeld;
    end
    
    methods
        function obj = Action(actionTaken, actionValue, price, quantity, currentBalance, stocksHeld)
            %ACTION Construct an instance of this class
            %   Detailed explanation goes here
            obj.actionTaken = actionTaken;
            obj.actionValue = actionValue;
            obj.price = price;
            obj.quantity = quantity;
            obj.currentBalance = currentBalance;
            obj.stocksHeld = stocksHeld;
        end
        
        function print(obj)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            fprintf("%s, %0.2f, %0.2f, %0.2f, %0.2f, %0.2f\n", obj.actionTaken, ...
                                                                obj.actionValue, ...
                                                                obj.price, ...
                                                                obj.quantity, ...
                                                                obj.currentBalance, ...
                                                                obj.stocksHeld);
        end
    end
end

