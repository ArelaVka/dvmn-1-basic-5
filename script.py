import base64

base64_encoded = 'c2hvcElkOjEyMzQuc2NpZDo0MzIxLmN1c3RvbWVyTnVtYmVyOmFiYzAwMC5zaG9wQXJ0aWNsZUlkOjU2Nzg5MC5wYXltZW50VHlwZTpBQy5vcmRlck51bWJlcjphYmMxMTExMTExLmN1c3ROYW1lOkpvaG4gRG9lLmN1c3RBZGRyOtCc0L7RgdC60LLQsCwg0LAv0Y8gMTAwLm9yZGVyRGV0YWlsczrQodGH0LDRgdGC0YzQtSDQtNC70Y8g0LLRgdC10YUsINCyINC/0LDQutC10YLQuNC60LDRhSwg0YDQvtGB0YHRi9C/0YzRjg=='

def decoding_base64(base64_data):
    final_dict ={}
    base64_decoded = base64.b64decode(base64_data)
    chunks = str(base64_decoded).split('.')
    for chunk in chunks:
        key, value = chunk.split(':')
        if value.isnumeric():
            final_dict[key] = int(value)
        else:
            final_dict[key] = value
    return final_dict

def print_final_dict(dictionary_to_print):
    print(dictionary_to_print)

def main():
    print_final_dict(decoding_base64(base64_encoded))


if __name__ == '__main__':
    main()
