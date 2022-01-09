# Election Analysis

## Overview of Election Audit
A Colorado Board of Elections employee tasked me with completing an election audit of a recent congressional election. The audit required a count of the total number of votes cast, a breakdown of votes by county, a breakdown of votes by candidate, and an overview of the winning candidate's votes.

## Results

![analysis outcomes](https://user-images.githubusercontent.com/94264643/148670814-466c82a2-ee8c-4473-855c-69cbb53614be.png)

- Within the data sample provided, a total of **369,711 votes** were analyzed for this election.
- The **vote count breakdown by county** is as follows:
  - Jefferson County: 10.5% of vote (38,855 votes)
  - Denver County: 82.8% of vote (306,055 votes)
  - Arapahoe County: 6.7% of vote (24,801 votes)
- Of the counties audited, **Denver County** had the highest percentage of voter turnout.
- The **vote count breakdown by candidate** is as follows:
  - Charles Casper Stockham: 23.0% of vote (85,213 votes)
  - Diana DeGette: 73.8% of vote (272,892 votes)
  - Raymon Anthony Doane: 3.1% of vote (11,606 votes)
- The winner of the election, **Diana DeGette**, received 73.8% of the vote with a total of 272,892 votes.

## Election Audit Summary
The code used to audit this election may be re-used for future elections, including elections held outside of this congressional district, as it is not district-specific. The code may be modified to accomodate less - or additional - data (for example, additional data may be available to analyze voter demographics against voter turnout, in which case additional code would need to be incorporated). Of course, if the auditor wants to exclude a summary of voter turnout by county, the corresponding code may be removed.
