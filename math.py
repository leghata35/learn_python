
def max(data = []):
    if len(data) > 1:
        max = data[0]
        for index in range(0, len(data)):
            if data[index] > max:
                max = data[index]
        return max
    else:
        return "La liste est vide"

def min(data = []):
    if len(data) > 1:
        min = data[0]
        for index in range(0, len(data)):
            if data[index] < min:
                min = data[index]
        return min
    else:
        return "La liste est vide"


numbers = [1000, 1200, 1999, 20, 19, 17, 25, 152, 2002, 2020, 189, 563, 71, 3050]


print("le maximum de la liste est : ", max(numbers))
print("le minimum de la liste est : ", min(numbers))

print("Good bey.")
