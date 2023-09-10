import random
import time

print('''
Ai Agents Version 0.5
Writer of code: Armin Samiani
currently in development and not completed yet''')


class AIAgent:
	def __init__(self, name):
		self.name = name
		self.job = random.choice(
			['teacher', 'chef', 'gardener', 'painter', 'musician', 'doctor', 'engineer', 'AI developer'])

		if self.job == 'teacher':
			self.skills = ['preparing lesson', 'grading assignments', 'teaching class', 'meeting with parents',
			               'organizing field trips', 'attending seminars']
		elif self.job == 'chef':
			self.skills = ['preparing ingredients', 'cooking meal', 'plating dish', 'cleaning kitchen',
			               'creating new recipes', 'ordering supplies']
		elif self.job == 'gardener':
			self.skills = ['planting seeds', 'watering plants', 'pruning plants', 'harvesting produce',
			               'weeding garden beds', 'applying fertilizers']
		elif self.job == 'painter':
			self.skills = ['sketching', 'mixing colors', 'painting', 'cleaning brushes', 'preparing canvases',
			               'visiting art galleries']
		elif self.job == 'musician':
			self.skills = ['practicing instrument', 'composing song', 'recording music',
			               'performing concert', 'tuning instruments', 'learning new pieces']
		elif self.job == 'doctor':
			self.skills = ['consulting patients', 'diagnosing illnesses', 'prescribing medication',
			               'performing check-ups', 'conducting surgeries', 'reading medical journals']
		elif self.job == 'engineer':
			self.skills = ['designing structures', 'calculating loads and stresses', 'inspecting construction sites',
			               'ensuring safety regulations', 'drafting blueprints', 'collaborating with architects']
		else:  # AI developer
			self.skills = ['coding AI algorithms', 'training machine learning models', 'optimizing neural networks',
			               'debugging code', 'attending AI conferences', 'reading AI research papers']

	def choose_best_activity(self):
		# Assign a random value to each skill
		skill_values = {skill: random.random() for skill in self.skills}
		# Choose the skill with the highest value
		best_skill = max(skill_values, key=skill_values.get)
		self.skills.remove(best_skill)  # remove the chosen skill so it won't be repeated
		return best_skill

	def simulate_day(self):
		print(f"\nSimulating {self.name}'s day as a {self.job}:")
		for _ in range(3):  # each agent does 3 activities in the morning
			activity = self.choose_best_activity()
			self.perform_activity(activity, "morning")

	def perform_activity(self, activity, time_of_day):
		print(f'{self.name} is {activity} in the {time_of_day}...')
		time.sleep(2)  # simulate time taken for activity


def firstnames():
	return ["John", "David", "Michael", "William", "James", "Robert", "Charles", "George", "Thomas", "Joseph",
	        "Benjamin", "Daniel", "Christopher", "Matthew", "Lucas", "Alexander", "Noah", "Ethan", "Jacob", "William",
	        "Henry", "Samuel", "Logan", "Nathan", "Anthony", "Ryan", "Dylan", "Christian", "Gabriel", "Isaiah", "Owen",
	        "Aiden", "Elijah", "Mason", "Oliver", "Jameson", "Lincoln", "Grayson", "Isaiah", "Mason"
	                                                                                         "Chris", "Alexander",
	        "Freddy", "David", "William", "James", "Joseph", "John", "Robert", "Matthew", "Michael",
	        "Charles", "Thomas", "Daniel", "Benjamin", "Joshua", "Ryan", "Nathan", "Noah", "Ethan", "Dylan",
	        "Gabriel", "Lucas", "Henry", "Samuel", "Logan", "Anthony", "Caleb", "Frank", "Franklin", "Aiden",
	        "Oliver", "Elijah", "Levi", "Lincoln", "Gill", "Aster", "Aren", "Bart", "Leo", "Leonardo", "Michael",
	        "Roman",
	        "Obediah", "Lester", "Rahim", "Al", "Mehran", "Mikael", "Vlad"]


def lastnames():
	return ["Smith", "Williams", "Brown", "Jones", "Davis", "Miller", "Wilson", "Moore", "Taylor",
	        "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
	        "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "Wright", "King", "Scott", "Green",
	        "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Morgan", "Perez", "Turner", "Phillips", "Phelps",
	        "Campbell",
	        "Murphy", "Rivera", "Carter", "Bell", "Walker", "Murphy", "Hill", "Ward", "Torres", "Peterson", "Cruz",
	        'White', "Black", "Scott", "Palmer",
	        "Daniels", "Johnson", "Anderson", "Bernard", "Howard", "Pitt", "Morris", "Clinton", "Eastwood", "Wallace",
	        "Berry"]


def gfn():
	fname = random.choice(firstnames())
	lname = random.choice(lastnames())
	full_name = fname + " " + lname
	return full_name


def pgfn():
	print(gfn())


def simulate_day(agent):
	print(f"""\nSimulating [ {agent.name} ] day as a {agent.job}:
""")
	time.sleep(5)
	for _ in range(3):  # each agent does 3 activities in the morning
		activity = agent.choose_best_activity()
		agent.perform_activity(activity, "morning")
	print(f'{agent.name} is having lunch...')
	time.sleep(2)
	for _ in range(3):  # each agent does 3 fun activities in the afternoon
		activity = agent.choose_best_activity()
		agent.perform_activity(activity, "afternoon")
	fun_activities = ['reading a book', 'listening to music',
	                  'watching a movie', 'playing a game', 'going for a walk', 'meeting with friends',
	                  'watching a game',
	                  'taking a nice warm shower', 'being bored', 'doing something interesting',
	                  'drinking a cool lemonade',
	                  'making a to-do list', 'getting the news', "in bathroom {don't interrupt}",
	                  'drinking a nice cup of tea', 'just chilling', 'spending itme with family', 'playing a video game']
	print(f'{random.choice(fun_activities)} in the evening...')
	time.sleep(3)
	print(f'{agent.name} is having dinner...')
	time.sleep(3)
	print(f'got to bed... Good night! zZZ')


def best_action_for_teacher(goals, constraints, possible_actions):
	best_action = None
	best_score = -float('inf')
	for action in possible_actions:
		score = calculate_score(action, goals, constraints)
		if score > best_score:
			best_action = action
			best_score = score
	return best_action


# create 3 AI agents
agents = [AIAgent(gfn()), AIAgent(gfn()), AIAgent(gfn())]

# simulate each agent's day
for agent in agents:
	simulate_day(agent)
