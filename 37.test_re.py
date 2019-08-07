

long_lat = {'Shanghai': "30 40.32' N, 120 51' E",
              'New York': "40 43' N, 74 0' W" ,
              'Paris': "42 51' N, 2 20' E" ,
              'London': "51 30' N, 0 5' E" ,
              "Berlin": "52 30' N, 13 25' E"
}

Info_s = "Tel:999992222"

import re

pattern_num = re.compile(".*?(\d+)")
tel_match = re.match(pattern_num, Info_s)
print(tel_match.group(1))

test_longitude = long_lat['Shanghai']
search_test = re.search('(\d+) ([\d\.\\\']+) (\w)', test_longitude)
print(search_test.group())
print(search_test.group(2))

all_n = re.findall("\d+ ", test_longitude)
print(all_n)

City = "New York"
SubFind = r"(\w+) (\w+)"
SubReplace = r"\2\t\1"
NewString = re.sub(SubFind,SubReplace, City)

print(NewString)


pat = re.compile("^[A-Z]+\d{1,}")
match_1 = re.match(pat, 'MRGPRX1')
print(match_1.group())

info_s1 = '179367_9059472_ROS1.1_1'
info_s2 =  '464_330984_3815(KIT)_9_2'

pat = re.compile(".*?([A-Z]+[A-Z\d]+).*")

mat_1 = re.match( pat, info_s1)
mat_2 = re.match( pat, info_s2)

print(mat_1.group(1))
print(mat_2.group(1))
