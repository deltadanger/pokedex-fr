types="ACIER	COMBAT	DRAGON	EAU	ELECTRIQUE	FEE	FEU	GLACE	INSECTE	NORMAL	PLANTE	POISON	PSY	ROCHE	SOL	SPECTRE	TENEBRE	VOL".split('\t')



table="""0.5 	2 	0.5 			0.5 	2 	0.5 	0.5 	0.5 	0.5 	0 	0.5 	0.5 	2 			0.5
					2 			0.5 				2 	0.5 			0.5 	2
		2 	0.5 	0.5 	2 	0.5 	2 			0.5 							
0.5 			0.5 	2 		0.5 	0.5 			2 							
0.5 				0.5 										2 			0.5
2 	0.5 	0 						0.5 			2 					0.5 	
0.5 			2 		0.5 	0.5 	0.5 	0.5 		0.5 			2 	2 			
2 	2 					2 	0.5 						2 				
	0.5 					2 				0.5 			2 	0.5 			2
	2 														0 		
			0.5 	0.5 		2 	2 	2 		0.5 	2 			0.5 			2
	0.5 				0.5 			0.5 		0.5 	0.5 	2 		2 			
	0.5 							2 				0.5 			2 	2 	
2 	2 		2 			0.5 			0.5 	2 	0.5 			2 			0.5
			2 	0 			2 			2 	0.5 		0.5 				
	0 							0.5 	0 		0.5 				2 	2 	
	2 				2 			2 				0 			0.5 	0.5 	
	0.5 			2 			2 	0.5 		0.5 			2 	0 			"""


dic = {}

table = table.split("\n")
for i in range(len(table)):
    dic[types[i]] = {}
    
    row = table[i].split("\t")
    for j in range(len(row)):
        try:
            dic[types[i]][types[j]] = float(row[j])
        except:
            dic[types[i]][types[j]] = 1.


text = ""
for type in types:
    text += """
    this.put(Type.{}, new HashMap<Type, Float>(){{{{""".format(type)
    for receiveType in types:
        
        text += """
        this.put(Type.{}, {}f);""".format(receiveType, dic[type][receiveType])
    
    text += """
    }});
"""

print text
