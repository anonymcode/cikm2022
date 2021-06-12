## Hyper-parameters
|           |                  |     AMZ-B |     AMZ-G |     ML-1M |    Steam |
|:----------|:-----------------|----------:|----------:|----------:|---------:|
| GA-SATF   | scaling          |    0.2    |    0.4    |    0      |    0     |
|           | pos_rank         |    2      |   20      |   12      |   10     |
|           | item_rank        |  600      |  800      |  100      |  400     |
|           | user_rank        |  800      |  900      |  300      |  700     |
|           | rescaled         |  False    |  False    |  True     |  False   |
|           | attention_decay  |    1      |    0      |    1.2    |    0     |
|           | iter             |  nan      |    1      |    5      |    0     |
| LA-SATF   | scaling          |    0.2    |    0.2    |    0.2    |    0     |
|           | item_rank        |  600      |  600      |  200      |  900     |
|           | user_rank        |  700      |  500      |  600      |  500     |
|           | rescaled         |  False    |  False    |  True     |  False   |
|           | attention_decay  |    0      |    0      |    1      |    1     |
|           | iter             |    2      |  nan      |    3      |    1     |
|           | attention_rank   |    1      |    1      |   20      |    1     |
|           | sequences_rank   |    2      |    2      |   20      |    2     |
|           | attention_window |    2      |    2      |   40      |    2     |
| PureSVD   | scaling          |    1      |    1      |    1      |    1     |
|           | rank             |  800      | 1500      |  100      |  100     |
| PureSVD-N | scaling          |    0.6    |    0.2    |   -0.2    |    0     |
|           | rank             | 2000      | 1000      | 1500      | 1500     |
|           | rescaled         | False     | False     | False     | False    |
| SASRec    | lr               |    0.0001 |    0.0001 |    0.0001 |    1e-05 |
|           | l2_emb           |    0      |    0      |    0      |    0     |
|           | num_heads        |    1      |    1      |    1      |    1     |
|           | batch_size       |  128      |  512      |  128      |  256     |
|           | num_blocks       |    1      |    2      |    2      |    3     |
|           | dropout_rate     |    0.2    |    0.2    |    0.4    |    0.2   |
|           | hidden_units     |  256      |  768      |  256      |  512     |
|           | epoch            |  100      |  100      |  120      |   80     |
