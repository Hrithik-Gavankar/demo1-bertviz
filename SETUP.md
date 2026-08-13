# Setup Guide

Run the BertViz attention demo locally using **any** of these editors:

- **Cursor**
- **VS Code**
- **Jupyter Lab**
- **Jupyter Notebook**
- **Google Colab** (no local setup)

**Requirements:** Python 3.10+, internet on first run, ~2 GB free disk space.

---

## Clone the repo

```bash
git clone https://github.com/Hrithik-Gavankar/demo1-bertviza
cd demo1-bertviza
```

---

## Part 1 — Common setup (all local editors)

### Step 1 — Create a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

You should see `(.venv)` at the start of your prompt.

```bash
python --version   # expect 3.10+
```

### Step 2 — Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Installs: `bertviz`, `transformers`, `torch`, `jupyter`, `ipykernel`, `ipywidgets`.

Takes **2–5 minutes** on first install.

### Step 3 — Verify setup (optional)

```bash
python verify_setup.py
```

Expected:

```text
Tokens: ['[CLS]', 'the', 'cat', 'sat', ...]
Layers: 12
Setup OK — open bertviz_demo.ipynb and run all cells.
```

### Step 4 — Register kernel (Jupyter Lab / Notebook only)

```bash
python -m ipykernel install --user --name=demo1-bertviz --display-name="Python (demo1-bertviz)"
```

Skip this if you only use **Cursor** or **VS Code** — they use `.venv` directly.

**macOS / Linux shortcut:** `./setup.sh` runs Steps 1–4 automatically.

---

## Part 2 — Pick your editor

### A) Cursor

1. **File → Open Folder** → select the cloned `demo1-bertviza` folder
2. Open `bertviz_demo.ipynb`
3. Kernel picker (top-right) → **`.venv (Python 3.x)`**
4. Run all cells

> Cursor does **not** show `Python (demo1-bertviz)` by name. Pick **`.venv`** instead.

---

### B) VS Code

1. Install **Python** and **Jupyter** extensions if prompted
2. **File → Open Folder** → `demo1-bertviza`
3. Open `bertviz_demo.ipynb`
4. Kernel picker → **`.venv (Python 3.x)`**
5. Run all cells

---

### C) Jupyter Lab

```bash
source .venv/bin/activate
jupyter lab
```

1. Open `bertviz_demo.ipynb`
2. **Kernel → Change Kernel → Python (demo1-bertviz)**
3. Run all cells

---

### D) Jupyter Notebook

```bash
source .venv/bin/activate
jupyter notebook
```

1. Open `bertviz_demo.ipynb`
2. **Kernel → Change kernel → Python (demo1-bertviz)**
3. Run all cells

---

### E) Google Colab

1. [BertViz Colab tutorial](https://colab.research.google.com/drive/1hXIQ77A4TYS4y3UthWF-Ci7V7vVUoxmQ?usp=sharing), or
2. New notebook + first cell:

```python
!pip install bertviz

from transformers import AutoTokenizer, AutoModel, utils
from bertviz import model_view, head_view

utils.logging.set_verbosity_error()
model_name = "bert-base-uncased"
sentence = "The cat sat on the mat because it was tired."

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, output_attentions=True)
inputs = tokenizer(sentence, return_tensors="pt")
outputs = model(**inputs)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

model_view(outputs.attentions, tokens)
head_view(outputs.attentions, tokens)
```

---

## Part 3 — OS quick reference

### macOS

```bash
git clone https://github.com/Hrithik-Gavankar/demo1-bertviza
cd demo1-bertviza
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=demo1-bertviz --display-name="Python (demo1-bertviz)"
```

### Linux (Ubuntu / Debian)

```bash
sudo apt update && sudo apt install python3 python3-venv python3-pip git -y
git clone https://github.com/Hrithik-Gavankar/demo1-bertviza
cd demo1-bertviza
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name=demo1-bertviz --display-name="Python (demo1-bertviz)"
```

### Windows (PowerShell)

```powershell
git clone https://github.com/Hrithik-Gavankar/demo1-bertviza
cd demo1-bertviza
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m ipykernel install --user --name=demo1-bertviz --display-name="Python (demo1-bertviz)"
```

If activation is blocked:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Troubleshooting

### `No module named 'transformers'` or `No module named 'bertviz'`

Wrong kernel. Select **`.venv (Python 3.x)`**, not system Python.

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Restart the notebook kernel and run again.

---

### `Running cells with 'Python 3.13.x' requires the ipykernel package`

Same fix — switch kernel to **`.venv`**.

```bash
source .venv/bin/activate
pip install ipykernel
```

Do **not** install packages on system Python (`~/.local/bin/python3.13`).

---

### Custom kernel name not visible in Cursor / VS Code

Expected. Use **`.venv (Python 3.x)`** instead of `Python (demo1-bertviz)`.

| Editor | Kernel to select |
|--------|------------------|
| Cursor | `.venv (Python 3.x)` |
| VS Code | `.venv (Python 3.x)` |
| Jupyter Lab | `Python (demo1-bertviz)` |
| Jupyter Notebook | `Python (demo1-bertviz)` |
| Colab | Built-in Python |

---

### Visualization blank

```bash
source .venv/bin/activate
pip install ipywidgets
```

Restart kernel → run all cells from the top.

---

### Model download slow

First run downloads `bert-base-uncased` (~440 MB). Needs internet once; Hugging Face caches it after that.

---

## What to explore in the notebook

1. **Tokenization** — notice `[CLS]`, `[SEP]`, and subword tokens
2. **Model View** — compare patterns across layers and heads
3. **Head View** — click **"it"** and see which tokens it attends to
4. Change the sentence and re-run — try your own examples
