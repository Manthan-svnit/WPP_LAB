
def decode_ways(s, index=0, current_decoding="", results=None):
    if results is None:
        results = []
    
    if index == len(s):
        results.append(current_decoding)
        return
    
    # Consider single-digit number
    num1 = int(s[index])
    if 1 <= num1 <= 9:
        decode_ways(s, index + 1, current_decoding + chr(64 + num1), results)
    
    # Consider two-digit number
    if index + 1 < len(s):
        num2 = int(s[index:index + 2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, current_decoding + chr(64 + num2), results)
    
    return results

# User Input:
encoded_message = input("Enter the encoded message: ")

decoded_messages = decode_ways(encoded_message)
print("Possible decodings:")
for message in decoded_messages:
    print(message)
