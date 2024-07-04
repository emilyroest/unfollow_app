import json
import argparse

def get_unique_values(following, followers):
    following_values = set(entry['string_list_data'][0]['value'] for entry in following['relationships_following'])
    followers_values = set(entry['string_list_data'][0]['value'] for entry in followers)

    unique_values = following_values - followers_values

    return list(unique_values)

def main():
    parser = argparse.ArgumentParser(description="Print values in following.json that are not in followers.json.")
    parser.add_argument('--following', required=True, help="Path to following.json file")
    parser.add_argument('--followers', required=True, help="Path to followers.json file")

    args = parser.parse_args()

    # Read following.json
    with open(args.following, 'r') as following_file:
        following_data = json.load(following_file)

    # Read followers.json
    with open(args.followers, 'r') as followers_file:
        followers_data = json.load(followers_file)

    # Get unique values
    unique_values = get_unique_values(following_data, followers_data)

    # Print the result
    print("Values in following.json that are not in followers.json:")
    for value in unique_values:
        print(value)

if __name__ == "__main__":
    main()


# python -m unfollow_app --following following.json --followers followers_1.json
