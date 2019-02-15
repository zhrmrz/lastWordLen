class Sol:
    def length(self,string):
        for char in range(len(string)):
            if string[char]==" ":
                last_space_index=char
        return len(string[last_space_index+1:])
if __name__ == '__main__':
    string="hi Hello World"
    p1=Sol()
    print(p1.length(string))
