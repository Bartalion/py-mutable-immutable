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
# (тут вище у твоєму файлі вже стоять 8 оголошених змінних)

aMUTABLE_TYPES = (list, dict, set, bytearray)

all_vars = [var1, var2, var3, var4, var5, var6, var7, var8]

sorted_variables = {
    "mutable": [v for v in all_vars if isinstance(v, MUTABLE_TYPES)],
    "immutable": [v for v in all_vars if not isinstance(v, MUTABLE_TYPES)],
}


