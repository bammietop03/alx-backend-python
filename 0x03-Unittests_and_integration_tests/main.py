from utils import access_nested_map


# nested_map = {"a": {"b": {"c": 1}}}
# print(access_nested_map(nested_map, ["a", "b", "c"]))

nested_map = {"a": 1}
print(access_nested_map(nested_map, ["a", "b", "c"]))