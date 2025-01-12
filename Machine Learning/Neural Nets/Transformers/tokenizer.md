# Tokenizer
- Encoded tokens are the input to Transformers. Most of the LLM issues are due to tokenization.
- Even single numbers may be split in different tokens, e.g. `677` split into `6` and `77` as two tokens.
- To play around with the output of different tokenizers, see [tiktokenizer](tiktokenizer.vercel.app) 
    - The splits may depend on context and seem arbitrary. 
    - The tokenizer will be trained with a training dataset.
- Since the GPT tokenizer training dataset has more english content than other languages, for a given sentence, the number of tokens used for english will be much lower than if the number of tokens used if the sentence was translated into another language. This is because for other languages, the sentence will be more 'broken up' into separate tokens as compared to english. 
- **Number of Tokens**
    - If number of tokens is high, it will bloat up the sequence length of all documents, and when these (large number of) tokens are inputted to the transformer in the attention block, we will run out of context and communication across tokens will have limited context.
    - Hence, more compressed tokens are better for transformer.
    - However, too much compression will not give the transformer attention layers enough time to 'think'. 
- **Unicode Code Points**
    - Strings are immutable sequences of Unicode code points.
      - *Explanation*: A string is a read-only, ordered collection of characters, where each character corresponds to a unique Unicode code point, and you can’t directly modify its content after creation.
    - Unicode code points are defined by the Unicode consortium as part of *The Unicode Standard*.
    - The Unicode Standard is a definition of ~150,000 characters from various languages, symbols, etc. It defines what these characters look like and what are the integers associated with these characters (Unicode code points).
    - To access Unicode code points for a single character in python, use `ord(char)`
- Raw Unicode characters already have a mapping to integers (Unicode code points), so why not just use these code points and not have any tokenization at all?
    - The vocab in this case would be quite long (~150K), hence the embedding table would be huge.  
    - Also, The Unicode Standard keeps changing - hence not a stable representation.
