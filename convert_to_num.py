import os

print("file exists: " + str(os.path.exists("loans.csv")))

with open("loans.csv", "r") as file:
    lines = file.readlines()
    print("numlines: " + str(len(lines)))
    newlines = []

    for line in lines:
        print("line: " + line)

        # Loan_Type
        line = line.replace("Refinance(CEMA)", "0")
        line = line.replace("Refinance", "0")
        line = line.replace("Purchase", "1")

        # Sponsor Experience
        line = line.replace("New to Market/Phase", "1")
        line = line.replace("Moderate Experience", "3")
        line = line.replace("Very Experienced", "4")
        line = line.replace("Experienced", "2")

        # Property_Type
        line = line.replace("Residential", "0")
        line = line.replace("Mixed Use", "1")
        line = line.replace("Multi-Family", "2")
        line = line.replace("Commercial", "3")
        line = line.replace("Land", "4")
        line = line.replace("Portfolio", "5")

        
        line = line.replace("Urban", "0")
        line = line.replace("Suburban", "1")
        line = line.replace("Rural", "2")

        line = line.replace("Low", "0")
        line = line.replace("Moderate", "1")
        line = line.replace("High", "2")
        line = line.replace("Hign", "2")

        line = line.replace("Value-Add", "0")
        line = line.replace("Stabilized", "1")
        line = line.replace("Ground Up", "2")
        line = line.replace("GroundUp", "2")

        line = line.replace("No", "0")
        line = line.replace("Yes", "1")

        # Credit Score
        line = line.replace("550-619", "1")
        line = line.replace("620-649", "2")
        line = line.replace("650-679", "3")
        line = line.replace("680-699", "4")
        line = line.replace("700-759", "5")
        line = line.replace("760-850", "6")

        # Credit Rating
        line = line.replace("Very Poor", "1")
        line = line.replace("Low Acceptable", "2")
        line = line.replace("Acceptable", "3")
        line = line.replace("Good", "4")
        line = line.replace("High Acceptable", "5")
        line = line.replace("Excellent", "6")

        # Sponsor Track Record
        line = line.replace("< $10 Million ", "0")
        line = line.replace("< $10 Million", "0")
        line = line.replace("<10Million", "0")
        line = line.replace("$10-40 Million ", "1")
        line = line.replace("$10-40 Million", "1")
        line = line.replace("10-40Million", "1")
        line = line.replace("10-40 Million ", "1")
        line = line.replace("$41-100 Million ", "2")
        line = line.replace("$41-100 Million", "2")
        line = line.replace("$101-200 Million ", "3")
        line = line.replace("$101-200 Million", "3")
        line = line.replace("$200 Million + ", "4")
        line = line.replace("$200 Million +", "4")


        # Payment Status
        line = line.replace("Alternative Recoveries", "0")
        line = line.replace("Paid Off", "0")
        line = line.replace("Current Forbearance", "0")
        line = line.replace("REO", "0")
        line = line.replace("Foreclosure", "0")
        line = line.replace("Interest Default (60 - 90  Days)", "0")
        line = line.replace("Interest Default (90+ Days)", "0")
        line = line.replace("Past Due (11 - 29 Days)", "0")
        line = line.replace("Past Due (30 - 59 Days)", "0")
        line = line.replace("Maturity Default (60 - 90  Days)", "0")
        line = line.replace("ACH Payment Processing", "0")
        line = line.replace("Current", "0")

        # Status 2
        line = line.replace("Safe", "1")
        line = line.replace("In Risk", "2")
        line = line.replace("Default", "3")
        
        # Risk Grade
        line = line.replace("A+", "9")
        line = line.replace("A", "8")
        line = line.replace("A-", "7")
        line = line.replace("B+", "6")
        line = line.replace("B", "5")
        line = line.replace("B-", "4")
        line = line.replace("C+", "3")
        line = line.replace("C", "2")
        line = line.replace("C-", "1")

        # In Default?
        line = line.replace("N", "0")
        line = line.replace("Y", "1")

        line = line.replace("%", "")
        line = line.replace("$", "")
        line = line.replace("\"", "")
        line = line.replace(" ", "")

        
        line = line.replace("8ccount_0um", "Account_Num")
        line = line.replace("8RV", "ARV")
        line = line.replace("8RV", "ARV")
        line = line.replace("Repeat_5orrower", "Repeat_Borrower")
        line = line.replace("2redit_Score", "Credit_Score")
        line = line.replace("2redit_Rating", "Credit_Rating")

        line = line.replace("Status", "target")
        
        newlines.append(line)

with open("loans_new.csv", "w") as newfile:
    for line in newlines:
        newfile.write(line)
