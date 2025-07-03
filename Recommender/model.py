import random 
def recommend_outfit (user_input,output_data):
    filtered =  outfit_data[outfit_data['Occation'] == user_input['Occation']]
    if filtered.empty:
        return "No Suitable outfits found."
    return filtered.sample(1).iloc[0] 