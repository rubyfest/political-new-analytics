import os
import pickle


def save_list(list_to_save, list_name):

    # Create the cache directory if it doesn't exist
    cache_dir = 'cache'

    os.makedirs(cache_dir, exist_ok=True)

    # Define the path for the cache file
    cache_file = os.path.join(cache_dir, f'{list_name}_cache.pkl')

    # Save the list to the cache file
    with open(cache_file, 'wb') as f:
        pickle.dump(list_to_save, f)

    print(f"List saved to {cache_file}")

def open_list(list_name):

    # Define the path for the cache file
    cache_file = os.path.join('cache', f'{list_name}_cache.pkl')

    # Open the cache file
    with open(cache_file, 'rb') as f:
        cached_list = pickle.load(f)

    return cached_list