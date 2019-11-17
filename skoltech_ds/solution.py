import argparse
from time import time as current_time
import pandas as pd
from algo import count_within_group


def solution_pandas(in_filename, out_filename, dt):
    input_data = pd.read_csv(in_filename)
    ids, counts = [], []
    # grouping data by features and count number of points before id within dt interval
    for _, group in input_data.groupby(['feature1', 'feature2'])['id', 'time']:
        sorted_group = group[['id', 'time']].sort_values('time', kind='mergesort')
        ids.extend(sorted_group['id'].values)
        counts.extend(count_within_group(sorted_group['time'].values, dt=dt))
    df = pd.DataFrame({'id': ids, 'count': counts}).sort_values('id')
    df.to_csv(out_filename, index=None)


def solution_python(in_filename, out_filename, dt):
    data = {}
    unique_feature = set()
    # read raw data and split data by groups based on features
    with open(in_filename, 'r') as f:
        _ = f.readline()
        for line in f:
            split_line = line.strip().split(',')
            id, features, time = split_line[0], split_line[1:-1], split_line[-1]
            id, features, time = int(id), tuple(map(int, features)), float(time)
            unique_feature.add(features)

            if features not in data:
                data[features] = {'id': [], 'time': []}
            data[features]['id'].append(id)
            data[features]['time'].append(time)

    # process grouped data
    result = {}  # this dictionary contains final {id: count} calculations
    for features in sorted(unique_feature):
        group = data[features]
        sorted_group = sorted(zip(group['id'], group['time']), key=lambda x: x[1])
        group_ids, group_times = zip(*sorted_group)
        counts = count_within_group(group_times, dt=dt)
        for pos, count in enumerate(counts):
            result[group_ids[pos]] = count

    # saving result
    with open(out_filename, 'w') as f:
        f.write('id,count\n')
        for id, n in sorted(result.items(), key=lambda x: x[0]):
            f.write("{},{}\n".format(id, n))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate number of incidents for each id within dT time if these \
                                                 incidents have same feature1, feature2 values")
    parser.add_argument('--input_filename', help="for example, incidents.csv", required=True)
    parser.add_argument('--output_filename', help="for example, output.csv", required=True)
    parser.add_argument('--dt', help="dT float value, for example 0.3", required=True, type=float)
    parser.add_argument('--use_pandas', help="if flag added use pandas solution (slow) otherwise use pure python \
                                              solution (fast)", required=False, action='store_true')
    args = parser.parse_args()
    start_time = current_time()
    if args.use_pandas:
        solution = solution_pandas
    else:
        solution = solution_python
    solution(args.input_filename, args.output_filename, args.dt)
    print('finished in %0.3f seconds' % (current_time() - start_time))
