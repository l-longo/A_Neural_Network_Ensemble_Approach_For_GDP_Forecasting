def fluctuation_test(y1, y2, actual, q_p, m):
    L1 = (actual - y1)**2
    L2 = (actual - y2)**2
    dL = L2 - L1 
    dvar = np.sqrt( np.sum((dL[:] - np.mean(dL))**2) /P )
    
    F_stat = np.zeros(P-int(m/2)*2 + 1)       
    for j in range(int(m/2),P-int(m/2)+1):
        F_stat[j-int(m/2)] = (1/(dvar*np.sqrt(m))) * np.sum(dL[j-int(m/2):j+int(m/2)-1])
        
    return F_stat, dL
