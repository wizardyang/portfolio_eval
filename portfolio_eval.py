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
calc_return_1yr(p_ijr)

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
sharpe_max = [0] * 15
w_ivv_opt = [0] * 15
w_ijh_opt = [0] * 15
w_ijr_opt = [0] * 15
w_efa_opt = [0] * 15
w_eem_opt = [0] * 15
w_iyr_opt = [0] * 15
w_ifgl_opt = [0] * 15
w_agg_opt = [0] * 15
w_mub_opt = [0] * 15
w_iau_opt = [0] * 15
return_opt = [0] * 15
sigma_opt = [0] * 15

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
                                    sharpe = p_return_1yr / p_sigma_1yr
                                    i = int(p_return_1yr*100)
                                    if sharpe > sharpe_max[i]:
                                        sharpe_max[i] = sharpe
                                        return_opt[i] = p_return_1yr
                                        sigma_opt[i] = p_sigma_1yr
                                        w_ivv_opt[i] = w_ivv
                                        w_ijh_opt[i] = w_ijh
                                        w_ijr_opt[i] = w_ijr
                                        w_efa_opt[i] = w_efa
                                        w_eem_opt[i] = w_eem
                                        w_iyr_opt[i] = w_iyr
                                        w_ifgl_opt[i] = w_ifgl
                                        w_agg_opt[i] = w_agg
                                        w_mub_opt[i] = w_mub
                                        w_iau_opt[i] = w_iau
                                    else:
                                        continue

print(sharpe_max)
print(return_opt)
print(sigma_opt)
print(w_ivv_opt)
print(w_ijh_opt)
print(w_ijr_opt)
print(w_efa_opt)
print(w_eem_opt)
print(w_iyr_opt)
print(w_ifgl_opt)
print(w_agg_opt)
print(w_mub_opt)
print(w_iau_opt)
