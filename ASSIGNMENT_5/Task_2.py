def demonstrate_list_slicing():

    original_list = list(range(1, 11))
    print(f"Original List: {original_list}")

    extracted_elements = original_list[0:5]
    print(f"Extracted First Five Elements: {extracted_elements}")

    reversed_extracted_elements = extracted_elements[::-1]

    print(f"Reversed Extracted Elements: {reversed_extracted_elements}")

demonstrate_list_slicing()
