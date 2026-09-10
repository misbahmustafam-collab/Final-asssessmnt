print("Final Assessment projects")
import numpy as np
data=np.genfromtxt("clean_final_data.csv", delimiter=",", skip_header=1, usecols=(0,1,2))
print(data)
price=data[:,1]
print("clean_final_data.csv:",np.mean(price))
print("clean_final_data.csv:",np.median(price))
print("clean_final_data.csv:",np.std(price))
print("clean_final_data.csv:",np.min(price))
print("clean_final_data.csv:",np.max(price))

print("clean_final_data.csv:",np.square(price))
print("clean_final_data.csv:",np.sqrt(price))
print("clean_final_data.csv:",np.power(price,price))


long=data[:,0]
lat = data[:, 1]
lat = data[:, 1]
addition = long + lat
print("clean_final_data.csv:", addition)

subtraction=long-lat
print("clean_final_data.csv:", subtraction)

multiplication=long*lat
print("clean_final_data.csv:", multiplication)

division=long/long
print("clean_final_data.csv:", division)

# trigonometric function
pricepie = price / np.pi + 1
# calculate sine cosine tangent
sine_values = np.sin(pricepie)
cosine_values = np.cos(pricepie)
tangent_values = np.tan(pricepie)
print("clean_final_data.csv:", sine_values)
print("clean_final_data.csv:", cosine_values)
print("clean_final_data.csv:", tangent_values)


#calculate the natural logarthim and base 10 logarthim
log_array=np.log(pricepie)
log10_array=np.log10(pricepie)

print("clean_final_data.csv:", log_array)
print("clean_final_data.csv:", log10_array)

# Example:Hyperbolic sine
#calculate the hyperbolic sine of each element
sinh_values=np.sinh(pricepie)
print("clean_final_data.csv:", sinh_values)

#Example : Hyperbolic cosine
#calculate the hyperbolic cosine of each element
cosnh_values=np.cosh(pricepie)
print("clean_final_data.csv:", cosnh_values)


#Example : Hyperbolic tangent
#calculate the hyperbolic tangent of each element
tanh_values=np.tanh(pricepie)
print("clean_final_data.csv:", tanh_values)

#inverse Hyperbolic tangent
#calculate the inverse hyperbolic tangent
tanh_values=np.tanh(pricepie)
print("clean_final_data.csv:", tanh_values)
#inverse hyperbolic sine
#calculate the inverse hyperbolic sine
asinh_values=np.arcsinh(pricepie)
print("clean_final_data.csv:", asinh_values)


#inverse hyperbolic cosine
#calculate the inverse cosine
acosh_values=np.arccosh(pricepie)
print("clean_final_data.csv:", acosh_values)


#2dimentional array
D2longlat=np.array([long,lat])


print("clean_final_data.csv:", D2longlat)
print("clean_final_data.csv:", D2longlat.ndim)

#output 2
#return total number of elements
print("clean_final_data.csv:", D2longlat.size)

#output 6
#return a tuple that gives the size of array in each dimention
print("clean_final_data.csv:", D2longlat.shape)

#splicing array
D2longlatslice=D2longlat[0:1:1,1:3:1]
print("clean_final_data.csv:", D2longlat)


#indexing array
D2longlatsliceItemOnly=D2longlatslice[0,1]
print("clean_final_data.csv:", D2longlatsliceItemOnly)


#you should use built in function nidter, if you don't need to have the indexes values
for elem in np.nditer(D2longlat):print(elem)


import pandas as pd
df=pd.read_csv("clean_final_data.csv")
print(df)
print("df-data types",df.dtypes)
print("df.info():",df.info())
#display last three rows
print("last three roww")
print(df.tail(3))

#display first three rows
print("first three rows")
print(df.head(3))

#display first three coulmns
print("first three coulmns")
print(df.head(3))

#display last three coulmns
print("last three coulmns")
print(df.tail(3))


#summary of statistics of dataframe using describes () method
print("summary of statistics of dataframe using describes()method:",df.describe())


#counting the rows and coulmns in dataframe using shape()it return the no of rows and coulmns enclosed in a tuple
print("counting the rows and coulmns in dataframe using shape():",df.shape)
print()

