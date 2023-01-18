---
title: "Natural Language Computing"
weight: -20
---

![](NLP_cover.jpg)

## Introduction and Motivation

How can we get computers to understand what we say and write? Applications include text classification, language translation, speech recognition, natural language understanding, information retrieval,interpretability and Large Language Models.

The <u>ultimate human-computer interaction</u>. (Until brain chips become a thing.)

Some question to think about.

How are **sounds** are **text** related?

How are words **combined** to make sentences?

How are words and phrases used to produce **meaning**?

### Definitions

| Category          | Definition                                                  | Example                                           |
| ----------------- | ----------------------------------------------------------- | ------------------------------------------------- |
| <u>Phonology</u>  | Study of patterns of speech <u>sounds</u>                   | "read" $\rightarrow$ */r iy d/*                   |
| <u>Morphology</u> | How words can be <u>changed</u> by inflection or derivation | "read", "reads","reader", "reading"               |
| <u>Syntax</u>     | <u>Ordering and structure</u> between words and phrases     | *NounPhrase $\rightarrow$ article adjective noun* |
| <u>Semantics</u>  | Study of how <u>meaning</u> is created by words and phrases | "books" $\rightarrow$ :books:                     |
| <u>Pragmatics</u> | Study of meaning <u>in contexts</u>                         | "I'm on fire today"                               |

### Why is NLP difficult?

Behold the chain of problems. We have some understanding of how language works, but how can we get computers to understand as well?

#### Phonological ambiguity :grey_question:

Problem for speech synthesis: "read/read", "object/object"

Problem for speech recognition: "too/two"

How to recognize speech? How to wreck a nice beach? Nanny? Omae Wa Mou Shindeiru.

> #### Syntax Resolution :arrow_heading_down:
>
> The following texts all sound the same, but which one is more likely?
>
> - "Buff a low buff a lobe a fellow Buff a low buff a low buff a lobe a fellow..."
>
> - "Buffalo buff aloe buff aloe buff aloe buff aloe buff aloe..."
>
> - "Buff aloe buff all owe Buffalo buffalo buff a lobe..."
>
> - "Buff aloe buff all own Buffalo buff aloe buff a lobe..."
>
> - **"Buffalo buffalo Buffalo buffalo buffalo Buffalo buffalo Buffalo buffalo"**
>
> We can make sense of sounds with our understanding of syntax and grammar.

#### Syntactic Ambiguity :grey_question:

Ordering and structure between words can be grouped into 'parse tree' structures given grammatical 'rules'.  

E.g. *"I shot an elephant in my pajamas"*

Is the elephant wearing your pajamas?

> #### Semantic Resolution :arrow_heading_down:
>
> We can resolve ambiguities because of our knowledge of **semantics** (meaning), but that won't always be the case.

#### Semantic Ambiguity :grey_question:

How is meaning created by use of words and phrases?

"Every man loves a woman"

1. $\forall x \: man(x) \exists y: (woman(y) \wedge loves (x,y))$
2. $\exists y: woman(y) \wedge \forall x :\ (man(x) \rightarrow loves (x,y))$

"I made her duck"

1. I cooked waterfowl meat for her to eat.
2. I cooked waterfowl that belonged to her.
3. I carved the wooden duck that she owns.
4. I caused her to quickly lower her head.

"Give me the pot"

1. It's time to bake.
2. It's time to get baked.

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

probabilistic chain rule




{{< katex display >}}P(A,B,C,D)=P(A)P(B|A)P(C|A,B)P(D|A,B,C){{< /katex >}}
simple prediction: approximate conditional probabilities ex. P(food| I like chinese) = P(I like chinese food)/P(I like chinese)

problem with chain rule: infinitely long sequences, division by 0, so assume stattistical independence and recent history (markov assumption of previous n grams) bi grams look at one word past

bi gram probabilities P(want|I) = Count (I want)/Count(I)

Evaluation of language models

Shannon's method

shoot darts at board, bigram once hit, another dart board

Shakespeare as a corpus, quadrigrams, increasing context, 

Extrinsic: external measure (task or application), sentiment analysis

Intrinsic: complexity, other stuff









