import pandas as pd
import random

zodiac_labels = list(range(12))  # Aries to Pisces

def generate_fake_dataset(n=100):
    data = []
    for _ in range(n):
        entry = {planet: random.choice(zodiac_labels) for planet in [
            'Sun', 'Moon', 'Mercury', 'Venus', 'Mars',
            'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'
        ]}
        entry['label'] = random.choice(['Romantic', 'Adventurous', 'Emotional', 'Practical'])
        data.append(entry)
    return pd.DataFrame(data)

df = generate_fake_dataset()
