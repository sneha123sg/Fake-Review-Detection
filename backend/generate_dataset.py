import pandas as pd
import random

# Genuine reviews
genuine_reviews = [
    "This product is amazing and works perfectly",
    "Very good quality and fast delivery",
    "I am satisfied with this purchase",
    "Excellent service and great experience",
    "Worth the money, highly recommend",
    "Product is exactly as described",
    "Good packaging and timely delivery",
    "Really happy with the performance",
    "Nice product and easy to use",
    "Quality is very good for the price"
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

# Generate 1200 samples
for _ in range(600):
    data.append([random.choice(genuine_reviews), 0])

for _ in range(600):
    data.append([random.choice(fake_reviews), 1])

# Shuffle dataset
random.shuffle(data)

df = pd.DataFrame(data, columns=["review", "label"])

# Save CSV
df.to_csv("reviews.csv", index=False)

print("Dataset with 1200 samples created successfully!")