# Accumulated Cyclone Energy module

def calc(wind):         # Converts a single wind point (in knots) to ACE
    if (wind <= 34):    # ACE does not calculate for tropical depressions
        return 0
    else:
        wind = float(wind)
        return float((wind * wind)/10000)
    
def calc_ignore(wind):  # Converts single wind point to ACE regardless of strength
    wind = float(wind)
    return float((wind * wind)/10000)

def hdp(wind):          # Converts single wind point to HDP
    if (wind <= 64):
        return 0
    else:
        wind = float(wind)
        return float((wind * wind)/10000)

def cumACE(winds):     # Parses winds and returns total ACE
    total = 0.0
    for wind in winds:
        total += calc(wind)
    return total

def cumACE_ignore(winds):   # Returns total ACE in winds regardless of strength
    total = 0.0
    for wind in winds:
        total += calc_ignore(wind)
    return total

def cumHDP(winds):   # Returns total HDP
    total = 0.0
    for wind in winds:
        total += hdp(wind)
    return total
    
def climo_at(ace):    # Categorizes season according to Atlantic climatology
    if (ace > 111):
        return "Above normal"
    elif (ace >= 153):
        return "Above normal (Hyperactive)"
    elif (ace < 66):
        return "Below normal"
    else:
        return "Near normal"

def climo_ep(ace):    # Categorizes season according to East Pacific climatology
    if (ace > 135):
        return "Above normal"
    elif (ace < 86):
        return "Below normal"
    else:
        return "Near normal"
