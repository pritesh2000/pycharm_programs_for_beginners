# Didn't understand properly about .get

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict.values()))

print(min(sample_dict, key=sample_dict.get))
