import csv

start = 0
end = 0

with open('unemployment.tsv', mode='r', encoding='utf-8') as idfi:
    idreader = csv.reader(idfi, delimiter='\t')
    ids = set()
    next(idreader, None)
    for idrow in idreader:
        ids.add(idrow[0])
    with open('commuter_raw.tsv', mode='r', encoding='latin-1') as fi:
        reader = csv.reader(fi, delimiter='\t', quotechar='\"')
        with open('commuter.tsv', mode='w', encoding='utf-8', newline='') as fo:
            writer = csv.writer(fo, delimiter='\t', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["home_id", "work_id", "total"])
            next(reader, None)
            for row in reader:
                start += 1
                hid = row[0] + row[1].zfill(3)
                wid = row[6] + row[7].zfill(3)
                total = row[12].replace(',', '')
                if int(total) > 9 and row[0] == row[6] and hid in ids and wid in ids and hid != wid:
                    end += 1
                    writer.writerow([hid, wid, total])

print(start)
print(end)
