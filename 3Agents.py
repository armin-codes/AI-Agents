import time, sys, random


class AIAgent:
	def __init__(self, name):
		self.name = name
		self.job = random.choice(['teacher', 'chef', 'gardener', 'painter', 'musician', 'doctor', 'engineer', 'AI developer'])
		if self.job == 'teacher':
			self.skills = ['preparing lesson', 'grading assignments', 'teaching class', 'meeting with parents',
			               'organizing field trips️', 'attending seminars', 'creating learning materials',
			               'motivating students', 'managing a classroom']
		elif self.job == 'chef':
			self.skills = ['preparing ingredients', 'cooking meal', 'plating dish', 'cleaning kitchen', 'operating kitchen equipment'
			               'creating new recipes', 'ordering supplies', 'tasting food', 'developing flavor profiles']

		elif self.job == 'gardener':
			self.skills = ['planting seeds', 'watering plants', 'pruning plants', 'harvesting produce',
			               'weeding garden beds', 'applying fertilizers', 'identifying plant diseases',
			               'controlling pests', 'creating sustainable gardens']
		elif self.job == 'painter':
			self.skills = ['using different painting techniques' 'cleaning brushes', 'preparing canvases', 'painting', 'sketching',
			               'visiting art galleries', 'understanding art history', 'creating interesting paintings', 'mixing colors',]
		elif self.job == 'musician':
			self.skills = ['practicing instrument', 'composing song', 'recording music', 'playing instruments', 'composing for different ensembles'
			               'performing in the streets', 'tuning instruments', 'learning new pieces', 'reading music']
		elif self.job == 'doctor':
			self.skills = ['consulting patients', 'diagnosing illnesses', 'prescribing medication',
			               'managing a medical practice', 'conducting medical research' 'providing patient care',
			               'performing check-ups', 'conducting surgeries', 'reading medical journals']

		elif self.job == 'engineer':
			self.skills = ['designing structures', 'calculating loads and stresses', 'inspecting construction sites',
			               'using 3D printing', 'designing sustainable structures', 'working with robotics'
			               'ensuring safety regulations', 'drafting blueprints', 'collaborating with architects']
		else:  # AI developer
			self.skills = ['coding AI algorithms', 'training machine learning models', 'optimizing neural networks',
			               'creating computer vision systems',
			               'debugging code', 'attending AI conferences', 'reading AI research papers',
			               'working with big data', 'developing natural language processing models']

	def choose_best_activity(self):

		skills = self.skills.copy()  # Create a local copy of the skills list

		skill_values = [(skill, random.random()) for skill in
		                skills]  # Create a list of tuples containing the skill and a random value
		best_skill = max(skill_values, key=lambda x: x[1])[0]  # Choose the skill with the highest value
		skills.remove(best_skill)  # remove the chosen skill from the local list
		return best_skill

	def simulate_day(self):
		print(f"\nSimulating {self.name}'s day as a {self.job}:")
		for i in range(3):  # each agent does 3 activities in the morning
			activity = self.choose_best_activity()
			self.perform_activity(activity, "morning")

	def perform_activity(self, activity, time_of_day):
		print(f'{self.name} is {activity} in the {time_of_day}.')  # simulate time taken for activity
		time.sleep(3.5)


def random_food():
	foods = ['Fried Chicken', 'Mashed potato', 'Pizza', 'Hamburger', 'Cheeseburger', 'Royal With Cheese', 'Spicy Ramen',
	         'Pan Pizza', 'Cesar Salad', 'Potato Salad', 'French fries', 'Meat Steaks', 'Chicken Teriyaki',
	         'Tuna Sandwich',
	         'Tacos', 'Burrito', 'Mashed Potato', 'Butter Chicken', 'Tuna burger', 'Rice and Chicken', 'Chicken Soup']
	rand_food = random.choice(foods)
	return rand_food


def random_routine():  # Returns random morning routine
	routines = ['Meditating for an hour', 'Reading the news', 'Reading a self care book', 'Watching the sunrise',
	            'Checking out some websites', 'Reading the newspaper', 'Listening some music', 'Stretching',
	            'Taking a walk']
	random_morning_routine = random.choice(routines)
	return random_morning_routine


