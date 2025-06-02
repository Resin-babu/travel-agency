from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  

countries_data = {
    "Italy": {
        "cities": ["Rome", "Venice", "Florence"],
        "interests": {"Adventure", "Art", "Photography"},
        "purposes": {"Cultural Exploration", "Relaxation"}
    },
    "Japan": {
        "cities": ["Tokyo", "Kyoto", "Osaka"],
        "interests": {"Technology", "Nature", "Food"},
        "purposes": {"Adventure"}
    },
    "New Zealand": {
        "cities": ["Auckland", "Queenstown"],
        "interests": {"Adventure", "Nature", "Sports"},
        "purposes": {"Relaxation", "Adventure"}
    },
     "France": {
        "cities": ["Paris", "Nice", "Lyon"],
        "interests": {"Art", "History", "Food"},
        "purposes": {"Cultural Exploration"}
    },
    "Canada": {
        "cities": ["Toronto", "Vancouver", "Montreal"],
        "interests": {"Nature", "Sports", "Technology"},
        "purposes": {"Relaxation"}
    },
    "Brazil": {
        "cities": ["Rio de Janeiro", "São Paulo", "Salvador"],
        "interests": {"Adventure", "Nature", "Food"},
        "purposes": {"Adventure"}
    },
    "Thailand": {
        "cities": ["Bangkok", "Chiang Mai", "Phuket"],
        "interests": {"Food", "Nature", "History"},
        "purposes": {"Relaxation", "Cultural Exploration"}
    },
    "Australia": {
        "cities": ["Sydney", "Melbourne", "Brisbane"],
        "interests": {"Sports", "Nature", "Adventure"},
        "purposes": {"Adventure"}
    },
    "India": {
        "cities": ["Delhi", "Mumbai", "Goa"],
        "interests": {"History", "Food", "Technology"},
        "purposes": {"Cultural Exploration", "Adventure"}
    },
    "Spain": {
        "cities": ["Madrid", "Barcelona", "Seville"],
        "interests": {"Art", "History", "Food"},
        "purposes": {"Relaxation"}
    },
    "Germany": {
        "cities": ["Berlin", "Munich", "Hamburg"],
        "interests": {"Technology", "History", "Art"},
        "purposes": {"Cultural Exploration", "Relaxation"}
    },
    "South Korea": {
        "cities": ["Seoul", "Busan", "Jeju"],
        "interests": {"Technology", "Food", "Photography"},
        "purposes": {"Adventure"}
    },
    "USA": {
        "cities": ["New York", "Los Angeles", "Chicago"],
        "interests": {"Technology", "Art", "Sports"},
        "purposes": {"Adventure", "Relaxation"}
    },
    "Egypt": {
        "cities": ["Cairo", "Luxor", "Alexandria"],
        "interests": {"History", "Adventure", "Art"},
        "purposes": {"Cultural Exploration"}
    },
    "Turkey": {
        "cities": ["Istanbul", "Antalya", "Cappadocia"],
        "interests": {"History", "Food", "Nature"},
        "purposes": {"Relaxation", "Cultural Exploration"}
    },
    "South Africa": {
        "cities": ["Cape Town", "Johannesburg", "Durban"],
        "interests": {"Adventure", "Nature", "Sports"},
        "purposes": {"Adventure"}
    },
    "Indonesia": {
        "cities": ["Jakarta", "Bali", "Yogyakarta"],
        "interests": {"Food", "Nature", "Art"},
        "purposes": {"Relaxation"}
    },
    "Switzerland": {
        "cities": ["Zurich", "Lucerne", "Geneva"],
        "interests": {"Nature", "Adventure", "Music", "Photography"},
        "purposes": {"Relaxation"}
    },
    "United Kingdom": {
        "cities": ["London", "Edinburgh", "Manchester"],
        "interests": {"History", "Art", "Technology", "Music"},
        "purposes": {"Cultural Exploration", "Relaxation"}
    },
    "Greece": {
        "cities": ["Athens", "Santorini", "Thessaloniki"],
        "interests": {"Art", "Music", "Photography"},
        "purposes": {"Cultural Exploration", "Relaxation"}
    }
}
    

def get_match_percentage(user_interests, user_purpose, country_info):
    interests_overlap = user_interests.intersection(country_info["interests"])
    interest_score = len(interests_overlap) / len(user_interests) if user_interests else 0
    purpose_score = 1 if user_purpose in country_info["purposes"] else 0
    match_score = (interest_score * 0.7 + purpose_score * 0.3) * 100
    return round(match_score, 2)

@app.route("/match", methods=["POST"])
def match():
    data = request.json
    user_interests = set([i.title() for i in data.get("interests", [])])
    user_purpose = data.get("purpose", "").title()

    results = []
    for country, info in countries_data.items():
        match = get_match_percentage(user_interests, user_purpose, info)
        results.append({
            "country": country,
            "cities": info["cities"],
            "match_percentage": match
        })
    results.sort(key=lambda x: x["match_percentage"], reverse=True)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
