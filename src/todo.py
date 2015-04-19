import re

class TODO(object):
	# create todo class
	"""
	docstring for TODO
	"""

	def __init__(self, comment, filename, line_number):
		print("'" + comment + "'")

		# define variables
		self.filename = filename
		self.line_number = line_number

		comment_lines = comment.splitlines()

		self.title = comment_lines[0]

		# search through body if for tags 
		if len(comment_lines) > 1 :
			self.body = "\n".join(comment_lines[1:]).rstrip()

			# find and extract tags
			self.tags = re.findall(r'#\w*', self.body)
			print(self.tags)

		else:
			self.body = ""


	def __repr__(self):

		# print set up
		ret = ""
		ret += "TODO\n"

		ret += "Title: " + str(self.title) + "\n"
		ret += "Body:  " + str(self.body) + "\n"
		ret += "File:  " + str(self.filename) + ":" + str(self.line_number) + "\n"

		if len(self.tags) > 0:
			ret += "Tags: "
		for tag in self.tags:
			ret += str(tag) + ", "

		return ret



if __name__ == '__main__':
	comment = """		TODO This is a todo
		This is a body #HASHTAGGALORE 
		#TWITTERSUCKS 
	"""
	test = TODO(comment, "file.py", 9999)

	print(test)


		