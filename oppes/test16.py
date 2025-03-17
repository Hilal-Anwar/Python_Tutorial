def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)

    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)

    f.close()
    g.close()


do_something('scores.csv', 'F', 'out.csv')