contact_info = {
    'name': 'Genesa Alvarez', 
    'address': '398 Day Lane',
    'city': 'Philadelphia',
    'state': 'PA',
    'zip':'19093'
                }
print(contact_info['address'])

print(f"""
          {contact_info['address']}
          {contact_info['city']}
          {contact_info['state']}
          {contact_info['zip']}
""")

del contact_info['name']

full_name = {'first name': 'Genesa', 'last name': 'Alvarez'}
full_name.update({'honorific': 'Dr.'})    # Added one more pair for honorific title
contact_info.update({'full_name': full_name})
print(contact_info)

print(f"""
           {contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
           {contact_info['address']}
           {contact_info['city']} {contact_info['state']} {contact_info['zip']}
""")