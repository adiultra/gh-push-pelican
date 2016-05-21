import random as r
import subprocess as sub


def execuTer(comMesg):
    name = "/tmp/samp" + repr(r.randint(0, 10000))
    cur_dir = sub.check_output("pwd").decode('utf8')[:-1]

    print("Random Directory name is : ", name)
    print("Current Directory name is : ", cur_dir)

    sub.call("mkdir " + name, shell=True)
    sub.call("cp -r output/* " + name, shell=True)
    sub.call("git commit -m \"" + comMesg + "\"", shell=True)

    sub.call("git checkout gh-pages", shell=True)
    sub.call("rm -r ./*", shell=True)
    sub.call("cp -r " + name + "/* " + cur_dir, shell=True)
    sub.call("rm -r " + name, shell=True)
    sub.call("git add --all", shell=True)
    sub.call("git commit -m \"" + comMesg + "\"", shell=True)
    sub.call("git checkout master", shell=True)
    sub.call("rm -r output", shell=True)


if __name__ == "__main__":
    execuTer("hell")
