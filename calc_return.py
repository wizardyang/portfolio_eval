import statistics 

def calc_return_1yr(p1):
    r_1yr = []
    time_len = len(p1)
    for t in range(0, time_len-1-12):
        r_1yr.append(p1[t] / p1[t+12] - 1)

    print(r_1yr)
    return [statistics.mean(r_1yr), statistics.pstdev(r_1yr)]


# 1-yr return
def calc_return3_1yr(p1, w1, p2, w2, p3, w3, time_len):
    r_1yr = []
    for t in range(0, time_len-1-12):
        q1 = 10000 * w1 / p1[t+12]
        q2 = 10000 * w2 / p2[t+12]
        q3 = 10000 * w3 / p3[t+12]
        p_1yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t]
        r_1yr.append(p_1yr / 10000 - 1)

    print(r_1yr)
    return [statistics.mean(r_1yr), statistics.pstdev(r_1yr)]

# 3-yr return
def calc_return3_3yr(p1, w1, p2, w2, p3, w3, time_len):
    r_3yr = []
    for t in range(0, time_len-1-36):
        q1 = 10000 * w1 / p1[t+36]
        q2 = 10000 * w2 / p2[t+36]
        q3 = 10000 * w3 / p3[t+36]
        p_3yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t]
        r_3yr.append((p_3yr / 10000)**(1/3) - 1)

    print(r_3yr)
    return [statistics.mean(r_3yr), statistics.pstdev(r_3yr)]

# 5-yr return
def calc_return3_5yr(p1, w1, p2, w2, p3, w3, time_len):
    r_5yr = []
    for t in range(0, time_len-1-60):
        q1 = 10000 * w1 / p1[t+60]
        q2 = 10000 * w2 / p2[t+60]
        q3 = 10000 * w3 / p3[t+60]
        p_5yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t]
        r_5yr.append((p_5yr / 10000)**(1/5) - 1)

    print(r_5yr)
    return [statistics.mean(r_5yr), statistics.pstdev(r_5yr)]


def calc_return10_1yr(p1, w1, p2, w2, p3, w3, p4, w4, p5, w5, p6, w6, p7, w7, p8, w8, p9, w9, p10, w10, time_len):
    r_1yr = []
    for t in range(0, time_len-1-12):
        q1 = 10000 * w1 / p1[t + 12]
        q2 = 10000 * w2 / p2[t + 12]
        q3 = 10000 * w3 / p3[t + 12]
        q4 = 10000 * w4 / p4[t + 12]
        q5 = 10000 * w5 / p5[t + 12]
        q6 = 10000 * w6 / p6[t + 12]
        q7 = 10000 * w7 / p7[t + 12]
        q8 = 10000 * w8 / p8[t + 12]
        q9 = 10000 * w9 / p9[t + 12]
        q10 = 10000 * w10 / p10[t + 12]
        p_1yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t] + q4 * p4[t] + q5 * p5[t] + q6 * p6[t] + q7 * p7[t] + q8 * p8[t] + q9 * p9[t] + q10 * p10[t]
        r_1yr.append(p_1yr / 10000 - 1)

    print(r_1yr)
    return [statistics.mean(r_1yr), statistics.pstdev(r_1yr)]


def calc_return10_3yr(p1, w1, p2, w2, p3, w3, p4, w4, p5, w5, p6, w6, p7, w7, p8, w8, p9, w9, p10, w10, time_len):
    r_3yr = []
    for t in range(0, time_len-1-36):
        q1 = 10000 * w1 / p1[t + 36]
        q2 = 10000 * w2 / p2[t + 36]
        q3 = 10000 * w3 / p3[t + 36]
        q4 = 10000 * w4 / p4[t + 36]
        q5 = 10000 * w5 / p5[t + 36]
        q6 = 10000 * w6 / p6[t + 36]
        q7 = 10000 * w7 / p7[t + 36]
        q8 = 10000 * w8 / p8[t + 36]
        q9 = 10000 * w9 / p9[t + 36]
        q10 = 10000 * w10 / p10[t + 36]
        p_3yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t] + q4 * p4[t] + q5 * p5[t] + q6 * p6[t] + q7 * p7[t] + q8 * p8[t] + q9 * p9[t] + q10 * p10[t]
        r_3yr.append((p_3yr / 10000)**(1/3) - 1)

    print(r_3yr)
    return [statistics.mean(r_3yr), statistics.pstdev(r_3yr)]


def calc_return10_5yr(p1, w1, p2, w2, p3, w3, p4, w4, p5, w5, p6, w6, p7, w7, p8, w8, p9, w9, p10, w10, time_len):
    r_5yr = []
    for t in range(0, time_len-1-60):
        q1 = 10000 * w1 / p1[t + 60]
        q2 = 10000 * w2 / p2[t + 60]
        q3 = 10000 * w3 / p3[t + 60]
        q4 = 10000 * w4 / p4[t + 60]
        q5 = 10000 * w5 / p5[t + 60]
        q6 = 10000 * w6 / p6[t + 60]
        q7 = 10000 * w7 / p7[t + 60]
        q8 = 10000 * w8 / p8[t + 60]
        q9 = 10000 * w9 / p9[t + 60]
        q10 = 10000 * w10 / p10[t + 60]
        p_5yr = q1 * p1[t] + q2 * p2[t] + q3 * p3[t] + q4 * p4[t] + q5 * p5[t] + q6 * p6[t] + q7 * p7[t] + q8 * p8[t] + q9 * p9[t] + q10 * p10[t]
        r_5yr.append((p_5yr / 10000)**(1/5) - 1)

    print(r_5yr)
    return [statistics.mean(r_5yr), statistics.pstdev(r_5yr)]
