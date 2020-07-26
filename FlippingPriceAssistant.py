#Class for the Menu border
class MenuBorder():
    def border(self):
        print(' ')
        for i in range(45):
            print(" *", end='')


#This is a class filled with the fees associated with selling
#These will and can be added when calculating the price
class FeesAndMore():
    eBayFee = 10
    eBayFeeConverted = eBayFee / 100
    payPallFee = 2.9
    payPallFeeConverted = payPallFee / 100
    payPallSaleFee = 0.30 
    lowBallOffer = 20
    shippingFee = 6
    lowBallOfferConverted = lowBallOffer / 100
    pricePartsTotal = 0
    clearPartsTotal = pricePartsTotal - pricePartsTotal
    bGradeSub = 20
    cGradesub = 30
    dGradeSub = 40

#this is a class for phone flipping prices if the user were interested in phone flipping
class PhoneFlipping():
    def Flipping(self):
        errorCheck = False #Variable to check for error loops 
        while errorCheck == False:
            averageSalePrice = eval(input('\n What is the average sale price of the phone: '))
            salePriceCheck = input(f'\nYou entered the Average sale price as ${averageSalePrice:,.2f} is this correct? Y or N: ').upper()
            if salePriceCheck == "Y":
                errorCheck = True
            elif salePriceCheck == "N":
                errorCheck = False
            else:
                print("You entered a charachter that was not recgonized please try again")
        #formula to make code more readable
        feeFormula = averageSalePrice - (averageSalePrice * (FeesAndMore.payPallFeeConverted + FeesAndMore.eBayFeeConverted)) - FeesAndMore.payPallSaleFee - FeesAndMore.shippingFee #Formula for the price after fees are taken out
        feesTotal = averageSalePrice * (FeesAndMore.eBayFeeConverted + FeesAndMore.payPallFeeConverted) + FeesAndMore.payPallSaleFee
        #Prices for the grading scale before desired profit
        aGradeBP = feeFormula
        aGradeLow = aGradeBP - (aGradeBP * FeesAndMore.lowBallOfferConverted) #lowballOffer
        bGradeBP = feeFormula - FeesAndMore.bGradeSub
        bGradeLow = bGradeBP - (bGradeBP * FeesAndMore.lowBallOfferConverted) #lowBallOffer
        cGradeBP = feeFormula -  FeesAndMore.cGradesub
        cGradeLow = cGradeBP - (cGradeBP * FeesAndMore.lowBallOfferConverted) #Lowballoffer
        dGradeBP = feeFormula - FeesAndMore.dGradeSub
        dGradeLow = dGradeBP - (dGradeBP * FeesAndMore.lowBallOfferConverted)#lowBallOffer
        #Menu that shows the grading scale before profit, also links to the menu border class to write asterks 
        MenuBorder.border('*')
        print("\n\n\t\t\t Grading Scale Before Profit")
        print(f'\n\t\t\t   A Grade high: ${aGradeBP:,.2f} ')
        print(f'\n\t\t\t   A Grade low: ${aGradeLow:,.2f} ')
        print(f'\n\t\t\t   B Grade high: ${bGradeBP:,.2f} ')
        print(f'\n\t\t\t   B Grade low: ${bGradeLow:,.2f} ')
        print(f'\n\t\t\t   C Grade high: ${cGradeBP:,.2f} ')
        print(f'\n\t\t\t   C Grade low: ${cGradeLow:,.2f} ')
        print(f'\n\t\t\t   D Grade high: ${cGradeBP:,.2f} ')
        print(f'\n\t\t\t   D Grade low: ${cGradeLow:,.2f} ')
        print(f'\n\t\t\t    Total fees: ${feesTotal:,.2f}')
        MenuBorder.border('*')
        #Start the loop to find and change scale based on profit until satisfied
        desiredProfit = False
        while desiredProfit == False:
            profitPercent = int(input('\n\n\nEnter the percentage of profit you would like as a whole number ranging from 1 - 100 (e.g: 20, 10, 5, etc): '))
            percentConverted = profitPercent / 100
            if profitPercent in range (1,100):
                #Grading Scale After Profit
                aGradePofit = aGradeBP - (aGradeBP * percentConverted)
                aGradeLowProfit = aGradeLow - (aGradeLow * percentConverted)
                bGradeProfit= bGradeBP - (bGradeBP * percentConverted)
                bGradeLowProfit = bGradeLow - (bGradeLow * percentConverted)
                cGradeProfit = cGradeBP - (cGradeBP * percentConverted) 
                cGradeLowProfit = cGradeLow - (cGradeLow * percentConverted)
                dGradeProfit = dGradeBP - (dGradeBP * percentConverted)
                dGradeLowProfit = dGradeLow - (dGradeLow * percentConverted)
                #Variables to store each grades profit based on percentage 
                aGradeProfitAmount = averageSalePrice - aGradePofit
                aGradeLowProfitAmount = averageSalePrice - aGradeLowProfit
                bGradeProfitAmount = averageSalePrice - bGradeProfit
                bGradeLowProfitAmount = averageSalePrice - bGradeLowProfit
                cGradeProfitAmount = averageSalePrice - cGradeProfit
                cGradeLowProfitAmount = averageSalePrice - cGradeLowProfit
                dGradeProfitAmount = averageSalePrice - dGradeProfit
                dGradeLowProfitAmount = averageSalePrice -  dGradeLowProfit
                #Displays menu border for the grading scale after profit
                MenuBorder.border('*')
                print("\n\n\t\t\t\tGrading Scale After Profit")
                print(f'\n\tA Grade high: ${aGradePofit:,.2f} with an estimated ${aGradeProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tA Grade low: ${aGradeLowProfit:,.2f} with an estimated ${aGradeLowProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tB Grade high: ${bGradeProfit:,.2f} with an estimated ${bGradeProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tB Grade low: ${bGradeLowProfit:,.2f} with an estimated ${bGradeLowProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tC Grade high: ${cGradeProfit:,.2f} with an estimated ${cGradeProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tC Grade low: ${cGradeLowProfit:,.2f} with an estimated ${cGradeLowProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tD Grade high: ${dGradeProfit:,.2f} with an estimated ${dGradeProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\tD Grade low: ${dGradeLowProfit:,.2f} with an estimated ${dGradeLowProfitAmount:,.2f} profit at a {profitPercent}% Profit Margin.')
                print(f'\n\t\t\tThe total amount in fees are ${feesTotal:,.2f}')
                MenuBorder.border('*')
                #Loops for satisfaction check
                satisfied = False
                while satisfied == False:
                    satisfiedCheck = input('\n\n Are you satisified with the desired profit percentage, profit amount, and prices offered? If Yes enter Y or if No enter N: ').lower()
                    if satisfiedCheck == 'y':
                        satisfied = True
                        desiredProfit = True
                    elif satisfiedCheck == 'y':
                        print('\n Please enter a new profit percentage')
                        desiredProfit = False
                        satisfied = True
                    else:
                        print('You entered a invalid charachter please try again')
                        satisfiedCheck = False
            elif profitPercent not in range(1,100):
                print('You entered a number that was not in range from 1 - 100. Please enter a number in range')
                desiredProfit = False



#Determines the selling option and calls that class 
SellingOptions = {0: 'Done Selling 🚫', 1: 'Flipping Phones 📱'}
selling = True
while selling == True:
    MenuBorder.border('*') 
    print('\n\n')
    for key, value in SellingOptions.items():
        print('\t\t\t\t',key, ':', value)
    MenuBorder.border('*')
    yourOption = eval(input('\n\nEnter the number of the selling option you would like: '))
    if yourOption == 0:
        print('\n🤑 You are now done selling 🤑')
        break

    if yourOption == 1:
        PhoneFlipping.Flipping('Flip')
        selling = False
    elif yourOption not in range(0,1):
        print('You entered an invalid option please try again')
