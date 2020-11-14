class X:
        def __init__(self,a):
              self.x=a

        def check(self, a , b, c):
              return a+b+c==self.x

if __name__=="__main__"
       a = int(input())
       b = int(input())
       c = int(input())

       checker= X(180)
       if checker.check(a,b,c):
           print("да")
       else:
           print("нет")
