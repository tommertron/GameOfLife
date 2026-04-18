from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'gameoflife-secret-key'

COLLEGE_CAREERS = {
    'Nurse': 80000,
    'Doctor': 150000,
    'Lawyer': 120000,
    'Judge': 160000,
    'Scientist': 130000,
    'Computer Programmer': 140000,
    'CEO': 1000000,
    'Accountant': 100000,
    'Teacher': 90000,
}

CAREERS = {
    'Mechanic': 40000,
    'Loan Collector': 30000,
    'Dishwasher': 20000,
    'Cook': 50000,
    'Uber Driver': 35000,
    'Musician': 19000,
    'Bodyguard': 70000,
    'Influencer': 200000,
    'Reality TV Star': 150000,
    'Famous Actor': 1000000,
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_players = int(request.form['num_players'])
            if num_players < 1:
                raise ValueError
        except ValueError:
            return render_template('index.html', error='Please enter a valid number of players.')
        session.clear()
        session['num_players'] = num_players
        session['players'] = {}
        session['college_pool'] = list(COLLEGE_CAREERS.keys())
        session['career_pool'] = list(CAREERS.keys())
        return redirect(url_for('player_setup', n=1))
    return render_template('index.html')


@app.route('/player/<int:n>', methods=['GET', 'POST'])
def player_setup(n):
    num_players = session.get('num_players')
    if not num_players or n > num_players:
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name'].strip() or f'Player {n}'
        college = request.form['college'] == 'yes'
        want_kids = request.form['kids'] == 'yes'

        college_pool = session['college_pool']
        career_pool = session['career_pool']

        if college:
            if not college_pool:
                college_pool = list(COLLEGE_CAREERS.keys())
            title = random.choice(college_pool)
            college_pool.remove(title)
            salary = COLLEGE_CAREERS[title]
            session['college_pool'] = college_pool
        else:
            if not career_pool:
                career_pool = list(CAREERS.keys())
            title = random.choice(career_pool)
            career_pool.remove(title)
            salary = CAREERS[title]
            session['career_pool'] = career_pool

        kids = random.randint(0, 6) if want_kids else random.choices([0, 1, 2], weights=[70, 20, 10])[0]

        players = session['players']
        players[str(n)] = {
            'name': name,
            'college': college,
            'career': title,
            'salary': salary,
            'kids': kids,
        }
        session['players'] = players

        if n < num_players:
            return redirect(url_for('player_setup', n=n + 1))
        return redirect(url_for('play'))

    return render_template('player.html', n=n, num_players=num_players)


@app.route('/play')
def play():
    players = session.get('players')
    if not players:
        return redirect(url_for('index'))

    results = []
    winner_name = None
    top_winnings = 0

    for key in sorted(players, key=int):
        p = players[key]
        turns = 8 if p['college'] else 10
        winnings = random.randint(50000, 500000) + p['salary'] * turns
        results.append({
            'name': p['name'],
            'career': p['career'],
            'salary': p['salary'],
            'kids': p['kids'],
            'college': p['college'],
            'winnings': winnings,
        })
        if winnings > top_winnings:
            top_winnings = winnings
            winner_name = p['name']

    session['results'] = results
    session['winner'] = winner_name
    return redirect(url_for('results'))


@app.route('/results')
def results():
    results = session.get('results')
    winner = session.get('winner')
    if not results:
        return redirect(url_for('index'))
    return render_template('results.html', results=results, winner=winner)


if __name__ == '__main__':
    app.run(debug=True)
