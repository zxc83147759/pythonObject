from operator import itemgetter

d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
print(sorted(d.items(), key=lambda x: x[1]))

print(sorted(d.items(), key=itemgetter(1)))

print(sorted(d, key=d.get))
