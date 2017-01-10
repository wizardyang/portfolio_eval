# Read price sequence of each fund
from extract_data import *
p_ivv = extract_data('ivv.txt')
p_ijh = extract_data('ijh.txt')
p_ijr = extract_data('ijr.txt')
p_efa = extract_data('efa.txt')
p_eem = extract_data('eem.txt')
p_iyr = extract_data('iyr.txt')
p_ifgl = extract_data('ifgl.txt')
p_agg = extract_data('agg.txt')
p_mub = extract_data('mub.txt')
p_iau = extract_data('iau.txt')
print(len(p_ivv))
print(len(p_ijh))
print(len(p_ijr))
print(len(p_efa))
print(len(p_eem))
print(len(p_iyr))
print(len(p_ifgl))
print(len(p_agg))
print(len(p_mub))
print(len(p_iau))

from calc_return import *

###################################################
# Portfolio of US stocks: IVV + IJH + IJR
###################################################
f1 = open('us_1yr_return.txt', 'w')
f3 = open('us_3yr_return.txt', 'w')
f5 = open('us_5yr_return.txt', 'w')
f1.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f3.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"Avg_return_3yr"+'\t'+"Sigma_3yr"+'\n')
f5.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"Avg_return_5yr"+'\t'+"Sigma_5yr"+'\n')
for w1 in range(0, 21):
    w_ivv = w1 * 0.05
    for w2 in range(0, 21-w1):
        w_ijh = w2 * 0.05
        w_ijr = 1 - w_ivv - w_ijh

        [p_return_1yr, p_sigma_1yr] = calc_return3_1yr(p_ivv, w_ivv, p_ijh, w_ijh, p_ijr, w_ijr, 200)
        print(p_return_1yr, p_sigma_1yr)
        f1.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t' + str(p_return_1yr) + '\t' + str(
            p_sigma_1yr) + '\n')

        [p_return_3yr, p_sigma_3yr] = calc_return3_3yr(p_ivv, w_ivv, p_ijh, w_ijh, p_ijr, w_ijr, 200)
        print(p_return_3yr, p_sigma_3yr)
        f3.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t' + str(p_return_3yr) + '\t' + str(
            p_sigma_3yr) + '\n')

        [p_return_5yr, p_sigma_5yr] = calc_return3_5yr(p_ivv, w_ivv, p_ijh, w_ijh, p_ijr, w_ijr, 200)
        print(p_return_5yr, p_sigma_5yr)
        f5.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t' + str(p_return_5yr) + '\t' + str(
            p_sigma_5yr) + '\n')

f1.close()
f3.close()
f5.close()

###################################################
# Portfolio of all 10 ETFs
###################################################
f1 = open('total_1yr_return_1.txt', 'w')
f2 = open('total_1yr_return_2.txt', 'w')
f3 = open('total_1yr_return_3.txt', 'w')
f4 = open('total_1yr_return_4.txt', 'w')
f5 = open('total_1yr_return_5.txt', 'w')
f6 = open('total_1yr_return_6.txt', 'w')
f7 = open('total_1yr_return_7.txt', 'w')
f8 = open('total_1yr_return_8.txt', 'w')
f9 = open('total_1yr_return_9.txt', 'w')
f10 = open('total_1yr_return_10.txt', 'w')
f11 = open('total_1yr_return_11.txt', 'w')
f12 = open('total_1yr_return_12.txt', 'w')
f13 = open('total_1yr_return_13.txt', 'w')
f14 = open('total_1yr_return_14.txt', 'w')
f15 = open('total_1yr_return_15.txt', 'w')
f1.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f2.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f3.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f4.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f5.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f6.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f7.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f8.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f9.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
         +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f10.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f11.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f12.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f13.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f14.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')
f15.write("IVV"+'\t'+"IJH"+'\t'+"IJR"+'\t'+"EFA"+'\t'+"EEM"+'\t'+"IYR"+'\t'+"IFGL"+'\t'+"AGG"+'\t'+"MUB"
          +'\t'+"IAU"+'\t'+"Avg_return_1yr"+'\t'+"Sigma_1yr"+'\n')

