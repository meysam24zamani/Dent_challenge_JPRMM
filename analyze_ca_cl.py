
atoms_map = {}

def calc_squared_dist(atom1, atom2):
	return (atom1["x"]-atom2["x"])**2 + (atom1["y"]-atom2["y"])**2 + (atom1["z"]-atom2["z"])**2


for file_num in range(2500):
	first_chain = True
	with open("analyzed_frames/ca_cla.out.%s"%(str(file_num+1))) as fd:
		atoms_map["CA"] = []
		atoms_map["CLA"] = []
		for line in fd:
			row = line.split()	
			atoms_map[row[1]].append({"x":float(row[3]), "y":float(row[4]), "z": float(row[5]), "id": row[0], "res_id": row[2]})
		
		min_dist = -1;
		min_cla = {}
		min_ca = {}
		for cla in atoms_map["CLA"]:
			for ca in atoms_map["CA"]:
				loc_dist = calc_squared_dist(cla, ca)
				if min_dist < 0 or loc_dist < min_dist:
					min_dist = loc_dist
					min_cla = cla
					min_ca = ca
		
		print("Frame "+str(file_num+1)+":\t"+"Residue ID: "+str(min_ca["res_id"])+"; Atom ID: "+str(min_ca["id"])+"; CLA ID: "+str(min_cla["id"]));				
			
