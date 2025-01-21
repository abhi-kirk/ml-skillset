# Distributed Training

## Parameter Servers
- *Problem*:
  - For distributed training, need to aggregate gradients across workers. 
- *Solution*:
  - A centralized dedicated server which recieves gradients from all workers, and updates the model parameters. It holds a single copy of the entire model. 
  - Can have multiple parameter servers. 
- *Advantages*:
  - Each worker does not need to hold its own copy of the model. 
  - No synchronization needed across workers. 
  - Applicable for data/model/hybrid parallelism. 
- *Limitations*:
  - Nontrivial communication costs. 
  - Blocking problem when recieving gradients from workers simultaneously. 

## Collective Communication
- *Problem*:
  - Want a more decentralized solution to reduce communication overhead and resolve the blocking problem. 
- *Solution*:
  - All workers hold a copy of the model each. 
  - `reduce`: All workers compute their own gradients. 
  - Workers synchronize gradients by communicating with each other. 
  - `allreduce`: Broadcast gradients to ensure synchronization. 
- *Advantages*:
  - Centralized solution no longer required; hence can scale horizontally by adding more workers. 
- *Limitations*:
  - Communication overhead between all workers. 
    - Solution is the *ring-allreduce* algorithm, where data is transferred in a ring-like fashion without the reduce operation. 
  - Risk of failures. 
    - Solution is model checkpointing. 

## Data Parallelism
- *Problem*:
  - Distributed training strategy for large amount of data but relatively smaller model. 
- *Solution*:
  - `gradient aggregation`: 
    - All workers are given a non-overlapping data shard. 
    - All workers hold a complete copy of the model. 
    - Each worker creates mini-batches from this shard, and for each mini-batch computes the gradient. Using gradient aggregation (sum), the total gradient for the shard is computed over several iterations. 
    - Each worker communicates its shard gradient to all other workers in a synchronization step. Another gradient aggregation (average) step accumulates a common set of gradients across all workers. 
      - If sum is used to aggregate gradients then we have to scale the learning rate accordingly. 
    - The full set of gradients is broadcasted to all workers to ensure synchronization. 
    - Each worker (after possibly scaling the learning rate with the number of workers) updates the model parameters for its own model. 
    - Checkpoint model from worker 0 only. 

## Model Parallelism
- *Problem*:
  - Distributed training strategy for a very large model but relatively smaller dataset. 
- *Solution*:
  - `model partitioning`:
    - The model is divided into smaller sub-models and distributed to workers; e.g. each worker has a sequential set of model layers. 
    - All workers hold the entire dataset in their respective memory/cache. 
    - Each worker computes the forward pass for its portion of the model, and communicates the activations to the next worker. 
    - The backward pass (gradient computation) proceeds in reverse. 
    - If the model is partitioned non-sequentually, then all workers communicate for a synchronization step (collective communication). 
    - Checkpoint from each worker. 

## Hybrid Parallelism
- *Problem*:
  - Distributed training strategy for a very large model as well as very large dataset. 
- *Solution*:
  - Use both data and model parallelism. 
    - E.g. Have a total of 8 GPUs split across 2 groups of 4 GPUs each. 
  - Model parallelism within a group of workers: 
    - Partition the model layers within a group. 
    - E.g. Split the model layers across the 4 GPUs inside each group. 
  - Data parallelism across the groups:
    - Each group processes a different data shard. 
    - E.g. Gradient accumulation across the 2 groups. 
- *Advantages*:
  - Fully distributed training at scale required for SOTA results. 
- *Limitations*:
  - Complexity. 
  - Communication overhead. 
- *Examples*:
  - SOTA Transformer pretraining: GPT, Llama. 
  - Tesla Dojo supercomputer. 


## Frameworks
- *Horovod*
  - Tensorflow/Keras (also supports Pytorch)
  - Usecase: Distributed CNN training (data parallelism) on Corning's on-prem GPU cluster. 
- *DDP*
  - Pytorch
  - Usecase: Distributed LLM pretraining (data parallelism) on JPMC AWS cloud. 