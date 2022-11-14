arr = ["Genowfa", "Onufry", "Clestyna", "Alojzy", "Pankracy"]
max = arr[0]
for i in arr:
    if len(i) > len(max):
        max = i
print(max)