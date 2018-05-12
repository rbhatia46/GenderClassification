from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# The fit method trains the decision tree on our dataset

# In a nutshell: fitting is equal to training. Then, after it is trained, the model can be used to make predictions, usually with a .predict() method call.
clf = clf.fit(X, Y)

prediction = clf.predict([[160,35 , 38]])

print(prediction)
