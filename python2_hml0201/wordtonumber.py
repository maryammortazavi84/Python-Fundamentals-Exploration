import sys
from word2number import w2n
class NumberWordReplacer:
    def __init__(self):
        pass

    def convert_file(self,input_file,output_file):
        con_lines = []

        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            con_words = []
            words = line.split()
            
            for word in words:
                try:
                    num = w2n.word_to_num(word)
                    con_words.append(str(num))
                except ValueError:
                    con_words.append(word)

            new_line = " ".join(con_words) + "\n"
            con_lines.append(new_line)


        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(con_lines)

        print("converted successfully!")



# _____________tester_______________
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_file> <output_file>")
        print("Example: python converter.py Numbers.txt Result.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    replacer = NumberWordReplacer()
    replacer.convert_file(input_file, output_file)


        
      



        
        
