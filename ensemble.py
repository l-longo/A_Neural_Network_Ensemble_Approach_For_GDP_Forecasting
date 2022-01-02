def ensemble(y1, y2, actual, p, in_sample_shape):
    we_dfm = np.zeros(totpred.shape[0])
    we_nn = np.zeros(totpred.shape[0])
    ensemble = np.zeros(totpred.shape[0])
    for i in range(in_sample_shape - 1,totpred.shape[0] - 1):
        mse_nn=1/(np.sum(y1[i-p:i+1]-actual[i-p:i+1])**2)
        mse_dfm=1/(np.sum(y2[i-p:i+1]-actual[i-p:i+1])**2)
        mse_sum = mse_dfm + mse_nn
        we_dfm[i+1] = mse_dfm/mse_sum 
        we_nn[i+1] = mse_nn/mse_sum 
        ensemble[i] = y1[i]*we_nn[i] + y2[i]*we_dfm[i]
        if i == 198:
            ensemble[i+1] = y1[i+1]*we_nn[i]  + y2[i+1]*we_dfm[i] 
    
    return we_dfm, we_nn, ensemble
