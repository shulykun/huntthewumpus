import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity


def make_dict(content_map):
    w_dict = []

    for node in content_map:
        for w in node['index'].split(' '):
            w_dict.append(w)

    return dict(zip(w_dict, list(range(len(w_dict)))))


def vectorize(sequense, content_dict):

    sequense_vec= np.zeros(len(content_dict))
    for i in sequense.split(' '):
        if i in content_dict:
            sequense_vec[content_dict[i]] = sequense_vec[content_dict[i]]+1

    return sequense_vec


def select_answer(input_sequense, content_map, sim_max = .15):

    content_dict = make_dict(content_map)

    z = vectorize(input_sequense, content_dict)
    y = np.array([vectorize(i['index'], content_dict) for i in content_map])
    v_sim = cosine_similarity([z],y)

    if v_sim.max() > sim_max:
        return content_map[v_sim.argmax()]

    else:
        return {}


def find_numbers(input_seq):
    numbers = re.findall('\d+', input_seq)
    if len(numbers):
        numbers = [int(i) for i in numbers]
    return numbers
