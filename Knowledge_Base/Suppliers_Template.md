# Supplier Record Template

## 1. Supplier Identity

Supplier ID:
Company Name:
Platform:
URL:
Country:
Category:
Primary Products:

## 2. Production

MOQ:
Production Capacity:
Production Lead Time:
Customization Available:
Samples Available:

## 3. Pricing & Terms

Unit Price:
Payment Terms:
Volume Discounts:
Additional Costs:

## 4. Shipping

Shipping Method:
Shipping Cost:
Shipping Time:
Shipping Conditions:

## 5. Quality Assessment

Product Quality:
Supply Stability:
Customer Reviews:
Certification:

## 6. Supplier Lifecycle

Status:

## 7. Source / Evidence

Primary Source:
Additional Sources:

## 8. Data Quality

Data Classification:
Verification Status:
Missing Required Data:

## 9. Notes

Notes:

# FIELD SEMANTICS

## Supplier ID

Canonical unique identifier of the Supplier.

Required: YES.

## Company Name

Canonical supplier company name.

Required: YES.

## Platform

Platform or marketplace where the supplier operates.

Required: CONDITIONAL.

## URL

Link to the supplier's storefront or profile.

Required: CONDITIONAL.

## Country

Country of the supplier.

Required: CONDITIONAL.

## Category

Product category the supplier operates in.

Required: YES.

## Primary Products

Main products offered by the supplier.

Required: CONDITIONAL.

## MOQ

Minimum order quantity.

Required: CONDITIONAL.

## Production Capacity

Supplier's production capacity.

Required: OPTIONAL.

## Production Lead Time

Time required to produce an order.

Required: CONDITIONAL.

## Customization Available

Whether product customization is available.

Required: OPTIONAL.

## Samples Available

Whether samples are available.

Required: OPTIONAL.

## Unit Price

Price per unit as offered by the supplier.

Required: CONDITIONAL.

## Payment Terms

Accepted payment terms and conditions.

Required: CONDITIONAL.

## Volume Discounts

Discount structure for larger orders.

Required: OPTIONAL.

## Additional Costs

Any additional costs beyond unit price.

Required: OPTIONAL.

## Shipping Method

Method used for shipping.

Required: CONDITIONAL.

## Shipping Cost

Cost of shipping.

Required: CONDITIONAL.

## Shipping Time

Estimated shipping time.

Required: CONDITIONAL.

## Shipping Conditions

Additional shipping conditions or constraints.

Required: OPTIONAL.

## Product Quality

Known or verified factual information about product quality.

Required: CONDITIONAL.

## Supply Stability

Known or verified factual information about supply stability.

Required: CONDITIONAL.

## Customer Reviews

Factual references to customer reviews, not an AI opinion.

Required: OPTIONAL.

## Certification

Known certifications held by the supplier.

Required: CONDITIONAL.

## Status

Canonical Supplier lifecycle status.

Required: YES.

The exact final enum values and their language are not defined by this proposal. Multiple inconsistent enum variants have been observed in this repository (in this template, and in Suppliers.md Database Rules) and must be resolved by a separate decision.

## Primary Source

Primary evidence/source for externally verifiable Supplier information.

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

Supplier Core Data describes the Supplier itself.

Analysis results, AI evaluations, reliability scores, recommendations, and other derived assessments are not part of the Supplier Core Record unless their structure is explicitly defined by a separate approved architectural decision.