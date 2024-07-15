class Cifrador:
    def __init__(self, d):
        self.d = d

    def encrypt(self, text: str, shift: int):
        """Encrypt the message using Cesar's encrypter basis alphabet list."""
        alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")
        result = ""

        for char in text:

            if char.upper() in alphabet:
                char = char.upper()
                # Calculate the position in the alphabet and change to "new letter" after shift
                original_index = alphabet.index(char)
                new_index = (original_index + shift) % len(alphabet)
                new_char = alphabet[new_index]
                result += new_char
            else:
                result += char

        return result    


    def cifrar(self, mensaje):
        return self.encrypt(mensaje, self.d)
    
    def descifrar(self, mensaje):
        return self.encrypt(mensaje, -self.d)