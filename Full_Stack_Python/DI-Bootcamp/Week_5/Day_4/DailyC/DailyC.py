

class Text:
    def __init__(self,string):
        self.content = string
        self.word_list = self.content.split()


    def word_frequency(self, word):
        if word in self.word_list:
            return f'the word "{word}" shows up {self.__word_frequency(word)} times in the current text'

    def __word_frequency(self,word):
        if word in self.word_list:
            return self.word_list.count(word)

    def most_common_word(self):
        word_set = set(self.word_list)
        word_dict = {}
        for word in word_set:
            word_dict.update({word:self.__word_frequency(word)})
        list_of_tuples = list(word_dict.items())
        return sorted(list_of_tuples, reverse=True)[0][0]
        



my_text = Text('''
Little Red Riding Hood decided to wear orange today.
You bite up because of your lower jaw.
The efficiency we have at removing trash has made creating trash more acceptable.
I'd always thought lightning was something only I could see.
Joyce enjoyed eating pancakes with ketchup.
She advised him to come back at once.
Erin accidentally created a new universe.
The efficiency with which he paired the socks in the drawer was quite admirable.
Joe discovered that traffic cones make excellent megaphones.
Gary didn't understand why Doug went upstairs to get one dollar bills when he invited him to go cow tipping.
When he encountered maize for the first time, he thought it incredibly corny.
There's no reason a hula hoop can't also be a circus ring.
A glittering gem is not enough.
Tuesdays are free if you bring a gnome costume.
We should play with legos at camp.
It's important to remember to be aware of rampaging grizzly bears.
Jenny made the announcement that her baby was an alien.
Dan ate the clouds like cotton candy.
She was sad to hear that fireflies are facing extinction due to artificial light, habitat loss, and pesticides.
He was sure the Devil created red sparkly glitter.
One small action would change her life, but whether it would be for better or for worse was yet to be determined.
He walked into the basement with the horror movie from the night before playing in his head.
I was very proud of my nickname throughout high school but today- I couldn't be any different to what my nickname was.
Today we gathered moss for my uncle's wedding.
He was the type of guy who liked Christmas lights on his house in the middle of July.
The light in his life was actually a fire burning all around him.
She saw the brake lights, but not in time.
Please put on these earmuffs because I can't you hear.
The llama couldn't resist trying the lemonade.
Wisdom is easily acquired when hiding under the bed with a saucepan on your head.
''')
print(my_text.word_frequency('your'))
print(my_text.most_common_word())