- **Encodings**
    - The Unicode Standard defines three encodings: UTF-8, UTF-16 and UTF-32. These encodings define the way we take unicode text and translate to binary data or byte streams.
    - UTF-8 is by far the most common. Takes a single code point and translates to a byte stream, where the byte stream is between 1 to 4 bytes (variable based on a schema). UTF-16 and UTF-32 can be wasteful (i.e., sentence not as compressed after encoding).
    - Each byte in the byte stream can only represent a maximum integer of 255. Hence, encoding from code points to byte streams decreases the vocab length.
    - Even with encodings we still have the issue of a large number of tokens for a given string sequence (even larger than what we have with just using unicode code points). We hence use a tokenizer to compress encodings.  
    - For more info read [this blog](https://www.reedbeta.com/blog/programmers-intro-to-unicode/).
- **Tokenizer**
    - Note that the Tokenizer is a completely separate, independent module from the LLM.
    - Tokenizer has its own training dataset of text (which could be different from that of the LLM), on which we train the vocabulary using the Byte Pair Encoding (BPE) algorithm.
    - Tokenizer then translates back and forth between raw text and sequences of tokens.
    - The LLM later only ever sees the tokens and never directly deals with any text. 


## Byte Pair Encoding (BPE) Algorithm
- The UTF-8 vocab size is very small, thus giving us very stretched out byte sequences.
    - If these bytes are considered as tokens directly, these very long token sequences will prohibit attention-learning inside a finite context window for transformers. 
- BPE allows us to compress the utf-8 encoded integer sequence.
    - BPE will increase the vocab size, however the extension in the length of vocab size can be tuned as a hyperparameter. 
- **Iterative Algorithm**:
    - Find the pair of tokens that occur most frequently.
    - Replace the pair with a new token, hence increasing vocab size but decreasing sequence length.
    - Repeat until max iterations are reached, or no more pairs are left. 


## Forced splits using regex patterns (GPT series)
- See GPT-2 paper
- During encoding for inference (not training), some types of characters should never be merged together. e.g merging of 'dog.' or 'dog?'
    - Spaces are exceptions
    - Enforced via a regex pattern
- The text is first forced into splits with regex. Then each split is encoded with the Tokenizer. Then all tokens are simply concatenated.
    - Hence merges are only done within an individual split.
- Training code for GPT-2 tokenizer was never released (github code is inference).
    - Spaces are not merged for some reason.
    - Case-sensitive for apostrophes


## Special tokens
- Introduced to delimit certain parts of the data, or to create a special structure of the token streams.
- `<|endoftext|>` is a special token used to delimit documents in the training set.
    - Inserted between documents start/end to signal the language model that the document has ended and what follows is another separate document.
    - This token did not go through the BPE merges - needs to be handled separately from BPE.
    - GPT-2 only has this single special token, while GPT-4 has four more ([Paper Reference for FIL](https://arxiv.org/pdf/2207.14255)).
    - Transformer architecture has to be modified slightly when inserting special tokens (including in embedding matrix, final layer). 
- Other examples (default example in toktokenizer app): `<|im_start|>`, `<|im_end|>` to delimit the text from system, assistant, user, etc.
    - These tokens can be found in the fine-tuned tokenizers/transformer models (e.g. a chat model).
    - Can create our own special tokens and append them to the tiktoken library. 


## sentencepiece ([Reference](https://github.com/google/sentencepiece))
- Commonly used with language models because, unlike toktoken, it can do both training and inference with BPE tokenizers (among others). Used in both Llama and Mistral series.
- **Big Difference**
    - With Tiktoken: String --> Code Points --> Bytes (UTF-8) --> Merge Bytes (BPE)
    - With SentencePiece: String --> Code Points --> Merge Code Points (BPE) --> Ignore Rare Code Points, and assign OOV tokens to `UNK` token or convert them to Bytes (UTF-8)
- The rarity of the code points is determined by the `character_coverage` hyperparameter.
- If `byte_fallback` is False, then all OOV tokens will be mapped to `UNK` - when fed to the transformer, this is equivalent to telling the attention layers that all these chars in text correspond to the same information. This is not what we want to do.


## vocab_size
- **Why can't the vocab_size be very large?**
    - vocab_size is used in two places in the transformer architecture: number of rows of the embedding table, and the number of neurons in the final linear layer.
    - Hence for a very large vocab_size: we might be under-training rare tokens, and the computational expense will be high.
- **Why can't vocab_size be very small?**
    - Too much information compression might not give the attention layers enough time to proces or 'think', before creating the logits.
- Usually kept around 10k-100k.
- Extending the vocab_size for a pre-trained model
    - Extend tokens in embedding and final layers, and freeze other weights to fine-tune (i.e. only train the new parameters corresponding to the new tokens).


## Misc.
- **Long Prompts Issue Solution**: [Gist tokens Paper Reference](https://arxiv.org/pdf/2304.08467)
    - Compress long prompts into new tokens, and then fine-tuning over these new tokens (no LoRA).
- Application to domain other than text (e.g. images, videos)
    - No need to change the transformer; simply tokenize your data for the input domain.
    - Video tokens example: [Sora](https://openai.com/index/video-generation-models-as-world-simulators/)


## LLM Issues because of Tokenization
- **Why can't LLM spell words?**
    - Some of the tokens can be very long, e.g. `.DefaultCellStyle` is a single token.
    - There is too much crammed in this single token, hence the LLM might perform poor on character-level tasks. E.g. `How many characters "l" are there in the word ".DefaultCellStyle"?`. 
- **Why can't LLM do super simple string processing tasks like reversing a string?**
    - Reason is the same as above - too much crammed into a single token. E.g. `Reverse the string ".DefaultCellStyle"`.
    - If asked to first split the characters of `.DefaultCellStyle` and then reverse, it will provide the correct answer. Since by splitting the characters, LLM is able to split a single token for `.DefaultCellStyle` into multiple tokens that it can now process. 
- **Why is LLM worse at non-english languages?**
    - The LLM sees less non-english data during its training.
    - Also, the Tokenizer is not sufficiently trained on non-english data. Due to this, the tokens are not sufficiently merged for non-english data, and hence it runs into issues with running out of context length because of a large number of tokens (i.e., a large vocab size). 
- **Why is LLM bad at simple arithmetic?**
    - Tokenization of numbers is a bit arbitrary - various lengths of groups of digits can come out to be individual tokens.
    - However, for simple arithmetic like addition, the model has to keep track of each individual digit. 
- **Why did GPT-2 have more than necessary trouble coding in Python?**
    - GPT-2 tokenizer considers each individual space as a separate token, hence bloating up the token/byte stream for python code because of indentation, thereby reducing the information in the context length for attention. 
- **Why did my LLM abruptly halt when it seems the string "<|endoftext|>"?**
    - `<|endoftext|>` is a special token. For some reason it is not being handled as a special token during inference encoding. 
- **What is this weird warning I get about a "trailing whitespace"?**
    - For completion models (e.g., instruct models), if there is a trailing space with the input text, then sampling for the next token can go out of distribution for the model.
    - This is because during training, all tokens/words are prefixed with a space by default. Hence, the model has very rarely seen tokens ending with space.
    - If partial tokens are given to a completion model, this might cause the model to output strange behavior (or break). This is because the model is trying to complete the sequence with an entire token, and not characters. This property is called 'unstable tokens'. 
- **Why did the LLM break if I ask it about "SolidGoldMagikarp"?**
    - [Blog Post](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation)
    - Clustering the embedding tokens based on their embedding representation, there was a cluster that looked really strange since the cluster elements did not seem to have a commonality, nor do the words made any sense (e.g. SolidGoldMagikarp).
    - When the LLM is asked questions including these tokens, we get strange/hallucinatory responses, including insults.
    - *Hypothesis*:
      - SolidGoldMagikarp is a reddit user who posts a lot.
      - The training dataset for Tokenizer was very different from the training dataset for the LLM.
      - The Tokenization data included reddit data including SolidGoldMagikarp.
      - Because SolidGoldMagikarp occurred many times in the dataset, it ended up being merged into an individual token (out of some ~50k tokens) for the Tokenizer vocabulary.
      - Hence for LLM training, an entire row of the embedding table is dedicated to this token which is initialized at random. 
      - This data was not present for LLM training. Hence, this token will never get activated and its weights never updated, resulting in an untrained token.
      - When this token is used in inference, since the embeddings are untrained, this results in undefined behavior. 
- **Why should I prefer to use YAML over JSON with LLMs?**
    - YAML text is sparse in number of tokens, while JSON is dense. 
    - This is because YAML uses spaces/indents and JSON uses brackets, and (groups of) spaces are handled separately by Tokenizer, while combinations of brackets and alphanumerals can create their own tokens. 