"""
Dataset setup
=================================

This module handle data files and generate the datasets used
by the models.
"""

import logging

__all__ = [
    #'get_dataset', 
    #'load_dataset', 'save_dataset', 'split_dataset',
    #'filter_dataset', 'aggregate_dataset', 'describe_dataset'
]




def get_dataset(source):
    """
    Get dataset from a source. 
        Parameters
    ==========
    source : <type>
    Returns
    =======
    `pd.DataFrame`
        Dataset
    """
    raise NotImplementedError


def split_dataset(dataset, validation_ratio=0.1, test_ratio=None, seed=None):
    """Split dataset in train and validation sets (test optional) 
    using events and a given ratio. 

    This split conserve class balance.

    Parameters
    ==========
    dataset : `pd.DataFramer`
        Original dataset.
    validation_ratio : `float`
        Portion of images for validation dataset. (default=0.1)
    test_ratio : `float` or `None`
        Portion of images for test dataset. (default=`None`)
    seed : `int`or `None`
        Split by images
    Returns
    =======
    tuple of `pd.DataFrame`
        train, val or train, val, test
    """
    # Replicability
    if seed is not None:
        r = np.random.RandomState(seed)
    else:
        r = None
    # Split in train/val if test_ratio is None
    # else split in train/val/test (new_val_ratio = validation_ratio/(1. - test_ratio))
    raise NotImplementedError

def load_dataset(dataset_filepath):
    """Load dataset.

    Parameters
    ----------
    dataset_filepath : `str`
        Path to dataset file. (.csv)
    Returns
    =======
    `pd.DataFrame`
        Loaded dataset    
    """
    raise NotImplementedError

def save_dataset(dataset, output_folder, dataset_name):
    """Save Dataset.
    Parameters
    ----------
    dataset : `pd.Dataframe`
        Dataset.
    output_folder : `str`
        Folder containing saved file.
    dataset_name : `str`
        File name or dataset split (i.e. 'train').
    Returns
    =======
    `str`
        Dataset filepath 
    """
    raise NotImplementedError

"""
Utils Functions
===============
"""

def describe_dataset(dataset):
    """
    Perform simple description of the dataset.

    Parameters
    ==========
    dataset : `for example pd.DataFrame`
        Dataset.
    """
    raise NotImplementedError

def aggregate_dataset(dataset):
    """
    Perform simple aggegation to dataset.

    Parameters
    ==========
    dataset : `for example pd.DataFrame`
        Dataset.
    Returns
    =======
    `pd.DataFrame`
        Dataset with aggregate information.
    """
    raise NotImplementedError

def filter_dataset(dataset):
    """
    Select a subset from the dataset given some restrictions.

    Parameters
    ==========
    dataset : `for example pd.DataFrame`
        Dataset.
    Returns
    =======
     `pd.DataFrame`
        Filtered dataset.
    """
    raise NotImplementedError
