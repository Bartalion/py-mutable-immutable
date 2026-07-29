lucky_number = 777
pi = 3.14
one_is_a_prime_number = False
name = "Richard"
my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
profile_info = ("michel", "michel@gmail.com", "12345678")
marks = {
    "John": 4,
    "Sergio": 3,
}

MUTABLE_TYPES = (list, dict, set, bytearray)

all_vars = [
    lucky_number,
    pi,
    one_is_a_prime_number,
    name,
    my_favourite_films,
    profile_info,
    marks,
    created_at,
]

sorted_variables = {
    "mutable": [v for v in all_vars if isinstance(v, MUTABLE_TYPES)],
    "immutable": [v for v in all_vars if not isinstance(v, MUTABLE_TYPES)],
}
