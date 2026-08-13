# Student FAQ — BertViz Demo

Common questions and answers for the Transformer attention visualization lab.

**Repo:** [demo1-bertviz](https://github.com/Hrithik-Gavankar/demo1-bertviz)  
**Model used:** `bert-base-uncased` (12 layers, 12 heads per layer)

---

## Model View & Head View

### Q1. What is a **layer** in Head View?

**Short answer:** A layer is one step in BERT’s stack. Layer 0 is closest to the raw tokens; deeper layers build richer meaning.

**Longer answer:**

BERT is not one big block. It is **12 Transformer layers stacked on top of each other**.

For each token, each layer does roughly:

1. **Self-attention** — “Which other tokens should I look at?”
2. **Feed-forward network** — refine the representation

So:

| Layer | Intuition |
|-------|-----------|
| **Layer 0–2** | Local patterns — nearby words, basic syntax |
| **Middle layers** | Phrases, relationships between words |
| **Layer 9–11** | Higher-level meaning — often useful for things like pronouns (“it” → “cat”) |

In **Head View**, when you pick **Layer 5**, you are seeing **only that layer’s** attention — not all 12 at once.

**Analogy:** Think of 12 transparent sheets stacked. Each sheet (layer) lets every token “look at” every other token. Head View shows one sheet in detail.

---

### Q2. I clicked a cell in **Model View** — what am I looking at? How does it connect to Head View?

**Short answer:** Each small square in Model View is **one attention head** at **one layer**. Clicking it shows that same head’s token-to-token connections. Head View is the zoomed-in version of the same data.

**Step by step:**

**Model View layout**

```
         Head 0   Head 1   Head 2  ...  Head 11
Layer 0   [■]      [■]      [■]           [■]
Layer 1   [■]      [■]      [■]           [■]
...
Layer 11  [■]      [■]      [■]           [■]
```

- **Each row** = one Transformer **layer** (0 to 11)
- **Each column** = one attention **head** (0 to 11)
- **Each cell [■]** = a mini heatmap of that head’s attention matrix

**What one cell represents**

For a single head at a single layer, BERT computes an attention matrix:

```
        Keys →   [CLS]  the   cat   sat   on   ...
Query ↓
[CLS]
the
cat
sat
...
```

Each value = “How much does this row token attend to this column token?”  
Darker / stronger color = higher weight (after softmax, weights sum to 1 per row).

**How Model View maps to Head View**

| Model View | Head View |
|------------|-----------|
| One thumbnail in the grid | Same head, shown as **lines** between tokens |
| You pick layer + head implicitly by which cell you focus on | You pick **layer** and **head(s)** from controls |
| Bird’s-eye — compare many heads quickly | Detail — click a token and follow lines |

They show the **same underlying numbers**, just different visuals.

**Important:** Cells in Model View do **not** connect layer to layer.  
Layer 3 Head 2 does not “map into” Layer 4 Head 5 as a direct pipe.  
Each cell is its **own** self-attention pattern at that depth. Deeper layers use the **output** of previous layers, but each thumbnail is only that one head’s attention at that one layer.

---

### Q3. What is an **attention head**? Why are there 12 per layer?

**Short answer:** A head is one independent “perspective” on which tokens to focus on. Multiple heads let the model notice different things in parallel.

**Example with our sentence:**

- One head might focus on **“it” → “cat”** (coreference)
- Another might focus on **“sat” → “on”** (syntax)
- Another might focus on **“[CLS]” → many tokens** (sentence summary)

12 heads × 12 layers = **144 different attention patterns** for one sentence. They are not all doing the same job.

---

### Q4. What do the **lines** in Head View mean?

- **Left column** = tokens acting as **queries** (“I am looking”)
- **Right column** = tokens acting as **keys** (“look at me”)
- **Line from token A to token B** = A attends to B
- **Thicker / darker line** = stronger attention weight

Click **“it”** on the left — lines going to **“cat”** suggest that head is using “cat” to interpret “it”.

**Caution:** Strong attention is a **hint**, not proof the model “understands” coreference the way humans do.

---

### Q5. Why does Model View look different in early vs late layers?

Early layers often show:

- Attention to **neighboring tokens**
- Attention to **punctuation** and **function words** (“the”, “on”)

Later layers often show:

- **Longer-range** links (e.g. “it” to “cat”)
- More **semantic** patterns

This is a common pattern in BERT research — not a strict rule for every head.

---

## Tokens & input

### Q6. What are `[CLS]` and `[SEP]`?

| Token | Meaning |
|-------|---------|
| **`[CLS]`** | Classification token — BERT puts it at the start; often used as a “whole sentence” summary |
| **`[SEP]`** | Separator — marks end of input (or between two sentences in pair tasks) |

They are **special tokens**, not words from your sentence. They still participate in attention like any other token.

---

### Q7. Why is everything lowercase (`the`, `cat`, not `The`, `Cat`)?

We use **`bert-base-uncased`**. The tokenizer lowercases text before encoding.  
If you used a **cased** model, capitalization would be preserved.

---

### Q8. Why does the model use **tokens** and not whole words?

BERT’s vocabulary is a fixed list of subword pieces. Common words = one token; rare words may split (e.g. `playing` → `play` + `##ing`).

Attention runs over the **token sequence**, not raw characters or full documents.

---

## Math & mechanics

### Q9. What is **self-attention** in one sentence?

Each token creates a **query** (“what do I need?”), **key** (“what do I contain?”), and **value** (“what do I pass on?”).  
Attention score = query · key → softmax → weighted sum of values.  
**Self**-attention means all tokens come from the **same sentence**.

---

### Q10. What does `output_attentions=True` do in the code?

Normally the model returns hidden states and predictions.  
With `output_attentions=True`, it **also returns** the attention weight tensors — one matrix per layer per head.  
BertViz needs those weights to draw Model View and Head View.

---

### Q11. What is the shape `(1, 12, 13, 13)` for attention?

For our sentence (~13 tokens):

| Dimension | Meaning |
|-----------|---------|
| `1` | Batch size (one sentence) |
| `12` | Number of heads |
| `13` | Query tokens |
| `13` | Key tokens |

So each head has a **13 × 13** attention matrix.

---

## Using the demo

### Q12. I changed the sentence — do I re-run everything?

Yes. Re-run from the **model load / forward pass** cell onward:

1. Tokenize new sentence  
2. `model(**inputs)`  
3. `model_view(...)` and `head_view(...)`

Attention depends on the **specific tokens** in that sentence.

---

### Q13. “It” doesn’t clearly point to “cat” in my view. Is the demo broken?

Not necessarily.

- Different **heads** behave differently — try another layer or head
- Attention is **soft** — weights spread across many tokens
- BERT **base** is not optimized only for coreference
- Visualization shows **one run**, not guaranteed human-like reasoning

Try: `"The trophy doesn't fit in the suitcase because it is too big."` — discuss whether “it” pulls toward “trophy” or “suitcase” in different heads.

---

### Q14. Model View vs Head View — when should I use which?

| Use Model View when… | Use Head View when… |
|----------------------|---------------------|
| You want the **big picture** | You want to **click tokens** and follow lines |
| You compare **layers and heads** | You study **one layer** in detail |
| You ask “which head looks interesting?” | You ask “what does **it** attend to?” |

---

### Q15. Does attention explain everything the model does?

**No.** Attention shows **where weights were placed** during self-attention. It does not fully explain:

- Final predictions  
- Knowledge stored in feed-forward layers  
- Behavior on tasks BERT wasn’t trained for  

Use BertViz for **intuition**, not as a complete explanation of “how BERT thinks.”

---

## Quick reference card

```
Sentence → Tokenize → BERT (12 layers)
                          ↓
              Each layer: 12 heads
                          ↓
              Each head: N×N attention matrix
                          ↓
         Model View = grid of all heads
         Head View   = lines for selected head(s)
```

**One-liner for class:**  
*“Each layer refines token meaning; each head is a different way of looking at the sentence; each line is how much one token looked at another.”*

---

## Further reading

- [BertViz GitHub](https://github.com/jessevig/bertviz)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [BertViz Colab tutorial](https://colab.research.google.com/drive/1hXIQ77A4TYS4y3UthWF-Ci7V7vVUoxmQ?usp=sharing)
