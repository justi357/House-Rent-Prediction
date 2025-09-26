import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\justi\\.cache\\kagglehub\\datasets\\iamsouravbanerjee\\house-rent-prediction-dataset\\versions\\9\\House_Rent_Dataset.csv")
print(df.head())

df.hist()
plt.show()
