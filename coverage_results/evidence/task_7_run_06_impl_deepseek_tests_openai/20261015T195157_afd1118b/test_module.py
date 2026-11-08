import unittest
from implementation_manual import shopping_list

class TestShoppingListFunction(unittest.TestCase):

    def test_normal_functionality(self):
        # Arrange
        products = [
            {"title": "Item1"},
            {"title": "Item2"},
            {"title": "Item3"},
            {"title": "Item4"}
        ]
        expected_html = "<ul><li>Item1</li><li>Item2</li><li>Item3</li><li>Item4</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_empty_shopping_list(self):
        # Arrange
        products = []
        expected_html = "<ul></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_single_item_list(self):
        # Arrange
        products = [{"title": "SingleItem"}]
        expected_html = "<ul><li>SingleItem</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_titles_with_html_content(self):
        # Arrange
        products = [{"title": "<b>BoldItem</b>"}, {"title": "<i>ItalicItem</i>"}]
        expected_html = "<ul><li><b>BoldItem</b></li><li><i>ItalicItem</i></li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_titles_with_whitespace(self):
        # Arrange
        products = [{"title": "  LeadingSpace"}, {"title": "TrailingSpace  "}, {"title": "  Both  "}]
        expected_html = "<ul><li>  LeadingSpace</li><li>TrailingSpace  </li><li>  Both  </li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_titles_with_special_characters(self):
        # Arrange
        products = [{"title": "Item & Co."}, {"title": "Item <Special>"}, {"title": "Item \"Quote\""}]
        expected_html = "<ul><li>Item & Co.</li><li>Item <Special></li><li>Item \"Quote\"</li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

    def test_titles_are_non_empty_and_non_none(self):
        # Arrange
        products = [{"title": "ValidTitle"}]

        # Act
        result = shopping_list(products)

        # Assert
        self.assertIn("<li>ValidTitle</li>", result)

    def test_missing_title_key_raises_key_error(self):
        # Arrange
        products = [{"name": "NoTitleKey"}]

        # Act & Assert
        with self.assertRaises(KeyError):
            shopping_list(products)

    def test_title_none_value_raises_type_error(self):
        # Arrange
        products = [{"title": None}]

        # Act & Assert
        with self.assertRaises(TypeError):
            shopping_list(products)

    def test_title_empty_string(self):
        # Arrange
        products = [{"title": ""}]
        expected_html = "<ul><li></li></ul>"

        # Act
        result = shopping_list(products)

        # Assert
        self.assertEqual(result, expected_html)

if __name__ == "__main__":
    unittest.main()