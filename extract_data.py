def extract_data(filename):
    # Read price sequence of each fund
    f = open(filename, 'r')
    p = []

    while(1):
        p_temp = f.readline()
        if p_temp == '':
            break
        p.append(float(p_temp))

    print(p)
    f.close()
    return p
