"""
------ Pseudocode:

create variable "guess" == 000000

while guess != 999999:
    ++guess
    submit guess

    if submission == valid:
        exit

"""
        
def generate():
    guess = 000000
    submission = False

    while guess < 999999:
        if submission == True:
            break
