#-------------------------------------------------------------------------
# AUTHOR: Drake Fafard
# FILENAME: naive_bayes.py
# SPECIFICATION: Run Naive Bayes algorithm on a given dataset to predict classes
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour for this question
#-----------------------------------------------------------*/
import csv

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB

#reading the training data in a csv file
#--> add your Python code here
db = []
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for instance in db:
    row = []
    # Column 1
    if instance[1] == 'Sunny':
        row.append(1)
    elif instance[1] == 'Overcast':
        row.append(2)
    elif instance[1] == 'Rain':
        row.append(3)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 2
    if instance[2] == 'Hot':
        row.append(1)
    elif instance[2] == 'Mild':
        row.append(2)
    elif instance[2] == 'Cool':
        row.append(3)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 3
    if instance[3] == 'Normal':
        row.append(1)
    elif instance[3] == 'High':
        row.append(2)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 4
    if instance[4] == 'Weak':
        row.append(1)
    elif instance[4] == 'Strong':
        row.append(2)
    else:
        row.append(1)
        print("Error: invalid type")
    X.append(row)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for instance in db:
    # Column 5
    if instance[5] == 'Yes':
        Y.append(1)
    elif instance[5] == 'No':
        Y.append(2)
    else:
        Y.append(1)
        print("Error: invalid type")

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
dbTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

#printing the header os the solution
#--> add your Python code here
print("Day \tOutlook \tTemperature \tHumidity \tWind  \tPlayTennis \tConfidence")

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
class_probabilities_list = []
class_decisions = []
for instance in dbTest:
    row = []
    # Column 1
    if instance[1] == 'Sunny':
        row.append(1)
    elif instance[1] == 'Overcast':
        row.append(2)
    elif instance[1] == 'Rain':
        row.append(3)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 2
    if instance[2] == 'Hot':
        row.append(1)
    elif instance[2] == 'Mild':
        row.append(2)
    elif instance[2] == 'Cool':
        row.append(3)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 3
    if instance[3] == 'Normal':
        row.append(1)
    elif instance[3] == 'High':
        row.append(2)
    else:
        row.append(1)
        print("Error: invalid type")

    # Column 4
    if instance[4] == 'Weak':
        row.append(1)
    elif instance[4] == 'Strong':
        row.append(2)
    else:
        row.append(1)
        print("Error: invalid type")

    class_probabilities = clf.predict_proba([row])[0]
    if(class_probabilities[0]>=class_probabilities[1]):
        class_decisions.append('yes')
        class_probabilities_list.append(class_probabilities[0])
    else:
        class_decisions.append('no')
        class_probabilities_list.append(class_probabilities[1])

index = 0
for instance in dbTest:
    outputString = f"{instance[0]:<{4}}\t{instance[1]:<{8}}\t{instance[2]:<{12}}\t{instance[3]:<{9}}"
    outputString += f"\t{instance[4]:<{6}}\t{class_decisions[index]:<{11}}\t"
    outputString += "{:.3f}".format(class_probabilities_list[index])
    print(outputString)

    index += 1

print("Probability for Sunny, Mild, Normal, Weak: " + str(clf.predict_proba([[1, 2, 1, 1]])[0]))