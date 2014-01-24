def ask(question):
	print question
	return raw_input("> ") == "Y"

fail = "Please answer with either Y or N.\n If you did answer with Y or N, it is likely that I do not know what your bacterium is."

print "This is BacteriaKey v0.15"
print "This was created as a side project by ScepticRail when attempting to learn Python."
print "Any and all errors are, of course, intentional. Reporting them is futile."

print""

print "Please answer all the following questions with either Y or N to identify your bacterium:"

print ""

grampos = ask("Is your bacterium Gram-positive?")

if grampos:
	
	catalase = ask("Is your bacterium catalase positive?") # Staphylococcus and Micrococcus are catalase positive. Streptococcus and Enterococcus. are catalase negative.
	
	if catalase:		
			
		coagulase = ask("Is your bacterium coagulase positive?") # This test differentiates Staphylococcus aureus from other coagulase negative Staphylococcus species.
		
		if coagulase:
			print "Your bacterium is STAPHYLOCOCCUS AUREUS."
					
		elif not coagulase:
			print "Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS."
				
		else:
			print fail
	
	elif not catalase:
		
		AG_haemo = ask("Does your bacterium exhibit alpha or gamma haemolysis?") # Partial haemolysis is termed alpha-haemolysis. Streptococcus pneumoniae and Streptococcus mitis are a-haemolytic 
		
		if AG_haemo:
		
			esculin = ask("Is your bacterium capable of hydrolising esculin in the presence of bile?") # commonly used to identify members of the genus Enterococcus (E faecalis and E. faecium). 
			
			if esculin:
			
				optochin = ask("Is your bacterium resistant to optochin?")
				
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
		
			B_haemo = ask("Does your organism exhibit beta haemolysis?") # Staphylococcus aureus, Streptococcus pyogenes and Streptococcus agalactiae are b-haemolytic 
			
			if B_haemo:
			
				CAMP = ask("Does your organism express the CAMP factor?") # differentiate between Staphylococcus aureus and Streptococcus agalactiae
				
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
	
	oxidase = ask("Is your bacterium oxidase positive?") # used to distinguish between oxidase negative Enterobacteriaceae and oxidase positive Pseudomadaceae. 
	
	if oxidase:
	
		nitrate = ask("Is your bacterium capable of reducing nitrate to nitrate or othe nitrogenous compounds?")
			
		if nitrate:
			print "Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS."
					
		elif not nitrate:
			print "I do not know."	
		
	elif not oxidase:
	
	else:
		print fail

else:
	print fail
