import os


def get_name(desire_name: str):
    count = 0
    split = os.path.splitext(desire_name)
    extension = split[-1]
    final_name = desire_name
    while os.path.exists(final_name):
        count += 1
        final_name = f"{desire_name}_{count}.{extension}"

    return final_name
