lista=[]
with open("kutyusok.txt", encoding="utf-8") as f:
    for sor in f:
        sor=sor.strip()
        sor=sor.upper()
        lista.append(sor)
print(f"{len(lista)} db név van a listában.")
