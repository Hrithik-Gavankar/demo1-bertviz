# BertViz — Transformer Attention Visualization

Visualize self-attention in BERT using [BertViz](https://github.com/jessevig/bertviz).

**Demo sentence:** `"The cat sat on the mat because it was tired."`

You will see how tokens connect through attention — including whether **"it"** attends to **"cat"**.

---

## Quick start

```bash
git clone https://github.com/Hrithik-Gavankar/demo1-bertviz
cd demo1-bertviz

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

python verify_setup.py             # optional — checks install
```

Open `bertviz_demo.ipynb` in **Cursor**, **VS Code**, or **Jupyter Lab** and run all cells.

**Kernel:** select **`.venv (Python 3.x)`** — not system Python.

Full setup for every editor and OS → [SETUP.md](SETUP.md)

Questions during the lab → [FAQ.md](FAQ.md)

---

## What you will see

| Step | View | What it shows |
|------|------|----------------|
| 1 | Tokenization | How BERT splits the sentence into tokens |
| 2 | **Model View** | Bird's-eye map of all layers × attention heads |
| 3 | **Head View** | Token-to-token attention lines (click **"it"**) |

---

## Project structure

```text
demo1-bertviz/
├── README.md
├── SETUP.md              # detailed setup (Cursor, VS Code, Jupyter, Colab)
├── requirements.txt
├── setup.sh              # automated setup (macOS / Linux)
├── verify_setup.py       # quick install check
└── bertviz_demo.ipynb    # main notebook
```

---

## Requirements

- Python 3.10+
- ~2 GB free disk space
- Internet on first run (downloads `bert-base-uncased`, ~440 MB)

---

## Troubleshooting

**`No module named 'transformers'`** → wrong kernel. Select `.venv` in the notebook kernel picker.

**Kernel not listed** → run `pip install -r requirements.txt` inside `.venv`, reload your editor.

More fixes → [SETUP.md](SETUP.md#troubleshooting)

---

## Try your own sentence

In the notebook, change:

```python
sentence = "The cat sat on the mat because it was tired."
```

Re-run the cells and explore Model View and Head View.

**Bonus:** `"The trophy doesn't fit in the suitcase because it is too big."` — which noun does **"it"** attend to?

---

## References

- [BertViz GitHub](https://github.com/jessevig/bertviz)
- [BertViz Colab tutorial](https://colab.research.google.com/drive/1hXIQ77A4TYS4y3UthWF-Ci7V7vVUoxmQ?usp=sharing)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
