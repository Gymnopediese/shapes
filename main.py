import turtle
dim = 7



class shape:
    arrete = []
    a = 25
    b = 25
    pos = [[0,0],[a,b]]
    done = [[0,0],[a,b]]
    turtle.tracer(False)
    def second(self,dim):
        c = 0
        a = self.a
        b = self.b
        ro = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        k = 0
        d = 25
        s = 50
        turtle.screensize(10000,10000)
        for c in range(dim - 2):
            #a = random.randint(25, 50)
            #b = random.randint(25, 50)
            for i in range(len(self.done)):
                self.square(int(self.done[i][0]), int(self.done[i][1]))
            self.done.clear()
            k += 1
            if k == 4:
                k = 0
            #s = random.randint(25, 100)
            #d = random.randint(25, 100)
            for i in range(len(self.pos)):

                if divmod(c,2)[1] == 0:
                    self.pos.append([self.pos[i][0] + (c + 1) * a * ro[k][0] + d*ro[k][0]*(c+1), self.pos[i][1] + (c + 1) * b * ro[k][1] + s*ro[k][1]*(c+1)])
                    self.done.append([self.pos[i][0] + (c + 1) * a * ro[k][0] + d*ro[k][0]*(c+1), self.pos[i][1] + (c + 1) * b * ro[k][1] + s*ro[k][1]*(c+1)])
                else:
                    self.pos.append(
                        [self.pos[i][0] + (c + 1) * a , self.pos[i][1] + (c + 1) * b * ro[k][1] + s*ro[k][1]*(c+1)])
                    self.done.append(
                        [self.pos[i][0] + (c + 1) * a, self.pos[i][1] + (c + 1) * b * ro[k][1] + s*ro[k][1]*(c+1)])

    def __init__(self,dim):
        self.second(dim)
        print("ond")
        r = 0
        print(self.arrete)
        for ii in range(1,dim-1):
            i = 0
            for x in range(2**(dim-1)):
                try:
                    self.link(self.arrete[i],self.arrete[i+2**(ii+1)])
                except Exception as e:
                    print(e)
                    pass
                i+=1
                if divmod(i,2**(ii+1))[1] == 0:
                    i+=2**(ii+1)
                r+=1
                self.printProgressBar(r,(dim-2)*2**(dim-1))

        turtle.hideturtle()
        turtle.mainloop()

    def printProgressBar(self,iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        import sys
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()
        # Print New Line on Complete
        if iteration == total:
            print()
    def link(self,a,b):
        turtle.penup()
        turtle.goto(a[0], a[1])
        turtle.pendown()
        turtle.goto(b[0], b[1])
    def square(self,base = -1,af = -1):
        if base!=-1:
            turtle.penup()
            turtle.goto(base,af)
            turtle.pendown()
        for i in range(4):
            turtle.forward(20)
            turtle.left(90)
            self.arrete.append(turtle.pos())

r = shape(dim)

