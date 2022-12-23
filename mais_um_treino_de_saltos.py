p = int(input())
nmsalt = int(input())
nms = []
lst_md = []
for y in range(p):
    slts = []
    nms.append(input())
    for x in range(nmsalt):
        slts.append(float(input()))
    if nmsalt != 0:
        md = sum(slts) / nmsalt
    else:
        md = 0
    lst_md.append(md)
nms_od = nms.copy()
nms_od.sort()
for t in range(p):
    for h in range(p):
        if nms_od[t] == nms[h]:
            print("{}: {:.1f}".format(nms_od[t], lst_md[h]))