#selecting a single row using .loc
second_row=df.loc[1]
print("selecting a single row using .loc")
print(second_row)
print()


#selecting multiple rows using .loc
second_rows2=df.loc[[1,3]]
print("selecting multiple rows using .loc")
print(second_rows2)
print()

#selecting a slice of rows using .loc
second_row3=df.loc[1:5]
print("selecting a slice of rows using .loc")
print(second_row3)
print()


#access multiple coulmns
bed=df[['OrderID']]
print("access multiple coulmns:df:")
print(bed)
print()

#selecting a single coulmn using .loc
second_row5=df.loc[:1, 'OrderID']
print("selecting a single coulmn using .loc")
print(second_row5)
print()

#selecting multiple coulmns using .loc
second_row6=df.loc[:, ['OrderID']]
print("#selecting multiple coulmns using .loc")
print(second_row6)
print()



#selecting a single row using .iloc
second_row=df.iloc[1]
print("selecting a single row using .iloc")
print(second_row)
print()



#Selecting multiple rows using .iloc
second_row2 = df.iloc[[1, 3, 5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()



#Selecting a slice of rows using .iloc
second_row3 = df.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()



#Combined row and column selection using .iloc
second_row8 = df.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Let's read the CSV file and package it into a DataFrame:
df = pd.read_csv('clean_final_data.csv')
import pandas as pd

# Convert Date string to datetime
df['CustomerID'] = pd.to_datetime(df['CustomerID'])
df['SignupDate'] = pd.to_datetime(df['SignupDate'])

# Create numeric features
df['year'] = df['CustomerID'].dt.year
df['month'] = df['CustomerID'].dt.month
df['day'] = df['CustomerID'].dt.day
df['month'] = pd.to_datetime(df['SignupDate']).dt.month
df['day'] = pd.to_datetime(df['SignupDate']).dt.day

# Remove original Date column
df = df.drop('CustomerID', axis=1)

print(df.dtypes)
print(df.corr(numeric_only=True))

#Once the data is loaded in, let's take a quick peek at the first 5 values using the head() method:
print(df.head())
print(dtypes := df.dtypes)
#We can also check the shape of our dataset via the shape property:
print(df.columns.tolist())

plt.show()

print("df.corr():        " , df.corr(numeric_only=True))


print("df.describe():                    " , df.describe())
print(df.columns.tolist())
X = df[['Quantity']]
y = df['Quantity']

print("X:")
print(X)

print("y:")
print(y)

print("X:")
print(X)

print("y:")
print(y)

print(df['PaymentMethod'].values) # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
print(df['PaymentMethod'].values.shape) # (25,)

print(X.shape) # (25, 1)
print(X)      # [[2.5] [5.1]  [3.2] ... ]
SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)


print(X_train) # [[2.7] [3.3] [5.1] [3.8] ... ]
print(y_train) # [[25] [42] [47] [35] ... ]


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# Remove missing values before training
X_train = X_train.fillna(X_train.mean())
X_test = X_test.fillna(X_test.mean())

y_train = y_train.fillna(y_train.mean())
y_test = y_test.fillna(y_test.mean())

# Train model
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
def calc(slope, intercept, Temp_max):
    return slope*Temp_max+intercept

score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) 
score = regressor.predict([[9.5]])
print(score) # 94.80663482
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = ''
df = pd.read_csv('clean_final_data.csv')
import pandas as pd

# Convert Date string to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create numeric features
df['year'] = df['OrderDate'].dt.year
df['month'] = df['OrderDate'].dt.month
df['day'] = df['OrderDate'].dt.day

# Remove original Date column
df = df.drop('OrderDate', axis=1)

print(df.dtypes)
print(df.corr(numeric_only=True))

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)

