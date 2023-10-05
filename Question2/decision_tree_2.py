#-------------------------------------------------------------------------
# AUTHOR: Drake Fafard
# FILENAME: decision_tree_2.py
# SPECIFICATION: generate and test decision trees off of datasets
# FOR: CS 4210- Assignment #2
# TIME SPENT: 2 hours for this question
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    accuracy = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    # X =
    for i in range(len(dbTraining)):
        row = []

        # First column
        if dbTraining[i][0] == 'Young':
            row.append(1)
        elif dbTraining[i][0] == "Prepresbyopic":
            row.append(2)
        elif dbTraining[i][0] == "Presbyopic":
            row.append(3)
        else:
            row.append(1)
            print("Typo Error")

        # Second column
        if dbTraining[i][1] == "Myope":
            row.append(1)
        elif dbTraining[i][1] == "Hypermetrope":
            row.append(2)
        else:
            row.append(1)
            print("Typo Error")

        # Third column
        if dbTraining[i][2] == "Yes":
            row.append(1)
        elif dbTraining[i][2] == "No":
            row.append(2)
        else:
            row.append(1)
            print("Typo Error")

        # Fourth column
        if dbTraining[i][3] == "Reduced":
            row.append(1)
        elif dbTraining[i][3] == "Normal":
            row.append(2)
        else:
            row.append(1)
            print("Typo Error")

        X.append(row)
    #print(X)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    # Y =
    for i in range(len(dbTraining)):
        # Result column
        if dbTraining[i][4] == "Yes":
            Y.append(1)
        elif dbTraining[i][4] == "No":
            Y.append(2)
        else:
            Y.append(1)
            print("Typo Error")
    #print(Y)
    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        accurateCount = 0
        inaccurateCount = 0
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0:  # skipping the header
                    dbTest.append(row)

        for data in dbTest:
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here
            row = []
            # First column
            if data[0] == 'Young':
                row.append(1)
            elif data[0] == "Prepresbyopic":
                row.append(2)
            elif data[0] == "Presbyopic":
                row.append(3)
            else:
                row.append(1)
                print("Typo Error")

            # Second column
            if data[1] == "Myope":
                row.append(1)
            elif data[1] == "Hypermetrope":
                row.append(2)
            else:
                row.append(1)
                print("Typo Error")

            # Third column
            if data[2] == "Yes":
                row.append(1)
            elif data[2] == "No":
                row.append(2)
            else:
                row.append(1)
                print("Typo Error")

            # Fourth column
            if data[3] == "Reduced":
                row.append(1)
            elif data[3] == "Normal":
                row.append(2)
            else:
                row.append(1)
                print("Typo Error")

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            class_predicted = clf.predict([row])[0]
            #print(class_predicted)
            actual_class = 1
            if data[4] == "Yes":
                actual_class = 1
            elif data[4] == "No":
                actual_class = 2
            else:
                actual_class = 1
                print("Typo Error")
            #print(actual_class)
            if(class_predicted == actual_class):
                accurateCount += 1
            else:
                inaccurateCount += 1
        # Compute accuracy in this run
        accuracy.append(accurateCount / (inaccurateCount + accurateCount))
    #find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    avgAccuracy = 0
    temp = 0
    runs = 0
    for runAccuracy in accuracy:
        temp += runAccuracy
        runs += 1
    avgAccuracy = temp / runs
    #print the average accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    print("final accuracy when training on " + ds + ": " + str(avgAccuracy))



