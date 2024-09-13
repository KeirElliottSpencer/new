
## Fizzbuzz warmup

for x in range(1, 20):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)

#Means of Departments

import pandas as pd

data = {'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'Sales'], 'Salary': [50000, 80000, 60000, 120000, 45000]}
df = pd.DataFrame(data)

df
df['Salary'].mean()

result = df.groupby('Department')['Salary'].mean().reset_index()
print(result)


#Write a Python function to find the second largest number in a list of integers.

def secondlargest(nums):
    # Order the numbers and remove duplicates
    nums_ordered = sorted(list(set(nums)))
    # Get the n - 1 value from the list length
    lenlist = len(nums_ordered) - 2 #1 to get the largest because of indexing, 2 for second to last
    second = nums_ordered[lenlist]
    # Return n - 1
    return second

list1 = [1,2,3,4,5,6,7,8,10,9,552,323,1339,3,24]
answer = secondlargest(list1)
print(answer)


#Given a 2D numpy array, write a function to calculate the row-wise mean and return the result as a 1D array.

import numpy as np

data = np.array([[1,2,3],[2,3,4],[3,4,5]])

def rowmean(row):
    answer = np.mean(row, axis=1)
    return answer

print(rowmean(data))


#Given a DataFrame with customer orders, find the top 3 customers who have made the most orders.

data = {'Customer': ['Alice', 'Bob', 'Alice', 'Alice', 'Bob', 'Charlie', 'Charlie', 'Terry'], 'OrderID': [1, 2, 3, 4, 5, 6, 7, 8]}
df = pd.DataFrame(data)


answer = df['Customer'].value_counts().head(3)
print(answer)
#What if the third and so on have the same value?
#Get top 4, check 3rd to the next highest and if they are the same then print them both and repeat this in a while loop until the values don't match



#Write a Python function that takes a string and returns the most frequent character in that string.

from collections import Counter
word = 'Sensational'
common_char = Counter(word).most_common(1)



#Use list comprehension to create a list of the squares of all even numbers from 0 to 10.



#Given a dataset (Pandas DataFrame), how would you handle missing data? What are some methods to fill or drop missing values?

df.dropna()
df.fillna(df.mean, inplace = True)
