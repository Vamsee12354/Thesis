import unittest
from implementation_manual import shopping_list

class TestShoppingList(unittest.TestCase):

    def test_shopping_list_normal_functionality(self):
        # Arrange
        products = [
            {"title": "Item1"},
            {"title": "Item2"},
            {"title": "Item3"},
            {"title": "Item4"}
        ]
        expected_output = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_output)

    def test_shopping_list_empty_list(self):
        # Arrange
        products = []
        expected_output = "<ul></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_output)

    def test_shopping_list_single_item(self):
        # Arrange
        products = [{"title": "Solo Item"}]
        expected_output = "<ul><li>Solo Item</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_output)

    def test_shopping_list_with_html_in_title(self):
        # Arrange
        # Specification states titles are rendered without sanitization
        products = [{"title": "<b>Bold Item</b>"}]
        expected_output = "<ul><li><b>Bold Item</b></li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()