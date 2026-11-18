sales_record = [
    ('Marcus Webb',      'East',  4250.00),
    ('Priya Sharma',     'West',  5875.50),
    ('Deshawn Carter',   'East',  3100.75),
    ('Latonya Rivers',   'South', 6420.00),
    ('Bob Nguyen',       'West',  4980.25),
] 

total_sales = 0

for name, region, sales in sales_record:
    print(f'{name} ({region}): ${sales:,.2f}') 
    if sales > 5000: 
        print('^ Top Performer!')