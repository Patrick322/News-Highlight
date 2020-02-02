def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The latest and tending news Review Website Online'
    return render_template('index.html', title = title)