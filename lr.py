import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def eqn(m,c,x):
    y=m*x+c
    return y

def compute_costerr(m,c,df,al):
    t1=0
    t2 = 0
    for i in (np.array(df)):
        xi=i[0]
        yi=i[1]
        t1 = t1 + eqn(m, c, xi) - yi
        t2 = xi * (eqn(m, c, xi) - yi) + t2

    temp1=(1/float(len(df)))*t1
    temp2 = (1 / float(len(df))) * t2
    c=c-(al*temp1)
    m=m-(al*temp2)
    return [m,c]
def gradient_descent(m,c,df,prec):
    n_iter=1000

    while (n_iter!=0):
        m1=m
        c1=c
        [m,c]= compute_costerr(m, c, df, 0.00001)
        #print [m,c],n_iter
        n_iter=n_iter-1
    return [m,c]
 #   pass


lin_reg= pd.read_csv('test.csv',sep=",")
df=pd.DataFrame(lin_reg)[['LotFrontage','LotArea']].dropna()

df.plot(kind='scatter',x='LotFrontage',y='LotArea')
c = 0.0
m = 0.0

form=str(m)+'*x+'+str(c)
x = np.array(range(0,200))
y = eval(form)

cu= gradient_descent(m,c,df,0.0000001)
form=str(cu[0])+'*x+'+str(cu[1])
x = np.array(range(0,200))
y = eval(form)

plt.plot(x,y, linestyle='solid',color='red')
plt.show()
