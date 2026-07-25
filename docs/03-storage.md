# Storage

### Purpose

This document defines how TypeLefter stores projects on disk.

The storage model is designed around four principles:

- user ownership
- transparency
- open formats
- separation of logical structure from physical storage

## Design Principles

### User ownership

Projects belong entirely to the author. Every part of a project should remain readable, editable, and recoverable without TypeLefter.

### Open formats

Primary project data is stored using open, human-readable formats. TypeLefter does not require proprietary file formats.

### Files are the source of truth

Markdown and YAML files define the complete state of the project. The SQLite database is an implementation detail used only for indexing and caching. It may be deleted and rebuilt at any time.

### Logical and physical independence

Logical objects are independent of how they are stored. Moving a card within a manuscript does not require moving its file. Renaming a file does not affect the identity of the card.

## Project Layout

A Table is represented as a directory.

```text
My Table/
├── cards/
├── stacks/
├── books/
└── .typelefter/
```

## Cards

Every card is stored as a Markdown document. Each card contains:

* front (editorial metadata)
* back (content)

Cards possess stable identifiers that are independent of filenames. Users are free to rename or reorganize card files.

## Stacks

Each Stack is stored as a YAML document.

A Stack defines:

- project metadata
- scope hierarchy
- membership

Stacks reference cards by their stable identifiers. Stacks never own card data.

## Books

Each Book is stored as a YAML document. A Book defines an ordered composition of cards. Books reference cards by their stable identifiers. Books never duplicate card content.

## Relationships

Cards reference one another using stable identifiers. Books reference cards. Stacks reference cards. No logical relationship depends on filenames or directory layout.

## SQLite

TypeLefter maintains an internal SQLite database containing derived information such as:

- search indexes
- autocomplete indexes
- entity graphs
- backlinks
- editor state
- caches

No user-authored content is stored exclusively within the database. Deleting the database must never result in permanent data loss.

## Portability

A project should remain usable through ordinary filesystem tools.

Projects should be easy to:

- browse
- edit
- version with Git
- synchronize
- archive
- recover

without requiring TypeLefter.

## Guiding Principle

Files persist information. Cards define information. Stacks define scope. Books define composition. Storage exists solely to preserve these concepts in an open, durable, and human-readable form.

