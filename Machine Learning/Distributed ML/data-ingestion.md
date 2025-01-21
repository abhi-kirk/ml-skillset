# Data Ingestion Patterns for Distributed ML

## Batching
- *Problem*: 
  - Performing expensive computations (model training) with large amounts of data (OOM). 
- *Solution*:
  - Split data into mini-batches. 
  - Train only with mini-batch to update model sequentially. 
  - Use non-overlapping batches, but shuffle data after every epoch. 
  - Use multiple i/o workers to load data concurrently. 
- *Advantages*:
  - Single compute node required. 
- *Limitations*:
  - Model should be able to update with partial data. 
  - Larger batch size correlates with better updates. Hence, batch size is dependent on available resources. 
  - Training is sequential, not parallel. 
- *Examples*:
  - Almost every deep neural net training (CNN, GNN, LLM). 


## Sharding
- *Problem*:
  - Batching solution is sequential, and hence very slow. 
- *Solution*:
  - Use multiple worker machines to process each data shard parallely. 
    - A *shard* is a horizontal non-overlapping partition of the data (i.e., all features included). 
    - Batching is done within a shard since each shard is shuffled after every epoch. 
  - Each worker machine has its own copy of the entire model. 
  - *Collective communication pattern* is used to update the parameters. 
- *Advantages*:
  - Horizontally scalable. 
- *Limitations*:
  - Model should be small enough to fit into a worker's memory. 
  - If dataset is growing continuously, we need to rebalance periodically. 
    - *Hash sharding* (auto-sharding) can be used. 
- *Examples*:
  - CNN distributed training with *Horovod*. 
  - LLM distributed training with *Pytorch-DDP*. 


## Caching
- *Problem*:
  - Training with multiple epochs, repeated i/o operations (reading from disk) to retrieve shards incurs significant overhead. 
- *Solution*:
  - Each worker, after the first pass/epoch, caches its shard for subsequent epochs. 
  - Note that entire shards are cached and not min-batches (since the shard will be shuffled after each epoch). 
- *Advantages*:
  - Reduces shard fetch time for epochs after the first. 
  - Speedup depends on the storage type used for caching: disk or RAM. 
    - Disk is more fault-tolerant and cheap, but slow. 
    - RAM is temporary and expensive, but fast. 
- *Limitations*:
  - Workers should have enough (fast) memory to hold the shards. 
  - Not done automatically for Horovod or Pytorch-DDP. 
- *Examples*:
  - Pytorch's `DataLoader`; use `persistent_workers=True` to keep workers alive across epochs. 