def findKey(data, target_key):
    if isinstance(data, dict):
        if target_key in data:
            return data[target_key]

        for value in data.values():
            result = findKey(value, target_key)
            if result is not None:
                return result

    elif isinstance(data, list):
        for item in data:
            result = findKey(item, target_key)
            if result is not None:
                return result