import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes_prediction_dataset.csv')
new_df = df.drop('gender', axis=1, inplace=False) # строки с полом и историей курения я удалила и перезаписала в другую переменную
new_df = new_df.drop('smoking_history', axis=1, inplace=False)
tmp = new_df.corr()
plt.figure(figsize=(7,7))
sns.heatmap(tmp, annot=True, cmap='Greens')
plt.imshow(tmp)
plt.title('Матрица корелляции Пирсона')
plt.savefig('matrix.jpg')