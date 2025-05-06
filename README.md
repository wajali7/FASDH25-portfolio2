# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
## Portfolio 2
The aim of portfolio 2 was to extract, count, and visualize mentions of Gaza’s place names from a large corpus of international news articles. We were asked to use either of the two text mining techniques for this process:
    Regex pattern matching
    Named Entity Recognition (NER)
In our group, I was assigned to use a gazetteer and regex to extract places in Gaza from the corpus. To accomplish this, I started by cloning the repository using Git Bash, which created local folders on my system. The structure of the folders was as follows: the Articles folder contained the full corpus of news articles, the gazetteers folder included a countries file and a geonames-gaza-selection file containing all place names from Gaza along with their alternative names, and a README file. The scripts folder contained the final script and its outputs, including the frequencies.tsv file, the regex_counts.tsv file, and the final regex script.

## Repository Structure 
FASHD25-portfolio2/

├── articles/
│   └──                      # Contains the collection of articles used or referenced in the project
├── gazetteers/
│   ├── geonames_gaza_selection.tsv   # GeoNames dataset with place names and alternate names
│   ├── countries/                    # Country-level gazetteers and reference data
│   └── readme/                       # Documentation explaining the usage of gazetteer files
├── Scripts/
│   ├── regex_script_final.py         # Python script for regex-based text analysis
│   ├── Mapping_NER/                  # Scripts for mapping NER results
│   ├── mapping_regex/                # Scripts for visualizing regex mapping results
│   ├── Gaza_NER2_ihtisham_wajahat_suleiman_suhrab.ipynb # NER processing scripts from contributors
│   └── build_gazetteer/              # Scripts for building gazetteers for geographic analysis
├── AI Documentations/
│   ├── AI_documentation_ihtisham.docx    # AI documentation by Ihtisham
│   ├── AI_documentation_wajahat_ali.docx  # AI documentation by wajahat ali
├── Outputs/
│   ├── regex_counts.tsv               # Output of place name counts from regex extraction
│   └── NER_gazetteers.tsv             # Output of place name counts from NER processing
├── Maps/
│   ├── regex_map.html                 # Interactive map of regex results
│   ├── regex_map.png                  # Static image map of regex results
│   ├── NER_map.html                   # Interactive map of NER results
│   └── NER_map.png                    # Static image map of NER results
├── .gitignore                         # File to exclude unnecessary files from version control
└── README.md                          # Project documentation (this file)
## Fork Cloning
we forked the main repository and cloned it our local systems

## Task 2A. Extracting, Counting, and Visualizing Mentions of Gaza Place Names
In our group, I was assigned to use a gazetteer and regex to extract Gaza place names from the corpus.
The second step of part 2A was to improve the recall of place names in the articles. Here we were given two options to carry out this task. 
### Creating Regex
The first option was to create a regular expression in the script that matches either the asciiname or any of its alternative names. The second option was to build a regex pattern for each asciiname by replacing characters that might be spelled differently with alternative characters. I chose the first option because it seemed easier to implement and more straightforward within the time we had.
After improving the recall, the next step was to adapt the script so that it included only articles related to the current war. This was done by adding a condition to the script that skipped the articles written before the war started, based on the dates mentioned in the filenames.

### Script
The next part of the task was to write a script that counted the number of mentions of each place name per month. This information was stored in a dictionary with each place name as a key and its monthly counts as values.
Lastly, I wrote a final script that created a TSV file named regex_counts.tsv. This file contained three columns: placename, month, and count. After thoroughly reviewing the final script, I ran it in Python and successfully generated the desired output.

