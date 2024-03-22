from rapidfuzz import process

# Define a function to find the best match in the TMDB dataset for each title in MovieLens dataset
def find_best_match(title, choices):
    return process.extractOne(title, choices, score_cutoff=75)[0]

# Processing Function
def process_batch(batch):
    # Initialize empty list to store index of each row and its correspinding best match
    batch_matches = []
    
    for index, row in batch[0].iterrows():
        query_title = row['Title']
        # For unsuccessful row, find best match to title in TMDB dataset and change title to that. Use 75% Similarity Score threshold.
        best_match = find_best_match(query_title, batch[1])
        batch_matches.append((index, best_match))
        
    return batch_matches

