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

def alphabet_cipher(input_msg):
    chart_new = chart.split('\n')
    
    # Split the input message into the code word and the raw_msg.
    # Convert to uppercase for later parsing
    code_word = input_msg.split(' ')[0].upper()
    raw_msg = input_msg.split(' ')[1].upper()

    # Gain the number of times code_word fits over raw_msg (+1).
    # Then, shorten to length of raw_msg.
    code_word_str = (((len(raw_msg)/len(code_word))+1) * code_word)[0:len(raw_msg)]

    # For each letter in the code word string and the message,
    # Find the column and row, respectively.
    # Note: row can be found by subtracting 1 from a column-index search.
    new_msg = ''
    for i in range(len(raw_msg)):
        code_ix = chart_new[0].index(code_word_str[i])
        msg_ix = chart_new[0].index(raw_msg[i])-1
        new_msg += chart_new[msg_ix][code_ix]

    return new_msg

alphabet_cipher('train murderontheorientexpress')