## Task 2B.
In part 2B, I was asked to extract place names from articles written in January 2024. 
## Counting
I needed to count how often each place was mentioned, clean the names to avoid duplicates (like treating “Gaza’s” and “Gaza” as the same), and save everything into a .tsv file.
To do this, I first copied the Gaza_NER2 notebook from the drive and renamed it using the names of my group members. I then removed the parts of the notebook that were not needed for this task.
### Installing libraries
Next, I installed the required libraries in Colab, such as stanza, os, and time. I set up the stanza pipeline and connected it to the larger corpus folder from the portfolio repository.
### Filtering articles to include only January 2024
I filtered the articles to include only those from January 2024 and ran the Named Entity Recognition (NER) to extract just the place names. After collecting the names, I counted how many times each one appeared.
### Cleaning the Data
To clean the data, I removed things like apostrophes or extra endings (for example, changing “Gaza’s” to “Gaza”) and merged the counts where names referred to the same place.
### Storing
In the final step, I saved the cleaned results into a .tsv file called ner_counts.tsv, with two columns: the place name and the count. Finally, I downloaded the notebook as a .ipynb file and added it to the GitHub repository.

## Task 3. Major Project Steps: From Articles to Maps
The project transforms a collection of textual articles into a geographic visualization by identifying and mapping place names mentioned in the text. The process involves several major steps, each building on the last to extract, enrich, and visualize geographic information.
### Named Entity Recognition (NER)
The workflow begins by applying a Named Entity Recognition model to the corpus of articles. This model identifies location names within the text and counts how often each appears. The results are stored in a .tsv file (ner_counts.tsv), which forms the foundation for subsequent geographic analysis.
### Extracting Place Names 
From ner_counts.tsv, place names are programmatically extracted using a Python script. Only the relevant column containing location names is collected and prepared as a list for processing.
### Geocoding via Gazetteer Construction:
Each place name is then passed to a custom function (get_coordinates) that queries the GeoNames API to obtain geographic coordinates (latitude and longitude). This step connects textual mentions to physical locations. If the API does not return coordinates—either due to ambiguity, uncommon spelling, or missing data—those entries are logged and flagged for manual follow-up.
### Manual Augmentation of Missing Data
For place names that failed automatic geolocation, coordinates are manually researched and appended using sources like Google Maps. This ensures completeness and accuracy in the final data.
### Building the Gazetteer:
All successfully geocoded places are written into a structured file (ner_gazetteer.tsv), which serves as a project-specific gazetteer. This file includes the name, latitude, and longitude of each location, linking text references to mappable data.
### Map Generation: 
The final step involves visualizing the gazetteer data. Interactive maps (ner_map.html) and static images (ner_map.png) are generated to show where mentioned places are located geographically. This turns abstract references in articles into concrete, spatial insights.

## Task 4.
Task 4 of this project was about identifying place names in a news article and showing them on a map. The goal was to see which places were mentioned the most and where they are in the world. To do this, I used two different methods: one using regular expressions (regex) and a gazetteer file, and the other using spaCy’s Named Entity Recognition (NER).
### Regex
In the first method, I used regex to search the article for place names. These names were counted and stored in a file called ner_counts.tsv. Then I used a gazetteer file (NER_gazetteer.tsv) that contains the latitude and longitude of many known places. By combining the place names and coordinates, I was able to create a map. 
### Building Map
I used Python and Plotly to build this map, which shows the frequency of each place with bubbles of different sizes. This map was saved in two formats: an interactive HTML file (task4_ner_map.html) and a static image (task4_ner_map.png). I also created a bonus version of the map as a dark-style heatmap (task4_density_heatmap.html) that shows how densely places are mentioned.
### NER
In the second method, I used the spaCy library, which has a built-in model to recognize named entities like countries, cities, and organizations. I wrote a script called task4b_visualize_ner.py that loads the article, uses spaCy to find named entities, and then highlights them in color using displaCy. 
### Storing Output
The output was saved as an HTML file called task4b_ner_visual.html, where the different types of entities are color-coded and easy to read.
Both methods have their strengths and weaknesses. The regex method is simple and gives more control, but it can miss complex or unusual place names. The spaCy method is more powerful and finds more entities, but sometimes it includes names that are not actual places. In the end, both approaches helped visualize the data and gave insight into which places were being talked about the most in the article.
This task helped me practice working with text data, using Python libraries like pandas, plotly, and spaCy, and building visual outputs that are easy to understand.

