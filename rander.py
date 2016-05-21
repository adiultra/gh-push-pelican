from subprocess import call
call("mkdir -p output", shell=True)

f1 = open("output/index.html", "w")
for k in range(200):
    f1.write(repr(k))

f2 = open("output/main.css", "w")
for k in range(200):
    f1.write(repr(k))

call("mkdir -p output/images", shell=True)

f1 = open("output/images/Hi.html", "w")
for k in range(200):
    f1.write(repr(k))
