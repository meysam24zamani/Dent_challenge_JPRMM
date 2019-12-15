interesting_pos= [151,152,153,395,396,397,398,111,112,152,153,110,503,116,153,197,202,206,209,210,462,500,465]
interesting_pos.sort()

# 465 valine missing in the mutated type
count=0
for file_num in range(1531, 2500):
	first_chain = True
	with open("frames/1a_prod_text.%s"%(str(file_num+1))) as fd:
		i = 0
		res_id = 0
		prev_res_id = 1
		with open("analyzed_frames/ca_cla.out.%s"%(str(file_num+1)), "w") as fdOut:
			for line in fd:
				if first_chain and line[:3]=="TER":
					first_chain = False
					continue
	
				if line[:4]!="ATOM":
					continue

				try:
					res_id = int(line[22:26])
				except:
					continue
				
				if res_id < prev_res_id:
					i=0
					res_id = 0
				else:
					prev_res_id = res_id
			
				while interesting_pos[i] < res_id:
					i+=1
					if i==len(interesting_pos):
						i=0
						break
			
				#line[13:15]=="CA"
				if line[:4]=="ATOM" and (first_chain and res_id==interesting_pos[i] and line[13:15]=="CA" or line[12:15]=="CLA" and res_id!=0):
					fdOut.write(str(int(line[6:11]))+"\t"+line[12:16]+"\t"+str(res_id)+"\t"+line[30:38]+"\t"+line[38:46]+"\t"+line[46:54]+"\n")
				
