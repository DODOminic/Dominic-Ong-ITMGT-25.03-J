
def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if letter==" ":
        return "\" \" "
    else:
        letter_unicode = ord(letter) - ord("A")
        new_letter_unicode = (letter_unicode+shift)%26
        new_letter=chr(new_letter_unicode+ord("A"))
        return new_letter

print(shift_letter("A", 1))
print(shift_letter("A", 2))
print(shift_letter("Z", 100))
print(shift_letter("X", 5))
print(shift_letter(" ",5))

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    ciphered_message=""
    for character in message:
        if character==" ":
            ciphered_message+=" "
        else:
            letter_unicode = ord(character)-ord("A")
            new_letter_unicode = (letter_unicode+shift)%26
            new_letter=chr(new_letter_unicode+ord("A"))
            ciphered_message+=new_letter
    return ciphered_message
print(caesar_cipher("XYZ",100))

def shift_by_letter(letter,letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #convert letter to number
    #use prev code
    shift=ord(letter_shift)-65
    
    if letter==" ":
        return "\" \" "
    
    letter_unicode = ord(letter) + shift
    new_letter = chr(letter_unicode)
    if  new_letter > "Z":
        new_letter = chr(ord(new_letter) - 26)
    return new_letter

print(shift_by_letter("A", "A"))
print(shift_by_letter("A", "C"))
print(shift_by_letter("Z", "Z"))
print(shift_by_letter(" ","B"))

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Turn message into numbers
    #Change each character in key based on the numbers from message
    #include the case of "longtext"
    key_unicode_list = []
    message_unicode_list = []
    final_unicode_list = []
    key_index = 0
    key_length = len(key)
    message_length = len(message)

    if len(message)<=len(key):
        for letter in key:
            key_unicode = ord(letter)
            key_unicode_list.append(key_unicode)

        for character in message:
            if character.isalpha():
                message_unicode = ord(character) - 65
                message_unicode_list.append(message_unicode)
            else:
                message_unicode_list.append(-1)  # Use -1 to represent spaces or non-alphabetic characters

        for key_unicode, message_unicode in zip(key_unicode_list, message_unicode_list):
            if message_unicode == -1:
                final_unicode_list.append(" ")
            else:
                unicode_sum = ((key_unicode + message_unicode) - 65) % 26
                final_unicode_list.append(chr(unicode_sum + 65))
    else:
        repeats = message_length // key_length
        remainder = message_length % key_length
        extended_key = key * repeats + key[:remainder]
        final_unicode_list.append(extended_key)

    final_message = "".join(final_unicode_list)
    return final_message

print(vigenere_cipher("ADCD", "XYZ"))


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    encoded_message=""
    while len(message)%shift!=0:
        message=message+"_"
    for i in range(len(message)):
        encoded_index=(i // shift) + (len(message) // shift) * (i % shift)
        encoded_message+=message[encoded_index]
    return encoded_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    There is no further brief for this number.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    original_message = ""
    for i in range(len(message)):
        original_index = (i // (len(message) // shift)) + (shift * (i % (len(message) // shift)))
        original_message += message[original_index]
    return original_message
print(scytale_decipher("IMNNA_FTAOIGROE", 3))
print(scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8))
print(scytale_decipher("IRIANMOGFANEOT__", 4))