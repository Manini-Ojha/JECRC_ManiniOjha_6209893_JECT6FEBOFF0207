##dumps(): Encryption
##loads(): Decryption

#JSON is used to link(?) the data

'''
1.JSON,
2.pickle

'''

import json
file=open('temp.txt','a+')
data={
    'fullname':'Rahul Ghosh',
    'userid': 6376531813,
    'password': '******'
}
print(f'Orignal data:{data}')
print(f'Type of orignal data: {type(data)}')
print()

# enc_data=json.dumps(data)

# print(f'New data:{enc_data}')
# print(f'type of data:{type(enc_data)}')
# print()

# dec_data=json.loads(enc_data)

# print(f'Original data: {dec_data}')
# print(f'type pf data: {type(dec_data)}')


enc_data=json.dumps(data)
file.write(enc_data)

file.seek(0)
enc_data=file.read()
print(type(enc_data))

or_data=json.loads(enc_data)
print(or_data,type(or_data))

file.close()