import csv


dates = []
opens = []
highs = []
lows = []
closes = []
adj_closes = []
volumes = []

with open("sp_october.csv", "r") as data_file:
    data = csv.reader(data_file)
    for line in data:
        date = line[0]
        open_price = line[1]
        high_price = line[2]
        low_price = line[3]
        close_price = line[4]
        adj_close_price = line[5]
        volume = line[6]
                      
        
        dates.append(date)
        opens.append(open_price)
        highs.append(high_price)
        lows.append(low_price)
        closes.append(close_price)
        adj_closes.append(adj_close_price)
        volumes.append(volume)

print(closes)
print(dates)    
print(opens)    
print(highs)
print(lows)
print(closes)
print(adj_closes)
print(volumes)

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
