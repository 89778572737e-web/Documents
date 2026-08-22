# Product Record Template

## 1. Product Identity

Product ID:
Name:
Category:
Subcategory:

## 2. Product Core Data

Description:

Primary Customer Problem:

Product Solution:

Key Features:

Advantages:

Disadvantages:

Unique Features:

Improvement Opportunities:

## 3. Supplier Relationship

Supplier ID:

## 4. Product Lifecycle

Status:

## 5. Source / Evidence

Primary Source:
Additional Sources:

## 6. Data Quality

Data Classification:
Verification Status:
Missing Required Data:

## 7. Notes

Notes:

# FIELD SEMANTICS

## Product ID
Canonical unique identifier of the Product.

Required: YES.

## Name
Canonical product name.

Required: YES.

## Category
Canonical Product category.

Required: YES.

## Subcategory
More specific classification where applicable.

Required: CONDITIONAL.

## Description
Canonical description of the Product itself, not an AI analysis.

Required: YES.

## Primary Customer Problem
The customer problem the Product is intended to address.

Required: YES.

## Product Solution
How the Product addresses that problem.

Required: YES.

## Key Features
Core factual characteristics of the Product.

Required: YES.

## Advantages
Known or verified advantages of the Product.

Required: CONDITIONAL.

## Disadvantages
Known limitations or disadvantages of the Product.

Required: CONDITIONAL.

## Unique Features
Features that materially differentiate the Product.

Required: CONDITIONAL.

## Improvement Opportunities
Potential improvements to the Product.

Required: OPTIONAL.

## Supplier ID
Structured reference to the canonical Supplier.

Required: CONDITIONAL.

The exact final relationship syntax is not defined here.

## Status
Canonical Product lifecycle status.

Required: YES.

The exact final enum values and their language are not changed by this proposal.

## Primary Source
Primary evidence/source for externally verifiable Product information.

Required: CONDITIONAL.

## Additional Sources
Additional evidence references.

Required: OPTIONAL.

## Data Classification
Classification of information, such as FACT/DATA, ASSUMPTION, ESTIMATE or another subsequently approved classification.

Required: YES.

## Verification Status
Indicates whether relevant factual information has been verified.

Required: YES.

## Missing Required Data
Explicit indication of required information that is currently unavailable.

Required: YES.

## Notes
Free-form notes only.

Required: OPTIONAL.

Structured relationships and structured data must not be placed in Notes.

# ARCHITECTURAL BOUNDARY

This template contains Product Core Data and only the minimum structural fields already supported by approved Decisions A–M.

It does NOT define or embed:

- Analysis History;
- Analysis entity;
- Decision entity;
- Analysis/Decision references;
- Analysis Status;
- Product Hunter results;
- Financial Evaluation results;
- Marketing analysis;
- Sales analysis;
- Business Manager decisions.

Those remain outside the Product Core Record until separately approved architectural decisions define their structure.

# FINANCIAL EVALUATION

Financial Evaluation Agent is already approved as a full Agent component under Decision P2.0.

Its final structural placement and relationship to Knowledge Base storage are NOT encoded in this template.

# WHAT THIS VERSION IMPLEMENTS CONCEPTUALLY

This proposed template is limited to the approved architectural decisions that directly affect the Product Record schema:

A — Product Entity
B — Product ID
H — Product Status
J — Required Fields
K — Source / Evidence
L — Template-to-Record Consistency
M — Product Core Data vs Analysis/Decision Data Boundary

Decision G is intentionally NOT listed here because its implementation mechanism has not yet been selected.

# FILE EXIT CRITERIA

Before this file can be approved for GitHub:

1. Product ID is explicitly represented.
2. Product Core Data is separated from Analysis/Decision Data.
3. Supplier relationship has a dedicated field.
4. Product lifecycle Status has a dedicated field.
5. Required/Conditional/Optional classification is explicit.
6. Source/Evidence representation is present.
7. Data Classification is present.
8. Verification Status is present.
9. Missing Required Data is explicitly represented.
10. No unapproved Analysis/Decision entity, reference system, or Analysis Status is embedded.
11. The template does not make unresolved Financial Evaluation architecture assumptions.
12. The template does not make an unresolved Test/Production separation mechanism assumption.

STATUS:
PROPOSED — NOT APPROVED

GITHUB:
UNCHANGED
