from flask import Flask, request, jsonify

app = Flask(__name__)

# Pet Data (you can expand this with more pets)
pets_data = [
    {
        "id": 1,
        "name": "Fluffy",
        "age": "2 Years",
        "breed": "Unknown but cutie",
        "size": "Small",
        "activity_level": "Low",
        "hypoallergenic": True,
        "special_needs": "None",
        "image": "assets/images/cat1.jpg",
        "details_link": "pet-details.html?id=1"
    },
    {
        "id": 2,
        "name": "Pookie",
        "age": "1 Year",
        "breed": "Homely",
        "size": "Medium",
        "activity_level": "High",
        "hypoallergenic": False,
        "special_needs": "Needs daily grooming",
        "image": "assets/images/cat2.jpg",
        "details_link": "pet-details.html?id=2"
    },
    {
        "id": 3,
        "name": "Cutie",            
        "age": "1 Year",
        "breed": "Beauty",
        "size": "Small",
        "activity_level": "Low",
        "hypoallergenic": True,
        "special_needs": "None",
        "image": "assets/images/cat3.jpg",
        "details_link": "pet-details.html?id=3"
    },
    {
       "id": 4,
       "name": "Butter",
       "age": "2 Years",
       "breed": "Pure Indian",
       "size": "Medium",
       "activity_level": "Moderate",
       "hypoallergenic": False,
       "special_needs": "None",
       "image": "assets/images/dog1.jpg",
       "details_link": "pet-details.html?id=4"
    },
    {
       "id": 5,
       "name": "Musky",
       "age": "2 Years",
       "breed": "Lonely but warm",
       "size": "Medium",
       "activity_level": "Low",
       "hypoallergenic": True,
       "special_needs": "None",
       "image": "assets/images/dog2.jpg",
       "details_link": "pet-details.html?id=5"
    },
    {
      "id": 6,
      "name": "Toothsy",
      "age": "2 Years",
      "breed": "Happyland",
      "size": "Small",
      "activity_level": "High",
      "hypoallergenic": False,
      "special_needs": "None",
      "image": "assets/images/dog3.jpg",
      "details_link": "pet-details.html?id=6"
    },
    {
      "id": 7,
      "name": "Lolly",
      "age": "7 months",
      "breed": "Unknown",
      "size": "Small",
      "activity_level": "Moderate",
      "hypoallergenic": True,
      "special_needs": "None",
      "image": "assets/images/kitt1.jpg",
      "details_link": "pet-details.html?id=7"
    },
    {
       "id": 8,
       "name": "Sheryy",
       "age": "5 months",
       "breed": "Unknown",
       "size": "Small",
       "activity_level": "High",
       "hypoallergenic": True,
       "special_needs": "None",
       "image": "assets/images/pupp1.jpg",
       "details_link": "pet-details.html?id=8" 
    }   
    # Add other pets here
]

# Endpoint to serve all pet data
@app.route('/api/pets', methods=['GET'])
def get_pets():
    return jsonify(pets_data)

# AIRecommendation logic
def recommend_pets(user_input):
    recommended = []
    for pet in pets_data:
        score = 0
        
        # Match size preference
        if user_input.get('size') and user_input['size'].lower() == pet['size'].lower():
            score += 1
        
        # Match hypoallergenic preference
        if 'hypoallergenic' in user_input and user_input['hypoallergenic'] == pet['hypoallergenic']:
            score += 1
        
        # Match activity level preference
        if user_input.get('activity_level') and user_input['activity_level'].lower() == pet['activity_level'].lower():
            score += 1
        
        if score >= 2:  # Recommend pet if it matches at least 2 preferences
            recommended.append(pet)

    return recommended

# Endpoint for pet AIRecommendations based on user input
@app.route('/get_AIRecommendations', methods=['POST'])
def get_AIRecommendations():
    user_input = request.json
    AIRecommendations = recommend_pets(user_input)
    return jsonify({'AIRecommendations': AIRecommendations})

if __name__ == '__main__':
    app.run(debug=True)
