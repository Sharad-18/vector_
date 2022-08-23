class vector:
    def __init__(self, vec) -> None:
        self.vec = vec

    def __str__(self) -> str:
        return f"{self.vec[0]}i +{self.vec[1]}j +{self.vec[2]}k"

    def __add__(self, vec2):
        if((len(self.vec))==(len(vec2.vec))):
            list = []
            for i in range(len(self.vec)):
                list.append(self.vec[i] + vec2.vec[i])
            return vector(list)
        else:
            print("sorry lenth of two vector is not same")

    def __mul__(self, vec2):
        if((len(self.vec))==(len(vec2.vec))):
            product = []
            for i in range(len(self.vec)):
                product.append(self.vec[i]*vec2.vec[i])
            return vector(product)
        else:
            print("sorry lenth of two vector is not same")
    def __len__(self):
        return len(self.vec)


v1 = vector([1, 2, 3])
v2 = vector([1, 5, 6])
print(v1)
print(v2)
print("The length of vector v1 is ", len(v1))
print("The length of vector v2 is ", len(v1))
print("The sum of vector v1 and v2 is ", v1+v2)
print("The product of vector v1 and v2 is ",v1*v2)
