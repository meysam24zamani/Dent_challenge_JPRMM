interesting_pos= (151,152,153,395,396,397,398,111,112,152,153,110,503,116,153,197,202,206,209,210,462,500,465)
# 465 valine missing in the mutated type
for file_num in range(277):
	first_chain = 1
	with open("1a_prod_text.%s"%(str(file_num+1))) as fd:
		for line in fd:
			splt_line = line.split()
			if splt_line[0]=="TER":
				first_chain = 0
			if splt_line[0]=="ATOM" and ((splt_line[2]=="CA" and first_chain and int(splt_line[5]) in interesting_pos) or splt_line[2]=="CLA"):
				print(splt_line[1]+" "+splt_line[2]+" "+splt_line[6]+" "+splt_line[7]+" "+splt_line[8])

