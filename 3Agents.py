import time, sys, random


class AIAgent:
	def __init__(self, name):
		self.name = name
		self.job = random.choice(
			['teacher', 'chef', 'gardener', 'painter', 'musician', 'doctor', 'engineer', 'AI developer'])
		if self.job == 'teacher':
			self.skills = ['preparing lesson', 'grading assignments', 'teaching class', 'meeting with parents',
			               'organizing field trips️', 'attending seminars', 'creating learning materials',
			               'motivating students', 'managing a classroom']
		elif self.job == 'chef':
			self.skills = ['preparing ingredients', 'cooking meal', 'plating dish', 'cleaning kitchen',
			               'creating new recipes', 'ordering supplies', 'tasting food', 'developing flavor profiles',
			               'operating kitchen equipment']
		elif self.job == 'gardener':
			self.skills = ['planting seeds', 'watering plants', 'pruning plants', 'harvesting produce',
			               'weeding garden beds', 'applying fertilizers', 'identifying plant diseases',
			               'controlling pests', 'creating sustainable gardens']
		elif self.job == 'painter':
			self.skills = ['sketching', 'mixing colors', 'painting', 'cleaning brushes', 'preparing canvases',
			               'using different painting techniques'
			               'visiting art galleries', 'understanding art history', 'creating interesting paintings']
		elif self.job == 'musician':
			self.skills = ['practicing instrument', 'composing song', 'recording music', 'playing instruments',
			               'composing for different ensembles'
			               'performing in the streets', 'tuning instruments', 'learning new pieces', 'reading music']
		elif self.job == 'doctor':
			self.skills = ['consulting patients', 'diagnosing illnesses', 'prescribing medication',
			               'managing a medical practice', 'conducting medical research'
			                                              'performing check-ups', 'conducting surgeries',
			               'reading medical journals', 'providing patient care', ]
		elif self.job == 'engineer':
			self.skills = ['designing structures', 'calculating loads and stresses', 'inspecting construction sites',
			               'using 3D printing', 'designing sustainable structures',
			               'ensuring safety regulations', 'drafting blueprints', 'collaborating with architects',
			               'working with robotics']
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
		print(f'{self.name} is {activity} in the {time_of_day}.')
		time.sleep(3.5)  # simulate time taken for activity


def random_food():
	foods = ['Fried Chicken', 'Mashed potato', 'Pizza', 'Hamburger', 'Cheeseburger', 'Royal With Cheese', 'Spicy Ramen',
	         'Pan Pizza', 'Cesar Salad', 'Potato Salad', 'French fries', 'Meat Steaks', 'Chicken Teriyaki',
	         'Tuna Sandwich',
	         'Tacos', 'Burrito', 'Mashed Potato', 'Butter Chicken', 'Tuna burger', 'Rice and Chicken', 'Chicken Soup']
	rand_food = random.choice(foods)
	return rand_food


def random_routine():
	routines = ['Meditating for an hour', 'Reading the news', 'Reading a self care book', 'Watching the sunrise',
	            'Checking out some websites', 'Reading the newspaper', 'Listening some music', 'Stretching', 'Taking a walk']
	random_morning_routine = random.choice(routines)
	return random_morning_routine


def get_name():  # Use the lists of names directly instead of calling functions
	firstnames = ["John", "David", "William", "James", "Robert", "Charles", "George", "Thomas", "Vincent", 'Jesse',
	              "Benjamin", "Daniel", "Christopher", "Matthew", "Lucas", "Jacob", "William", "Gabriel", 'Hank',
	              "Henry", "Samuel", "Logan", "Nathan", "Anthony", "Dylan", "Christian", "Gabriel", "Lucas",
	              "Aiden", "Elijah", "Mason", "Kevin", "Lincoln", "Grayson", "Brad", "Mason", "Chris", "Mehran",
	              "Mikael", "Vlad", 'Billiam', "Leonardo", 'Billy', 'Willy' "Oliver", "Farbod" "Darius", "Aren",
	              "Freddy", "James", "Joseph", "Robert", "Alexander", "Victor", "Lance", "Mr.", "Stanley", "Roman",
	              "Rahim", "Al", "Quentin", "Bobby", "Levi", "Lincoln", "Bart", "Leo", 'Mike', 'Will',
	              "Joshua", "Ryan", "Noah", "Ethan", "Bret", "Clint", 'Walter', "Jebediah", "Lester", "Dwight"
	              "Henry", "Anthony", "Caleb", "Dylan", "Michael", "Peter", "Timothy", "Jimothy", "Sam" 'Bill',
	              "Obediah", "Gill", "Aster", "Frank", "Franklin", "Aiden", "Agent.", 'Gabe', 'Martin', 'Todd', ]

	lastnames = ["Daniels", "Johnson", "Anderson", "Miller", "Wilson", "Moore", "Taylor", "Bernard", "Hill", "Jayson",
	             "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Walker",
	             "Franklin",
	             'Kennedy', "Clinton", "Philip", "Brown", "Jones", "Davis", "Robinson", "Scott", "Torres", "Murphy",
	             "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "Wright", "King", "Murphy", "Rivera",
	             "Westwood", "Howard", "Pitt", "Smith", "Williams", "Hudson", "Turner", "Green", "Carter", "Bell",
	             "Peterson"
	             "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Morgan", "Perez", "Berry", "Campbell", "Phelps",
	             "Morris", "Eastwood", "Wallace", "Phillips", "Cruz", "Ward", 'White', "Black", "Scott", "Palmer"]
	full_name = f"{random.choice(firstnames)} {random.choice(lastnames)}"  # Use string formatting instead of concatenation
	return full_name


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
		time.sleep(1)
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
	                  'going for a walk','reading a book', 'listening to music', 'spending itme with family',
	                  'watching a game', 'playing a video game' 'meeting with friends', 'drinking a cool lemonade'
	                  "in bathroom, don't interrupt", 'watching a movie', 'playing a game', 'just chilling'
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
