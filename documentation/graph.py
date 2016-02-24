import pygal

sunset_1 = pygal.StackedBar()

iterations = [0, 13, 0, 0, 0, 0]
shall = [47, 47 - iterations[1], 0, 0, 0, 0]
should = [19, 19, 0, 0, 0, 0]
could = [6, 6, 0, 0, 0, 0]

sunset_1.title = 'Sunset graph 1 du projet'
sunset_1.x_labels = map(str, range(0, 5))
sunset_1.add('Iterations', iterations)
sunset_1.add('Shall', shall)
sunset_1.add('Should', should)
sunset_1.add('Could', could)
sunset_1.render_to_file('sunset_1.svg')



sunset_2 = pygal.Histogram()

iterations = [(13, 1.1, 1.4), (0, 2, 2.5)]
shall = [(47, 1, 1.5), (0, 2, 2.5)]
should = [(66, 1, 1.5), (0, 2, 2.5)]
could = [(72, 1, 1.5), (0, 2, 2.5)]

sunset_2.title = 'Sunset graph 2 du projet'
sunset_2.add('Fait', iterations)
sunset_2.add('Shall', shall)
sunset_2.add('Should', should)
sunset_2.add('Could', could)
sunset_2.render_to_file('sunset_2.svg')