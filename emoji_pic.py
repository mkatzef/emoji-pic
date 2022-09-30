import sys
import os
import imageio
import numpy as np

color_options = {  # rgb to emoji
    'red': (np.array((255,0,0)), '🟥'),
    'orange': (np.array((255,165,0)), '🟧'),
    'yellow': (np.array((255,255,0)), '🟨'),
    'green': (np.array((0,255,0)), '🟩'),
    'blue': (np.array((0,0,255)), '🟦'),
    'purple': (np.array((255,0,255)), '🟪'),
    'black': (np.array((0,0,0)), '⬛'),
    'white': (np.array((255,255,255)), '⬜'),
    'brown': (np.array((210,105,30)), '🟫')
}


def abs_error(v1, v2):
    return sum(abs(v1-v2))


def pow_error(v1, v2, a=2):
    return np.mean(abs(v1-v2) ** a) ** (1/a)


def nearest_emoji(pixel, dist_func=pow_error):
    ret = ''
    min_dist = None

    for col, emoji in color_options.values():
        dist = dist_func(pixel, col)
        if min_dist is None or dist < min_dist:
            min_dist = dist
            ret = emoji
    return ret


def main(img_path, n_cols=20):
    content = imageio.imread(img_path)

    img_rows, img_cols, img_channels = content.shape
    assert img_channels == 3, "Unexpected number of image channels: " + str(img_channels) + " (expected 3)"

    n_rows = int(round(n_cols * img_rows / img_cols))
    img_row_stepsize = int(np.ceil(img_rows / n_rows))
    img_col_stepsize = int(np.ceil(img_cols / n_cols))

    output = []
    for out_row in range(n_rows):
        new_row = []

        img_row_start = out_row * img_row_stepsize
        img_row_end = (out_row + 1) * img_row_stepsize
        src_rows = content[img_row_start : img_row_end, :, :]
        for out_col in range(n_cols):
            img_col_start = out_col * img_col_stepsize
            img_col_end = (out_col + 1) * img_col_stepsize
            src = src_rows[:, img_col_start : img_col_end][:]
            src = (1 + np.tanh(10*(src / 255 - 0.5))) * 255 / 2
            src = src.astype(int)
            mean_pixel = np.array(tuple(np.mean(src[:, :, i]) for i in range(3)))
            new_emoji = nearest_emoji(mean_pixel)

            new_row.append(new_emoji)
        output.append(new_row)

    print('\n'.join([''.join(r) for r in output]))


if __name__ == '__main__':
    usage = "usage: python3 emoji_pic.py path_to_picture [n_columns]"
    if len(sys.argv) < 2:
        print(usage)
        sys.exit(1)

    last_arg = sys.argv[-1]
    n_cols = 15
    if last_arg.isnumeric():
        n_cols = int(last_arg)
        if len(sys.argv) < 3:
            print(usage)
            sys.exit(1)
        last_arg = sys.argv[-2]

    if not os.path.isfile(last_arg):
        print("Could not find file:", last_arg)
        print(usage)
    else:
        main(last_arg, n_cols)
