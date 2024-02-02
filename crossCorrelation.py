
def crossCorrelation (f, p):
    list = [0] * len(f)
    list = [x * y for x, y in zip(f, p)]
    return sum(list)


s1 = [.012, .003, .01, .1, .02, .001]
s2 = [.001, .012, .003, .01, .1, .02]
s3 = [.1, .02, .001, .012, .003, .01]

# CROSS CORRELATION TEST
getCrossCorrelation_s1s2 = crossCorrelation(s1, s2)
getCrossCorrelation_s1s3 = crossCorrelation(s1, s3)

print("Set 1 and Set 2: ", getCrossCorrelation_s1s2)
print("Set 1 and Set 3: ", getCrossCorrelation_s1s3)