### Install environment:
I used Python 3 for this take-home code challenge.
You can install required libraries (basically pandas) via

``` pip install -r requirements.txt```

### Run
I did 2 solutions:

1.) First solution uses python system libraries only. Running time 10-15 seconds. Memory consumption ~ 200 mb.
To run:

```python solution.py --input_filename incidents.csv --output_filename output_python.txt --dt 0.3```

2.) Other solution uses pandas library to groupby a dataframe by features. Running time ~40 seconds. Memory consumption ~200 mb.
To run:

```python solution.py --input_filename incidents.csv --output_filename output_pandas.csv --dt 0.3 --use_pandas```

Both solution groupby the incidents dataframe by features columns, and uses two pointers algorithm for count calculation.

Use check correctness in solution in `check_correctness.ipynb` notebook.

Initial task below (in Russian)

![Alt text](task.png?raw=true "Title")
