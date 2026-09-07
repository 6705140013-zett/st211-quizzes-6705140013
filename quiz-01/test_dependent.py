from solution import BankAccount

shared_account = BankAccount(100)

def test_a_deposit():
    shared_account.deposit(50)
    assert shared_account.balance == 150

def test_b_withdraw():
    shared_account.withdraw(30)
    # Balance becomes 120 because test_a_deposit already modified shared_account
    assert shared_account.balance == 120