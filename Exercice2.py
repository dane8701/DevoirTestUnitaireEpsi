import re
import string
import random
import os
import unittest

class Code:

    def validPass(self, chaine):
        num_format = re.compile('[0-9]')
        letter_format = re.compile('[a-zA-Z]')
        caract_format = re.compile("[!\#$%&'()*+,-./:;<=>?@[\]^_`{|}~]")
        upper_format = re.compile('[A-Z]')
        lower_format = re.compile('[a-z]')
        # caract_evident_format = re.match('')

        if(len(chaine) < 10 and len(chaine) > 25):
            print("Le mot de passe doit contenir entre 10 et 25 caractères.")
            return False
        elif not(re.match(num_format, chaine)):
            print("Le mot de passe doit contenir des chiffres.")
            return False
        elif not(re.match(letter_format, chaine)):
            print("Le mot de passe doit contenir des lettres.")
            return False
        elif not(re.match(caract_format, chaine)):
            print("Le mot de passe doit contenir des caractères spéciaux.")
            return False
        elif not(re.match(upper_format, chaine)):
            print("Le mot de passe doit contenir des lettres miniscules.")
            return False
        elif not(re.match(lower_format, chaine)):
            print("Le mot de passe doit contenir des lettres majuscule.")
            return False
        else:
            True

class CodeTest(unittest.TestCase):

    def test_ne_contient_pas_entre_10_et_25_caractere(self):
        password = Code()
        chaine = "ijhefoeae"
        self.assertFalse(password.validPass(chaine))

    def test_ne_contient_pas_des_chiffres(self):
        password = Code()
        chaine = "jqhfbekhzhfaeiufbzf"
        self.assertFalse(password.validPass(chaine), False)

    
    def test_ne_contient_pas_des_lettres(self):
        password = Code()
        chaine = "65419865165196499"
        self.assertFalse(password.validPass(chaine), False)

    def test_ne_contient_pas_des_caracteres_speciaux(self):
        password = Code()
        chaine = "oeqbgqrjzg654169erg"
        self.assertFalse(password.validPass(chaine), False)

    def test_ne_contient_pas_de_lettres_majuscule(self):
        password = Code()
        chaine = "oeqbgqrjzg654169erg"
        self.assertFalse(password.validPass(chaine), False)

    def test_ne_contient_pas_de_lettres_miniscule(self):
        password = Code()
        chaine = "IUFHGZJLG5616Z4ERG"
        self.assertFalse(password.validPass(chaine), False)

    def test_tout_est_ok(self):
        password = Code()
        chaine = "bhHBfdDQF684erg@"
        self.assertFalse(password.validPass(chaine), True)

if __name__ == '__main__':
    unittest.main()
