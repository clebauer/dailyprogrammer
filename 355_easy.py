# Initialize internal chart
chart = '''  ABCDEFGHIJKLMNOPQRSTUVWXYZ
A abcdefghijklmnopqrstuvwxyz
B bcdefghijklmnopqrstuvwxyza
C cdefghijklmnopqrstuvwxyzab
D defghijklmnopqrstuvwxyzabc
E efghijklmnopqrstuvwxyzabcd
F fghijklmnopqrstuvwxyzabcde
G ghijklmnopqrstuvwxyzabcdef
H hijklmnopqrstuvwxyzabcdefg
I ijklmnopqrstuvwxyzabcdefgh
J jklmnopqrstuvwxyzabcdefghi
K klmnopqrstuvwxyzabcdefghij
L lmnopqrstuvwxyzabcdefghijk
M mnopqrstuvwxyzabcdefghijkl
N nopqrstuvwxyzabcdefghijklm
O opqrstuvwxyzabcdefghijklmn
P pqrstuvwxyzabcdefghijklmno
Q qrstuvwxyzabcdefghijklmnop
R rstuvwxyzabcdefghijklmnopq
S stuvwxyzabcdefghijklmnopqr
T tuvwxyzabcdefghijklmnopqrs
U uvwxyzabcdefghijklmnopqrst
V vwxyzabcdefghijklmnopqrstu
W wxyzabcdefghijklmnopqrstuv
X xyzabcdefghijklmnopqrstuvw
Y yzabcdefghijklmnopqrstuvwx
Z zabcdefghijklmnopqrstuvwxy'''

chart_new = chart.split('\n')

# Functions:
def split_msg(input_msg):
    # Split the input message into the code word and the raw_msg.
    # Convert to uppercase for later parsing
    code_word = input_msg.split(' ')[0].upper()
    raw_msg = input_msg.split(' ')[1].upper()
    
    return code_word, raw_msg

def encode(input_msg):
    new_msg = ''
    
    # Split the input message into the code word and the raw_msg.
    # Convert to uppercase for later parsing
    code_word, raw_msg = split_msg(input_msg)

    # Gain the number of times code_word fits over raw_msg (+1).
    # Then, shorten to length of raw_msg.
    code_word_str = (((len(raw_msg)/len(code_word))+1) * code_word)[0:len(raw_msg)]

    # For each letter in the code word string and the message,
    # Find the column and row, respectively.
    # Note: row can be found by subtracting 1 from a column-index search.
    for i in range(len(raw_msg)):
        code_ix = chart_new[0].index(code_word_str[i])
        msg_ix = chart_new[0].index(raw_msg[i])-1
        new_msg += chart_new[msg_ix][code_ix]

    return new_msg

def decode(input_msg):
    new_msg = ''
    # Split the input message into the code word and the encoded_msg.
    # Convert to uppercase for later parsing
    code_word, encoded_msg = split_msg(input_msg)
    encoded_msg = encoded_msg.lower()
    
    # Gain the number of times code_word fits over encoded_msg (+1).
    # Then, shorten to length of encoded_msg.
    code_word_str = (((len(encoded_msg)/len(code_word))+1) * code_word)[0:len(encoded_msg)]
    
    # now code_word_str == TRAINTRAINTRAINTRAINTRAI
    
    # For each letter in the code word string and the message,
    # Find the column first; this tells us where the index of the next character is.
    # Go through each row contain 
    for i in range(len(encoded_msg)): # for each letter in the message
        code_ix = chart_new[0].index(code_word_str[i])
        for j in range(len(chart_new)):
            if chart_new[j][code_ix] == encoded_msg[i]:
                new_msg += chart_new[j][0]

    return new_msg.lower()

decode('cloak klatrgafedvtssdwywcyty')
