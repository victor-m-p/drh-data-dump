import pandas as pd

# load
entity_tags = pd.read_csv("../data_raw/entity_tags.csv")

# we only want the entity tags associated with entries in our data
entry_data = pd.read_csv("../data_clean/entry_data.csv")
entry_data = entry_data["entry_id"].unique()
entity_tags = entity_tags[entity_tags["entry_id"].isin(entry_data)]

# save
entity_tags.to_csv("../data_clean/entity_tags.csv", index=False)
