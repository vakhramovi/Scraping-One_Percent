import requests
import math
import json

def get_data():

	headers = {
	    'authority': 'e1k3unhdf2.execute-api.us-east-1.amazonaws.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,ka;q=0.6',
	    'origin': 'https://directories.onepercentfortheplanet.org',
	    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
	}

	params = {
	    'accountType': 'business',
	    'location': 'usa',
	    'pageSize': '20',
	}
	s = requests.Session()
	response = s.get('https://e1k3unhdf2.execute-api.us-east-1.amazonaws.com/search', params=params, headers=headers).json()
	
	TotalResults = int(response.get("totalResults"))
	
	pages = math.ceil(TotalResults / 20)

	all_elements = []
	with open("one_percent.json", "w", encoding="utf-8") as file_json:
		for page in range(1, pages + 1):
			response = s.get(f"https://e1k3unhdf2.execute-api.us-east-1.amazonaws.com/search?accountType=business&location=usa&pageSize=20&page={page}").json()

			results = response.get("results")
			for el in results:
				uri = el.get("uri")
				
				response = s.get(f"https://e1k3unhdf2.execute-api.us-east-1.amazonaws.com/accounts/{uri}").json()

				
				name = response.get("name", "None")
				type_ = response.get("type")
				website = response.get("website", "None")
				currency = response.get("currency", "None")
				summary = response.get("summary", "None")
				country = response.get("address", {}).get("country", "None")
				linkedin = response.get("linkedin", "None")
				instagram = response.get("instagram", "None")
				facebook = response.get("facebook", "None")
				youtube = response.get("youtube", "None")
				twitter = response.get("twitter", "None")


				element_list = {
					"Name" : name,
					"Type" : type_,
					"Website" : website,
					"Currency" : currency,
					"Summary" : summary,
					"Country" : country,
					"Linkedin" : linkedin,
					"Instagram" : instagram,
					"Facebook" : facebook,
					"Youtube" : youtube,
					"Twitter" : twitter
				}
				all_elements.append(element_list)
			json.dump(all_elements, file_json, indent=4, ensure_ascii=False)
        		
			
def main():
	get_data()

if __name__ == '__main__':
	main()