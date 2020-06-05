import pandas as pd
import numpy as np
import pickle
import datetime


if __name__ == '__main__':
        model_final=pd.read_csv('prediction (1).csv')
        #print(model_final)
        #print(model_final['Date'])
        #print(model_final.dtypes)
        date_time = '2020-06-02'
        #print(type(date_time))
        x=model_final[model_final['Date']==date_time]
        #print(model_final[model_final['Date']==date_time])
        print(x)
        print("Active")
        a=x.iloc[0][2]
        print(a)
        print("death")
        b=x.iloc[0][3]
        print(b)
        print("recovered")
        c=x.iloc[0][4]
        print(c)	
        #format = '%Y-%m-%d' # The format 
        #datetime_str = datetime.datetime.strptime(date_time, format) 
        #print((datetime_str).date())
        #Sprint(type((datetime_str)))
        
        
	
# Driver code 
    
#print(dater)
    
