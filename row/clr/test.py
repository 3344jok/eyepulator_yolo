import os 
fs=os.listdir(".")
print(fs)
for p in fs:
    if p.endswith(".txt"):
        with open(p, "r") as f:
            line=f.readline()
            print(p+":"+line)
        if line.startswith("15"):
            with open(p, "w") as f:
                line="0"+line[2:]
                f.write(line)

print("over")