import sys


class Node:  # class for handling nodes and trees

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def smallestfactor(self):
        if self.data > 1:
            for i in range(2, self.data):
                if (self.data % i) == 0:
                    return i
                else:
                    continue
        else:
            return None

    def factor(self):
        x = self.smallestfactor()
        if x:
            self.left = Node(int(self.data / x))
            self.right = Node(x)
            self.left.factor()

    def degree(self):
        return bool(self.left) + bool(self.right)

    def printtree(self, b=-1, first=True, bstr="    ", pol=None):
        if first:
            sys.stdout.write(bstr)
        if self.left:
            b += 1
            self.left.printtree(b=b, first=False, pol="left")
        if b == 0:
            print(" " + str(self.data))
        elif pol == "left":
            print(bstr * b + "┌──" + str(self.data))
        elif pol == "right":
            print(bstr * b + "└──" + str(self.data))
        else:
            print("you probably don't need to use this function")
        if self.right:
            b += 1
            self.right.printtree(b=b, first=False, pol="right")

