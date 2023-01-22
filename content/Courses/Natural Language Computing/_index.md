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
| <u>Phonology</u>  | Study of patterns of speech <u>sounds</u>                   | "read" {{< katex >}}\rightarrow{{< /katex >}} */r iy d/*                   |
| <u>Morphology</u> | How words can be <u>changed</u> by inflection or derivation | "read", "reads","reader", "reading"               |
| <u>Syntax</u>     | <u>Ordering and structure</u> between words and phrases     | *NounPhrase {{< katex >}}\rightarrow{{< /katex >}} article adjective noun* |
| <u>Semantics</u>  | Study of how <u>meaning</u> is created by words and phrases | "books" {{< katex >}}\rightarrow{{< /katex >}} :books:                     |
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

1. {{< katex >}}\forall x \: man(x) \exists y: (woman(y) \wedge loves (x,y)){{< /katex >}}
2. {{< katex >}}\exists y: woman(y) \wedge \forall x :\ (man(x) \rightarrow loves (x,y)){{< /katex >}}

"I made her duck"

1. I cooked waterfowl meat for her to eat.
2. I cooked waterfowl that belonged to her.
3. I carved the wooden duck that she owns.
4. I caused her to quickly lower her head.

"Give me the pot"

1. It's time to bake.
2. It's time to get baked.

> #### Pragmatics Resolution :arrow_heading_down:
>
> :question: No one woman is so popular right? Yeah there isn't.
>
> :a: Every man loves a woman.
>
> :question:What type of food did you make for her?
>
> :a: I cooked waterfowl meat for her to eat.
>
> :question:Are we in Canada? Yes.
>
> :a: It's time to get baked.

## General NLP

Involves **resolving ambiguity** at all levels, reasoning with world knowledge (used to be explicitly encoded in symbolic systems by experts), and tend to use **probabilities**.

### Machine Translation

Interpretation and generation.

#### Word-to-word translation?

There is disparity of meanings between languages. What defines a nation?Semantic and syntactic ambiguities: 

"The spirit is willing, but the flesh is weak"

{{< katex >}}\rightarrow{{< /katex >}} Russian {{< katex >}}\rightarrow{{< /katex >}} English {{< katex >}}\rightarrow{{< /katex >}} 

"The vodka is good, but the meat is rotten"

#### Solution: Statistical Machine Translation

Learn statistics on parallel texts. Speech Translation, Spectrograms  for another lecture.







