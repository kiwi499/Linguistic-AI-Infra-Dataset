# Linguistic-AI-Infra-Dataset
Establish a standard dataset

### About ConLL-U (.conllu)
#### You can check this link for more details:[CoNLL-U Format](https://universaldependencies.org/format.html)
#### Labels
Sentences consist of one or more word lines, and word lines contain the following fields:

*ID*: Word index, integer starting at 1 for each new sentence; may be a range for multiword tokens; may be a decimal number for empty nodes (decimal numbers can be lower than 1 but must be greater than 0).

*FORM*: Word form or punctuation symbol.

*LEMMA*: Lemma or stem of word form.

*UPOS*: Universal part-of-speech tag.

*XPOS*: Optional language-specific (or treebank-specific) part-of-speech / morphological tag; **underscore** "__" if not available.

*FEATS*: List of morphological features from the universal feature inventory or from a defined language-specific extension; **underscore** "__" if not available.

*HEAD*: Head of the current word, which is either a value of ID or zero (0).

*DEPREL*: Universal dependency relation to the HEAD (root iff HEAD = 0) or a defined language-specific subtype of one.

*DEPS*: Enhanced dependency graph in the form of a list of head-deprel pairs.

*MISC*: Any other annotation.

The fields DEPS and MISC replace the obsolete fields PHEAD and PDEPREL of the CoNLL-X format. In addition, we have modified the usage of the ID, FORM, LEMMA, XPOS, FEATS and HEAD fields as explained below.


**The fields must additionally meet the following constraints:**

Fields must not be empty.

Fields other than FORM, LEMMA, and MISC must not contain space characters.

**Underscore** ( _ ) is used to denote unspecified values in all fields except ID. Note that no format-level distinction is made for the rare cases where the FORM or LEMMA is the literal underscore – processing in such cases is application-dependent. Further, in UD treebanks the UPOS, HEAD, and DEPREL columns are not allowed to be left unspecified except in multiword tokens, where all must be unspecified, and empty nodes, where UPOS is optional and HEAD and DEPREL must be unspecified. The enhanced DEPS annotation is optional in UD treebanks, but if it is provided, it must be provided for all sentences in the treebank.

#### Remember
Different languages chose different tags to show its special semantic relations.
