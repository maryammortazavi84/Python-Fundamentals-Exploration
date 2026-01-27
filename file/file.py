from pathlib import Path
# path = Path("pi_digits.txt")
# content = path.read_text()
# pi_float = float("".join(content.split()))
# print(pi_float)
# final = []
# path = Path("some_text.txt")
# content = path.read_text()
# for line in content.split():
#     final.append(line)

# final_text="".join(f"{line}\n" for line in final)
# path.write_text(final_text)
path_list = ["files/pi_digits.txt","files/some_text.txt"]
for path_str in path_list:
    path = Path(path_str)
    print(path.read_text())
    print("********")