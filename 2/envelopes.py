necessityEnvelop = 0
freedomEnvelop = 0
educationEnvelop = 0
longTermEnvelop = 0
playEnvelop = 0
giveEnvelop = 0
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05
expectedIncome = 1000
print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.""")

summa=0
while (summa < expectedIncome):
    print("\n Enter the amount please:")
    line = int(input())
    summa += line
    necessityEnvelop += line * necRate
    freedomEnvelop += line * ffaRate
    educationEnvelop += line * eduRate
    longTermEnvelop += line * ltssRate
    playEnvelop += line * playRate
    giveEnvelop += line * giveRate

    

	
print("At the end we have:\n\
    Necessity Envelop has:                       " + str(int(necessityEnvelop)) + "\n\
    Financial Freedom Envelop has:               " + str(int(freedomEnvelop)) + "\n\
    Education Envelop                            " + str(int(educationEnvelop)) + "\n\
    Long Term Saving for Spending Envelop has:   " + str(int(longTermEnvelop)) + "\n\
    Play Envelop has:                            " + str(int(playEnvelop)) + "\n\
    Give Envelop has:                            " + str(int(giveEnvelop)) + "\n\
    _______________________________________________________________\n\
\
    Thanks for using our software :)")
