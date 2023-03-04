class Scanner:
    def __init__(self, filelocation):
        self.position = 0
        file = open(filelocation)
        self.read_file = file.read().split()
        file.close()


    def next(self):
        value = self.read_file[self.position]
        self.position+=1
        return value
    
    def next_int(self):
        value = None
        for i in range(self.position, len(self.read_file)):
            num = self.read_file[i]
            self.position+=1
            try:
                value = int(float(num))
                break
            except ValueError:
                continue
        return value
    
    def next_float(self):
        value = None
        for i in range(self.position, len(self.read_file)):
            num = self.read_file[i]
            self.position += 1
            try:
                value = float(value)
                break
            except ValueError:
                continue
        return value
    
    def reset(self):
        self.position = 0
