#str = "X-DSPAM-Confidence:    0.8475"
#place = str.find(':')
#print(place)
#piece = str [place+1:]
#number = float(piece)
#print(number)

fname = input('Enter file name:')
fh = open(fname)
avr = 0
for line in fh:
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line :
        #line = line.strip()
        #line1 = float(line)
        #avr = line1 + avr
        continue
    print(line)
count = 0
#for line in fh:
        #line.startswith("X-DSPAM-Confidence: ")
        #count = count + 1
        #quit()
#los = avr/count
#print("Average spam confidence:",los)