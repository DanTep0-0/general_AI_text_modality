import numpy as np
import pymorphy2 as morph_analiser
import re
import pickle

books = ["Neznaika_Everything.txt", "Garry_Potter.txt"]

####################
# World Utilities:
####################


####################################################################################
# 1 Functions of World creating, downloading, finding worlds and textes with names
####################################################################################

def get_world_location(file_name):
    return "./Sketch_Simple_Text_GAI/Text_Knowledge_Analysed/" + file_name

def get_text_location(file_name):
     return "./Sketch_Simple_Text_GAI/Text_Knowledge/" + file_name


def analyse_text(text): # text is list of words, divided by " "
        morph = morph_analiser.MorphAnalyzer()
        Analysed_text = []
        #print(text[0])
        # print(text[1])
        # print(text[2])
        for i, w in enumerate(text):
            if (i % 100) == 0:
                print(i)
            # print("#######")
            # print("word: " + str(w))
            # print("##############")
            clean_word = "".join(filter(str.isalpha, w))
            #print("clean word = " + str(clean_word))

            part = {"subject": 0, "verb": 0, "adjecktiv": 0, "numeral": 0}
            animacy = None
            gender = {"neutr": 0, "femn": 0, "masc": 0}
            number = None
            time = {"past": 0, "pres": 0, "futr": 0}

            #print("Word morphology: " + str(self.morph.parse(clean_word)[0 : 1]))

            for meaning in morph.parse(clean_word)[0 : 1]:
                if meaning.tag.POS == "NOUN": part["subject"] += meaning.score
                elif meaning.tag.POS == "VERB" or meaning.tag.POS == "INFN": part["verb"] += meaning.score
                elif meaning.tag.POS == "ADJF" or meaning.tag.POS == "ADJS": part["adjecktiv"] += meaning.score
                elif meaning.tag.POS == "NUMR": part["numeral"] += meaning.score

                if animacy is None:
                    if meaning.tag.animacy != None:
                        animacy == True
                    else: animacy == False

                if number is None:
                    if meaning.tag.number == "sing": number = 1
                    elif meaning.tag.number == "plur": number = 2

                if meaning.tag.gender == "femn" and number != 2: gender["femn"] += meaning.score
                elif meaning.tag.gender == "masc" and number != 2: gender["masc"] += meaning.score

                if meaning.tag.tense == "past": time["past"] +=  meaning.score
                elif meaning.tag.tense == "pres": time["pres"] += meaning.score
                elif meaning.tag.tense == "futr": time["futr"] += meaning.score

            Analysed_text.append({"word": w, "part": part, "animacy": animacy, "gender": gender, "number": number, "time": time})

        return Analysed_text


def analyse_world(world_to_analyse):
    try:
            print("received location: " + str(world_to_analyse))
            with open(world_to_analyse, "r", encoding="utf8") as f:
                world_text = f.read()
    except:
        print("Text loading Error")
        return
        
    try:
        World = analyse_text(re.split(' |\n', world_text, flags=re.M)) # \n doesn't work. but it's ok for now
    except Exception as e:
        print("World analysing Error: ")
        print(type(e))
        print(e.args)
        return
                
    print("World successfuly analysed")
    
    return World


def save_analysed_world(file_name, World):
    # try:
    #      open(get_world_location(file_name), "x", encoding="utf8").close()
    # except Exception:
    #     print(str(Exception.args))
        
    #obj = {"a": 5, "b": 6}

    f = open(get_world_location(file_name), "wb")
    pickle.dump(World, f)
    #f.write("".join(World))
    f.close()
    
    return


def create_world_from_book(file_name):
     text_location = get_text_location(file_name)
     save_analysed_world(file_name, analyse_world(text_location))


def load_world(file_name):
     with open(get_world_location(file_name), "rb") as f:
        World = pickle.load(f)

     return World 
     

#####################################################################
# 2 
#####################################################################





#####################################################################
# 3 Own skript: Creating and savng all worlds
#####################################################################

if __name__ == '__main__':

    
    # for book in enumerate(books):
    #      create_world_from_book(book)
     
    create_world_from_book(books[1])
    #print(load_world(books[0])[0 : 100])

    # with open(get_world_location(books[0]), "r", encoding="utf8") as f:
    #     world_text = f.read()
    # print(world_text)