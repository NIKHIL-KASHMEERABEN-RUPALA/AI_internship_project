from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionRecommendCareer(Action):
    def name(self):
        return "action_recommend_career"
    
    def run(self, dispatcher, tracker, domain):
        user_input = tracker.latest_message.get('text')
        
        # Logic for keyword-based recommendation
        if "tech" in user_input or "coding" in user_input:
            dispatcher.utter_message("You might enjoy a career in Software Development, Data Science, or Engineering.")
        elif "art" in user_input or "painting" in user_input:
            dispatcher.utter_message("You might consider careers in Fine Arts, Photography, or Graphic Design.")
        elif "business" in user_input or "finance" in user_input:
            dispatcher.utter_message("You could explore careers in Business Management, Finance, or Marketing.")
        else:
            dispatcher.utter_message("Let's figure it out together! Could you tell me more about your interests?")
        return []
