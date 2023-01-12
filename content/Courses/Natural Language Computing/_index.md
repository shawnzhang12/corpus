---
title: "Natural Language Computing"
weight: -20
---

## Overview

natural language computing - get computers to understand what we say and write, statistics of language

application:

text classification, language translation, speech recognition, natural language understanding, information retrieval, interpretability and LLMs

one of the ultimate human-computer interaction

a little deeper: how are sounds and text related, how are words combined to make sentences, meaning and organization

linguistics knowledge: 

phonology: patterns of speech sounds

morphology: changed by inflection

syntax: ordering and structure between word and phrases,

semantics: study of how meaning is created by words and phrases

pragmatics: the study of meaning in contexts



Ambiguity - Phonological

problem for speech synthesis: read/read

problem for speech recognition: too, two

context: how to wreck a nice beach, how to recognize speech

syntax ambiguity: buffalo buffalo buffaloooooo

syntactic ambiguity: ordering and structure between words, tree parsing

semantic ambiguity: every man loves a woman, i made her duck, give me the pot

miscellaneous ambiguity: news headlines

nlp: resolve ambiguity, reason with world knowledge, tend to use probability, turing test

Chatbots: ELIZA pattern matching



applications:

machine translation: interpretation and generation, word-to-word was popular, syntactic ambiguities, definitions, solution use statistical machine translation

waveforms and spectrograms, speech recognition



Lecture 2: Corpora, Language Models and Smoothing

What are we counting, how do we count thing?

Corpora: A body of language data (not the same as vocabulary), useful when occurs naturally, could be domain specific (medical, law) so watch out for bias

vocab: unique words

size of corpus: total number of words

word order is dependent! need sequence models

P(car|the old) = 0 if it never appears in past, 

solution: condition on a fixed number of words, check the sequences 'the old' and 'old car' probably both > 0

Word prediction: P(w|w_t-1)

N-grams: token sequences of length N, pros: cheap to train, good baseline

language model: probabilities of words in an ordered sequence P(w1, w2, w3, ...)

Term Count (count): term w in corpus C

relative frequency (Fc): relative to the total number of tokens

probabilistic chain rule!  P(A,B,C,D) = P(A)P(B|A)P(C|A,B)P(D|A,B,C)

simple prediction: approximate conditional probabilities ex. P(food| I like chinese) = P(I like chinese food)/P(I like chinese)

problem with chain rule: infinitely long sequences, division by 0, so assume stattistical independence and recent history (markov assumption of previous n grams) bi grams look at one word past

bi gram probabilities P(want|I) = Count (I want)/Count(I)

Evaluation of language models

Shannon's method

shoot darts at board, bigram once hit, another dart board

Shakespeare as a corpus, quadrigrams, increasing context, 

Extrinsic: external measure (task or application), sentiment analysis

Intrinsic: complexity, other stuff









