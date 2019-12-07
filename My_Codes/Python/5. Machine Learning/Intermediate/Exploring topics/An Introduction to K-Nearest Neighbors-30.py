## 3. Finding Similar Rows With Euclidean Distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']
import math
def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

lebron_distance = nba.apply(euclidean_distance, axis=1)

## 4. Normalizing Columns ##

nba_numeric = nba[distance_columns]
nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()

## 5. Finding the Nearest Neighbor ##

from scipy.spatial import distance

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values("dist", inplace=True)
second_smallest = distance_frame.iloc[1]["idx"]
most_similar_to_lebron = nba.loc[int(second_smallest)]["player"]

## 8. Computing Error ##

actual = test[y_column]
mse = (((predictions - actual) ** 2).sum()) / len(predictions)