class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        list=[]
        for i in range(1,n+1):
            if i%5==0:
                if i%3==0:
                    list.append("FizzBuzz")
                else:
                    list.append("Buzz")
            elif i%3==0:
                list.append("Fizz")
            else:
                list.append(str(i))
        return list