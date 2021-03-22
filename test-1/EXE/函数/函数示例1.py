s1 = 'SPAM'
s2 = 'SCAM'
#方法一
# def intersect(seq1,seq2):
#     res = []
#     for x in seq1:
#         if x in seq2:
#             res.append(x)
#     return res

#方法二
def intersect(seq1,seq2):
    res = [x for x in seq1 if x in seq2]
    return res

print(intersect(s1,s2))

i1 = (1,2,3,4)
i2 = (3,4,5,6)
print(intersect(i1,i2))


