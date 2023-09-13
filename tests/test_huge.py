import unittest
from unittest.mock import patch

from huge import get_name


@patch("requests.get")
class TestHuge(unittest.TestCase):
    def test_main(self, mocked_request):
        # Patch a JSONified response
        mocked_request.return_value.json.return_value = [{"name": "Mars"}]
        result = get_name.main()
        self.assertEqual(result, 0)
