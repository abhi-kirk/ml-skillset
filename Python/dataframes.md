## Dataframes

### Replace `null` values in column `Col`:
- With `mean`:
```python
df.loc[df['Col'].isnull(), 'Col'] = np.round(df['Col'].mean())
```
- With `mode`:
```python
df.loc[df['Col'].isnull(), 'Col'] = df['Col'].value_counts().index[0]
```

### Sampling:
- Shuffle entire dataset:
```python
df = df.sample(frac=1, random_state=42)
```
- Bootstrap dataframe `X` (choose same number of rows with replacement):
```python
n_rows = X.shape[0]
bs_indices = np.random.choice(
    range(n_rows), 
    n_rows,
    replace=True 
)
X_bs = X.iloc[bs_indices, :]
```

