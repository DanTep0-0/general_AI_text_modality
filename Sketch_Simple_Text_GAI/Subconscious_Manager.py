import numpy as np
import threading
import Input_sensations as input_senses
import Conscious_Manager as identity
import Memory_Interface as memory
import Conscious_Manager as identity
import Thought_Generator as thoughts


class Subconscious_Manager:

    def __init__(self, ticks=3):

        ##### Setting up the World-Perception

        self.senses_body = input_senses.Senses_Body()
        self.memory = memory.Memory_Interface()
        self.thoughts = thoughts.Thought_Generator()
        self.identity = identity.Conscious_Manager()
        self.ticks = ticks # Perception speed


        ##### Easy-version of receiving of "first feelings"
        
        # Our thoughts with respekt to relevance, importance and connected with Intentions
        self.thoughts_container = []

        # All important for us Intentions. It's realisation can be "freezed" for a time
        # We create our "first intention". No arguments, that's why the Intention will be "find out, what's going on"
        self.intention_container = [] # Intentions with information about importance and about immidiate importance
        
        # It's our Short Memory
        self.perception_history = [] # Important samples of our perception will be memorised

        # Our Attension to certain processes / Ability to use certain parts. In %
        self.inclusion = {
            "memory": 0.5,
            "thinking": 0.3,
            "movements": 0.2

        }


        # Our orientation in the world
        self.our_location = self.senses_body.location

        # Our current understanding of what's going on, where we are, what are we now doing and so on
        # Hence contains information about the most important Intentions now 
        # Without inclusion, without request
        current_perception = self.formulate_perception(self.senses_body, self.intention_container, self.thoughts_container, self.perception_history) # It's a komplex Knowledge-Format (Maybe a Vector)

        # With inclusion
        self.receive_perception(current_perception, self.inclusion["memory"], request=False)
        self.memory.memorise_perception(current_perception, self.inclusion["memory"], request=False)

        # Without inclusion
        first_Intentions = self.create_intention(self.senses_body, current_perception, request=False) 
        self.receive_intentions(first_Intentions, request=False)

        # Having Intentions. we start thinking and akting
        # Quick thoughts and decigions are pre-programmed. And are realised in Subconcious_Manager
        quick_thought = self.get_quick_thought(first_Intentions)
        self.make_quick_decigion(quick_thought)
        self.identity.start_thought_three(first_Intentions)



        print("Subconscious_Manager created")

        

    def create_intention(self, senses_body, current_perception):
        pass


    def formulate_perception(self, senses_body, intention_container, thoughts_container):
        pass

    def generate_thought(self, thinking_inclusion):
        pass
        Thought = None
        self.receive_thought(Thought, thinking_inclusion)


    def receive_intentions(self, intentions):
        """
        Updates current intention_container
        
        """

        pass


    def receive_perception(self, intention, memory_inclusion):
        """
        Updates current perception_container
        
        """

        pass


    def receive_thought(self, thought, thinking_inclusion):
        """
        Updates current perception_container
        
        """

        pass


    def get_quick_thought(self, first_Intentions):
        pass
        parameters = self.parameters_of_reaktion(first_Intentions)
        quick_thought = self.thoughts.generate_specific_thought(parameters)


    def make_quick_decigion(self, quick_thought):
        pass
        acting_parameters = self.reaktion_aktion_parameters(quick_thought)
        self.act(acting_parameters, self.senses_body)

    # def get_input(self, desired_input_dic):
    #     """
    #     Gets input information from all Senses
    #     """

    #     Text_input = self.senses_body.get_text_input(desired_input_dic["text"][0], desired_input_dic["text"][1])
    #     #print(Text_input)

    #     return Text_input
    

    # def preprocess_input(self, input):
    #     Preprocessed_input = None

    #     return Preprocessed_input
    

    # def manage(self, Concious_Intensions, desired_input):

    #     #get_input(self, {"text": ["./Sketch_Simple_Text_GAI/Text_Knowledge/Neznaika_Everything.txt", 120]})

    #     input = self.get_input(self, desired_input)
    #     preprocessed_input = self.preprocess_input(self, input)

    #     identity.notify_preprocessed_input(preprocessed_input)
    #     new_intensions, 

    #     return Subconcious_Intensions
