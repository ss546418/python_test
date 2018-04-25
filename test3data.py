import pandas as pd
import matplotlib.pyplot as plt

t_data=pd.read_excel('3data_3.xlsx', sep=" ")
print(t_data)
t_data['STW_C']=(t_data['STW_C']-t_data['STW_C'].min())/(t_data['STW_C'].max()-t_data['STW_C'].min())
t_data['2330_C']=(t_data['2330_C']-t_data['2330_C'].min())/(t_data['2330_C'].max()-t_data['2330_C'].min())
t_data['TW_C']=(t_data['TW_C']-t_data['TW_C'].min())/(t_data['TW_C'].max()-t_data['TW_C'].min())

print(t_data)

t_data=t_data.drop('D', 1)
t_data.set_index('T').plot()
plt.legend()
plt.show()
