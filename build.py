import os

resolve_dist_path = lambda file: os.path.join("dist", file.split('.')[0])

def wipe_dir(dir):
	for filename in os.listdir(dir):
		path = os.path.join(dir, filename)
		try:
			if os.path.isfile(path):
				os.remove(path)
				print(f"Deleted: {path}")
		except Exception as e:
			print(f"Failed to delete {path}: {e}")
			exit(1)
	print("Wiped " + dir)

if __name__ == "__main__":
	s = input("This will delete all files in dist, continue? [Y/n] ")
	if s.lower() == "n":
		exit(0)
	wipe_dir("dist")

	files = os.listdir("src")

	print(f"Building {len(files)} script(s)")
	for filename in files:
		path = os.path.join("src", filename)

		if not os.path.isfile(path):
			continue

		with open(path, 'r') as f:
			contents = f.read()

		out = resolve_dist_path(filename)
		with open(out, "w") as f:
			f.write(contents)

		print(f"Created: {out}")