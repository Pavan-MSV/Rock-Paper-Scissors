import random
from collections import Counter, defaultdict

def move_that_beats(m):
    return {'R': 'P', 'P': 'S', 'S': 'R'}[m]

def predict_by_frequency(history):
    if not history:
        return random.choice(['R','P','S'])
    c = Counter(history)
    most_common, count = c.most_common(1)[0]
    return most_common

def predict_by_markov(history):
    n = len(history)
    if n == 0:
        return random.choice(['R','P','S'])
    if n >= 2:
        trans = defaultdict(Counter)
        for i in range(n-2):
            key = (history[i], history[i+1])
            trans[key][history[i+2]] += 1
        last_key = (history[-2], history[-1])
        if last_key in trans and trans[last_key]:
            return trans[last_key].most_common(1)[0][0]
    if n >= 1:
        trans1 = defaultdict(Counter)
        for i in range(n-1):
            trans1[history[i]][history[i+1]] += 1
        last = history[-1]
        if last in trans1 and trans1[last]:
            return trans1[last].most_common(1)[0][0]
    return predict_by_frequency(history)

def detect_short_cycle(history, max_cycle_len=6, min_repeats=3):
    n = len(history)
    for cycle_len in range(1, max_cycle_len + 1):
        needed = cycle_len * min_repeats
        if n < needed:
            continue
        tail = history[-needed:]
        pattern = tail[:cycle_len]
        if pattern * min_repeats == tail:
            next_index = n % cycle_len
            return pattern[next_index]
    return None

def player(prev_play, opponent_history = []):
    if prev_play:
        if prev_play in ('R','P','S'):
            opponent_history.append(prev_play)
    hist = opponent_history

    EPS_RANDOM = 0.07

    cyc_pred = detect_short_cycle(hist, max_cycle_len=6, min_repeats=3)
    if cyc_pred:
        if random.random() > EPS_RANDOM:
            return move_that_beats(cyc_pred)
        else:
            return random.choice(['R','P','S'])

    markov_pred = predict_by_markov(hist)
    conf = 0.0
    if len(hist) >= 3:
        last2 = (hist[-2], hist[-1])
        count_next = 0
        count_total = 0
        for i in range(len(hist) - 2):
            if (hist[i], hist[i+1]) == last2:
                count_total += 1
                if hist[i+2] == markov_pred:
                    count_next += 1
        if count_total > 0:
            conf = count_next / count_total

    if conf >= 0.55:
        if random.random() > EPS_RANDOM:
            return move_that_beats(markov_pred)
        else:
            return random.choice(['R','P','S'])

    freq_pred = predict_by_frequency(hist)
    if hist:
        share = Counter(hist).most_common(1)[0][1] / len(hist)
    else:
        share = 0.0

    if share >= 0.4:
        if random.random() > EPS_RANDOM:
            return move_that_beats(freq_pred)
        else:
            return random.choice(['R','P','S'])

    if len(hist) >= 2:
        beat_prev_counts = Counter()
        for i in range(len(hist)-1):
            if hist[i+1] == move_that_beats(hist[i]):
                beat_prev_counts[hist[i+1]] += 1
        if beat_prev_counts:
            pred = beat_prev_counts.most_common(1)[0][0]
            if random.random() > EPS_RANDOM:
                return move_that_beats(pred)
            else:
                return random.choice(['R','P','S'])

    if hist:
        if random.random() > EPS_RANDOM:
            return move_that_beats(hist[-1])
        else:
            return random.choice(['R','P','S'])

    return random.choice(['R','P','S'])
