
# Non Efficient Approach 

# class SparseVector:

#     def __init__(self, vec: int) -> None:
#         self.vector = vec

#     def dotProduct(self, vec) -> int:
        
#         dot = 0
#         for i in range(len(self.vector)):
#             dot += self.vector[i] * vec.vector[i]
#         return dot
    

class SparseVector:
    def __init__(self, vec: list[int]):
        
        self.nonzero = {}

        for i, n in enumerate(vec):
            if n != 0:
                self.nonzero[i] = n

    def dotProduct(self, vec:list[int]):
        result = 0
        for i, n in self.nonzero.items():
            if i in vec.nonzero:
                result += n * vec.nonzero[i]
        return result
        





nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
ans = v1.dotProduct(v2)
print(ans)