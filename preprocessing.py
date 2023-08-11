import os
import cv2
import csv
import random

dataset_folder = "dataset"
output_final = "dataset.csv"
index_mapping = "label_mapping.csv"

dataset = []

for subfolder in os.listdir(dataset_folder):
    subfolder_path = os.path.join(dataset_folder, subfolder)
    if os.path.isdir(subfolder_path):
        for image_file in os.listdir(subfolder_path):
            image_path = os.path.join(subfolder_path, image_file)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(image, (128, 128))
            flattened_image = resized_image.flatten()
            row = [subfolder] + list(flattened_image)
            dataset.append(row)
print("[INFO]: 1/3 Conversion completed successfully :D")
random.shuffle(dataset)
label_to_index = {}
index = 0
for row in dataset:
    label = row[0]  
    if label not in label_to_index:
        label_to_index[label] = index
        index += 1
for row in dataset:
    label = row[0]  
    index = label_to_index[label]
    row[0] = index
with open(output_final, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dataset)

print("[INFO]: 2/3 dataset is saved successfully too :D")
with open(index_mapping, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Label', 'Index'])
    for label, index in label_to_index.items():
        writer.writerow([label, index])
print("[INFO]: 3/3 Index mapping saved successfully :D")
print("[INFO]: Now split the dataset into train/test using split.py")