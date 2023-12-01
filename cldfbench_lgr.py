import pathlib

from cldfbench import Dataset as BaseDataset


class Dataset(BaseDataset):
    id = 'lgr'
    dir = pathlib.Path(__file__).parent
