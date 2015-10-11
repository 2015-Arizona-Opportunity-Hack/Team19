__author__ = 'saipc'
scores = {
    'a': 2,
    'b': 3
}

totalSim = {
    'a': 20,
    'b': 30
}

rankings = [ (score/ totalSim[item], item) for item, score in scores.items()]

for item, score in scores.items():
    score = score / totalSim[item]
    rankings.append((score, item))