def get_name():  # Returns a random first and last name
	man_names = ["John", "David", "William", "James", "Robert", "Charles", "George", "Thomas", "Vincent", 'Jesse',
	             "Benjamin", "Daniel", "Christopher", "Matthew", "Lucas", "Jacob", "William", "Gabriel", 'Hank',
	             "Henry", "Samuel", "Logan", "Nathan", "Anthony", "Dylan", "Christian", "Gabriel", "Lucas",
	             "Aiden", "Elijah", "Mason", "Kevin", "Lincoln", "Grayson", "Brad", "Mason", "Chris", "Mehran",
	             "Mikael", "Vlad", 'Billiam', "Leonardo", 'Billy', 'Willy' "Oliver", "Farbod", "Darius", "Aren",
	             "Freddy", "James", "Joseph", "Robert", "Alexander", "Victor", "Lance", "Mr.", "Stanley", "Roman",
	             "Rahim", "Al", "Quentin", "Bobby", "Levi", "Lincoln", "Bart", "Leo", 'Mike', 'Will',
	             "Joshua", "Ryan", "Noah", "Ethan", "Bret", "Clint", 'Walter', "Jebediah", "Lester", "Dwight",
	             "Henry", "Anthony", "Caleb", "Dylan", "Michael", "Peter", "Timothy", "Jimothy", "Sam", 'Bill',
	             "Obediah", "Gill", "Aster", "Frank", "Franklin", "Aiden", "Agent.", 'Gabe', 'Martin', 'Todd', ]

	woman_names = ["Mary", "Jessica", "Sarah", "Lisa", "Jennifer", "Amanda", "Ashley", "Emily", "Samantha", "Brittany",
	               "Anna", "Susan", "Danielle", "Amy", "Andrea", "Stephanie", "Michelle", "Aurora", "Autumn", "Erica",
	               "Nicole", "Megan", "Katherine", "Elizabeth", "Lauren", "Victoria", "Rachel", "Barbara", "Claire",
	               "Christine", "Rebecca", "Amanda", "Deborah", "Sharon", "Kimberly", "Patricia", "Laura", "Linda",
	               "Barbara", "Abigail", "Addison", "Alexandra", "Alice", "Allison", "Alyssa", "Amber", "Amelia", "Diana"
	               "Angela", "Annabelle", "Ariel", "Ashley", "Audrey", "Beatrice", "Bella", "Clara", "Daisy", "Ella",
	               "Brittany", "Brooke", "Caroline", "Charlotte", "Chloe", "Christina", "Evelyn" "Emily", "Emma",
	               "Dorothy", "Eleanor", "Elizabeth"]

	lastnames = ["Daniels", "Johnson", "Anderson", "Miller", "Wilson", "Moore", "Taylor", "Bernard", "Hill", "Jayson",
	             "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Walker",
	             "Peterson"
	             'Kennedy', "Clinton", "Philip", "Brown", "Jones", "Davis", "Robinson", "Scott", "Torres", "Murphy",
	             "Franklin",
	             "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "Wright", "King", "Murphy", "Rivera",
	             "Westwood", "Howard", "Pitt", "Smith", "Williams", "Hudson", "Turner", "Green", "Carter", "Bell",
	             "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Morgan", "Perez", "Berry", "Campbell", "Phelps",
	             "Morris", "Eastwood", "Wallace", "Phillips", "Cruz", "Ward", 'White', "Black", "Scott", "Palmer"]
	random.shuffle(man_names)  # Randomize the lists of first and last names.
	random.shuffle(woman_names)
	random.shuffle(lastnames)
	first_name = man_names[0] if random.random() < 0.5 else woman_names[0]  # Get a random first name and last name.
	last_name = lastnames[0]
	return f"{first_name} {last_name}"  # Return the full name.


def random_transport():
	transport = ['going to work by bus ', 'going to work with bicycle ', 'going to work with personal car ',
	             'walking to work ', 'running to work ', 'going to work with cab ', "driving to work "]
	rand_transport = random.choice(transport)
	return rand_transport


def print_dots():
	sys.stdout.write("-")
	sys.stdout.flush()


def loading():
	sys.stdout.write(random_transport())
	num_dots = 1
	while num_dots <= 10:
		print_dots()
		time.sleep(random.randint(1, 3))
		num_dots += 1
	sys.stdout.write("> Arrived at work!\n")


def simulate_day():
	print(f"""Simulating [ {agent.name} ] day as a {agent.job}:
""")
	time.sleep(2)


def simulate_morning():
	print(f"""{agent.name} is {random_routine()} before work.\n""")
	time.sleep(5)
	print(f"""{agent.name} wants to go to work\n""")
	time.sleep(2.5)
	loading()
	for x in range(3):  # each agent does 3 activities in the morning
		activity = agent.choose_best_activity()  # Agent chooses an activity
		agent.perform_activity(activity, "morning")
	print(f'{agent.name} is having {random_food()} for lunch.')
	time.sleep(2)
	for y in range(3):  # each agent does 3 fun activities in the afternoon
		activity = agent.choose_best_activity()
		agent.perform_activity(activity, "afternoon")
	fun_activities = [
		'going for a walk', 'reading a book', 'listening to music', 'spending itme with family',
		'watching a game', 'playing a video game' 'meeting with friends', 'drinking a cool lemonade'
		                                                                  "in bathroom, don't interrupt",
		'watching a movie', 'playing a game', 'just chilling'
		                                      'taking a nice warm shower', 'being bored', 'doing something interesting',
		'drinking a nice cup of tea', 'making a to-do list', 'getting the news']
	print(f'{agent.name} is {random.choice(fun_activities)} in the evening.')
	time.sleep(3)
	print(f'{agent.name} is having {random_food()} for dinner.')
	time.sleep(3)
	print(f'''{agent.name} going to bed. Good night!
''')


agents = [AIAgent(get_name()) for a in range(3)]  # create 3 AI agents

for agent in agents:  # simulate each agent's day
	simulate_day()
	simulate_morning()
