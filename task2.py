age = int(input("enter your age:"))
income = float(input("enter your monthly income"))
job = str(input("Do you have a valid job:(yes/no)")).strip().title()
loan = float(input("Enter the amount of loan you want: RS. "))


def loan_amount_calculator( age, income, job, loan):
    if age >= 21 and income >= 30000 and job == "Yes":
        if 30000 <= income <= 49999:
            max_loan = 300000
        elif 50000 <= income <= 79999:
            max_loan = 500000
        elif 80000 <= income <= 99999:
            max_loan = 800000
        else:
            max_loan = 1000000
          

        print(f"Maximum loan available: RS. {max_loan}")
        print(f"Requested loan amount: RS. {loan}")

        if loan <= max_loan:
            print("Loan status: Approved")
        else:
            print("Loan status: Not Approved")
            print("Reason: Requested loan amount exceeds the maximum limit.")
    else:
        print("Loan status: Not Approved")
        if age < 21:
            print("Reason: Age is below the minimum requirement of 21.")
        if income < 30000:
            print("Reason: Monthly income is below the minimum requirement of Rs. 30,000.")
        if job != "Yes":
            print("Reason: Valid job is required for loan eligibility.")

loan_amount_calculator(age, income, job, loan)