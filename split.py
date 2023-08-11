import csv
import random

with open('dataset.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

    
data2 = random.shuffle(data)
split_index = int(len(data) * 0.8)



train_data = data[:split_index]
test_data = data[split_index:]



with open('train.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(train_data)
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(test_data)