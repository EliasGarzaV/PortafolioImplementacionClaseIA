import numpy as np

def evaluate_model_calssification(real, pred):
  vp, vn, fp, fn = 0,0,0,0
  
  for p, r in zip(pred, real):
    if(p and r):
      vp += 1
    elif(not p and not r):
      vn += 1
    elif(not p and r):
      fn += 1
    else:
      fp += 1
      
  return vp, vn, fp, fn

def get_metrics_classification(vp, vn, fp, fn):
    acc = (vp + vn) / (vp + vn + fp + fn) 
    prec = vp / (vp + fp) 
    rec = vp / (vp + fn)
    f1 = (2*prec*rec) / (prec + rec)
    
    return acc, prec, rec, f1

def get_metrics_regression(real, pred):
  mae = np.mean(np.abs(real - pred))
  mape = np.mean(np.abs(real - pred) / real)
  mse = np.mean((real - pred)**2)
  
  return mse, mae, mape