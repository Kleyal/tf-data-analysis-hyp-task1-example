import pandas as pd
import numpy as np


chat_id = 405993924 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    significance_level = 0.06
    res = proportions_ztest([x_success, y_success],[x_cnt, y_cnt], alternative = 'larger')
    return res[1] < significance_level
