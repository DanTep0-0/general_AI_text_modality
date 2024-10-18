import numpy as np
import World_utils


class Senses_Body:

    # Unreal Version of Senses, because it's simplified version. And we work here only with text inputs
    # That's why I made Senses together with Body

    def __init__(self):
        self.location = {"location": World_utils.books[0], "position": 0}
        self.world = World_utils.load_world(self.location["location"])
        self.world_size = len(self.world)
        self.observable_radius = 5
        
        print("Senses_Body created")


    def readWords(self, start, end):
        """
        Returns all Words from "start" to "end" position inclusive.
        Return includes also with all additional information
        
        """
        if start <= end:
            return self.world[start : end+1]
        else:
            return self.world[end : start+1][::-1]
        
    
    def get_words_around(self, position, radius):
        left = position - radius
        right = position + radius

        if left < 0: left = 0
        if left > self.world_size: left = self.world_size

        return self.world[left : right+1]


    def move(self, position_change):

        # Move Funktion if we see only word. that we've just read:

        # if self.location["position"] == 0:
        #     start = 0
        # else:
        #     start = self.location["position"] + np.sign(position_change)
        
        # end = start + int(position_change - np.sign(position_change))

        # valid_change = False
        # if start >= 0 and start <= self.world_size and end >= 0 and end <= self.world_size:
        #     valid_change = True
        #     self.location["position"] = end

        # if valid_change:
        #     return self.readWords(start, end)
        # else:
        #     return []

        ###################################################
        # Move Funktion if we see word around our position:

        end = self.location["position"] + position_change
        if end < 0: end = 0
        if end > self.world_size: end = self.world_size

        return self.get_words_around(end, self.observable_radius)
    
    
    def teleport(self, new_location_dic):
        if self.location["location"] != new_location_dic["location"]:
            self.world = World_utils.load_world(new_location_dic["location"])
            self.world_size = len(self.world)

        self.location = {"location": new_location_dic["location"], "position": new_location_dic["position"]}
        return self.get_words_around(new_location_dic["position"], self.observable_radius)
