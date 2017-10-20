import regression
import csv
import argparse as ap
import os

parser = ap.ArgumentParser()
parser.add_argument('-r', action = 'store', dest = 'r', type = str, help = "Pass the .csv file with datasets.")
parser.add_argument('-w', action = 'store', dest = 'w', type = str, help = "Pass the .txt file with datasets.")

args = parser.parse_args()

def write(data, File):

    csvf = open(File, 'w')

    for i in data:
        row = str(i)+','+str(data[i])+'\n'
        csvf.write(row)

    csvf.close()

def convert_and_write(x, y, File):
    if len(x) == len(y):
        d = {}
        for i in range(len(x)):
            d.update({x[i]:y[i]})

        write(d, File)
        return 1
    return 0

def read(File):
    x, y = [], []
    with open(File, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            entry = row
            x.append(float(entry[0]))
            y.append(float(entry[1]))

    return x, y


def cvt_txt_csv(txtfile):
    f = open(txtfile, 'r')
    lines = f.readlines()
    x = list(lines[0].split(','))
    y = list(lines[1].split(','))
    f.close()

    lastx = x[-1]
    lasty = y[-1]

    if '\n' in lastx:
        x[-1] = lastx.rstrip('\n')
    if '\n' in lasty:
        y[-1] = lasty.rstrip('\n')

    if len(x) == len(y):

        for i in range(len(x)):
            x[i] = float(x[i])
            y[i] = float(y[i])
 
        convert_and_write(x, y, os.path.dirname(txtfile)+'/'+os.path.basename(txtfile)+'.csv')

    return 0


if __name__ == '__main__':

    if args.r:
        x, y = read(args.r)
        regression.regression(x, y)

    elif args.w:
        cvt_txt_csv(args.w)
