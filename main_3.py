import os

def compile_files(fileslist):
    data = {}
    for file in fileslist:
        with open(file, encoding="utf-8") as f:
            filedata = f.readlines()
            data[len(filedata)] = (file, " ".join(filedata))
            data = dict(sorted(data.items()))


    with open("result_data.txt", "w", encoding="utf-8") as new_file:
        for key, value in data.items():
            new_file.write(f"{value[0]} \n")
            new_file.write(f"{key} \n")
            new_file.write(f"{value[1]} \n")

files = ["1.txt", "2.txt", "3.txt"]
files = [os.path.join(os.getcwd(), file) for file in files]

compile_files(files)