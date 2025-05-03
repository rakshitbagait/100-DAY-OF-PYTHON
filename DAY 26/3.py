# how to iterate over pandas dataframe

import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for (key,value) in student_data_frame.items():
    print(value)
    print(key)
# loop through rows of a data frame

for (key,value) in student_data_frame.iterrows():
    print(value.student)

{"A":"Alpha","B":"Bravo"}