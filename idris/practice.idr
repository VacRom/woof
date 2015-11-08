module wholoves

data a = Mary | Maurice
data b = loveMary | loveMaurice
data c = True | False | Unknown
data wholoves a b = does a b

-- "Tell me, does __ love __ ?""
tellMe: wholoves a b -> c
tellMe (does Mary loveMary) = Unknown
tellMe (does Mary loveMaurice) = True
tellMe (does Maurice loveMary) = False
tellMe (does _ loveMaurice) = Unknown
