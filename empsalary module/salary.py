def gross(basic):
    return basic + basic * 0.20 + basic * 0.10

def deductions(basic):
    return basic * 0.05

def net(basic):
    return gross(basic) - deductions(basic)