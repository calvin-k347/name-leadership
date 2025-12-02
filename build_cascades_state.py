import os
import pandas as pd
from name_processing import annotate_name
from functools import lru_cache
path_to_data = "./data/by_state"
listed_files = [ f for f in os.listdir(path_to_data)]
@lru_cache()
def fast_annotate(name):
    return annotate_name(name)
rows = []
data_frame = pd.DataFrame(columns=["spelling"
                                       ,"sex"
                                       ,"count", 
                                       "decade", 
                                       "stress_pos", 
                                       "syll_count", 
                                       "ends_in_vowel", 
                                       "initial_vowel"])
for file in listed_files:
    df = pd.read_csv(path_to_data + "/" +file, header=None, names=["state", "sex","year", "name", "count"])
    year = 0
    state = file[0:2]
    for i, row in df.iterrows():
        annotations = fast_annotate(row["name"])
        if annotations == "NAME ERROR":
            continue
        rows.append({
            "spelling": row["name"],
            "sex": row["sex"],
            "count": row["count"],
            "year": int(row["year"]),
            "stress": annotations["stress"],
            "syll_count": annotations["syll_count"],
            "ends_in_vowel": annotations["ends_in_vowel"],
            "initial_vowel": annotations["initial_vowel"],
            "glides": annotations["glides"],
            "nasals": annotations["nasals"],
            "affricates": annotations["affricates"],
            "fricitives": annotations["fricitives"],
            "stops": annotations["stops"],
            "vowel_ratio": annotations["vowel_ratio"],
            "glides_r": annotations["glides_r"],
            "nasals_r": annotations["nasals_r"],
            "affricates_r": annotations["affricates_r"],
            "fricitives_r": annotations["fricitives_r"],
            "stops_r": annotations["stops_r"],
            "pronouncation": annotations["pronouncation"]
        })
    print(state)
    data = pd.DataFrame(rows)
    data.to_csv(f"states/{state}.csv")
    rows = []
