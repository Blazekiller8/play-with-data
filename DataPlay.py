import pandas as pd
import matplotlib.pyplot as plt

# to read csv file named "samplee"
df = pd.read_csv("ibm/train.csv")

# to save as html file
# named as "Table"
df.to_html("full_data.html")

df.describe().to_html("data_desc.html")

elderly_dist_df = df[["EmployeeNumber","Age","DistanceFromHome"]]
elderly_dist_df.sort_values(by="Age").groupby('Age', as_index=False)['DistanceFromHome'].mean().plot.line(x="Age",y="DistanceFromHome")

pay_dist_df = df[["EmployeeNumber","Department","DailyRate"]]
pay_dist_df.groupby('Department', as_index=False)['DailyRate'].mean().plot.bar(x="Department",y="DailyRate",color='purple')

satisfication_dist_df = df[["EmployeeNumber","JobRole","JobSatisfaction"]]
satisfication_dist_df.groupby('JobRole', as_index=False)['JobSatisfaction'].mean().plot.bar(x="JobRole",y="JobSatisfaction",color='orange')

hike_dist_df = df[["EmployeeNumber","PerformanceRating","PercentSalaryHike"]]
hike_dist_df.groupby('PerformanceRating', as_index=False)['PercentSalaryHike'].mean().plot.barh(x="PerformanceRating",y="PercentSalaryHike",color=['green','yellow'] )

hourly_dist_df = df[["EmployeeNumber","Age","HourlyRate"]]
hourly_dist_df.groupby('Age', as_index=False)['HourlyRate'].mean().plot.bar(x="Age",y="HourlyRate",color='red')

divorced_df = df[df["MaritalStatus"] == "Divorced" ]
divorced_df[["Age"]].value_counts().sort_values(ascending=True).to_excel("divorced_age.xlsx") 

edu_df = df[df["Gender"] == "Female" ]
edu_df[["EducationField"]].value_counts().sort_values(ascending=True).to_excel("female_edu.xlsx") 

print(df.groupby("Gender")["MonthlyIncome"].mean().to_markdown(tablefmt="grid"))

plt.show()
