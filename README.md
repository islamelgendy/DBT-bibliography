# A Systematic Mapping Study of the Metrics, Uses, and Subjects of Diversity-Based Testing Techniques

In this README file, we give a few details about the systematic mapping study on Diversity-Based Testing (DBT) techniques.

## Contents

1. The folder `search-results` contains the raw files taken from each search engine. Each search engine has its own subfolder, where the results are saved in either .csv or .bib files.
2. The folder `processing-steps` contains the search results and the steps taken to screen them to reach the final set of studies.
3. The folder `plots` contains the matplotlib files used to generate the plots in the study.
4. The file `Collection.bib` contains the BibTeX format of all 137 papers in our study.
5. The file `Appendix.pdf` contains more detailed information about the similarity metrics in the study. It includes all similarity metrics, both generic and specialized metrics.

## Search Operationalization 
We collected papers for our study on the 24th of June, 2024 using searches on
IEEE Xplore\footnote[^1], the ACM Digital Library[^2], Scopus[^3], and
SpringerLink[^4].

[^1]: https://ieeexplore.ieee.org/Xplore
[^2]: https://dl.acm.org
[^3]: https://www.scopus.com/
[^4]: https://link.springer.com

The search query we used for IEEE Xplore, Scopus, and ACM was `"software test*" AND ("divers*" OR "similar*" in title or keywords)`, 
where '*' is a wildcard matching any string. 

This means looking for the text <em>"software test*"</em> anywhere in the paper and a
variation of the terms _"divers*"_ (i.e., "diversity", "diversify", or "diversification", etc.) 
or _"similar*"_ (i.e., "similar" and "similarity") in the title or the keywords.

1. The exact search query used in IEEE Xplore was: 
```
("All Metadata":software test*) AND (("Document Title":divers* OR "Document Title":similar*) OR ("Author Keywords":divers* OR "Author Keywords":similar*))
```
2. The exact search query used in ACM was: 
```
AllField:("software testing") AND ( Title:(similar* OR divers*) OR Keyword:(similar* OR divers*) )
```
3. The exact search query used in Scopus was: 
```
ALL( "software test*" ) AND ( KEY ( divers* OR similar* ) OR TITLE ( divers* OR similar* ) ) AND ( LIMIT-TO ( SUBJAREA , "COMP" ) ) AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) ) AND ( LIMIT-TO ( LANGUAGE , "English" ) )
```
4. The exact search query used in SpringerLink was `"software test*" AND ("similar*" OR "divers*")`. However, we used
   the search engine to filter the results based on:
   1. Discipline: `Computer Science`.
   2. Subdiscipline: `Software Engineering`.
   3. Language: `English`.
   4. Content-Type: `Conference Paper` or `Article`.

## Test re-test
According to the guidelines by Kitchenham~\cite{Keele2007}, the first author has applied a test re-test approach, where he made a second extraction of the statistics and information on a random selection of papers to check the consistency of information extraction. The random set contained 17 papers, which are 10% of the papers in the study. We used an online random number generator[^5] for the papers to be reviewed, where the numbers refer to the indices of the papers in our final list. These papers are:
1. Xie2005: A dynamic optimization strategy for evolutionary testing.
2. Cruciani2019: Scalable Approaches for Test Suite Reduction.
3. Noor2015: A similarity-based approach for test case prioritization using historical failure data.
4. Attaoui2023: Black-box safety analysis and retraining of DNNs based on feature extraction and clustering.
5. Ojdanic2023: Syntactic Versus Semantic Similarity of Artificial and Real Faults in Mutation Testing Studies.
6. Hemmati2013: Achieving Scalable Model-Based Testing through Test Case Diversity.
7. Guarnieri2022: An Automated Framework for Cost Reduction of Mutation Testing Based on Program Similarity.
8. Chen2019C: History-Guided Configuration Diversification for Compiler Test-Program Generation.
9. Semerath2020: Diversity of graph models and graph generators in mutation testing.
10. Farzat2010: Test Case Selection Method for Emergency Changes.
11. Gong2012: Diversity Maximization Speedup for Fault Localization.
12. Wu2012: Test case prioritization incorporating ordered sequence of program elements.
13. Panchapakesan2013: Dynamic white-box software testing using a recursive hybrid evolutionary strategy/genetic algorithm.
14. You2013: Evaluation and Analysis of Spectrum-Based Fault Localization with Modified Similarity Coefficients for Software Debugging.
15. Ledru2012: Prioritizing test cases with string distances.
16. Yu2023: Black-Box Test Case Prioritization Using Log Analysis and Test Case Diversity.
17. Cartaxo2009: On the use of a similarity function for test case selection in the context of model-based testing.

[^5]: https://www.random.org/integers/
