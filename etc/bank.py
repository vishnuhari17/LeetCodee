def import_and_create_bank(filename):
    bank={}
    file=open(filename,'r')
    l=len(file.readlines())
    file.seek(0)
    for i in range(l):
        line=file.readline()
        words = line.split(":")
        m=words[0].strip()
        n=words[1].strip()
        if n.isdigit() == True:
            if m not in bank:
                bank[m] = int(words[1])
            else:
                bank[m] += int(words[1])
    file.close()
    return bank

def valid(password):
    up = 0
    low = 0
    for i in range(len(password)):
        if password[i].isupper() == True:
            up = 1
        if password[i].islower() == True:
            low = 1
    if len(password)>=8:
        if password.isalnum() == True:
            if up==1 and low==1:
                return True
    return False

def signup(user_accounts, log_in, username, password):
    if username not in user_accounts:
        if valid(password) == True:
            user_accounts[username] = password
            log_in[username] = False
            return True
    return False

def import_and_create_accounts(filename):
    file = open(filename,"r")
    user_accounts={}
    log_in={}
    l = len(file.readlines())
    file.seek(0)
    for i in range(l):
        line = file.readline()
        words = line.split("-")
        username = words[0].strip()
        password = words[1].strip()
        signup(user_accounts, log_in, username, password)
    print(user_accounts, log_in)

def login(user_accounts, log_in, username, password):
    if username in user_accounts:
        if password == user_accounts[username]
            log_in[username] = True
            return True
        else:
            return False

def update(bank, log_in, username, amount):
    if log_in[username] == True:
        if username not in bank:
            bank[username] = 0
        else:
            if amount > 0:
                bank[username] += amount
            else:
                if bank[username] >= -amount:
                    bank[username] -= amount
                else:
                    return False
        return True
    return False

def transfer(bank, log_in, userA, userB, amount):
    if log_in[userA] == True:
        if userB in log_in:
            update(bank, log_in, userA, -amount)
            update((bank, log_in, userB, amount))
            return True
    return False

def change_password(user_accounts, log_in, username, old_password, new_password):
    if username in user_accounts and log_in[username] == True:
        if user_accounts[username] == old_password and new_password != old_password:
            if valid(new_password) == True:
                user_accounts[username] = new_password
                return True
    return False

def delete_account(user_accounts, log_in, bank, username, password):
    if username in user_accounts and log_in[username] == True:
        if user_accounts[username]==password:
            del user_accounts[username]
            del log_in[username]
            return True
    return False

