#internal symbols. don't change. to change display, change SYMBOL_format variables
DOT = '.' #dot symbol
DASH = '-' #dash symbol
EOS = '_' #end of symbol symbol
EOW = '/' #end of word symbol
SIGN0 = '0' #signal 0 symbol (no beep)
SIGN1 = '1' #signal 1 symbol (beep)
UNKNOWN = ' ' #unknown symbols placeholder
SPACE = ' ' #space between words in plaintext symbol

#symbol formatting - can be strings of any length
DOT_format = "."
DASH_format = "-"
EOS_format = " "
EOW_format = " / "
SIGN0_format = "."
SIGN1_format = "|"

#lengths
DOT_L = 1 #dot length in 1s
DASH_L = 3 #dash length in 1s
EOD_L = 1 #end of dot/dash length in 0s
EOS_L = 3 #end of symbol length in 0s
EOW_L = 7 #end of word length in 0s

#boolean settings
EXTENDED = True #if includes extended alphabet, like punctuation symbols
USE_UNKNOWN_SYMBOL = False #if using unknown symbol for unknown characters instead of skipping them

#alphabets
alphabet_normal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', #letters a-m
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', #letters n-z
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', #digits
                   UNKNOWN] #unknown
alphabet_normal_extended = ['&', '\'', '@', ')', '(', ':', ',', '=', '!', '.', '-', '+', '\"', '?', '/', '\n']
alphabet_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', #letters a-m
                  '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', #letters n-z
                  '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', #digits
                  '........'] #unknown
alphabet_morse_extended = ['.-...', '.----.', '.--.-.', '-.--.-', '-.--.', '---...', '--..--', '-...-', '-.-.--', '.-.-.-', '-....-', '.-.-.', '.-..-.', '..--..', '-..-.', '.-.-']

if EXTENDED:
    alphabet_normal += alphabet_normal_extended
    alphabet_morse += alphabet_morse_extended

#s - String
#mc - Morse Compatible string
#m - Morse (string of . - | _)
#ml - Morse Letter/Symbol (one letter of morse code)
#mb - Morse Binary (string of 0 and 1)

def s_to_mc(s: str):
    s = s.lower()
    mc = ""
    for c in s:
        if c in alphabet_normal or c == SPACE:
            mc += c
        elif USE_UNKNOWN_SYMBOL:
            mc += UNKNOWN
    return mc

def ml_to_mb(m: str):
    mb = ""
    for d in m:
        if d == DOT:
            mb += SIGN1 * DOT_L
        elif d == DASH:
            mb += SIGN1 * DASH_L
        mb += SIGN0 * EOD_L
    return mb[0:-EOD_L]

def mc_to_m(mc: str):
    m = ""
    for c in mc:
        if c in alphabet_normal:
            index = alphabet_normal.index(c)
            m += alphabet_morse[index]
            m += EOS
        else: #if it's a space
            m = m[0:-len(EOS)] + EOW #removing EOS symbol
    return m[0:-len(EOW)]

def m_to_mb(m: str):
    mb = ""
    words = m.split(EOW)
    for w in words:
        letters = w.split(EOS)
        for l in letters:
            mb += ml_to_mb(l)
            mb += SIGN0 * EOS_L #separator for letters
        mb = mb[0:-EOS_L] + SIGN0 * EOW_L #separator for words
    return mb[0:-EOW_L] #minus extra end word units

def mb_to_m(mb: str):
    m = ""
    words = mb.split(SIGN0 * EOW_L)
    for w in words:
        letters = w.split(SIGN0 * EOS_L)
        for l in letters:
            symbols = l.split(SIGN0 * EOD_L)
            for s in symbols:
                if s == SIGN1 * DOT_L: m += DOT
                else: m += DASH
            m += EOS
        m = m[0:-len(EOS)] + EOW
    return m[0:-len(EOW)]

def m_to_mc(m: str):
    mc = ""
    words = m.split(EOW)
    for w in words:
        letters = w.split(EOS)
        for l in letters:
            index = alphabet_morse.index(l)
            mc += alphabet_normal[index]
        mc += SPACE
    return mc

def format_morse(inp, input_type):
    out = ""
    match input_type:
        case "m":
            orig = [DOT, DASH, EOS, EOW]
            repl = [DOT_format, DASH_format, EOS_format, EOW_format]
        case "mb":
            orig = [SIGN0, SIGN1]
            repl = [SIGN0_format, SIGN1_format]
        case _:
            return inp
    for c in inp:
        if c in orig:
            out += repl[orig.index(c)]
    return out

plaintext = "Hi! This is a test of morse code! A quick brown fox jumps over the lazy dog 1234567890-++%$=!! üüü"
nextstep = plaintext; print(nextstep); print()
nextstep = s_to_mc(nextstep); print(nextstep); print()
nextstep = mc_to_m(nextstep); print(format_morse(nextstep, "m")); print()
nextstep = m_to_mb(nextstep); print(format_morse(nextstep, "mb")); print("\n\n")
nextstep = mb_to_m(nextstep); print(format_morse(nextstep, "m")); print()
nextstep = m_to_mc(nextstep); print(nextstep)
