from twython import Twython
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plot_ABH
import plot_nutella_biscuits

counter_ABH= plot_ABH.calculate_counter()
counter_nutella_biscuits= plot_nutella_biscuits.calculate_counter()

plt.plot(counter_ABH.keys(), counter_ABH.values(), label='ABH')
plt.plot(counter_nutella_biscuits.keys(), counter_nutella_biscuits.values(), label="nutella biscuits")
plt.legend()
plt.xlabel('date')
plt.ylabel('numero tweets')
plt.show()