grid_config = dict(
    # mlrank
    user_rank = range(100, 1000, 100),
    item_rank = range(100, 1000, 100),
    attention_rank = [5, 10, 15, 20],
    sequences_rank = [5, 10, 15, 20],
    # attention
    attention_window = [20, 40, 60, 80],
    attention_decay = [0.0, 1.0],
    stochastic_attention_axis = [None],
    # normalization
    scaling = [0.0, 0.2, 0.4, 0.6],
    rescaled = [False, True],
)
