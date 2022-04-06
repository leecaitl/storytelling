import random
import itertools
import os
import pickle


def splitByBodyType(files):
    bodyTypes = {}

    for f in files:
        bt = f.split("_")[0]
        if bt not in bodyTypes:
            bodyTypes[bt] = []
        bodyTypes[bt].append(f)

    return bodyTypes


def getPairings():
    filenames = os.listdir("images")
    if ".DS_Store" in set(filenames):
        filenames.remove(".DS_Store")

    bts = splitByBodyType(filenames)

    story = set()
    stimuli = [random.choice(bts[i]) for i in bts.keys()]

    story = story | set(random.sample(sorted(stimuli)[:4], 2))
    story = story | set(random.sample(sorted(stimuli)[4:8], 2))
    story = story | set(random.sample(sorted(stimuli)[8:], 2))
    nonStory = set(stimuli) - story

    return stimuli, story, nonStory


if __name__ == '__main__':
    allCombos = []
    for i in range(1000):
        allCombos.append(getPairings())

    with open('stimuli.pkl', 'wb') as f:
        pickle.dump(allCombos, f)
