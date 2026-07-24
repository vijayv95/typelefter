# Domain Model

## Purpose

This document defines the fundamental concepts of TypeLefter and the relationships between them.

The domain model describes **what exists** within TypeLefter. It intentionally avoids implementation details such as storage formats, databases, user interface, or programming language.

# Design Principles

TypeLefter is built around two complementary models:

- **Containment** — where things belong.
- **Knowledge** — what things are known within a given context.

The containment hierarchy provides structure. Entities provide meaning.

# Containment Hierarchy

Every item in TypeLefter belongs to a hierarchy.

```
Table
└── Stack
    ├── Research
    ├── Notes
    ├── Worldbuilding
    ├── Characters
    └── Book
        ├── Chapters
        └── Front Matter
```

Each level narrows the context established by its parent.

## Table

A **Table** is the root workspace. It represents the author's complete writing environment and contains one or more Stacks. A Table may also define entities and resources that are shared across every Stack.

## Stack

A **Stack** represents a complete writing project. A Stack contains everything required to develop a story, article, thesis, or other long-form work.

Examples include:

- research
- planning
- outlines
- worldbuilding
- notes
- entity definitions
- one or more Books

The Stack is the primary unit of creative work.

## Book

A **Book** represents the finished manuscript. It contains the material intended for reading or publication.

Typical contents include:

- front matter
- chapters
- appendices

A Book exists within a Stack and automatically shares the Stack's knowledge.

# Entities

An **Entity** represents something that exists within the writer's world.

Examples include:

- Character
- Location
- Organization
- Item
- Event
- Timeline
- Language

Unlike documents, entities are identified by their identity rather than their display name. An entity may be referenced from anywhere within its visible scope.

# Scope

Every container may define entities. Entities become visible to every descendant of the container in which they are defined.

```
Table
└── Stack
    └── Book
        └── Chapter
```

A Chapter may reference:

- Chapter entities
- Book entities
- Stack entities
- Table entities

A parent cannot automatically reference entities defined within its descendants.

Knowledge always flows downward through the hierarchy.

# Entity Extensions

An entity may be extended within a narrower scope. Extensions add context without creating a new entity.

For example, a Table may define a character:

```
Character
Name: Alice Morgan
```

A Stack describing Alice's childhood may extend that same entity:

```
Character Extension
Target: Alice Morgan

Favourite Toy: Teddy Bear
Best Friend: Emma
```

The entity remains the same. The Stack simply contributes additional knowledge that is visible within its scope.

# Presentation

Entity extensions may also define how an entity is presented within a scope.

For example:

```
Entity: Alice Morgan

Aliases:
- Alice
- Allie
- Aligator
```

Different books, chapters, or narrators may refer to the same entity using different names while preserving a single underlying identity.

# References

Documents reference entities rather than plain text. A visible name within the manuscript is therefore both human-readable and machine-understandable.

This enables features such as:

- hyperlinks
- autocomplete
- rename refactoring
- navigation
- relationship graphs
- appearance tracking

without requiring writers to manually maintain links.

# Guiding Principle

The hierarchy defines **where** information belongs. Entities define **what** exists. Scopes determine **what is visible**.

TypeLefter combines these concepts to provide a writing environment where knowledge is structured, reusable, and context-aware.
