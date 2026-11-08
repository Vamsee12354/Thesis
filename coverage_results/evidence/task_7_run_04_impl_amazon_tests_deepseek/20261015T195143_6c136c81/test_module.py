import unittest
from implementation_manual import shopping_list

class TestShoppingList(unittest.TestCase):
    def test_normal_functionality(self):
        input_list = [
            {"title": "Item1"},
            {"title": "Item2"},
            {"title": "Item3"},
            {"title": "Item4"}
        ]
        expected_output = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"
        self.assertEqual(shopping_list(input_list), expected_output)

    def test_empty_list(self):
        self.assertEqual(shopping_list([]), "<ul></ul>")

    def test_html_in_titles(self):
        input_list = [
            {"title": "<strong>Item1</strong>"},
            {"title": "<em>Item2</em>"}
        ]
        expected_output = "<ul><li><strong>Item1</strong></li><li><em>Item2</em></li></ul>"
        self.assertEqual(shopping_list(input_list), expected_output)

    def test_single_item(self):
        input_list = [{"title": "Single Item"}]
        expected_output = "<ul><li>Single Item</li></ul>"
        self.assertEqual(shopping_list(input_list), expected_output)