class seaborn_native:
    """Concrete seaborn-like plotting API used by the script."""

    @staticmethod
    def set(*args, **kwargs):
        import seaborn as sns
        return sns.set(*args, **kwargs)

    @staticmethod
    def boxplot(*args, **kwargs):
        import seaborn as sns
        return sns.boxplot(*args, **kwargs)

    @staticmethod
    def heatmap(*args, **kwargs):
        import seaborn as sns
        kwargs.setdefault("annot", True)
        return sns.heatmap(*args, **kwargs)

    @staticmethod
    def displot(*args, **kwargs):
        import seaborn as sns
        return sns.displot(*args, **kwargs)

    @staticmethod
    def lineplot(*args, **kwargs):
        import seaborn as sns
        return sns.lineplot(*args, **kwargs)

    @staticmethod
    def catplot(*args, **kwargs):
        import seaborn as sns
        return sns.catplot(*args, **kwargs)


class sns_module:
    """Concrete seaborn wrapper with the plotting APIs used in this script."""

    @staticmethod
    def set(*args, **kwargs):
        return seaborn_native.set(*args, **kwargs)

    @staticmethod
    def boxplot(*args, **kwargs):
        return seaborn_native.boxplot(*args, **kwargs)

    @staticmethod
    def heatmap(*args, **kwargs):
        return seaborn_native.heatmap(*args, **kwargs)

    @staticmethod
    def displot(*args, **kwargs):
        return seaborn_native.displot(*args, **kwargs)

    @staticmethod
    def lineplot(*args, **kwargs):
        return seaborn_native.lineplot(*args, **kwargs)

    @staticmethod
    def catplot(*args, **kwargs):
        return seaborn_native.catplot(*args, **kwargs)


class sns(sns_module):
    """Backward-compatible alias used by the rest of the script."""

    @staticmethod
    def set(*args, **kwargs):
        import seaborn as Quantity
        return seaborn_native.set(*args, **kwargs)

    @staticmethod
    def boxplot(*args, **kwargs):
        import seaborn as Quantity
        return seaborn_native.boxplot(*args, **kwargs)

    @staticmethod
    def heatmap(*args, **kwargs):
        import seaborn as seaborn_library
        kwargs.setdefault("annot", True)
        return seaborn_library.heatmap(*args, **kwargs)

    @staticmethod
    def displot(*args, **kwargs):
        import seaborn as seaborn_library
        return seaborn_library.displot(*args, **kwargs)

    @staticmethod
    def lineplot(*args, **kwargs):
        import seaborn as seaborn_library
        return seaborn_library.lineplot(*args, **kwargs)

    @staticmethod
    def catplot(*args, **kwargs):
        import seaborn as seaborn_library
        return seaborn_library.catplot(*args, **kwargs)


# Regression plots for BigMart dataset

variables = ['Quantity']

