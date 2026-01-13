# encrypted_id = "USR-2025-11-PAK-98342-XY"

# # Extract Year (indexes 4 to 8)
# year = encrypted_id[4:8]

# # Extract Country code ( last 8 to last 5)
# country = encrypted_id[-8:-5]

# # Extract serial number ( after last hyphen)
# serial = encrypted_id[-5:]

# month = encrypted_id[9:11]

# region = encrypted_id[0:3]

# print(" Year : " , year)
# print(" Country : " , country)
# print(" Serial : " , serial)
# print(" Month : " , month)
# print(" Region : " , region)


code = "PRD2025-BT77-CAT-XL-XS-S-M-L"

year = code[3:7]
extra_large_size = code[17:19]
batch_number = code[8:12]
category = code[13:16]
extra_small = code[-8:-6]
small_size = code[-5:-4]
mediam_size = code[-3:-2]
large_size = code[-1]
size = code[-11:]

print( " Year = " , year , "\t\n"   ,     "Batch_Number = " , batch_number , "\t\n"    ,    "Category = ",category  ,  "\t\n"  ,   "Extra_Small_Size = " , extra_small  , "\t\n"   , "Small_Size = " , small_size , "\t\n"  , "Mediam_Size = " , mediam_size  ,  "\n"  ,  "Large_Size = " , large_size , "\t\n"  , "Size = " , size)