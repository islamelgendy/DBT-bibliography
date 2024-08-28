# A Systematic Mapping Study of the Metrics, Uses, and Subjects of Diversity-Based Testing Techniques

In this README file, we give a few details about the systematic mapping study on Diversity-Based Testing (DBT) techniques.

## Contents

1. The folder `search-results` contains the raw files taken from each search engine. Each search engine has its own subfolder, where the results are saved in either .csv or .bib files.
2. The folder `processing-steps` contains the search results and the steps taken to screen them to reach the final set of studies.
3. The folder `plots` contains the matplotlib files used to generate the plots in the study.
4. The file `Collection.bib` contains the BibTeX format of all 167 papers in our study.
5. The file `Appendix.pdf` contains more detailed information about the similarity metrics in the study. It includes all similarity metrics, both generic and specialized metrics.

## Search Operationalization 
We collected papers for our study on the 24th of June, 2024 using searches on
IEEE Xplore[^1], the ACM Digital Library[^2], Scopus[^3], and
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
1. Abd2019: Similarity distance measure and prioritization algorithm for test case prioritization in software product line testing.
2. Cruciani2019: Scalable Approaches for Test Suite Reduction.
3. Noor2015: A similarity-based approach for test case prioritization using historical failure data.
4. Attaoui2023: Black-box safety analysis and retraining of DNNs based on feature extraction and clustering.
5. Ojdanic2023: Syntactic Versus Semantic Similarity of Artificial and Real Faults in Mutation Testing Studies.
6. Hemmati2013: Achieving Scalable Model-Based Testing through Test Case Diversity.
7. Guarnieri2022: An Automated Framework for Cost Reduction of Mutation Testing Based on Program Similarity.
8. Chen2019C: History-Guided Configuration Diversification for Compiler Test-Program Generation.
9. De2020: Using mutation testing to measure behavioural test diversity.
10. Farzat2010: Test Case Selection Method for Emergency Changes.
11. Gong2012: Diversity Maximization Speedup for Fault Localization.
12. Wu2012: Test case prioritization incorporating ordered sequence of program elements.
13. Asoudeh2013: A Multi-objective Genetic Algorithm for Generating Test Suites from Extended Finite State Machines.
14. You2013: Evaluation and Analysis of Spectrum-Based Fault Localization with Modified Similarity Coefficients for Software Debugging.
15. Ledru2012: Prioritizing test cases with string distances.
16. Yu2023: Black-Box Test Case Prioritization Using Log Analysis and Test Case Diversity.
17. Cartaxo2009: On the use of a similarity function for test case selection in the context of model-based testing.

[^5]: https://www.random.org/integers/

## Highlights
Here are the highlights of our study:
1. The first paper on DBT techniques in our collected results was published in 2005, and the number of publications has had a strong upward trend year on year since then. The venue featuring the most papers to date (14) is the Transactions on Software Engineering (TSE) journal with the International Conference on Software Testing, Verification and Validation (ICST) appearing next, with 11 papers. The paper with the most citations (431) is that of Kim et al. [^6] on proposing a  new adequacy metric for testing a deep learning system that leverages diversity, published in 2019. It is also the highest mean number of citations per year followed by Henard et al. [^7], on diversity for configurations of software product lines for testing, published in 2014; and Hemmati et al. [^8] on test case selection for model-based tests, published in 2013. Finally, the most prolific author in the field is Lionel Briand, having published 15 papers on the topic of DBT.
2. Many similarity metrics were used in the literature, and we found 79 metrics in this study. The most used similarity metrics in the literature are generic metrics, where the most popular similarity metrics were Euclidean distance, Edit distance, and Jaccard distance found in 35, 31 and 30 papers, respectively. Since many of the testing subjects in the literature are either numeric or strings, it was natrual for researchers to use Euclidean distance for numeric data and Edit distance for strings. Also, Jaccard distance is widely used when the testing artefacts can be represented as sets. The mapping study results are not indicative of which metric would be best to use, as different factors can affect this choice such as the nature of the data. There is no clear indication of which metric performs the best, as different authors reported different results based on their empirical studies and the similarity metrics used in their studies.
3. DBT techniques used different software artefacts as a basis for the similarity calculations. These artefacts included input, output, test script, test execution, etc. The most used artefact reported in the literature was test inputs with 20.9% of the papers reported in this study. After that, 18.2% of the collected papers used test scripts as a basis for their approaches. Over one-third of the DBT techniques used either input or test script diversity, because both of them are simple to use as they are usually obtained without the need to instrument, run the tests, or build any models of the software under test, making them very appealing to use by testers.
4. The collected papers in this study handled a range of software testing problems including: test data generation, test case prioritisation, test suite reduction, test case selection, test suite quality evaluation, and fault localisation. Test data generation is the most researched problem in software testing where DBT techniques have been used in 40.5% of the papers. Test case prioritisation comes next after test data generation in terms of the number of papers using DBT techniques with 19.6% of the papers. Followed by test case selection, test suite quality evaluation, test suite reduction, and fault localisation with 13.1%, 8.9%, 7.1%, and 4.8%, respectively. In test data generation, DBT techniques achieved overall higher mutation scores than random testing 8 with an increase of up to 30%, assisted in preventing the search process from stagnating in search-based approaches, showed a significant increase in crash detection of between 28% to 97%, and decreased the average generation time of valid tests in deep learning systems by 15.7% to 47%. Furthermore, DBT techniques increased the overall average percentage of fault detection compared to other test case prioritisation techniques, improved fault-detection rate by up to 45% over the coverage-based selection and 110% over the random selection, and achieved 82.2% test suite reduction maintaining both coverage and mutation score of the original test suites.
5. The subjects reported in the collected papers were stand-alone programs and libraries, web applications, database applications, mobile applications, model-based applications, compilers, and neural network models. Almost two-thirds implemented their approaches on console programs and libraries written in different languages such as Java, C, Python, etc. In the last three years, there has been a significant increase of DBT techniques for testing neural networks and deep learning systems. Model-based systems come next in the popularity of reported studies. Moreover, a few studies reported the use of diversity in web applications, but one might have expected such systems to receive more attention since
they are widely used in both industry and academia. Also, only three papers applied diversity in autonomous vehicles, three in compilers, and three in mobile applications. There is only one paper that used diversity in databases.
6. The trend line shows an increase in DBT tools in software testing with a notable increase in the past 5 years. The highest number of developed DBT tools was in 2022. Most of the reported DBT tools (82.6%) were developed to deal with the
problems of test data generation and test case prioritisation. Only one DBT tool was developed for test suite quality evaluation, one for test case selection, and one for test adaptation. The tool developed for test case selection is only for database applications.


[^6]: Kim J, Feldt R, Yoo S. Guiding deep learning system testing using surprise adequacy. In: International Conference on Software Engineering (ICSE). 2019:1039–1049. 10.1109/ICSE.2019.00108.
[^7]: Henard C, Papadakis M, Perrouin G, Klein J, Heymans P, Le Traon Y. Bypassing the combinatorial explosion: Using similarity to generate and prioritize t-wise test configurations for software product lines. Transactions on Software Engineering. 2014;40(7):650–670. 10.1109/TSE.2014.2327020.
[^8]: Hemmati H, Arcuri A, Briand L. Achieving scalable model-based testing through test case diversity. Transactions on Software Engineering and Methodology (TOSEM). 2013;22(1):1–42. 10.1145/2430536.2430540.
