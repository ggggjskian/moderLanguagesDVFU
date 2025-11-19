
class Translator:

    def __init__(self, path_to_input_file: str):
        self.path_to_input_file = path_to_input_file
    
    def parse_code(self) -> list:
        temp_arr = []
        with open(self.path_to_input_file,"r") as f:
            for line in f:
                temp_arr.append(line)

        return temp_arr
    
    def translate_code(self) -> None:
       input_code = parse_code()
       for lines in input_code:
           match :
               case :
                   break
               case :
                   break
               case :
                   break


    def execute_code(self) -> None:
        from output_file import main
        main()



a = Translator("/data/DVFU/ModernLanguages/lab2/test.go")
print(a.parse_code())
