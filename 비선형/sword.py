class Tnode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


strong = int(input("추가 강화 수치 입력 >>"))

if __name__ == "__main__":
    D = Tnode(40+strong, None, None)
    E = Tnode(35, None, None)
    B = Tnode(20, D, None)
    C = Tnode(15, E, None)
    A = Tnode(10, B, C)


print(f"태양의 검 최종 루트 공격력 합계 : {A.data + B.data + D.data}")

# print(A.data)
# print(B.data)
# print(C.data)
# print(D.data)
# print(E.data)