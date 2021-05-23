arr = [57.8, 46.51, 97, 56.6, 6, 99, 102, 34.6, 5.65, 0.1]

for i in arr:
    r, kk = str(f"{i:.2f}").split(".")
    print(f"{r} rubles {int(kk):02} cop, ", end=" ")
