salary = float(input("Enter your monthly salary: "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 30000:
    if age >= 21:
        if credit_score >= 700:
            print("You are eligible for the bank loan.")
        else:
            print("Loan denied due to low credit score.")
    else:
        print("Loan denied due to age restriction.")
else:
    print("Loan denied due to insufficient salary.")
