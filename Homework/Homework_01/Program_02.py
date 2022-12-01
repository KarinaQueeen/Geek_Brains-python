# Программа доказывает, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат

result = []
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            result.append(not (x or y or z) == (not x and not y and not z))
print(all(result))

# или

print(all((not (x or y or z) == (not x and not y and not z))
      for x in range(2) for y in range(2) for z in range(2)))
