class Array:
    def __init__(self) -> None:
        self.length = 0
        self.dict = {}

    def __str__(self) -> str:
        # print(str(self.__dict__), type(str(self.__dict__)))
        return str(self.__dict__)

    def push(self, item):
        self.dict[self.length] = item
        self.length += 1   

    def get(self):
        return self.dict    

    def get_index_value(self, index):
        return self.dict[index]

    def pop(self):
        lastitem = self.dict[self.length - 1] 
        del self.dict[self.length - 1]
        self.length -= 1

        print("The final dict: ", self.dict)
        return lastitem

    def delete(self, item):
        deleteditem = self.dict[item]

        for i in range(item, self.length-1):
            self.dict[i] = self.dict[i+1]

        del self.dict[self.length-1]
        self.length -= 1

        print(self.dict)    
        return deleteditem

    def insert(self, index, item):
        for i in range(self.length, index, -1):
            print("i: ", i)
            self.dict[i] = self.dict[i-1]

        self.length += 1    
        self.dict[index] = item    


arr = Array()
print(arr)
arr.push('hi')
arr.push(10)
arr.push('hello')
arr.push(20)
arr.push(30)
arr.push(40)
arr.push(100)
arr.push('bye')

print(arr.get())
print(arr.get_index_value(1))

print("Poping: ", arr.pop())
print("Poping: ", arr.pop())

print()
print(arr.delete(1))

arr.insert(0, 'finale')
print("final: ", arr.get())
