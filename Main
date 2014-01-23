def ask(question):
	print question
	return raw_input("> ") == "Y"


print "This is Bacterial Identification Tool v0.02"
print "This was created as a side project by ScepticRail when attempting to learn Python."
print "Any and all errors are, of course, intentional. Reporting them is futile."

print""

print "Please answer all the following questions with either Y or N to identify your bacterium:"

print ""

grampos = ask("Is your bacterium Gram-positive?")

if grampos:
	
	print "Is your bacterium catalase positive?\n"
	
	catalase = raw_input(">")
	
	if catalase == "Y":
	
		print "Is your bacterium coagulase positive?\n"
				
	coagulase = raw_input(">")
				
	if coagulase == "Y":
		print "Your bacterium is STAPHYLOCOCCUS AUREUS."
					
	elif coagulase == "N":
		print "Is your bacterium capable of reducing nitrate to nitrate or othe nitrogenous compounds?\n"
					
	nitrate = raw_input(">")
					
	if nitrate == "Y":
		print "Your bacterium is STAPHYLOCOCCUS EPIDERMIDIS."
					
	elif nitrate == "N":
		print "I do not know."
			
	elif catalase == "N":
		print "Does your bacterium exhibit alpha haemolysis?"
						
	else:
		print "Please answer with either Y or N"
	
elif not grampos:
	print "Very well."

else:
	print "Please answer with either Y or N"
