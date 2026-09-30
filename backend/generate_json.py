# import json
# import random

# # Genuine reviews
# genuine_reviews = [
#     "This product is amazing and works perfectly",
#     "Very good quality and worth the price",
#     "I am satisfied with this purchase",
#     "Excellent product and great experience",
#     "Loved it and will buy again",
#     "Good value for money",
#     "Product is exactly as described",
#     "Fast delivery and good packaging",
#     "Nice design and easy to use",
#     "Highly durable and reliable"
# ]

# # Fake reviews
# fake_reviews = [
#     "Best product ever!!! Buy now!!!",
#     "Amazing amazing amazing amazing",
#     "This changed my life completely 100%",
#     "Superb product highly highly recommend!!!",
#     "Buy this now best deal ever!!!",
#     "100% perfect product no issues at all",
#     "Excellent excellent excellent!!!",
#     "Top quality guaranteed!!!",
#     "Unbelievable performance must buy!!!",
#     "Perfect perfect perfect product!!!"
# ]

# data = []

# # Create 600 Genuine reviews
# for _ in range(600):
#     review = random.choice(genuine_reviews)
#     data.append({
#         "review": review,
#         "label": 0
#     })

# # Create 600 Fake reviews
# for _ in range(600):
#     review = random.choice(fake_reviews)
#     data.append({
#         "review": review,
#         "label": 1
#     })

# # Shuffle the dataset
# random.shuffle(data)

# # Save as JSON
# with open("reviews.json", "w") as f:
#     json.dump(data, f, indent=2)

# print("JSON dataset created successfully!")
# print("Total reviews:", len(data))
# print("Genuine reviews:", sum(1 for item in data if item["label"] == 0))
# print("Fake reviews:", sum(1 for item in data if item["label"] == 1))