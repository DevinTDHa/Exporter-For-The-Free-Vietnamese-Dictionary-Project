from convert import *

input_data = """
@cam
* noun
- Orange
=cam thuộc giống cam quít+the orange belongs to the citrus genus
=rượu cam+orange-flavoured liqueur
-Children's disease due to malnutrition
#Syn
- quả cam
-Cam
=trục cam+a cam-shaft
- Xem máu cam
* verb
- To content oneself with, to resign oneself to
=không cam làm nô lệ+not to resign oneself to servitude
=có nhiều nhặn gì cho cam

@chuột
* noun
- Rat, mouse
=ướt như chuột lột+drenched to the bone, like a drowned rat
!chuột chạy cùng sào
-to be at the end of one's tether
!cháy nhà ra mặt chuột
-xem cháy
!chuột sa chĩnh gạo
-xem chĩnh
"""

if __name__ == "__main__":
    # Parse the input data
    entries = parse_dictionary(input_data)

    from pprint import pprint

    pprint(entries)

    # Output to JSONL file
    # write_to_jsonl(entries, "dictionary_data.jsonl")

    # print("Dictionary has been successfully converted to JSONL format.")
