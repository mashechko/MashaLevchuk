# 5. Дан список имен, отфильтровать все имена, где есть буква k

names = ['Masha', 'Sasha', 'Alex', 'Mike', 'Aleksey']

names_k = list(filter(lambda x: 'k' in x, names))

print(names_k)