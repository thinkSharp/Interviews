def multiply( A, B) :
    ans = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    dicA={}
    dicB={}
    # for matrix A
    for _idx1 in range(len(A)):
        for _idx2 in range(len(A[0])):
            if A[_idx1][_idx2]!=0:
                dicA[(_idx1, _idx2)] = A[_idx1][_idx2]
    print(dicA)
    # for matrix B
    for _idx3 in range(len(B)):
        for _idx4 in range(len(B[0])):
            if B[_idx3][_idx4]!=0:
                dicB[(_idx3, _idx4)] = B[_idx3][_idx4]
    print(dicB)
    for _key1, va in dicA.items():
        i = _key1[0]
        j = _key1[1]
        for _key2,vb in dicB.items():
            k = _key2[0]
            l = _key2[1]
            if j==k:
                ans[i][l] = ans[i][l] + va * vb
                print("ak:{0}, bk:{1}, result:{2}".format((i,j),(k,l), ans[i][j]))
    return ans

def test_multiply():
    result = multiply([[1,0,0],[-1,0,3]], [[7,0,0],[0,0,0],[0,0,1]])
    print(result)
test_multiply()


