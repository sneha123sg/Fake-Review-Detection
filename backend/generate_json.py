# import json
# import random

# positive = [
#     "This product is amazing and works perfectly",
#     "Very good quality and worth the price",
#     "Excellent product, highly recommended",
#     "Loved it, will buy again",
#     "Great experience using this",
#     "Very satisfied with the performance",
#     "Good value for money",
#     "Fantastic quality and fast delivery",
#     "Nice design and easy to use",
#     "Highly durable and reliable"
# ]

# negative = [
#     "Worst product ever, waste of money",
#     "Fake product, do not buy",
#     "Very bad quality and not worth it",
#     "Completely disappointed",
#     "This is a scam product",
#     "Terrible experience",
#     "Not as described, very poor",
#     "Totally useless item",
#     "Fake and misleading",
#     "Horrible quality"
# ]

# data = []

# for i in range(1200):  # 1200 reviews
#     if random.random() > 0.5:
#         review = random.choice(positive)
#     else:
#         review = random.choice(negative)
    
#     data.append({"review": review})

# with open("reviews.json", "w") as f:
#     json.dump(data, f, indent=2)

# print("JSON dataset created successfully!")


import json
import random

# Genuine reviews
genuine_reviews = [
    "This product is amazing and works perfectly",
    "Very good quality and worth the price",
    "I am satisfied with this purchase",
    "Excellent product and great experience",
    "Loved it and will buy again",
    "Good value for money",
    "Product is exactly as described",
    "Fast delivery and good packaging",
    "Nice design and easy to use",
    "Highly durable and reliable"
]

# Fake reviews
fake_reviews = [
    "Best product ever!!! Buy now!!!",
    "Amazing amazing amazing amazing",
    "This changed my life completely 100%",
    "Superb product highly highly recommend!!!",
    "Buy this now best deal ever!!!",
    "100% perfect product no issues at all",
    "Excellent excellent excellent!!!",
    "Top quality guaranteed!!!",
    "Unbelievable performance must buy!!!",
    "Perfect perfect perfect product!!!"
]

data = []

# Create 600 Genuine reviews
for _ in range(600):
    review = random.choice(genuine_reviews)
    data.append({
        "review": review,
        "label": 0
    })

# Create 600 Fake reviews
for _ in range(600):
    review = random.choice(fake_reviews)
    data.append({
        "review": review,
        "label": 1
    })

# Shuffle the dataset
random.shuffle(data)

# Save as JSON
with open("reviews.json", "w") as f:
    json.dump(data, f, indent=2)

print("JSON dataset created successfully!")
print("Total reviews:", len(data))
print("Genuine reviews:", sum(1 for item in data if item["label"] == 0))
print("Fake reviews:", sum(1 for item in data if item["label"] == 1))