for w1 in range(0, 21):
    w_ivv = w1 * 0.05
    for w2 in range(0, 21-w1):
        w_ijh = w2 * 0.05
        for w3 in range(0, 21-w1-w2):
            w_ijr = w3 * 0.05
            for w4 in range(0, 21-w1-w2-w3):
                w_efa = w4 * 0.05
                for w5 in range(0, 21-w1-w2-w3-w4):
                    w_eem = w5 * 0.05
                    for w6 in range(0, 21-w1-w2-w3-w4-w5):
                        w_iyr = w6 * 0.05
                        for w7 in range(0, 21-w1-w2-w3-w4-w5-w6):
                            w_ifgl = w7 * 0.05
                            for w8 in range(0, 21-w1-w2-w3-w4-w5-w6-w7):
                                w_agg = w8 * 0.05
                                for w9 in range(0, 21-w1-w2-w3-w4-w5-w6-w7-w8):
                                    w_mub = w9 * 0.05
                                    w_iau = 1 - w_ivv - w_ijh - w_ijr - w_efa - w_eem - w_iyr - w_ifgl - w_agg - w_mub

                                    [p_return_1yr, p_sigma_1yr] = calc_return10_1yr(p_ivv, w_ivv, p_ijh, w_ijh, p_ijr,
                                                                                    w_ijr, p_efa, w_efa, p_eem, w_eem,
                                                                                    p_iyr, w_iyr, p_ifgl, w_ifgl, p_agg,
                                                                                    w_agg, p_mub, w_mub, p_iau, w_iau,
                                                                                    109)
                                    print(p_return_1yr, p_sigma_1yr)

                                    if (p_return_1yr > 0.04) & (p_return_1yr < 0.05):
                                        f4.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t' + str(
                                            w_efa) + '\t' + str(w_eem) + '\t'
                                                 + str(w_iyr) + '\t' + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(
                                            w_mub) + '\t' + str(w_iau) + '\t'
                                                 + str(p_return_1yr) + '\t' + str(p_sigma_1yr) + '\n')


                                    elif (p_return_1yr > 0.05) & (p_return_1yr < 0.06):
                                        f5.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                 + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                 + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                 + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                 + '\n')

                                    elif (p_return_1yr > 0.06) & (p_return_1yr < 0.07):
                                        f6.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                 + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                 + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                 + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                 + '\n')

                                    elif (p_return_1yr > 0.07) & (p_return_1yr < 0.08):
                                        f7.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                 + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                 + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                 + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                 + '\n')

                                    elif (p_return_1yr > 0.08) & (p_return_1yr < 0.09):
                                        f8.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                 + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                 + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                 + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                 + '\n')

                                    elif (p_return_1yr > 0.09) & (p_return_1yr < 0.10):
                                        f9.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                 + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                 + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                 + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                 + '\n')

                                    elif (p_return_1yr > 0.10) & (p_return_1yr < 0.11):
                                        f10.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                  + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                  + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                  + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                  + '\n')

                                    elif (p_return_1yr > 0.11) & (p_return_1yr < 0.12):
                                        f11.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                  + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                  + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                  + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                  + '\n')

                                    elif (p_return_1yr > 0.12) & (p_return_1yr < 0.13):
                                        f12.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                  + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                  + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                  + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                  + '\n')

                                    elif (p_return_1yr > 0.13) & (p_return_1yr < 0.14):
                                        f13.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                  + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                  + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                  + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                  + '\n')

                                    elif (p_return_1yr > 0.14) & (p_return_1yr < 0.15):
                                        f14.write(str(w_ivv) + '\t' + str(w_ijh) + '\t' + str(w_ijr) + '\t'
                                                  + str(w_efa) + '\t' + str(w_eem) + '\t' + str(w_iyr) + '\t'
                                                  + str(w_ifgl) + '\t' + str(w_agg) + '\t' + str(w_mub) + '\t'
                                                  + str(w_iau) + '\t' + str(p_return_1yr) + '\t' + str(p_sigma_1yr)
                                                  + '\n')

                                    else:
                                        continue

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()
f15.close()
