
def jensenalpha(ret_i, ret_rf, b, ret_m):
        jalpha = ret_i - (b * (ret_m - ret_rf) + ret_rf)
        return jalpha


def capm(ret_rf, b, er_m):
        er_i = ret_rf + (b * (er_m - ret_rf))
        return er_i


def alpha_fcn(ret_i, ret_m):
        alpha = ret_i - ret_m
        return alpha


def beta_fcn(covariance, variance):
        beta = covariance / variance
        return beta


