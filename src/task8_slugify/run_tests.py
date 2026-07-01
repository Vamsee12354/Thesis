import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from implementation_manual import slugify_manual

tests = {}

# test_no_text
tests["test_no_text"] = slugify_manual('') == None

# test_functionality
tests["test_functionality"] = slugify_manual('Writing slugify code helloWorld') == 'writing-slugify-code-helloworld'

# test_all_capitals
tests["test_all_capitals"] = slugify_manual('THE TEXTIS ALL CAPS') == 'the-textis-all-caps'

# test_sentence_with_no_space (user reverted this to expect camelCase splitting)
tests["test_sentence_with_no_space"] = slugify_manual('WritingslugifycodehelloWorld') == 'writing-slugify-code-helloworld'

# test_sentence_with_punctuations
tests["test_sentence_with_punctuations"] = slugify_manual('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam') == 'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam'

# test_single_word
tests["test_single_word"] = slugify_manual('Lorem') == 'lorem'

# test_spaces_single_word
tests["test_spaces_single_word"] = slugify_manual('                      Lorem') == 'lorem'

# test_repeated_spaces_between_words
tests["test_repeated_spaces_between_words"] = slugify_manual('Lorem          ipsum              dolor sit amet,                  consetetur sadipscing                elitr, sed                   diam') == 'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam'

# test_letters_spaces
result_letters = slugify_manual('L o r e m i p s u m d o l o r s i t a m e t , c o n s e t e t u r')
tests["test_letters_spaces"] = result_letters == 'l-o-r-e-m-i-p-s-u-m-d-o-l-o-r-s-i-t-a-m-e-t-c-o-n-s-e-t-e-t-u-r'

# test_different_language
tests["test_different_language"] = slugify_manual('Für die WMCE wählen Radiosprecher von Weltmusikprogrammen aus 24 Europäischen Ländern jeden Monat ihre persönliche Top 10 der aktuellen Albumveröffentlichungen.') == 'für-die-wmce-wählen-radiosprecher-von-weltmusikprogrammen-aus-24-europäischen-ländern-jeden-monat-ihre-persönliche-top-10-der-aktuellen-albumveröffentlichungen'

# test_already_slugified
tests["test_already_slugified"] = slugify_manual('writing-slugify-code-helloworld') == 'writing-slugify-code-helloworld'

# test_multiple_batches_text
tests["test_multiple_batches_text"] = slugify_manual('WritingslugifycodehelloWorld') == 'writingslugifycodehelloworld'

# test_symbols_inbetween_text
tests["test_symbols_inbetween_text"] = slugify_manual('Lorem @##$  ipsum &&&!@ dolor &!&@#! sit *!&@!# amet !@@#!@!/., consetetur $%#$#% sadipscing ,.,.><< > elitr $%%%^^^^^, sed diam') == 'lorem-ipsum-dolor-sit-amet-consetetur-sadipscing-elitr-sed-diam'

# test_ignore
tests["test_ignore"] = slugify_manual("hello%world", lowercase=True, ignore="%", truncate=None) == "hello%world"

# test_separator
tests["test_separator"] = slugify_manual("hello%  world", separator='+', ignore="%", truncate=None) == "hello%+world"

# test_truncate_1
result_trunc1 = slugify_manual("hello%  world", separator='+', ignore="%", truncate=2)
tests["test_truncate_1"] = result_trunc1 == None

# test_truncate_2
result_trunc2 = slugify_manual("Writing slugify code helloWorld", separator='-', truncate=14)
tests["test_truncate_2"] = result_trunc2 == "writing"

passed = sum(1 for v in tests.values() if v)
failed = sum(1 for v in tests.values() if not v)
print(f"PASSED: {passed}/{len(tests)}")
print(f"FAILED: {failed}/{len(tests)}")
print()
for name, result in tests.items():
    status = "PASS" if result else "FAIL"
    print(f"  {status}: {name}")

# Print actual values for failed tests
print()
for name, result in tests.items():
    if not result:
        print(f"  FAIL detail - {name}")

# Show actual outputs for key failing cases
print()
print("Actual outputs for potentially failing tests:")
print(f"  sentence_with_no_space: {repr(slugify_manual('WritingslugifycodehelloWorld'))}")
print(f"  multiple_batches_text: {repr(slugify_manual('WritingslugifycodehelloWorld'))}")
print(f"  letters_spaces: {repr(result_letters)}")
print(f"  truncate_1: {repr(result_trunc1)}")
print(f"  truncate_2: {repr(result_trunc2)}")
print(f"  already_slugified: {repr(slugify_manual('writing-slugify-code-helloworld'))}")
