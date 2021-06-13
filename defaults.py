import os


num_threads = '16'
wandb_silent = 'true'


def configure_environment():
    os.environ['WANDB_SILENT'] = wandb_silent
    if num_threads:
        os.environ['OMP_NUM_THREADS'] = num_threads
        os.environ['MKL_NUM_THREADS'] = num_threads
        os.environ['NUMBA_NUM_THREADS'] = num_threads