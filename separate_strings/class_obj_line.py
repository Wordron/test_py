from f_separate_str import separate_str

class Line:
    def __init__(self, string):
        self.separated_str = [string]
    def separate(self, delim):
        temp_self_separated_str = self.separated_str
        self.separated_str = []
        for i in temp_self_separated_str:
            temp = separate_str(i, delim)
            for j in temp:
                self.separated_str.append(j)


if __name__ == "__main__":
    read_file = Line("1:2:3;4:5;6;7:8;9:10")

    read_file.separate(":")
    print("separating \':\' :")
    for i in read_file.separated_str:
        print(i)

    read_file.separate(";")
    print("\nseparating \';\' :")
    for i in read_file.separated_str:
        print(i)
