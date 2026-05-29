# Tests for task4_get_reading_duration
import unittest
from implementation_manual import get_read_duration

class Test_get_read_duration(unittest.TestCase):
    def test_no_text(self):
        self.assertEqual(get_read_duration(""),0)

    def test_symbol_reading(self):
        self.assertEqual(get_read_duration("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@@@@@@@@@@###########################"),False)

    def test_normal_functionality(self):
        self.assertEqual(get_read_duration("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."),0.5)


    def test_other_language(self):
        self.assertEqual(get_read_duration("సాయంత్రం సమయంలో చిన్న కుక్క అందమైన వీధిలో వేగంగా పరుగెత్తుతూ ఉండగా, ఇంటి బయట కూర్చున్న కుటుంబ సభ్యులు మృదువైన సంగీతం వింటూ వేడి భోజనం సిద్ధం చేస్తున్నారు, పిల్లలు నవ్వుతూ ఆడుకుంటున్నారు, చల్లని గాలి వీచడంతో మొత్తం వాతావరణం ఎంతో ప్రశాంతంగా మరియు ఆనందంగా కనిపిస్తోంది."),0.5)

    def test_individual_letters(self):
        self.assertEqual(get_read_duration("L o r e m i p s u m d o l o r s i t a m e t , c o n s e t e t u r"),False)

    def test_same_letter_working(self):
        self.assertEqual(get_read_duration("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"),False)

    

    

if __name__ == "__main__":
    unittest.main()