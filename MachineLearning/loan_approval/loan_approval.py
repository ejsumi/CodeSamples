import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('loan_approval/loan_approval_data.csv')

# fix: mode computed on full df (including the 2 held-out prediction rows) leaked prediction data into training stats
train_mask = df['Loan_Approved'].notna()
df['Self_Employed'] = df['Self_Employed'].fillna(df.loc[train_mask, 'Self_Employed'].mode()[0])
#print(df.info())

catg_cols = ['Gender', 'Married','Education','Self_Employed','Property_Area']
encoder = LabelEncoder()
df[catg_cols] = df[catg_cols].apply(encoder.fit_transform)

num_cols = ['ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term']  # fix: Credit_History is a binary flag, not a continuous value to scale
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

df_pred= df.tail(2).copy()
df = df.iloc[:-2]
#print(df_pred)

X = df.drop(columns=['Loan_Approved'])
y = df['Loan_Approved']

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)  # fix: hyperparameters were missing, spec requires n_estimators=150, max_depth=10
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("accuracy : ",accuracy_score(y_test,y_pred))
#print(df_pred)
x_target = df_pred.drop(columns=['Loan_Approved'])
y_target = model.predict(x_target)

print(y_target)