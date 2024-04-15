import datasets

dataset = datasets.load_dataset("GEM/FairytaleQA")


def create_fairy_tales_dataset():
    """
    Create a fairytale files from FairytaleQA
    :return:
    """
    for story in dataset['train']:
        story_name = story["story_name"]
        with open(f"./stories/{story_name}", "a") as f:
            f.write(story["content"])
