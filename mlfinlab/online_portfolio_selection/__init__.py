"""
Classes derived from Online Portfolio Selection module

"""
# Parent Method
from mlfinlab.online_portfolio_selection.online_portfolio_selection import OLPS
from mlfinlab.online_portfolio_selection.UP import UP
# Benchmarks
from mlfinlab.online_portfolio_selection.benchmarks.buy_and_hold import BuyAndHold
from mlfinlab.online_portfolio_selection.benchmarks.best_stock import BestStock
from mlfinlab.online_portfolio_selection.benchmarks.constant_rebalanced_portfolio import ConstantRebalancedPortfolio
from mlfinlab.online_portfolio_selection.benchmarks.best_constant_rebalanced_portfolio import BestConstantRebalancedPortfolio
# Momentum
from mlfinlab.online_portfolio_selection.momentum.exponential_gradient import ExponentialGradient
from mlfinlab.online_portfolio_selection.momentum.follow_the_leader import FollowTheLeader
from mlfinlab.online_portfolio_selection.momentum.follow_the_regularized_leader import FollowTheRegularizedLeader
# Mean Reversion
from mlfinlab.online_portfolio_selection.pattern_matching.CORN import CORN
from mlfinlab.online_portfolio_selection.mean_reversion.passive_aggressive_mean_reversion import PassiveAggressiveMeanReversion
from mlfinlab.online_portfolio_selection.mean_reversion.constant_weighted_mean_reversion import ConstantWeightedMeanReversion
from mlfinlab.online_portfolio_selection.mean_reversion.online_moving_average_reversion import OnlineMovingAverageReversion
# Pattern Matching
from mlfinlab.online_portfolio_selection.pattern_matching.CORN import CORN
from mlfinlab.online_portfolio_selection.pattern_matching.CORN_U import CORN_U
from mlfinlab.online_portfolio_selection.pattern_matching.CORN_K import CORN_K
from mlfinlab.online_portfolio_selection.pattern_matching.SCORN import SCORN
from mlfinlab.online_portfolio_selection.pattern_matching.SCORN_K import SCORN_K
from mlfinlab.online_portfolio_selection.pattern_matching.FCORN import FCORN
from mlfinlab.online_portfolio_selection.pattern_matching.FCORN_K import FCORN_K
