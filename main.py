from tqdm import tqdm


def count_within_group(x: list, dt: float):
    """
    Two pointers algorithm. Start two pointer from last point. Decrease i (left point) if within dt.
    Decrease j (right point) if difference of values between points > dt.
    :param x: list of values
    :param dt: max difference between point values
    :return: dict, position: number of points with values < dt for each point in a subgroup
    """
    assert len(x) > 0
    i, j = len(x) - 1, len(x) - 1
    counter = {x: 0 for x in range(len(x))}
    while True:
        if j < 0:
            break
        elif i < 0:
            j -= 1
            i = j
        elif j == i:
            i -= 1
        elif x[j] - x[i] <= dt:
            counter[j] += 1
            i -= 1
        else:
            j -= 1
            i = j
    return counter


if __name__ == '__main__':
    # TODO argparse
    # TODO cleanup
    filename = 'incidents.csv'
    data = {}
    ids = {}
    unique_feature = set()

    with open(filename, 'r') as f:
        first_line = f.readline()
        # todo assert header
        # id, feature1, feature2, time
        split_header = first_line.rstrip().split(',')
        id, time = split_header[0], split_header[-1]
        assert id == 'id' and time == 'time' and len(split_header) > 2, \
            f"please ensure header in format 'id,feature1,feature2,...,featureX,time', current header is {first_line}"
        features = split_header[1:-1]

        print(id, features, time)

        for line in tqdm(f):
            split_line = line.strip().split(',')
            id, features, time = split_line[0], split_line[1:-1], split_line[-1]
            # todo assert fileformat
            # todo assert id is not decreasing
            id = int(id)
            features = tuple(map(int, features))
            time = float(time)

            unique_feature.add(features)

            if features not in data:
                data[features] = []
                ids[features] = []
            ids[features].append(id)
            data[features].append(time)

    result = {}
    for features in tqdm(sorted(unique_feature)):
        # print(ids[features], data[features])
        sorted_group = sorted(zip(ids[features], data[features]), key=lambda x: x[1])
        group_ids, group_data = zip(*sorted_group)
        counter_dict = count_within_group(data[features], dt=0.3)
        # print(counter_dict)
        for pos, value in counter_dict.items():
            result[group_ids[pos]] = value

    #print(sorted(result.items(), key=lambda x: x[0]))
    with open('output.txt', 'w') as f:
        f.write('id,count\n')
        for id, n in tqdm(sorted(result.items(), key=lambda x: x[0])):
            f.write(f"{id},{n}\n")
