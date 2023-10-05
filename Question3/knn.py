#-------------------------------------------------------------------------
# AUTHOR: Drake Fafard
# FILENAME: knn.py
# SPECIFICATION: Run KNN algorithm on a given dataset
# FOR: CS 4210- Assignment #2
# TIME SPENT: 1 hour for this question
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

correctNum = 0
incorrectNum = 0
#loop your data to allow each instance to be your test set
instanceNum = 0
for instance in db:
    #add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    #--> add your Python code here
    X = []
    for xIndex in range(len(db)):
        if xIndex != instanceNum:
            row = [int(db[xIndex][0]), int(db[xIndex][1])]
            X.append(row)


    #transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    #--> add your Python code here
    Y = []
    for yIndex in range(len(db)):
        if yIndex != instanceNum:
            if db[yIndex][2] == '+':
                Y.append(1)
            else:
                Y.append(2)

    #store the test sample of this iteration in the vector testSample
    #--> add your Python code here
    testSample = [int(instance[0]), int(instance[1])]
    if instance[2] == '+':
        testSample.append(1)
    else:
        testSample.append(2)
    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([[testSample[0], testSample[1]]])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    if class_predicted == testSample[2]:
        correctNum += 1
    else:
        incorrectNum += 1

    instanceNum += 1
#print the error rate
#--> add your Python code here
print("Error rate: " + str(incorrectNum / (correctNum + incorrectNum)))






