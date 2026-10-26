def main():

    #__________________________________________________________________________
  
    # EXAMPLE: 1 => int (integer)
 
    # Bought 6 shares
    trade_one_net_position: int = 6
    print(f"trade_one_net_position: {trade_one_net_position}")
   
    # Sold 6 shares
    trade_two_net_position: int = -6
    print(f"trade_two_net_position: {trade_two_net_position}")
    #__________________________________________________________________________
    
    # EXAMPLE: 2 => float (floating point)

    # Positive trade result
    result_of_trade_one: float = 128.75
    print(f"result_of_trade_one: {result_of_trade_one}")

    # Negative trade result
    result_of_trade_two: float = -64.50
    print(f"result_of_trade_two: {result_of_trade_two}")
    #___________________________________________________________

    # EXAMPLE: 3 => bool (boolean)

    # Is the trading bot active?
    is_trading_bot_active: bool = True 
    print(f"is_trading_bot_active: {is_trading_bot_active}")

    # Has the trade reached the stop loss
    has_reached_stop_loss: bool = False
    print(f"has_reached_stop_loss: {has_reached_stop_loss}")
    #__________________________________________________________________________
    
    # EXAMPLE: 4 => str (string)

    # The name of the stock that you are trading.
    currently_trading: str = "NVDA"
    print(f"currently_trading: {currently_trading}")
    #__________________________________________________________________________
   
if __name__ == "__main__":
    main()
