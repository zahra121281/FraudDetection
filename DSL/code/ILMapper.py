import os 
class ILMapper:
    def __init__(self , proj_path):
        self.stack = []
        self.il_codes = []
        self.global_variables = []
        self.label_counter = 0
        self.proj_path = proj_path

    def Create_timing( self ) : 
        timing_file_path = os.path.join(self.proj_path, "timing.py")
        if not os.path.exists(timing_file_path):
            content = (
                "import time\n\n"
                "def timeit(f):\n"
                "\tdef timed(*args, **kw):\n"
                "\t\tts = time.time()\n"
                "\t\tresult = f(*args, **kw)\n"
                "\t\tte = time.time()\n"
                "\t\tprint(\"func: {} ===> took: {:.4f} sec\".format(f.__name__, float(te - ts)))\n"
                "\t\treturn result\n"
                "\treturn timed\n"
            )
            with open(timing_file_path, 'w') as file:
                file.write(content)

    def Create_settings(self , 
    def generate_libraries( self ) : 
        self.Create_timing()

        
        
    def generate_intermediate_language(self, post_order_array):
        for item in post_order_array:
            if self.is_operator(item):
                self.il_codes.append(self.generate_il_based_on_operator(item))
                if None in self.il_codes:
                    print("what")
            else:
                if self.is_identifier(item):
                    self.add_global_variable(item)
                self.stack.append(item)

        result = ''
        for string in self.il_codes:
            if string is not None:
                result += string

        with open("output.il", "w") as my_file:
            my_file.write(self.get_msil_header())
            my_file.write(result)
            my_file.write(self.get_msil_footer())
        return result

    