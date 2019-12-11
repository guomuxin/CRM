while True:
    a = input()
    with open("a,txt","a+",encoding="utf-8") as f:
        f.write(a)
        f.seek(0,0)
        print(f.read())