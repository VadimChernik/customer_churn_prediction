import pickle

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

output_file = 'model.bin'
seed = 42

df = pd.read_excel('data/ecommerce_dataset.xlsx',sheet_name='E Comm')

df.columns = df.columns.str.lower().str.replace(' ', '_')

del df['customerid']

df['tenure'] = df['tenure'].fillna(value=df['tenure'].median())
df['warehousetohome'] = df['warehousetohome'].fillna(value=df['warehousetohome'].median())
df['hourspendonapp'] = df['hourspendonapp'].fillna(value=df['hourspendonapp'].median())
df['orderamounthikefromlastyear'] = df['orderamounthikefromlastyear'].fillna(value=df['orderamounthikefromlastyear'].median())
df['couponused'] = df['couponused'].fillna(value=df['couponused'].median())
df['ordercount'] = df['ordercount'].fillna(value=df['ordercount'].median())
df['daysincelastorder'] = df['daysincelastorder'].fillna(value=df['daysincelastorder'].median())

df.loc[df['preferredpaymentmode'] == 'COD', 'preferredpaymentmode'] = 'Cash on Delivery'
df.loc[df['preferredpaymentmode'] == 'CC', 'preferredpaymentmode'] = 'Credit Card'
df.loc[df['preferredlogindevice'] == 'Phone', 'preferredlogindevice'] = 'Mobile Phone'
df.loc[df['preferedordercat'] == 'Mobile', 'preferedordercat'] = 'Mobile Phone'

numerical = ['tenure', 'warehousetohome', 'hourspendonapp','numberofdeviceregistered', 
             'numberofaddress', 'orderamounthikefromlastyear', 'couponused', 'ordercount',
             'daysincelastorder', 'cashbackamount']

categorical = ['citytier','preferredlogindevice', 'preferredpaymentmode',
               'satisfactionscore', 'gender', 'complain', 'preferedordercat', 
               'maritalstatus']

for col in categorical:
  df[col] = df[col].astype(str)

df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=seed)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=seed)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train["churn"]
y_val = df_val["churn"]
y_test = df_test["churn"]

del df_train["churn"]
del df_val["churn"]
del df_test["churn"]

def train(df_train, y_train):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = RandomForestClassifier(n_estimators=100,
                                   max_depth=15,
                                   min_samples_leaf=1,
                                   random_state=seed)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')
    X = dv.transform(dicts)
    y_pred = model.predict_proba(X)[:, 1]

    return y_pred

dv, model = train(df_train, y_train)

y_pred = predict(df_test, dv, model)
auc = roc_auc_score(y_test, y_pred)

with open(output_file, "wb") as f_out:
    pickle.dump((dv, model), f_out)