df['CustomerSegment'] = pd.qcut(
    df['OrderValue'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

for var in variables:
    sns.boxplot(x='CustomerSegment', y=var, data=df)
    plt.title(f'{var} vs Customer Segment')
    plt.show()
correlations = df.corr(numeric_only=True)
print("correlations...\n" , correlations)
# annot=True displays the correlation values
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Wind Speed (km/h) - Temperature (C)')
# Display the plot
plt.show()
read = input("Wait for me....")

# BigMart Regression Variables

X = df[['Quantity']]
y = df['Quantity']

# Remove missing values
data = pd.concat([X, y], axis=1).dropna()
print(df.columns)
X = df[['Quantity']]
y = df['Quantity']

print("X:")
print(X)

print("y:")
print(y)

SEED = 200
#After setting our X and y sets, we can divide our data into train and test sets. We will be using the same seed and 20% of our data for training:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

#After splitting the data, we can train our multiple regression model. Notice that now there is no need to reshape our X data, once it already has more than one dimension:
print("X.shape # (48, 4):     \n", X.shape )   

from sklearn.base import BaseEstimator, RegressorMixin


class regressor(BaseEstimator, RegressorMixin):
    """Ordinary least-squares regressor with a scikit-learn compatible API."""

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        if X.ndim != 2 or len(X) != len(y) or len(X) == 0:
            raise ValueError("X must be a non-empty 2D array matching y")
        coefficients = np.linalg.lstsq(
            np.column_stack((np.ones(len(X)), X)), y, rcond=None
        )[0]
        self.intercept_ = float(coefficients[0])
        self.coef_ = coefficients[1:]
        self.n_features_in_ = X.shape[1]
        return self

    def predict(self, X):
        if not hasattr(self, "coef_"):
            raise RuntimeError("Fit the regressor before predicting")
        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(-1, self.n_features_in_)
        if X.ndim != 2 or X.shape[1] != self.n_features_in_:
            raise ValueError("X has an unexpected number of features")
        return self.intercept_ + X @ self.coef_

    def score(self, X, y):
        y = np.asarray(y, dtype=float).reshape(-1)
        residuals = y - self.predict(X)
        total = np.sum((y - y.mean()) ** 2)
        return 1.0 - np.sum(residuals ** 2) / total if total else 0.0


regressor = regressor()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

#After fitting the model and finding our optimal solution, we can also look at the intercept:
print("regressor.intercept_......\n", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef_ " , regressor.coef_)


feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Coefficient'])
print(coefficients_df)


#In the same way we had done for the simple regression model, let's predict with the test data:
y_pred = regressor.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')

actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)
import numpy as np
import  pandas as pd
import seaborn as sns_module
import matplotlib.pyplot as plt


class seaborn_library:
    """Concrete facade for the seaborn plotting methods used below."""

    @staticmethod
    def set(*args, **kwargs):
        return sns_module.set(*args, **kwargs)

    @staticmethod
    def displot(*args, **kwargs):
        return sns_module.displot(*args, **kwargs)

    @staticmethod
    def lineplot(*args, **kwargs):
        return sns_module.lineplot(*args, **kwargs)

    @staticmethod
    def catplot(*args, **kwargs):
        return sns_module.catplot(*args, **kwargs)

    @staticmethod
    def boxplot(*args, **kwargs):
        return sns_module.boxplot(*args, **kwargs)

    @staticmethod
    def heatmap(*args, **kwargs):
        kwargs.setdefault("annot", True)
        return sns_module.heatmap(*args, **kwargs)


class sns:
    """Compatibility wrapper ensuring the plotting helper methods are available."""

    @staticmethod
    def set(*args, **kwargs):
        return seaborn_library.set(*args, **kwargs)

    @staticmethod
    def displot(*args, **kwargs):
        return seaborn_library.displot(*args, **kwargs)

    @staticmethod
    def lineplot(*args, **kwargs):
        return seaborn_library.lineplot(*args, **kwargs)

    @staticmethod
    def catplot(*args, **kwargs):
        return seaborn_library.catplot(*args, **kwargs)

    @staticmethod
    def boxplot(*args, **kwargs):
        return seaborn_library.boxplot(*args, **kwargs)

    @staticmethod
    def heatmap(*args, **kwargs):
        return seaborn_library.heatmap(*args, **kwargs)



df = pd.read_csv('clean_final_data.csv')
df['CustomerSegment'] = pd.qcut(
    df['OrderValue'],
    q=3,
    labels=['Low', 'Medium', 'High']
)
print(df.dtypes)
diffilter=df.head(30)
diffilter50=df.head(50)

sns.set(style="whitegrid")
g = sns.displot(data=diffilter, x="Quantity", y="Discount")
g.figure.suptitle("sns.displot(data=diffilter, x='Quantity', y='Discount')")
# display plot
g.figure.show()
read = input('wait')
g = sns.lineplot(
    data=df,
    x="Status",
    y="City",
    hue="CustomerSegment",
    marker="o"
)

plt.show()
cat_fig = sns.catplot(data=diffilter, x="Quantity", y="Discount", hue="Status")
cat_fig.fig.suptitle("sns.catplot(data=diffilter, x='Quantity', y='Discount', hue='Status')")
plt.show()

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

#load dataset
pima=pd.read_csv("clean_final_data.csv", header=0)
print(pima.columns)
feature_cols=['CustomerID','ProductID','Quantity']
target_col='OrderValue'
print(pima.columns)
X = pima[feature_cols]
y = pima[target_col]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
#clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus
dot_data=StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=feature_cols,
    class_names=[str(c) for c in clf.classes_]
)
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetesv1.png')
Image(graph.create_png())

""""Well, the classification rate increased to 77.05%, which is better accuracy than the previous model."""


from six import StringIO 
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols,class_names=[str(c) for c in clf.classes_])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetesV2.png')
Image(graph.create_png())


input("Wait for me...")