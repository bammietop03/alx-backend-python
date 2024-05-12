# Learning Unittests and Integration Tests

## Parameterized
The parameterized package in Python offers several useful extensions beyond parameterized.expand for creating parameterized test cases. Some of the notable extensions include:

### 1. parameterized.class_parameters
    @class_parameters(
    {"nested_map": {"a": 1}, "path": ("a",), "expected_result": 1},
    {"nested_map": {"a": {"b": 2}}, "path": ("a",), "expected_result": {"b": 2}},
    )
    class TestAccessNestedMapWithClassParameters(unittest.TestCase):

        def test_access_nested_map(self):
            self.assertEqual(access_nested_map(self.nested_map, self.path), self.expected_result)

### 2. parameterized.named_parameters
    @named_parameters(
    ("Case 1", {"a": 1}, ("a",), 1),
    ("Case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
    )
    class TestAccessNestedMapWithNamedParameters(unittest.TestCase):

        @parameterized.expand([
            ("Case 1", {"a": 1}, ("a",), 1),
            ("Case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ])
        def test_access_nested_map(self, name, nested_map, path, expected_result):
            self.assertEqual(access_nested_map(nested_map, path), expected_result)

### 3. parameterized.named_class_parameters
    @named_class_parameters(
    {"nested_map": {"a": 1}, "path": ("a",), "expected_result": 1},
    {"nested_map": {"a": {"b": 2}}, "path": ("a",), "expected_result": {"b": 2}},
    )
    class TestAccessNestedMapWithNamedClassParameters(unittest.TestCase):

        def test_access_nested_map(self):
            self.assertEqual(access_nested_map(self.nested_map, self.path), self.expected_result)

### 4. parameterized.skip_if and parameterized.skip_unless
    @parameterized.expand([
        (1, 2, 3),
        (4, 5, 9),
        (7, 8, 15),
    ])
    @skip_if(True, "Skipping this test case because condition is True")
    def test_addition(self, a, b, expected_result):
        self.assertEqual(a + b, expected_result)

### 5. parameterized.skip
    @parameterized.expand([
        (1, 2, 3),
        (4, 5, 9),
        (7, 8, 15),
    ])
    @skip("Skipping this test case unconditionally")
    def test_addition(self, a, b, expected_result):
        self.assertEqual(a + b, expected_result)

### 6. parameterized.iterated
    @parametrize.iterated([
        (1, 2, 3),
        (4, 5, 9),
        (7, 8, 15),
    ])
    def test_addition(self, a, b, expected_result):
        self.assertEqual(a + b, expected_result)