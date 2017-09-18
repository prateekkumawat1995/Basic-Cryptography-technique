# Transposition Cipher - encryption and decryption
# Using Python 3.6

#
def transposition(matrix, words):
    cipher = ''
    length = len(matrix)
    blanks = ''.join(' ' for i in range(length - 1))

    for x in range(0, len(words), length):
        item = words[x: x + length] + blanks
        for pos in matrix:                # Telling the loop to where to position each bit of plain text in cipher text
            cipher += item[pos - 1]

    return cipher.lower()

# Reversing the key bit
def reverse(matrix):
    length = len(matrix)
    arr = [0] * length
    for i in range(length):
        arr[matrix[i] - 1] = i + 1
    return arr

if __name__ == '__main__':

    text = 'Common sense is not so common.';
    matrix = [2, 4, 1, 3]
    print('The initial plain text is ' + text)
    print('The starting Matrix mechanism ' + str(matrix))
    ciphertext = transposition(matrix, text)
    print('Cipher Text is ' + ciphertext)
    secret = reverse(matrix)
    print('The reversed Key ' + str(secret))
    print('Decrypted text is ' + transposition(secret, ciphertext))