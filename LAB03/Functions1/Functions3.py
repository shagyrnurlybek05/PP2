def count_animals(heads,legs):
    rabbits = (legs/2) - heads
    chickens = heads - rabbits
    print(f'there is {rabbits} rabits and {chickens} chickens')
count_animals(int(input('Number of heads: ')), int(input('number of legs: ')) )