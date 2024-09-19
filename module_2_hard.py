vst_1 = [3, 4, 5, 6, 7, 8, 9, 10]
vst = {}
k = 0
for i in range(2, len(vst_1) + 1):

    x = vst_1[k]
    k = k + 1
    for j in range(1, i):
        y = x - j
        kod_ = [y, j]
#        vst.add(kod_)
        print(kod_)
    vst = set(vst)