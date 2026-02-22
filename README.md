# A guidebook to creating TeX-formatted tables
Here is a tutorial on how to create formatted tables using Stata, Python, and LLMs. <br>

I remember the first time I was assigned a data task to replicate a summary statistics table. I struggled and wondered if there was a command that could automate all the formatting, especially as tables in economics journals look astonishingly similar. I assumed there had to be a clean, simple syntax for generating a decent table with just a few small tweaks, but I was quickly disappointed by how few resources I could find online about automating the process. It wasn’t beginner-friendly. <br>

So, here comes this note, and with three purposes: 
  1. to summarize some current existing Stata commands, 
  2. to provide to-go python functions for the readers,
  3. to explore the existing LLMs. <br>

Finally, I will use the tools provided here to replicate the balance table and the regression table in [The Effect of Early-Childhood Education on Social Preferences](https://www.journals.uchicago.edu/doi/10.1086/706858) by Alexander Cappelen, John List, Anya Samek, and Bertil Tungodden. You could find the data under its [supplemental material](https://www.journals.uchicago.edu/doi/suppl/10.1086/706858#).
