import random
import json

images = ['1.jpeg', '2.jpeg', '3.jpeg', '4.jpeg', '5.jpeg', '6.jpeg', '7.jpeg', '8.jpeg', '9.jpeg', '10.jpeg',
          '11.jpeg', '12.jpeg', '13.jpeg', '14.jpeg', '15.jpeg', '16.jpeg', '17.jpeg', '18.jpeg']


def shuffle_the_cards():
    with open("static/data.json", "r") as file:
        s = file.read()
    dictionary = json.loads(s)
    for index in range(len(dictionary["table"])):
        random_image = random.choice(images)
        dictionary["table"][index]["image"] = f"{random_image}"
        images.remove(random_image)
    str_dict = json.dumps(dictionary)
    with open("static/data.json", "w") as file:
        file.write(str_dict)


shuffle_the_cards()
