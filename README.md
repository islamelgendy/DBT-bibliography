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
