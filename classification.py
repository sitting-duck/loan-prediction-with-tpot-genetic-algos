from tpot import TPOTClassifier
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import simplejson

digits = load_digits()
#digits = pd.read_csv('loans.csv', sep=',', dtype=np.float64)
#digits = pd.read_csv('loans.csv', sep=',', dtype=np.str)

print("digits.data: " + str(digits.data))
print("digits.target: " + str(digits.target))

#print("digits: " + str(digits))

digits_data_json_file = open("digits_data.json", "w")
#digits_data_json_file.write(simplejson.dumps(simplejson.loads(str(digits.data)), indent=4, sort_keys=True))

digits_target_json_file = open("digits_target.json", "w")
#digits_target_json_file.write(simplejson.dumps(simplejson.loads(str(digits.target)), indent=4, sort_keys=True))

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, train_size=0.75, test_size=0.25, random_state=42)

tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
tpot.fit(X_train, y_train)

print(tpot.score(X_test, y_test))

tpot.export('tpot_digits_pipeline.py')
