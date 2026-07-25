# Domain Model

## Purpose

This document defines the fundamental concepts of TypeLefter and the relationships between them. The domain model describes **what exists** within TypeLefter. It intentionally excludes implementation details such as storage formats, databases, and user interface.

# Design Principles

TypeLefter is built around three core concepts:

- **Cards** represent information.
- **Containers** organize cards.
- **Scopes** determine what information is visible.

Everything else is derived from these principles.

# Cards

A **Card** is the fundamental unit of information in TypeLefter. Every piece of information is represented as a card, regardless of its purpose.

Examples include:

- Scene
- Chapter
- Character
- Location
- Organization
- Research Note
- Lore Entry
- Timeline Event
- Idea
- Checklist
- To-do
- Reference

Cards are first-class objects.

# Card Structure

Every card has two sides.

## Front

The front contains the information required to identify, organize, and manage the card.

Typical fields include:

- Stable identifier
- Title or short description
- Type
- Status
- Tags
- Scope
- Manuscript location
- Relationships
- User-defined metadata

The front is intended for planning and organization.

## Back

The back contains the card's primary content.

Depending on the card type, this may be:

- prose
- Markdown
- character sheet
- research notes
- worldbuilding
- checklist items

The back is the information the author creates.

# Containers

Containers organize cards into a hierarchy.

```text
Table
└── Stack
    └── Book
```

Containers establish context but do not define the cards themselves. Cards may move between containers without changing their identity.

## Table

A **Table** is the root workspace. It contains one or more Stacks and may define information shared across every project.

## Stack

A **Stack** represents a complete writing project. It contains every card associated with that project, including:

- Books
- Research
- Worldbuilding
- Characters
- Notes
- Draft material

Cards within a Stack may or may not belong to a manuscript.

## Book

A **Book** represents an assembled manuscript. A Book is not defined by its own content. Instead, it is an ordered collection of cards that together form a readable work. Adding a card to a Book places it within the manuscript. Removing a card from a Book removes it from the manuscript without deleting the card.

# Manuscript Position

Cards that belong to a Book possess manuscript metadata describing their position.

Examples include:

- Chapter
- Scene order
- Parent card
- Sequence

This information exists on the card's front. Reordering a manuscript modifies only this organizational information. The card's content remains unchanged.

# Entities

Entities are cards that represent things within the writer's world.

Examples include:

- Character
- Location
- Organization
- Object
- Event

Every entity has a stable identity independent of its display name. Documents reference entities by identity rather than by text.

# Entity Extensions

A scope may extend an existing entity. Extensions contribute additional information without creating a new entity.

Examples include:

- childhood memories
- military rank
- local notes
- relationships
- aliases
- narrator-specific names

The resulting entity is the composition of its inherited definition and every applicable extension.

# Scope

Every container defines a scope. Information defined within a scope is visible to every descendant.

```text
Table
    ↓
Stack
    ↓
Book
```

Knowledge flows downward. Parents cannot automatically access information defined by their descendants.

# References

Cards may reference other cards.

Examples include:

- scenes referencing characters
- research referencing locations
- notes referencing ideas
- chapters referencing scenes

References are based on stable identity rather than filenames or visible text.

# Views

Different views present the same underlying cards.

Examples include:

- manuscript view
- corkboard
- outline
- graph
- timeline
- search results

These views never duplicate information. They simply present different aspects of the same collection of cards.

# Guiding Principle

TypeLefter models a writing project as a collection of interconnected cards. Containers organize those cards. Scopes determine visibility. Books assemble cards into manuscripts. Every feature of the application is built upon these shared abstractions rather than introducing separate representations for drafting, planning, outlining, or worldbuilding.
