import seaborn as sns
import matplotlib.pyplot as plt 

df = sns.load_dataset("tips")
df.head()
print(df.head())
print("\n")

# sns.jointplot(x = "total_bill" , y = "tip", data = df , kind = "reg")
# plt.show()

# sns.jointplot(x = "total_bill" , y = "tip", data = df , kind = "scatter")
# plt.show()

# sns.jointplot(x = "total_bill" , y = "tip", data = df , kind = "hex")
# plt.show()

# sns.jointplot(x = "total_bill" , y = "tip", data = df , kind = "kde")
# plt.show()

# sns.pairplot(df,hue = "sex")
# plt.show()

# sns.displot(df["total_bill"],kde = False)
# sns.rugplot(df['total_bill'],color = 'black')
# plt.show()


# create simple dashboard
sns.set(style="whitegrid")
fig, axs = plt.subplots(2,2, figsize=(10,8))
sns.lineplot(x="total_bill", y="tip", data=df, ax=axs[0,0])
axs[0,0].set_title("Line Plot")
sns.barplot(x="day", y="total_bill", data=df, ax=axs[0,1])
axs[0,1].set_title("Bar Plot")
sns.scatterplot(x="total_bill", y="tip", data=df, ax=axs[1,0])
axs[1,0].set_title("Scatter Plot")
sns.histplot(df["total_bill"], kde=False, ax=axs[1,1])
axs[1,1].set_title("Histogram")
plt.tight_layout()
plt.show()
