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

## Status

Canonical Product lifecycle status.

Required: YES.

## Primary Source

Primary evidence/source for externally verifiable Product information.

Required: CONDITIONAL.

## Additional Sources

Additional evidence references.

Required: OPTIONAL.

## Data Classification

Classification of information, such as FACT/DATA, ASSUMPTION, ESTIMATE or another approved classification.

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

Product Core Data describes the Product itself.

Analysis results, decision records, agent-specific outputs, and analysis history are not part of the Product Core Record unless their structure is explicitly defined by a separate approved architectural decision.

<!-- VERIFICATION MARKER: 2026-08-23 -->