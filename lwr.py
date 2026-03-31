import numpy as np
import matplotlib.pyplot as plt

def kernel(x,x_i,tau):
  return np.exp(-np.sum(x-x_i)**2/(2*tau**2))

def lwr(x_query,X,y,tau):
  m = X.shape[0]
  W = np.eye(m)

  for i in range(m):
    W[i,i] = kernel(x_query,X[i],tau)

  XTWX = X.T@W@X

  if np.linalg.det(XTWX) == 0:
    theta = np.linalg.pinv(XTWX@X.T@W@y)
  else:
    theta = np.linalg.inv(XTWX)@X.T@W@y

  return x_query@theta

np.random.seed(0)
x = np.linspace(0,10,100)
y = np.sin(x) + np.random.normal(0,0.2,100)


import pandas as pd

data_df = pd.DataFrame({'x':x,'y':y})
print("Generated synthetic dataset")
print(data_df.head(10).to_string(index=False))

X = np.vstack((np.ones(len(x)),x)).T
x_query_vals = np.linspace(0,10,300)
x_query = np.vstack((np.ones(len(x_query_vals)),x_query_vals)).T

tau = 0.5

y_pred = np.array([lwr(xq,X,y,tau) for xq in x_query])


plt.figure(figsize=(12,6))
plt.scatter(x,y,color='blue',label="Training data",alpha=0.6)
plt.plot(x_query_vals,y_pred,color='red',label = f"LWR predicton tau = {tau}",linewidth=2)

plt.title("LWR")
plt.xlabel("Input Feature",fontsize =12)
plt.ylabel("Target",fontsize =12)
plt.grid(True)
plt.legend()


#optional
plt.annotate(
    "Red Curve : LWR Prediction\nBlue:Nosiy Training data",
    xy = (7.5,np.sin(7.5)),
    xytext = (4,-1.5),
    textcoords= "data",
    fontsize = 12,
    color = "darkgreen",
    ha = "left",
    va = "top",
    bbox = dict(boxstyle = "round", pad = 0.4,fc = "wheat",ec='gray',alpha = 0.85),

)



plt.tight_layout()
plt.show()
