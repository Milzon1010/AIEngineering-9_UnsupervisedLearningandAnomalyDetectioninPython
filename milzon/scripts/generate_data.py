# milzon/scripts/generate_data.py

import pandas as pd
import numpy as np
import os

np.random.seed(42)
n_total = 500
n_fake = int(0.05 * n_total)

def generate_segment(name, count, f_range, l_range, c_range, p_range):
    return pd.DataFrame({
        "segment": [name]*count,
        "followers_count": np.random.randint(*f_range, count),
        "avg_likes": np.random.randint(*l_range, count),
        "avg_comments": np.random.randint(*c_range, count),
        "posts_per_week": np.random.randint(*p_range, count),
    })

# ========================
# 📊 Realistic Influencer Segments (Based on Your Pattern)
# ========================

# Micro Influencers
micro = generate_segment("micro", 200,
                         f_range=(1000, 10000),
                         l_range=(50, 500),
                         c_range=(5, 30),
                         p_range=(4, 10))

# Mid-tier Influencers
mid = generate_segment("mid", 200,
                       f_range=(10000, 100000),
                       l_range=(500, 5000),
                       c_range=(30, 200),
                       p_range=(3, 7))

# Macro Influencers
macro = generate_segment("macro", 75,
                         f_range=(100000, 1000000),
                         l_range=(5000, 50000),
                         c_range=(100, 1000),
                         p_range=(1, 5))

# ========================
# 🕵️ Fake Influencers (with suspicious patterns)
# ========================
fake = pd.DataFrame({
    "segment": ["fake"] * n_fake,
    "followers_count": np.random.randint(50000, 1000000, n_fake),
    "avg_likes": np.random.randint(10, 300, n_fake),   # super low engagement
    "avg_comments": np.random.randint(1, 10, n_fake),
    "posts_per_week": np.random.randint(0, 2, n_fake),  # inactive
})

# ========================
# 🔗 Combine All
# ========================
df = pd.concat([micro, mid, macro, fake], ignore_index=True)

# 🧮 Add Feature: engagement_rate (%)
df["engagement_rate"] = 100 * (df["avg_likes"] + df["avg_comments"]) / df["followers_count"]

# ✅ Optional: check distribution
print("📊 Data segment counts:")
print(df["segment"].value_counts())
print("🎯 Total records:", df.shape)

# 💾 Save to CSV
os.makedirs("milzon/data", exist_ok=True)
df.to_csv("milzon/data/influencers.csv", index=False)
print("✅ influencers.csv saved to milzon/data/")
