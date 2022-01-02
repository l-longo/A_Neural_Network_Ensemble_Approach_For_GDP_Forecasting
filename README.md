# **A neural network ensemble approach for GDP forecasting**
Replication code for the paper: [A neural network ensemble approach for GDP forecasting](https://www.sciencedirect.com/science/article/abs/pii/S016518892100213X) (L. Longo, M. Riccaboni, A. Rungi), published in the Journal of Economic Dynamics and Control (2022).

The repository includes the following Python codes and functions:
* LSTM one quarter ahead forecast;
* DFM-GAS one quarter ahead forecast;
* Function to generate ensemble;
* Function for fluctuation test by [Giacomini, Rossi (2010)](https://onlinelibrary.wiley.com/doi/10.1002/jae.1177).


If you use the code or mention the work, please [cite](https://scholar.googleusercontent.com/scholar.bib?q=info:EdPFhWv2KosJ:scholar.google.com/&output=citation&scisdr=CgUWYz1QEKTDhy2Ffq8:AAGBfm0AAAAAYdGAZq9Vpe14Co5yJMKDgkAzFW4paXNw&scisig=AAGBfm0AAAAAYdGAZv8pg9qqXjnDGyg_GZ7HWbayYpdb&scisf=4&ct=citation&cd=-1&hl=en) the original published paper.


# One quarter ahead forecast
After running running codes for single models' prediction, you may save the vector of predicted GDP values (available in the data folder) and import in your Python console:

```
data = pd.read_excel('gdp.xlsx',index_col=0).dropna()[1:]
dfm-gas = pd.read_excel('gaspred+1ur_rw.xlsx', index_col = 0)
lstm = pd.read_excel('lstm+1.xlsx', index_col = 0)
```

In order to run ensemble you have to upload in-sample estimates of the models:
```
dfm-gas_insample = pd.read_excel('in_sample_dfm.xlsx', index_col = 0).in_sample
lstm_insample = pd.read_excel('in_sample_lstm.xlsx', index_col = 0).pred
lstm_insample.index = var_insample.index
```
And then you concatenate:
```
totpred.insert(loc=1,column='LSTM+1',value=pd.concat([lstm_insample,lstm['LSTM+1']])) 
totpred.insert(loc=2,column='DFM_GAS',value=pd.concat([var_insample,var.pred])) 
```
To obtain ensemble prediction and weights:
```
we_dfm, we_nn, ensemble = ensemble(totpred['LSTM+1'], 
                                   totpred['DFM_GAS'], totpred['GDPR'], 40, lstm.shape[0])
```
