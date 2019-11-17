import subprocess

command = ["ls", "-al"]
f = open("out.txt", "w", encoding="utf-8")
subprocess.run(command,
               stdout= f,
               shell=True)
f.close()