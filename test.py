# Remove duplicate lines
lines_seen = set()
outfile = open("inRange_dist.txt", "w")
for line in open("inRange.txt", "r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()