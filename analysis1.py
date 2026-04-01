import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv(r'D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\ad_spend_data.csv')
print(df.head(10))
print(df.shape)

# Explore Data
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Clean Data
df['c_date'] = pd.to_datetime(df['c_date'])
df['campaign_name'] = df['campaign_name'].str.lower()
df['category'] = df['category'].str.lower()
print(df.head())

df['ROI'] = (df['revenue'] - df['mark_spent']) / df['mark_spent'] * 100
df['CTR'] = df['clicks'] / df['impressions'] * 100
df['CPC'] = df['mark_spent'] / df['clicks']
df['ROAS'] = df['revenue'] / df['mark_spent']

print(df[['campaign_name', 'ROI', 'CTR', 'CPC', 'ROAS']].head())

campaign_performance = df.groupby('campaign_name')[['ROI', 'CTR', 'CPC', 'ROAS']].mean().round(2)
print(campaign_performance)

spend_revenue = df.groupby('campaign_name')[['mark_spent', 'revenue']].sum().round(2)


spend_revenue.reset_index().plot(kind='bar',
                                x='campaign_name',
                                y=['mark_spent','revenue'], 
                                color=['blue','green'],
                                figsize=(12,8))
plt.title('Amount Spent, Revenue vs Campaign Name')
plt.xlabel('Campaign Name')
plt.ylabel('Amount Spent, Revenue')
plt.tight_layout()
plt.show()

