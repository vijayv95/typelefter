name: Tech Debt
description: Track long-term or emerging technical debt.
labels: [tech-debt]
body:

- type: textarea
  attributes:
  label: Description
- type: textarea
  attributes:
  label: Reason / Origin
- type: dropdown
  attributes:
  label: Category
  options: [code, architecture, process, docs, dependency]
- type: input
  attributes:
  label: Affected modules / files
- type: textarea
  attributes:
  label: Impact
- type: textarea
  attributes:
  label: Cost Estimate (1–3)
- type: textarea
  attributes:
  label: Acceptance Criteria
