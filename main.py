class FairyTaleProcessor:

	def __init__(self, input_file, code_file, output_file):
		self.input_file = input_file
		self.code_file = code_file
		self.output_file = output_file
		self.stack = []

	def process_ntvh(self, line):

		self.stack.append(line)

	def process_ntvhi(self, line):

		self.stack.append(line)

	def process_file(self):
		try:

			with open(self.input_file, 'r') as input_f, \
         open(self.code_file, 'r') as code_f, \
         open(self.output_file, 'w') as output_f:

				command = code_f.readline().strip()

				for line in input_f:
					line = line.strip()
					if command == "NTVH":
						self.process_ntvh(line)
					elif command == "NTVHI":
						self.process_ntvhi(line)

				while self.stack:
					output_f.write(self.stack.pop() + '\n')

		except FileNotFoundError:
			print("One or more input/output files are missing.")


def main():
	processor = FairyTaleProcessor('input.txt', 'code.ftasm', 'output.txt')
	processor.process_file()


if __name__ == "__main__":
	main()
