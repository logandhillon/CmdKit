import importlib
import inspect
import os
from cmdkit import Command, commands
import textwrap

def discover_commands():
	# discover all modules
	root = os.path.abspath("")
	module_names = [
		file[:-3] for file in os.listdir(root)
		if file.endswith('.py') and not file.startswith('__')
	]

	# load the commands
	for module_name in module_names:
		module = importlib.import_module(f"{module_name}")
		for _, body in inspect.getmembers(module):
			if inspect.isclass(body) and issubclass(body, Command) and body != Command:
				body()

# FIXME: this only gets the contents of the exec() method body, thus, breaking the script if it has content outside of said method
def create_command_files():
	output_dir = "dist"
	os.makedirs(output_dir, exist_ok=True)

	for command_name, command_instance in commands.items():
		file_path = os.path.join(output_dir, command_name)
		with open(file_path, "w") as file:
			file.write(process_exec_body(inspect.getsource(command_instance)))
			
def process_exec_body(input_string):
	lines = input_string.split('\n', 1)
	if len(lines) > 1:
		_, stripped_lines = lines
		stripped_lines = textwrap.dedent(stripped_lines)
		stripped_lines = textwrap.dedent(stripped_lines)
		return stripped_lines
	else:
		return ''

			
if __name__ == "__main__":
	discover_commands()
	create_command_files()
