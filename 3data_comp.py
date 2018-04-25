import pandas as pd
import matplotlib.pyplot as plt

TXF=pd.read_csv('3dada.txt',sep="\t")
SGX=pd.read_csv('3data2.txt',sep="\t")
print(TXF)
TXF['P']=(TXF['P']-TXF['P'].min())/(TXF['P'].max()-TXF['P'].min())
SGX['P']=(SGX['P']-SGX['P'].min())/(SGX['P'].max()-SGX['P'].min())
fig = plt.figure()
plt.plot(TXF['T'], TXF['P'])
plt.plot(SGX['T'], SGX['P'])
#plt.gcf().autofmt_xdate()
##.autofmt_xdate()
##plt.xlim(0,18000)
##plt.ylim(0,30)
##plt.show()
##TXF.set_index('T').plot()
##SGX.plot()
plt.show()
