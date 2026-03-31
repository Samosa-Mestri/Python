#KNN

from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
print("Datasets are loaded")

iris_df = pd.DataFrame(data = iris, columns = iris.feature_names)
iris_df['target'] = iris.target
print("Complete datasets")
print(iris_df.to_string(index=False))

x_train,x_test,y_train,y_test = train_test_split(iris.data,iris.target,test_size = 0.2, random_state =42)

print("Target Labels")
for i in range(len(iris.target_names)):
  print("Label",i,":",iris.target_names[i])
print("\n")

classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

correct = 0
incorrect = 0

print("Predications: ")
for i in range(len(x_test)):
  actual_label = y_test[i]
  predicted_label = y_pred[i]
  if actual_label == predicted_label:
    status = "Correct"
  else:
    status = "Wrong"

  if status == "Correct":
    correct += 1
  else:
    incorrect += 1

  print(f"Sample :{x_test[i]} , Actual Label: {iris.target_names[actual_label]}",
        f"Predicted : {iris.target_names[predicted_label]} -> {status}")

print("SUmmary")
print("Total Samples",len(y_test))
print("Correct = ", correct)
print("Incorrect = ",incorrect)
print("Accuracy = ",classifier.score(x_test,y_test))
