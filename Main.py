def ask(question):
	print question
	return raw_input("> ") == "Y"


print "This is BacteriaKey v0.03"
print "This was created as a side project by ScepticRail when attempting to learn Python."
print "Any and all errors are, of course, intentional. Reporting them is futile."

print""

print "Please answer all the following questions with either Y or N to identify your bacterium:"

print ""

grampos = ask("Is your bacterium Gram-positive?")

if grampos:
	
	catalase = ask("Is your bacterium catalase positive?")
	
	if catalase:			
		
		coagulase = ask("Is your bacterium coagulase positive?")
		
		if coagulase:
			print "Your bacterium is STAPHYLOCOCCUS AUREUS."
					
		elif not coagulase:
	
			nitrate = ask("Is your bacterium capable of reducing nitrate to nitrate or othe nitrogenous compounds?")
			
			if nitrate:
				print "Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS."
					
			elif not nitrate:
				print "I do not know."
			
	elif not catalase:
		print "Does your bacterium exhibit alpha haemolysis?"
						
	else:
		print "Please answer with either \'Y\' or \'N\'"
	
elif not gramtest:
	print "Very well."

else:
	print "Please answer with either Y or N"
