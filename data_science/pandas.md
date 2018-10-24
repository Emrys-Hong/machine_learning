Read [10mins panda tutorial](https://pandas.pydata.org/pandas-docs/stable/10min.html) for 10 mins for a general knowledge of pandas


## input/output data from excel
```
# input data
data = pd.read_csv('student.csv')

# output data
data.to_excel('path/to/excel')
# set index=False to ignore index
```
## convert dataframe to dictionary and convert back
```
# convert df to dictionary
dict = df.to_dict()

# convert dict to dataframe
df = pd.DataFrame(dict,index=[list of index])
```

## concat df
```
# concat vertically
df = pd.concat([df1, df2], axis = 0) # default zero to let them concat along
```

## get value
```
df.get_value(index, column)
```

## drop row or column
```
df.drop(['B', 'C'], axis=1)
## inplace = True for inplace
df.drop([0, 1])
```
