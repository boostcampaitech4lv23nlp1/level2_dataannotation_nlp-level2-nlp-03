import pandas as pd
import numpy as np
from fleiss import fleissKappa

col_list = ['sj', 'Chanmuzi', 'hd', 'kh']
df = pd.read_excel('text_all.xlsx',engine='openpyxl', index_col=0)[col_list]
class_list = ['no_relation', 'per:event', 'per:theory', 'org:naming', 'org:event', 'org:members_of', 'date:event', 'law:definition', 'law:subordinate']
class_dict = {c : idx for idx, c in enumerate(class_list)}
for col in col_list:
    df[col] = df[col].apply(lambda x: class_dict[x])
num_classes = len(class_list)
result = df.to_numpy()


# print(result)
# result = result.to_numpy()
# print(result)
# num_classes = int(np.max(result))
# print(num_classes)

transformed_result = []
for i in range(len(result)):
    temp = np.zeros(num_classes)
    for j in range(len(result[i])):
        temp[int(result[i][j]-1)] += 1
    transformed_result.append(temp.astype(int).tolist())

kappa = fleissKappa(transformed_result,len(result[0]))