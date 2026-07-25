# Domain Model

### Purpose

This document defines the conceptual model of TypeLefter. It describes the logical objects that make up a project and the relationships between them. It does not describe how those objects are stored or presented.

## Design Principles

TypeLefter is built around four concepts:

- Cards
- References
- Scopes
- Compositions

Every feature in the application is expressed using these abstractions.

## Cards

A **Card** is the fundamental unit of information. Everything a writer creates is represented as a card.

Examples include:

- Scene
- Chapter
- Character
- Location
- Organization
- Timeline Event
- Research Note
- Lore Entry
- Idea
- Checklist

Cards possess a stable identity that never changes. Cards may be renamed, reorganized, or moved between projects without changing their identity.

## Card Structure

Every card has two sides.

### Front

The front contains editorial information.

Examples include:

- Identifier
- Type
- Description
- Status
- Tags
- Relationships
- User-defined metadata

The front exists to help authors organize and understand their work.

### Back

The back contains the card's primary content.

Examples include:

- prose
- Markdown
- character sheets
- research
- worldbuilding
- notes

The back is the information the author creates.

## References

Cards reference other cards using their stable identities.

Examples include:

- scenes referencing characters
- research notes referencing locations
- characters referencing organizations
- lore referencing events

References are independent of filenames or display names.

## Scope

A **Scope** determines which cards are visible within a particular context. Scopes are defined by Stacks. Cards inherit visibility from ancestor scopes. Knowledge flows downward through the scope hierarchy.

## Stack

A **Stack** represents a writing project.

A Stack defines:

- project scope
- project configuration
- project membership

A Stack references the cards that belong to the project. A Stack does not own those cards.

## Book

A **Book** represents a manuscript. A Book is an ordered composition of cards belonging to a Stack.

The Book defines:

- reading order
- manuscript structure

A Book does not contain card content. It simply references cards in a particular sequence. Removing a card from a Book removes it from the manuscript but does not delete the card.

## Entity Cards

Some cards represent entities within the writer's world.

Examples include:

- Character
- Location
- Organization
- Item
- Event

Entity cards have stable identities independent of how they are referred to within the manuscript.

## Entity Extensions

An entity may be extended within a narrower scope. Extensions contribute additional information without creating a new entity.

Examples include:

- aliases
- childhood memories
- local relationships
- narrator-specific names
- project-specific notes

The resolved entity is the composition of its inherited definition and every applicable extension.

## Views

Views present cards in different ways.

Examples include:

- editor
- corkboard
- outline
- graph
- timeline
- search

Views never duplicate information. They simply present different aspects of the same underlying cards.

## Guiding Principle

TypeLefter models writing as a collection of interconnected cards. Scopes determine visibility. Books assemble cards into manuscripts. Everything else is a view of the same underlying model.

