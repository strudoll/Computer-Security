import string

def frequency_analysis(symbols):
    alphabet_list = list(string.ascii_uppercase)
    freq_list = [0] * 26

    for char in symbols:
        if char in alphabet_list:
            freq_list[alphabet_list.index(char)] += 1

    total_symbols = sum(freq_list)
    freq_list = [freq / total_symbols for freq in freq_list]

    return freq_list

def crossCorrelation(f, p):
    correlation_list = [x * y for x, y in zip(f, p)]
    return sum(correlation_list)

def get_caesar_shift(enc_message, expected_distribution):
    shift_float = crossCorrelation(frequency_analysis(enc_message), expected_distribution)
    shift = int(shift_float)
    return shift

def get_vigenere_keyword(enc_message, size, expected_dist):
    keyword = ""

    for i in range(size):
        m = enc_message[i::size] 
        shift = get_caesar_shift(m, expected_dist)
        keyword += chr((shift % 26) + 65) 

    return keyword

## VIGENERE CIPHER TEST
encrypted_message = "TEZHRAIRGMQHNJSQPTLNZJNEVMQHRXAVASLIWDNFOELOPFWGZ UHSTIRGLUMCSW GTTQCSJULNLQK OHL MHCMPWLCEHTFNUHNPHTSFFADJHTLNBYORWEFRYE PIISO K ZQR GMPTLQCSPRMOCMKESMTYLUTFRMIEOWXXFMWECCLWSQGWUASSWFGTTMYSGU L QNQGEFGTTIDSWMOAGMKEOQL U KOVN AMZHZRGACMKHZRHSQLKLBMJAXTKLVRGFCBTLNAM SMYAHEGIEHTKNFOELNBMWFGORHWTPAY MVOSGUVUSPD"
expected_distribution = [.1828846265,.1026665037, .0751699827, .0653216702, .0615957725, .0571201113, .0566844326,.0531700534,.0498790855,.0497856396,.0331754796,.0328292310,.0227579536,.0223367596,.0202656783,.0198306716,.0170389377,.0162490441,.0150432428,.0142766662,.0125888074, 0.0079611644, 0.0056096272,0.0014092016, 0.0009752181, 0.0008367550, 0.0005128469]

key_size = 4
vigenere_keyword = get_vigenere_keyword(encrypted_message, key_size, expected_distribution)
print("Vigenere Keyword:", vigenere_keyword)


