import random


def get_random_number():
    # Generate a random number between 1 to 100000
    random_number = random.randrange(start=1, stop=1000000)
    return random_number

def get_random_repo_name():
    random_number = get_random_number()
    # Concatenate this random number with a "repo_" prefix Ex : repo_234567
    repo_name = f'repo_{random_number}'
    return repo_name
