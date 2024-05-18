from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionProvideSummary(Action):

    def name(self) -> Text:
        return "action_provide_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot("date")
        from_time = tracker.get_slot("from_time")
        to_time = tracker.get_slot("to_time")

        summary = f"Here is your absence request: Precard type: hourly absence, Date: {date}, From: {from_time}, To: {to_time}.  from .py"
        dispatcher.utter_message(text=summary)

        return []

class ActionAskForFromTime(Action):

    def name(self) -> Text:
        return "action_ask_for_from_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What is the start time for your request? from .py")
        return []

class ActionAskForToTime(Action):

    def name(self) -> Text:
        return "action_ask_for_to_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What is the end time for your request? from .py")
        return []

class ActionAskForDate(Action):

    def name(self) -> Text:
        return "action_ask_for_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="On which date would you like to request the absence? from .py")
        return []
