import os


def get_name(desire_name: str):
    count = 0
    final_name = desire_name
    while os.path.exists(final_name):
        count += 1
        final_name = f"{desire_name}_{count}"

    return final_name

