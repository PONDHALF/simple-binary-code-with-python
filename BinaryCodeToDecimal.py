# =====================================
# Convert Binary code to decimal number
# Scripts By @PONDHALF
# =====================================


########################################################
# How Binary code work?
# 
# ex: binary code; 1 1 0 0 1 1 0 0 (len == 7)
# equals: 2^7 + 2^6 + 2^3 + 2^2 = 204 (skip binary code number 0)
# easy understand (binary code number == 1:yes, 0:no)
# so: 11001100 == 204 confirm!
#
########################################################


# input data type int
x = int(input("Input: "))

# split numbers (ex: input;123 => split;[1, 2, 3])
split = [int(i) for i in str(x)]

# get lenght of data
size = len(split)

# set anwser to 0 cuz we need to plus number after this loop
output = 0
# loop since i=0 to size of data(ex: data size equals 3; loop; i=0, i=1, i=2) 
for i in range(size):
    # we need backward numbers of size 
    # example: data's size equals 3 
    # variable size equals in loop size=2; size=1; size=0;
    size -= 1
    
    # get number in array index[..]
    # and if index[..] == 1 (condition) 
    if split[i] == 1:
        
        # hint: this condition we skip 0 
        # if split number equls 0, cuz we dont need 0 (binary basic)

        # output plus 2^size (if size of data equals 3 => means loop; 2^2 + 2^1 + 2^0)
        output += 2 ** size

# output answer with function print(..)
print(output)
