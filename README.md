# BioInformatics

Training Biolumisence bacteria GC content and genus using Random Forest Algorithm to prove that genus is also a contributing factor to increase of temperature besides GC content. 

The bacteria that we study on are from Bacillaceae family and also biolumisence bacteria. 

We notice that there is no significant correlation between gc content and temperature when it comes biolumisence bacteria (though we only have around 21 biolumisence bacteria to work with.) However, when we run random forest algorithm, we discover that genus plays a role in contributing in increase of temperature. 

We perform random forest with Bacillaceae family, and there is somewhat a significant correlation between GC content and temperature (around 0.41) with p-value of 0.012. When we run a random forest algorithm to determine if genus does play a role, it turns out that it does, and it plays even more significant role compared to that in biolumisence (with signifiance around 0.44 roughly). 

Biolumisence data comes from the blast database whereas Bacillaceae bacteria data comes from Gold. 
Credits to Rachel Calder and David Mateo Ricci for coming up with this research topic and collecting the relevant data.

link to the paper: https://docs.google.com/document/d/1B5BRTxpjODs-vjkRd0jhvgnU5i0aqnOejLhsAvz6orc/edit?usp=sharing

2004: Correlations between genomic GC levels and optimal growth temperatures in prokaryotes. Egyptian Journal of Medical Human Genetics. 2004 Jul [accessed 2018 May 2]. https://www.sciencedirect.com/science/article/pii/S0014579304009342
2006: Genomic GC level, optimal growth temperature, and genome size in prokaryotes.                                                         Egyptian Journal of Medical Human Genetics. 2006 Jun 19 [accessed 2018 May 2]. https://www.sciencedirect.com/science/article/pii/S0006291X06013088#bib15
2006: On the correlation between genomic GC content and optimal growth temperature in prokaryotes: Data quality and confounding features. Egyptian Journal of Medical Human Genetics. 2006 Feb 20 [accessed 2018 May 2]. https://sciencedirect.com/science/article/pii/S0006291X06003214
