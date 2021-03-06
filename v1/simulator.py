
# Cryptocurrency Market Simulator

from env import Coin
from portfolio import Portfolio
from random import randint
from enum import Enum

class Action(Enum):
    HOLD=0
    BUY=1
    SELL=2


class Simulator:
    def __init__(self, num_coins_per_order=1, 
        portfolio_cash=1000.0, 
        coin=Coin("ethereum"),
        features=["rolling_mean", "rolling_std", "sharpe_ratio", "bollinger_upper", "bollinger_lower"]):
        self.num_coins_per_order = num_coins_per_order
        self.coin = coin
        self.portfolio = Portfolio(portfolio_cash=portfolio_cash, coin=coin)
        self.features = features
    
    def get_current_state(self):
        return self.portfolio.getCurrentState(self.features)
    
    
    def get_current_holdings(self):
        return self.portfolio.getCurrentHoldings()
    

    def get_ran_action(self):
        return Action(randint(0,2))

    
    def act_and_step(self, action):
        #print 'Taking action:', action
        if action == Action.BUY:
            self.portfolio.buy(self.num_coins_per_order)
        elif action == Action.SELL:
            self.portfolio.sell(self.num_coins_per_order)

        state = self.get_current_state()
        reward = self.portfolio.getReturnsPercent()

        if self.portfolio.step() is False:
            return [state, reward, True]
        
        return [state, reward, False]
    
    
    def reset(self):
        self.portfolio.reset()
        
    
    def get_state_size(self):
        return len(self.get_current_state())

    def get_action_size(self):
        return len(Action)
    
    
    def plot_coin_price(self):
        self.coin.plot()