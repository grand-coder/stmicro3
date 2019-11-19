import subprocess
# 原始(沒有存任何東西)
result = subprocess.run("ls", shell=True)
print("*" * 30)
print(result)
# 直接導到PIPE(沒有存檔)
result = subprocess.run("ls",
                        shell=True,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
print("*" * 30)
try:
    text = result.stdout.decode("utf-8")
except:
    text = result.stdout.decode("BIG5")
print(text)
# 導到檔案
f = open("test.log", "wb")
result = subprocess.run("ls {}".format("-al"),
                        shell=True,
                        stdout=f)
f.close()
