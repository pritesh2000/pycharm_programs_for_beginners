import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
+91 9823983298
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiii'''

# patt = re.compile(r'fass')          # Give string span of that
# patt = re.compile(r'.adm')        # . means any character or other
# patt = re.compile(r'^Tata')       # Start with
# patt = re.compile(r'iiiiiiii$')         # Ends with
# patt = re.compile(r'ai*')               # ai a aur 0 aur kitne bhi i
# patt = re.compile(r'ai+')                   # a aur i compalsary
# patt = re.compile(r'ai{2}')                   # a aur i {2}
# patt = re.compile(r'(ai){1}')                   # () made group
# patt = re.compile(r'(ai){1}|t')                   # | either or

# Special Sequences
# patt = re.compile(r'\ATata')                   # Beginning with
# patt = re.compile(r'27\b')                   # Beginning with or ending with

# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'\+91 \d{10}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)

