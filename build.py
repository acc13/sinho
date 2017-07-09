import os

with open("header.part") as header:
	with open("footer.part") as footer:
		headerc = header.read()
		footerc = footer.read()
		for root, directories, files in os.walk("."):
			for filename in files:
				filepath = os.path.join(root, filename)
				if filepath.endswith('.body'):
					with open(filename) as body:
						outfile = (filename[0:filename.find('.')] + ".html")
						with open(outfile, "w+") as out:
							print("building " + outfile)
							out.write(headerc)
							out.write(body.read())
							out.write(footerc)

