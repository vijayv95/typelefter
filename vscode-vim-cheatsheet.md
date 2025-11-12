# 🧠 VS Code + Vim/Neovim Cheat Sheet

This cheat sheet summarizes the essential commands and motions when using **Vim or Neovim inside VS Code** (via the Vim or Neovim extension).

---

## 🔄 Modes

| Mode             | How to Enter | Description                                               |
| ---------------- | ------------ | --------------------------------------------------------- |
| **Normal**       | `Esc`        | Navigate, delete, copy, or change text — default Vim mode |
| **Insert**       | `i`          | Type normally                                             |
| **Visual**       | `v`          | Select text character-by-character                        |
| **Visual Line**  | `V`          | Select entire lines                                       |
| **Visual Block** | `Ctrl+v`     | Select rectangular text blocks                            |
| **Command**      | `:`          | Run commands (`:w`, `:q`, etc.)                           |

---

## 🧭 Navigation

| Action                          | Key                       |
| ------------------------------- | ------------------------- |
| Left / Right / Up / Down        | `h` / `l` / `k` / `j`     |
| Start / End of line             | `0` / `$`                 |
| Next / Previous word            | `w` / `b`                 |
| Next / Previous end of word     | `e` / `ge`                |
| Top / Middle / Bottom of screen | `H` / `M` / `L`           |
| Page up / down                  | `Ctrl+u` / `Ctrl+d`       |
| Go to line number               | `:<number>` or `gg` / `G` |
| Match parentheses               | `%`                       |

---

## ✏️ Editing

| Action                       | Key            |
| ---------------------------- | -------------- |
| Insert before / after cursor | `i` / `a`      |
| Open new line below / above  | `o` / `O`      |
| Delete character             | `x`            |
| Delete line                  | `dd`           |
| Delete word                  | `dw`           |
| Undo / Redo                  | `u` / `Ctrl+r` |
| Change word                  | `cw`           |
| Replace character            | `r<char>`      |
| Join lines                   | `J`            |
| Repeat last action           | `.`            |

---

## 📋 Copy & Paste

| Action                      | Key              |
| --------------------------- | ---------------- |
| Yank (copy) word / line     | `yw` / `yy`      |
| Paste after / before cursor | `p` / `P`        |
| Visual select + yank        | `v` → move → `y` |
| Visual select + delete      | `v` → move → `d` |

---

## 🔍 Search & Replace

| Action                | Key             |
| --------------------- | --------------- |
| Search forward        | `/text`         |
| Search backward       | `?text`         |
| Next / Previous match | `n` / `N`       |
| Replace one           | `:s/old/new/`   |
| Replace all in file   | `:%s/old/new/g` |

---

## 💾 File & Buffer Management (VS Code Integrated)

| Action                | Key / Command                  |
| --------------------- | ------------------------------ |
| Save                  | `:w` or `ZZ`                   |
| Quit                  | `:q`                           |
| Save & Quit           | `:wq`                          |
| Force quit            | `:q!`                          |
| Open Command Palette  | `Ctrl+Shift+P`                 |
| Switch Tabs / Buffers | `:bnext`, `:bprev`, `gt`, `gT` |
| Toggle Explorer       | `Ctrl+b` (or VS Code shortcut) |

---

## ⚙️ VS Code Extensions Integration

| Action           | Key                                           |
| ---------------- | --------------------------------------------- |
| Toggle Terminal  | `Ctrl+``                                      |
| Comment Line     | `gc` (if `vim-commentary` or similar enabled) |
| Open Search      | `Ctrl+Shift+F`                                |
| Find File        | `Ctrl+P`                                      |
| Go to Definition | `gd`                                          |
| Rename Symbol    | `<leader>rn` (often mapped)                   |

---

## 🪄 Useful Tips

- Use `:noh` to clear search highlights.
- To select visually then copy to system clipboard:
  - `"+y` — copies selection to clipboard.
- To paste from system clipboard:
  - `"+p`.
- To move between editor panes in VS Code:
  - `Ctrl+w h/j/k/l`.

---

## 🧩 Optional Neovim Mappings (if configured)

| Action         | Mapping             | Description              |
| -------------- | ------------------- | ------------------------ |
| Save file      | `<leader>w`         | Equivalent to `:w`       |
| Quit file      | `<leader>q`         | Equivalent to `:q`       |
| Format code    | `<leader>f`         | Runs VS Code’s formatter |
| Comment toggle | `gcc`               | Comment current line     |
| Comment block  | `gc` in visual mode | Comment selection        |

---

## 🔑 Common VS Code + Vim Integration Settings

Put these in your `settings.json`:

```jsonc
"vim.useSystemClipboard": true,
"vim.hlsearch": true,
"vim.incsearch": true,
"vim.useCtrlKeys": true,
"vim.leader": " ",
"vim.insertModeKeyBindings": [],
"vim.normalModeKeyBindingsNonRecursive": [],
"vim.handleKeys": {
  "<C-c>": false,
  "<C-v>": false
}
```
