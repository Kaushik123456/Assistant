# # import requests
# # import json

# # send_url = "http://api.ipstack.com/check?access_key=49fbf1709be0b9a85347365915d7b814"
# # geo_req = requests.get(send_url)
# # geo_json = json.loads(geo_req.text)
# # latitude = geo_json['latitude']
# # longitude = geo_json['longitude']
# # city = geo_json['city']
# # print(city)

# # import googlemaps
# # gmaps = googlemaps.Client(key='AIzaSyBEzLqJ5U5830OLnuqVn1LkBj1EINbxxwA')
# # loc = gmaps.geolocate()
# # print(loc)

# import requests
# import string
# from lxml import html
# from googlesearch import search
# from bs4 import BeautifulSoup

# # to search
# # print(chatbot_query('how old is samuel l jackson'))

# def chatbot_query(query, index=0):
#     fallback = 'Sorry, I cannot think of a reply for that.'
#     result = ''

#     try:
#         search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

#         page = requests.get(search_result_list[index])

#         tree = html.fromstring(page.content)

#         soup = BeautifulSoup(page.content, features="lxml")

#         article_text = ''
#         article = soup.findAll('p')
#         for element in article:
#             article_text += '\n' + ''.join(element.findAll(text = True))
#         article_text = article_text.replace('\n', '')
#         first_sentence = article_text.split('.')
#         first_sentence = first_sentence[0].split('?')[0]

#         chars_without_whitespace = first_sentence.translate(
#             { ord(c): None for c in string.whitespace }
#         )

#         if len(chars_without_whitespace) > 0:
#             result = first_sentence
#         else:
#             result = fallback

#         return result
#     except:
#         if len(result) == 0: result = fallback
#         return result

# print(chatbot_query('who is black widow'))

str = "hello everyone this is kaushik"
words = ""
j=0
for i in str.split(" "):
    print(i)
    if(i == "hello"):
        pass
    else:
        words += i+" " 
print(words)