def ask(question):
	print question
	return raw_input("> ") == "Y"

fail = "Please answer with either Y or N.\n If you did answer with Y or N, it is likely that I do not know what your bacterium is."

print ""

print """This is BacteriaKey v0.3

This was created as a side project by ScepticRail when attempting to learn Python.

This dichotomous key is largely based on that of the University of Wyoming.
It allows for the identification of approximately 20 different bacteria.
Please note that only tests identifying Coccal bacteria are showcased here.

Any and all errors are, of course, intentional. Reporting them is futile.

"""

print""

print "Please answer all the following questions with either Y or N to identify your bacterium:"

print ""

grampos = ask("Is your bacterium Gram-positive?")

if grampos:	
	
	# Staphylococcus and Micrococcus are catalase positive. Streptococcus and Enterococcus. are catalase negative.
	catalase = ask("Is your bacterium catalase-positive?") 
	
	if catalase:		
		
		# This test differentiates Staphylococcus aureus from other coagulase negative Staphylococcus species.
		coagulase = ask("Is your bacterium coagulase-positive?") 
		
		if coagulase:
			print "Your bacterium is STAPHYLOCOCCUS AUREUS."
					
		elif not coagulase:
			print "Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS."
				
		else:
			print fail
	
	elif not catalase:
		
		# Partial haemolysis is termed alpha-haemolysis. Streptococcus pneumoniae and Streptococcus mitis are a-haemolytic 
		AG_haemo = ask("Does your bacterium exhibit alpha or gamma haemolysis?") 
		
		if AG_haemo:
		
			# commonly used to identify members of the genus Enterococcus (E faecalis and E. faecium). 
			esculin = ask("Is your bacterium capable of hydrolising esculin in the presence of bile?")
			
			if esculin:
			
				optochin = ask("Is your bacterium optochin-resistant?")
				
				if optochin:
					print "Your bacterium is STREPTOCOCCUS MITIS."
					
				elif not optochin:
					print "Your bacterium is STREPTOCOCCUS PNEUMONIAE."
					
				else:
					print fail
					
			elif not esculin:
				print "Your bacterium is ENTEROCCOCUS FAECALIS."
				
			else:
				print fail
		
		elif not AG_haemo:
		
			# Staphylococcus aureus, Streptococcus pyogenes and Streptococcus agalactiae are b-haemolytic 
			B_haemo = ask("Does your organism exhibit beta haemolysis?") 
			
			if B_haemo:
				
				# differentiate between Staphylococcus aureus and Streptococcus agalactiae
				CAMP = ask("Does your organism express the CAMP factor?") 
				
				if CAMP:
					print "Your bacterium is STREPTOCOCCUS AGALACTIAE."
					
				elif not CAMP:
					print "Your bacterium is STREPTOCOCCUS PYOGENES."
				
				else:
					print fail
		else:
			print fail
			
	else:
		print fail
	
elif not grampos:
	
	# used to distinguish between oxidase negative Enterobacteriaceae and oxidase positive Pseudomadaceae. 
	oxidase = ask("Is your bacterium oxidase-positive?") 
	
	if oxidase:
	
		nitrate = ask("Is your bacterium nitratase-positive?")
			
		if nitrate:
			print "Your bacterium is PSEUDOMONAS AERUGINOSA."
					
		elif not nitrate:
			print "Your bacterium is ALCALIGENES FAECALIS."
			
		else:	
			print fail
		
	elif not oxidase:
		
		# crazy complicated
		lactose = ask("Is your bacterium capable of fermenting lactose?")
		
		if lactose:
		
			#tests an organism's ability to ferment glucose 
			durham = ask("Is your bacterium hydrogen lyase-positive?")
			
			if durham:
				
				# can your bacterium swim through a medium called SIM (who' knows)
				motile = ask("Is your bacterium motile?")
				
				if motile:
				
					mixed_acid = ask("Does your bacterium utilise the mixed acid fermentation pathway (MR+)?")
					
					if mixed_acid:
						print "Your bacterium is CITROBACTER FREUNDII."
						
					elif not mixed_acid:
						print "Your bacterium is ENTEROBACTER AEROGENES."
					
					else:
						print fail
						
				elif not motile:
				
					# Klebsiella pneumoniae and Proteus mirabilis are citrate positive. Escherichia coli and Shigella dysenteriae are citrate negative.
					citrate = ask("Is your bacterium capable of using citrate as its sole carbon source?")
					
					if citrate:
						
						# Also complicated, full of stupid reagents
						tryptophan = ask("Is your bacterium able to convert tryptophan to indole?")
						
						if tryptophan:
							print "Your bacterium is KLEBSIELLA OXYTOCA."
						
						elif not tryptophan:
							
							nitrate = ask("Is your bacterium capable of reducing nitrate to nitrate or othe nitrogenous compounds?")
			
							if nitrate:
								print "Your bacterium is PSEUDOMONAS AERUGINOSA."
					
							elif not nitrate:
								print "Your bacterium is ACTINOBACTER CALCOACETICUS."
			
							else:	
								print fail
							
						else:
							print fail
						
					elif not citrate:
						print "Your bacterium is ESCHERICHIA COLI."
						
					else:
						print fail
				
				else:
					print fail
					
			elif not durham:
				print "Your bacterium is SERRATIA MARCESCENS."
				
			else:
				print fail
	
		elif not lactose:
		
			# can your bacterium swim through a medium called SIM (who' knows)
			motile = ask("Is your bacterium motile?")
			
			if motile:
					
					tryptophan = ask("Is your bacterium able to convert tryptophan to indole?")
						
					if tryptophan:
						print "Your bacterium is KLEBSIELLA OXYTOCA."
						
					elif not tryptophan:
						
						urease = ask("Is your bacterium urease-positive?")
							
						if urease:
							print "Your bacterium is PROTEUS MIRABILIS."
								
						elif not urease:
							print "Your bacterium is SALMONELLA TYPHIMURIUM."
								
						else:
							print fail
						
					else:
						print fail
			
			elif not motile:
					print "Your bacterium is SHIGELLA DYSENTERIAE."
				
			else:
					print fail
		
		else:
			print fail
			
	else:
		print fail

else:
	print fail
