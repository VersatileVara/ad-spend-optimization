import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\ad_spend_data.csv")

#Check the details first 5 rows
print(df.head())

#Check the shape of the matrix
print(df.shape)

# Check missing values
print(df.isnull().sum())

# Basic statistics
print(df.describe())

# Column names, data types, memory
print(df.info())

# Convert date column to datetime
df['c_date'] = pd.to_datetime(df['c_date'])

# Verify
print(df.dtypes)
print(df.head())

# Fix inconsistent casing in campaign_name
df['campaign_name'] = df['campaign_name'].str.lower()
df['category'] = df['category'].str.lower()

# Verify
print(df['campaign_name'].unique())

df['ROI'] = (df['revenue'] - df['mark_spent']) / df['mark_spent'] * 100
df['CTR'] = df['clicks'] / df['impressions'] * 100
df['CPC'] = df['mark_spent'] / df['clicks']
df['ROAS'] = df['revenue'] / df['mark_spent']

print(df[['campaign_name', 'ROI', 'CTR', 'CPC', 'ROAS']].head())

campaign_performance = df.groupby('campaign_name')[['ROI', 'CTR', 'CPC', 'ROAS']].mean().round(2)

plt.figure(figsize=(12, 7))
colors = ['green' if x > 0 else 'red' for x in campaign_performance['ROI']]
plt.barh(campaign_performance.index, campaign_performance['ROI'], color=colors)
plt.axvline(x=0, color='black', linewidth=0.8, linestyle='--')
plt.title('ROI by Campaign:: Green = Profitable, Red = Loss', fontsize=14)
plt.xlabel('ROI (%)')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\roi_by_campaign.png")
plt.show()

# Group by category and find average metrics
category_performance = df.groupby('category')[['ROI', 'CTR', 'CPC', 'ROAS']].mean().round(2)

plt.figure(figsize=(10, 6))
sns.barplot(data=category_performance.reset_index(), 
            x='category', y='ROI', palette='Blues_d')
plt.title('Average ROI by Ad Channel Category')
plt.xlabel('Category')
plt.ylabel('ROI (%)')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\roi_by_category.png")
plt.show()

plt.figure(figsize=(12, 7))
sns.barplot(data=campaign_performance.reset_index(), 
            x='ROAS', y='campaign_name', palette='RdYlGn')
plt.axvline(x=1, color='black', linewidth=0.8, linestyle='--')
plt.title('ROAS by Campaign — Above 1x means Profitable', fontsize=14)
plt.xlabel('ROAS (Revenue per ₹1 Spent)')
plt.tight_layout()
plt.savefig(r'D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\/roas_by_campaign.png')
plt.show()

spend_revenue = df.groupby('campaign_name')[['mark_spent', 'revenue']].sum().round(2)
print(spend_revenue)


spend_revenue.reset_index().plot(kind='bar', 
                                  x='campaign_name',
                                  y=['mark_spent', 'revenue'],
                                  color=['#FF6B6B', '#4CAF50'],
                                  figsize=(12, 8))
plt.title('Marketing Spend vs Revenue by Campaign', fontsize=14)
plt.xlabel('Campaign')
plt.ylabel('Amount (₹)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\spend_vs_revenue.png")
plt.show()

avg_ctr = campaign_performance['CTR'].mean()
colors = ['green' if x > avg_ctr else 'red' for x in campaign_performance['CTR']]

plt.figure(figsize=(12, 8))
plt.barh(campaign_performance.index, campaign_performance['CTR'], color=colors)
plt.axvline(x=avg_ctr, color='black', linewidth=0.8, linestyle='--')
plt.title('CTR by Campaign — Green = Above Average, Red = Below Average', fontsize=14)
plt.xlabel('CTR (%)')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\CTR_by_campaign.png")
plt.show()

avg_roas = campaign_performance['ROAS'].mean()
colors = ['green' if x > avg_roas else 'red' for x in campaign_performance['ROAS']]

plt.figure(figsize=(12, 8))
plt.barh(campaign_performance.index, campaign_performance['ROAS'], color=colors)
plt.axvline(x=avg_roas, color='black', linewidth=0.8, linestyle='--')
plt.title('ROAS by Campaign — Green = Above Average, Red = Below Average')
plt.xlabel('ROAS')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\ROAS_by_campaign.png")
plt.show()


avg_cpc = campaign_performance['CPC'].mean()

colors= ['green' if x < avg_cpc else 'red' for x in campaign_performance['CPC']]
plt.figure(figsize=(12,8))
plt.barh(campaign_performance.index, campaign_performance['CPC'], color=colors)
plt.axvline(x = avg_cpc, color='black', linewidth=0.8, linestyle='--')
plt.title('CPC by Campaign — Green = Above Average, Red = Below Average')
plt.xlabel('CPC')
plt.tight_layout()
plt.savefig(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\CPC_by_campaign.png")
plt.show()

df.to_csv(r"D:\DataAnalytics\DataAnalyticsProject\ad_spend_optimization\cleaned_ad_spend.csv", index=False)