## Finalizing Check 
we finalized the following checklist:
    regex_counts.tsv 
    regex_script_final.py 
    Gaza_NER2_<Ihtisham_Suhrab_Sulaiman_Wajahat>.ipynb 
    NER_gazetteer.tsv build_gazetteer.ipynb 
    regex_map.html 
    regex_map.png 
    ner_map.html 
    ner_map.png 
    AI_documentation.docx 
## Describe Adventages and Disadvantages of Regex- Gazetteers and NER
### Regex-Gazetteers
The Regex plus Gazetteer approach is simple to implement and easily customizable for specific inputs by adding or modifying word lists in the gazetteer. It works well for detecting predefined patterns like dates, locations, or known entities and doesn't require complex models. However, this technique is not useful with unlisted entities and lacks the ability to generalize beyond its predefined rules and lists. It’s also prone to errors in unstructured, noisy, or diverse datasets where rigid patterns may not always hold.

### NER
NER models easily identify entities in diverse and unstructured text with higher accuracy and flexibility. They handle ambiguous cases better by learning from contextual patterns and can recognize new, unseen entities if well-trained. The Disadvantages is that NER requires substantial annotated data for training, is computationally intensive, and can be challenging to adapt to highly domain-specific tasks without fine-tuning. Moreever, pre-trained NER models sometimes miss out on niche entities not common in general-purpose datasets.

## Images of final maps
! [image(FASDH25-portfolio2/maps/regex.map.html)]
! [image(FASDH25-portfolio2/maps/regex.map.png)]
! [image(FASDH25-portfolio2/maps/ner.map.html)]
! [image(FASDH25-portfolio2/maps/ner.map.png)]

## Compare january 2024 maps
In this task, two different approaches were used to identify and visualize the places mentioned in a news article from January 2024. The first method used regular expressions combined with a gazetteer file, while the second used spaCy’s built-in named entity recognition (NER). Both methods aimed to highlight which places were most frequently mentioned, but they worked in different ways and produced different kinds of outputs.
The regex method involved searching the article using specific text patterns to find known place names. These names were then matched to a gazetteer that provided the latitude and longitude of each location. Using this data, an interactive map was created, where each place appeared as a circle on the world map, and the size of the circle showed how many times that place was mentioned in the article. This map made it easy to see which regions were mentioned most often. However, this method had some limitations — it only worked well when the place names matched exactly with the ones listed in the gazetteer. If a place was written differently or not included in the list, it could be missed entirely.
On the other hand, the spaCy NER method used a pre-trained model to automatically detect named entities in the text, such as cities, countries, and other geopolitical terms. The results were displayed using displaCy, which highlighted each entity in color inside the article text. While this output didn’t create a map, it gave a visual overview of all the places that spaCy could recognize. One of the main advantages of this method was that it was more flexible and could identify places even if they weren’t written exactly as expected. However, it also picked up some entities that weren’t actually geographic locations, and it didn’t provide coordinates, so it couldn’t directly generate a map without extra processing.

## Self Ciritical Analysis
One of the main weaknesses of the project was my limited experience with coding in Python. I struggled with writing and interpreting code, which slowed down my progress. Working with regular expressions was also bit challenging especially when dealing with multiple alternative place names and unpredictable spellings. If I had more time I would have focused on improving my coding skills and understanding of regex. Another limitation was the risk of mising place mentions due to spelling variations not captured by the gazetteer or regex patterns. I also needed time to properly review the corpus data and verify if the identified mentions made sense in context. Lastly we were really confused about the outputs of our scripts whether they are right or wrong as we did not have any source to verify them. If we were already provided with the output of the project scripts we could have at least compared our work with them and we could have less stressed about our work. Lastly, we were often unsure about whether the outputs of our scripts were correct, as we had no sample outputs to compare against. Having access to a reference output would have made it easier to verify our results and reduced the stress and uncertainty during the project.
