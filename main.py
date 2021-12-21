import pandas as pd
from IR_phase1 import IR
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    data = pd.read_excel(r'IR.xlsx')
    content = data['content'].tolist()
    titles = data['title'].tolist()
    weighted_posting_list = IR().get_weighted_posting_list(content)
    print(weighted_posting_list)