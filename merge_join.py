import pandas as pd

df1 = pd.DataFrame({'Year': [2005, 2006, 2007, 2000],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'Year': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year': [2005, 2009, 20010, 2004],
                    'Unemployment': [2, 3, 2, 2],
                    'Low_tier_HPI': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])

# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))
#
# df1.set_index('HPI', inplace=True)
# df3.set_index('HPI', inplace=True)
#
# joined = df1.join(df3)
# print(joined)


merged = pd.merge(df1, df3, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)
