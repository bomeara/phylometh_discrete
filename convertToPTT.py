import sys

def modifyFAA(fileName,output,proteins):
	with open(fileName) as fin,open(output,'w') as out:
		for line in fin:
			if line[0] == ">":
				line_spt = line.split()
				values=proteins.get(line_spt[0][1:])
				l = ">gi|{}|ref|{}| {}\n".format(values.get("PID"),values.get("Synonym")," ".join(line_spt[1:]))
				out.write(l)
			else:
				out.write(line)
	return None


def readData(line):
	convert = {}
	line_spt = line.strip().split("\t")
	location = line_spt[2]+".."+line_spt[3]
	convert["Location"] = location
	convert["Strand"] = line_spt[4]
	convert["Length"] = line_spt[9]
	convert["PID"] = line_spt[5]
	convert["Gene"] = line_spt[6]
	convert["Synonym"] = line_spt[8]
	convert["Code"] = "-"
	convert["COG"] = line_spt[10]
	convert["Product"] = line_spt[11]
	return convert


def main():
	genes = {}
	fileName = sys.argv[1]+".txt"
	output = sys.argv[1]+".ptt"
	faa = sys.argv[1]+".faa"
	mod = "mod_"+sys.argv[1]+".faa"
	with open(fileName) as fin, open(ouput,'w') as out:
		out.write(sys.argv[2]+", complete genome\n")
		fin.readline()
		lines = fin.readlines()
		total = str(len(lines))
		out.write(total+" proteins\n")
		header=["Location","Strand","Length","PID","Gene","Synonym","Code","COG","Product"]
		out.write("\t".join(header))
		out.write("\n")
		for line in lines:
			convert = readData(line)
			genes[convert.get("Synonym")] = convert
			values = list(map(lambda x: convert.get(x),header))
			out.write("\t".join(values))
			out.write("\n")
	modifyFAA(faa,mod,genes)

	return 0

main()
