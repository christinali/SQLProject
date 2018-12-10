# -*- coding: utf-8 -*-
import urllib3
import json
import requests

comment1 = {"id": "0", "username": "Matthew O'Boyle", "up": 7, "down": 2, "comment": "Here's a comment", 
"date": "2018-12-01", "overall": 4, "difficulty": 3.4, "grade": "B+"} 
comment2 = {"id": "1", "username": "Feroze", "up": 12, "down": 1, "comment": "Feroze's comment", 
"date": "2018-11-29", "overall": 3.45, "difficulty": 1.4, "grade": "A-"} 
comment3 = {"id": "2", "username": "Christina", "up": 1, "down": 8, "comment": "Christina's comment", 
"date": "2018-11-26", "overall": 3.7, "difficulty": 1.7, "grade": "A"} 
comment4 = {"id": "3", "username": "Salil", "up": 47, "down": 3, "comment": "Salil's comment", 
"date": "2018-11-21", "overall": 3.2, "difficulty": 3.45, "grade": "B-"} 

jun = {"name": "Jun Yang", "id": 1, "overall": 4.7, "difficulty": 2.1}
rob = {"name": "Robert Duvall", "id": 2, "overall": 4.3, "difficulty": 2.9}
jeff = {"name": "Jeff Forbes", "id": 3, "overall": 4.1, "difficulty": 4.1}
susan = {"name": "Susan Rodger", "id": 4, "overall": 2.1, "difficulty": 1.1}
astrachan = {"name": "Astrachan", "id": 5, "overall": 1.2, "difficulty": 4.5}

profs1 = [jun, rob, jeff]
profs2 = [susan, astrachan, rob]

class1 = {"id": "0", "num": 316, "dept": "Compsci", "name": "Databases", "overall": 4.1, 
"difficulty": 1.2, "comments": [comment1, comment2, comment3], "profs": profs1, 
"nextSemProf": jun, "recommendedSem": "Senior Fall"}

class2 = {"id": "1", "num": 201, "dept": "Compsci", "name": "Algorithms", "overall": 3.7, 
"difficulty": 4.5, "comments": [comment3, comment1, comment4], "profs": profs2, 
"nextSemProf": jeff, "recommendedSem": "Junior Spring"}

def getFullClasses(): 
    return [class1, class2]
    
def getAllReviews(): 
    return [comment1, comment2, comment3, comment4]
    
    
    
    
classes = """<select class="parameter" name="subject">
        
        
        
            
                <option value="AAAS - African and African American S">AAAS - African and African American S</option>
            
        
            
                <option value="ACCOUNTG - Accounting">ACCOUNTG - Accounting</option>
            
        
            
                <option value="ADF - American Dance Festival">ADF - American Dance Festival</option>
            
        
            
                <option value="AEP - Anesthesiology/Environ Physio">AEP - Anesthesiology/Environ Physio</option>
            
        
            
                <option value="AEROSCI - Aerospace Studies-AFROTC">AEROSCI - Aerospace Studies-AFROTC</option>
            
        
            
                <option value="AFA@ - AFA (UNC-CH)">AFA@ - AFA (UNC-CH)</option>
            
        
            
                <option value="AMES - Asian &amp; Middle Eastern Studies">AMES - Asian &amp; Middle Eastern Studies</option>
            
        
            
                <option value="AMH - Amharic">AMH - Amharic</option>
            
        
            
                <option value="AMHARIC - Amharic">AMHARIC - Amharic</option>
            
        
            
                <option value="AMI - Arts of the Moving Image">AMI - Arts of the Moving Image</option>
            
        
            
                <option value="AMXTIAN - American Christianity">AMXTIAN - American Christianity</option>
            
        
            
                <option value="ANATOMY - Anatomy">ANATOMY - Anatomy</option>
            
        
            
                <option value="ANE - Anesthesiology">ANE - Anesthesiology</option>
            
        
            
                <option value="ANESTH - Anesthesiology">ANESTH - Anesthesiology</option>
            
        
            
                <option value="APLSCI - Applied Science Certificate Pr">APLSCI - Applied Science Certificate Pr</option>
            
        
            
                <option value="ARABIC - Arabic">ARABIC - Arabic</option>
            
        
            
                <option value="ARTHIST - Art History">ARTHIST - Art History</option>
            
        
            
                <option value="ARTS&amp;SCI - Arts and Science IDEAS themes">ARTS&amp;SCI - Arts and Science IDEAS themes</option>
            
        
            
                <option value="ARTSINST - Institute of the Arts">ARTSINST - Institute of the Arts</option>
            
        
            
                <option value="ARTSVIS - Visual Arts">ARTSVIS - Visual Arts</option>
            
        
            
                <option value="ASEP - Anesthesiol, Surg &amp; Envtl Phys">ASEP - Anesthesiol, Surg &amp; Envtl Phys</option>
            
        
            
                <option value="AYMARA - Aymara">AYMARA - Aymara</option>
            
        
            
                <option value="BA - Business Administration">BA - Business Administration</option>
            
        
            
                <option value="BALTFIN - Balto-Finnic">BALTFIN - Balto-Finnic</option>
            
        
            
                <option value="BCS - Black Church Studies">BCS - Black Church Studies</option>
            
        
            
                <option value="BES - BioMed Engineering and Surgery">BES - BioMed Engineering and Surgery</option>
            
        
            
                <option value="BIB - Biostatistics &amp; Bioinformatics">BIB - Biostatistics &amp; Bioinformatics</option>
            
        
            
                <option value="BIMP - Biomed Imaging &amp; Med Physics">BIMP - Biomed Imaging &amp; Med Physics</option>
            
        
            
                <option value="BIOCHEM - Biochemistry">BIOCHEM - Biochemistry</option>
            
        
            
                <option value="BIOETHIC - Bioethics and Science Policy">BIOETHIC - Bioethics and Science Policy</option>
            
        
            
                <option value="BIOLOGY - Biology">BIOLOGY - Biology</option>
            
        
            
                <option value="BIOMETRY - Biometry">BIOMETRY - Biometry</option>
            
        
            
                <option value="BIOPHY - Biophysics">BIOPHY - Biophysics</option>
            
        
            
                <option value="BIOSTAT - Biostatistics">BIOSTAT - Biostatistics</option>
            
        
            
                <option value="BME - Biomedical Engineering">BME - Biomedical Engineering</option>
            
        
            
                <option value="BMI - Biometry">BMI - Biometry</option>
            
        
            
                <option value="BO - BO @ NCSU">BO - BO @ NCSU</option>
            
        
            
                <option value="BPP - Biophysics Study Program">BPP - Biophysics Study Program</option>
            
        
            
                <option value="BRAINSOC - Brain &amp; Society">BRAINSOC - Brain &amp; Society</option>
            
        
            
                <option value="BSP - Behavioral Neuro Study Program">BSP - Behavioral Neuro Study Program</option>
            
        
            
                <option value="CANADIAN - Canadian Studies">CANADIAN - Canadian Studies</option>
            
        
            
                <option value="CAS - Casper">CAS - Casper</option>
            
        
            
                <option value="CBB - Computational Bio  Bioinformat">CBB - Computational Bio  Bioinformat</option>
            
        
            
                <option value="CBP - Cancer Biology Study Program">CBP - Cancer Biology Study Program</option>
            
        
            
                <option value="CEE - Civil and Environmental Egr">CEE - Civil and Environmental Egr</option>
            
        
            
                <option value="CEL@ - CEL (UNC-CH)">CEL@ - CEL (UNC-CH)</option>
            
        
            
                <option value="CELLBIO - Cell Biology">CELLBIO - Cell Biology</option>
            
        
            
                <option value="CESC - Civic Engagement&amp;Social Change">CESC - Civic Engagement&amp;Social Change</option>
            
        
            
                <option value="CFM - Community &amp; Family Medicine">CFM - Community &amp; Family Medicine</option>
            
        
            
                <option value="CHEM - Chemistry">CHEM - Chemistry</option>
            
        
            
                <option value="CHILDPOL - Child Policy">CHILDPOL - Child Policy</option>
            
        
            
                <option value="CHINESE - Chinese">CHINESE - Chinese</option>
            
        
            
                <option value="CHURHST - Church History">CHURHST - Church History</option>
            
        
            
                <option value="CHURMIN - Church Ministry">CHURMIN - Church Ministry</option>
            
        
            
                <option value="CIF - Colloquia/Interfield/Field Edu">CIF - Colloquia/Interfield/Field Edu</option>
            
        
            
                <option value="CLINARTS - Clinical Arts">CLINARTS - Clinical Arts</option>
            
        
            
                <option value="CLP - Clinical Leadership Program">CLP - Clinical Leadership Program</option>
            
        
            
                <option value="CLST - Classical Studies">CLST - Classical Studies</option>
            
        
            
                <option value="CMAC - Cmputnl Media, Arts &amp; Cultures">CMAC - Cmputnl Media, Arts &amp; Cultures</option>
            
        
            
                <option value="CMB - Cell and Molecular Biology">CMB - Cell and Molecular Biology</option>
            
        
            
                <option value="CNT@ - CNT (USC)">CNT@ - CNT (USC)</option>
            
        
            
                <option value="COMMFAM - Community and Family Medicine">COMMFAM - Community and Family Medicine</option>
            
        
            
                <option value="COMPSCI - Computer Science">COMPSCI - Computer Science</option>
            
        
            
                <option value="CONTDIV - Continuation - Divinity">CONTDIV - Continuation - Divinity</option>
            
        
            
                <option value="CONTEGRP - Continuation-Engineering">CONTEGRP - Continuation-Engineering</option>
            
        
            
                <option value="CONTENV - Continuation-Completion(NSOE)">CONTENV - Continuation-Completion(NSOE)</option>
            
        
            
                <option value="CONTGRAD - Continuation-Graduate School">CONTGRAD - Continuation-Graduate School</option>
            
        
            
                <option value="CONTNUR - Course Continuation - Nursing">CONTNUR - Course Continuation - Nursing</option>
            
        
            
                <option value="CONTPPS - Course Continuation - PPS">CONTPPS - Course Continuation - PPS</option>
            
        
            
                <option value="CORE - Clinical Core">CORE - Clinical Core</option>
            
        
            
                <option value="CPE - Clinical Pastoral Education">CPE - Clinical Pastoral Education</option>
            
        
            
                <option value="CRB - Cell and Regulatory Biology St">CRB - Cell and Regulatory Biology St</option>
            
        
            
                <option value="CREOLE - Creole">CREOLE - Creole</option>
            
        
            
                <option value="CRP - Clinical Research Training Prg">CRP - Clinical Research Training Prg</option>
            
        
            
                <option value="CRS - Continuation of Enrollment">CRS - Continuation of Enrollment</option>
            
        
            
                <option value="CRSP - Clinical Research Study Prog">CRSP - Clinical Research Study Prog</option>
            
        
            
                <option value="CSE@ - CSE (UNC-CH)">CSE@ - CSE (UNC-CH)</option>
            
        
            
                <option value="CTA - CTA @">CTA - CTA @</option>
            
        
            
                <option value="CTN - Continuation - Graduate School">CTN - Continuation - Graduate School</option>
            
        
            
                <option value="CTW - CTW @">CTW - CTW @</option>
            
        
            
                <option value="CULANTH - Cultural Anthropology">CULANTH - Cultural Anthropology</option>
            
        
            
                <option value="CVS - Cardiovascular Study Program">CVS - Cardiovascular Study Program</option>
            
        
            
                <option value="DANCE - Dance">DANCE - Dance</option>
            
        
            
                <option value="DECISION - Decision Sciences">DECISION - Decision Sciences</option>
            
        
            
                <option value="DECSCI - Decision Sciences Program">DECSCI - Decision Sciences Program</option>
            
        
            
                <option value="DERMATOL - Dermatology">DERMATOL - Dermatology</option>
            
        
            
                <option value="DIVINITY - Divinity">DIVINITY - Divinity</option>
            
        
            
                <option value="DMNISTRY - Doctor of Ministry">DMNISTRY - Doctor of Ministry</option>
            
        
            
                <option value="DOCST - Documentary Studies">DOCST - Documentary Studies</option>
            
        
            
                <option value="DPC - Distinguished Professor Course">DPC - Distinguished Professor Course</option>
            
        
            
                <option value="DRAMA - Drama">DRAMA - Drama</option>
            
        
            
                <option value="DUTCH - Dutch">DUTCH - Dutch</option>
            
        
            
                <option value="ECE - Electrical &amp; Computer Egr">ECE - Electrical &amp; Computer Egr</option>
            
        
            
                <option value="ECON - Economics">ECON - Economics</option>
            
        
            
                <option value="EDI@ - EDI (UNC-CH)">EDI@ - EDI (UNC-CH)</option>
            
        
            
                <option value="EDUC - Education">EDUC - Education</option>
            
        
            
                <option value="EGR - Engineering">EGR - Engineering</option>
            
        
            
                <option value="EGRMGMT - Engineering Management">EGRMGMT - Engineering Management</option>
            
        
            
                <option value="EHD - Education and Human Developmnt">EHD - Education and Human Developmnt</option>
            
        
            
                <option value="ENERGY - Energy">ENERGY - Energy</option>
            
        
            
                <option value="ENGLISH - English">ENGLISH - English</option>
            
        
            
                <option value="ENR - Enrollment Fee">ENR - Enrollment Fee</option>
            
        
            
                <option value="ENRGYEGR - Energy Engineering">ENRGYEGR - Energy Engineering</option>
            
        
            
                <option value="ENRGYENV - Energy &amp; Environment">ENRGYENV - Energy &amp; Environment</option>
            
        
            
                <option value="ENTREPRN - Entrepreneurship &amp; Innovation">ENTREPRN - Entrepreneurship &amp; Innovation</option>
            
        
            
                <option value="ENVIRON - Environment">ENVIRON - Environment</option>
            
        
            
                <option value="EOS - Earth and Ocean Sciences">EOS - Earth and Ocean Sciences</option>
            
        
            
                <option value="EPH - Epidemiology &amp; Public Health">EPH - Epidemiology &amp; Public Health</option>
            
        
            
                <option value="ERS - Education Research Studies">ERS - Education Research Studies</option>
            
        
            
                <option value="ETHICS - Study of Ethics">ETHICS - Study of Ethics</option>
            
        
            
                <option value="EVANTH - Evolutionary Anthropology">EVANTH - Evolutionary Anthropology</option>
            
        
            
                <option value="EXP - Study Away">EXP - Study Away</option>
            
        
            
                <option value="FA - FA @">FA - FA @</option>
            
        
            
                <option value="FIELDEDU - Field Education">FIELDEDU - Field Education</option>
            
        
            
                <option value="FINANCE - Finance">FINANCE - Finance</option>
            
        
            
                <option value="FLDCTN - Field Edu Continuation - Div">FLDCTN - Field Edu Continuation - Div</option>
            
        
            
                <option value="FOCUS - Focus">FOCUS - Focus</option>
            
        
            
                <option value="FREETIME - Free Time">FREETIME - Free Time</option>
            
        
            
                <option value="FRENCH - French">FRENCH - French</option>
            
        
            
                <option value="FUQINTRD - Interdisciplinary">FUQINTRD - Interdisciplinary</option>
            
        
            
                <option value="GATE - Global Academic Travel Exp">GATE - Global Academic Travel Exp</option>
            
        
            
                <option value="GBLDEVLP - Global Development Engineering">GBLDEVLP - Global Development Engineering</option>
            
        
            
                <option value="GENETICS - Genetics">GENETICS - Genetics</option>
            
        
            
                <option value="GENOME - Science &amp; Society">GENOME - Science &amp; Society</option>
            
        
            
                <option value="GEOADMIN - Global Education Admn Use Only">GEOADMIN - Global Education Admn Use Only</option>
            
        
            
                <option value="GEOLOGY - Geology">GEOLOGY - Geology</option>
            
        
            
                <option value="GEORGIAN - Georgian">GEORGIAN - Georgian</option>
            
        
            
                <option value="GERMAN - German">GERMAN - German</option>
            
        
            
                <option value="GERMANST - German Studies">GERMANST - German Studies</option>
            
        
            
                <option value="GHS - Global Health Study Program">GHS - Global Health Study Program</option>
            
        
            
                <option value="GHSR - Global Health Student Research">GHSR - Global Health Student Research</option>
            
        
            
                <option value="GLHLTH - Global Health">GLHLTH - Global Health</option>
            
        
            
                <option value="GREEK - Greek">GREEK - Greek</option>
            
        
            
                <option value="GRY@ - GRY@UNC">GRY@ - GRY@UNC</option>
            
        
            
                <option value="GS - Graduate Studies">GS - Graduate Studies</option>
            
        
            
                <option value="GSF - Gender Sexuality &amp; Feminist St">GSF - Gender Sexuality &amp; Feminist St</option>
            
        
            
                <option value="HCVIS - Historical&amp;Cultural Visualiztn">HCVIS - Historical&amp;Cultural Visualiztn</option>
            
        
            
                <option value="HEBREW - Hebrew">HEBREW - Hebrew</option>
            
        
            
                <option value="HED@ - HED (NCCU)">HED@ - HED (NCCU)</option>
            
        
            
                <option value="HGP - Human Genetics Study Program">HGP - Human Genetics Study Program</option>
            
        
            
                <option value="HINDI - Hindi">HINDI - Hindi</option>
            
        
            
                <option value="HISTORY - History">HISTORY - History</option>
            
        
            
                <option value="HISTREL - History of Religion">HISTREL - History of Religion</option>
            
        
            
                <option value="HISTTHEO - Historical Theology">HISTTHEO - Historical Theology</option>
            
        
            
                <option value="HLTHMGMT - Health Sector Management">HLTHMGMT - Health Sector Management</option>
            
        
            
                <option value="HLTHSCI - Health Sciences">HLTHSCI - Health Sciences</option>
            
        
            
                <option value="HNM - Health and Nursing Ministries">HNM - Health and Nursing Ministries</option>
            
        
            
                <option value="HOUSECS - House Course">HOUSECS - House Course</option>
            
        
            
                <option value="HSP - Hispanic Summer Program">HSP - Hispanic Summer Program</option>
            
        
            
                <option value="HTHPOL - Health Policy">HTHPOL - Health Policy</option>
            
        
            
                <option value="HUMANDEV - Human Development">HUMANDEV - Human Development</option>
            
        
            
                <option value="HUNGARN - Hungarian">HUNGARN - Hungarian</option>
            
        
            
                <option value="I&amp;E - Innovation &amp; Entrepreneurship">I&amp;E - Innovation &amp; Entrepreneurship</option>
            
        
            
                <option value="ICS - Internatl Comparative Studies">ICS - Internatl Comparative Studies</option>
            
        
            
                <option value="IDP - Infectious Diseases Study Prog">IDP - Infectious Diseases Study Prog</option>
            
        
            
                <option value="IDS - Interdisciplinary Data Science">IDS - Interdisciplinary Data Science</option>
            
        
            
                <option value="ILE - Integrative Leadership Exp">ILE - Integrative Leadership Exp</option>
            
        
            
                <option value="IMMUNOL - Immunology">IMMUNOL - Immunology</option>
            
        
            
                <option value="IMPINV - Initiative on Impact Investing">IMPINV - Initiative on Impact Investing</option>
            
        
            
                <option value="INCC_PHL - Philosophy">INCC_PHL - Philosophy</option>
            
        
            
                <option value="INCG_BIO - BIOLOGY">INCG_BIO - BIOLOGY</option>
            
        
            
                <option value="INCG_CST - CLASSICAL STUDIES">INCG_CST - CLASSICAL STUDIES</option>
            
        
            
                <option value="INCG_HDF - Human Dev/Fam Studies">INCG_HDF - Human Dev/Fam Studies</option>
            
        
            
                <option value="INCG_MAS - Master of Applied Arts/Science">INCG_MAS - Master of Applied Arts/Science</option>
            
        
            
                <option value="INCG_MBA - MBA">INCG_MBA - MBA</option>
            
        
            
                <option value="INCG_PSY - Psychology">INCG_PSY - Psychology</option>
            
        
            
                <option value="INCG_REL - Religious Studies">INCG_REL - Religious Studies</option>
            
        
            
                <option value="INCG_SPA - Spanish">INCG_SPA - Spanish</option>
            
        
            
                <option value="INCH_AAD - Afri, Afri-Amer, Diaspora Stds">INCH_AAD - Afri, Afri-Amer, Diaspora Stds</option>
            
        
            
                <option value="INCH_AAR - Archeology">INCH_AAR - Archeology</option>
            
        
            
                <option value="INCH_AFA - African American Studies">INCH_AFA - African American Studies</option>
            
        
            
                <option value="INCH_AFR - African Studies">INCH_AFR - African Studies</option>
            
        
            
                <option value="INCH_ANT - Anthropology">INCH_ANT - Anthropology</option>
            
        
            
                <option value="INCH_ARB - Arabic">INCH_ARB - Arabic</option>
            
        
            
                <option value="INCH_ARH - Art History">INCH_ARH - Art History</option>
            
        
            
                <option value="INCH_ART - Art">INCH_ART - Art</option>
            
        
            
                <option value="INCH_ASA - Asian Studies">INCH_ASA - Asian Studies</option>
            
        
            
                <option value="INCH_AST - American Studies">INCH_AST - American Studies</option>
            
        
            
                <option value="INCH_ASY - Astronomy">INCH_ASY - Astronomy</option>
            
        
            
                <option value="INCH_BCM - Biochemistry">INCH_BCM - Biochemistry</option>
            
        
            
                <option value="INCH_BCS - Bosnian-Croatian-Serbian">INCH_BCS - Bosnian-Croatian-Serbian</option>
            
        
            
                <option value="INCH_BEN - Bengali">INCH_BEN - Bengali</option>
            
        
            
                <option value="INCH_BIO - Biology">INCH_BIO - Biology</option>
            
        
            
                <option value="INCH_BME - Biomedical Engineering">INCH_BME - Biomedical Engineering</option>
            
        
            
                <option value="INCH_BST - Biostatistics">INCH_BST - Biostatistics</option>
            
        
            
                <option value="INCH_BUS - Business">INCH_BUS - Business</option>
            
        
            
                <option value="INCH_CBI - Cell Biology">INCH_CBI - Cell Biology</option>
            
        
            
                <option value="INCH_CBM - Chemical Biology Med Chemistry">INCH_CBM - Chemical Biology Med Chemistry</option>
            
        
            
                <option value="INCH_CHM - Chemistry">INCH_CHM - Chemistry</option>
            
        
            
                <option value="INCH_CHN - Chinese">INCH_CHN - Chinese</option>
            
        
            
                <option value="INCH_CHR - Cherokee">INCH_CHR - Cherokee</option>
            
        
            
                <option value="INCH_CLR - Classical Archaeology">INCH_CLR - Classical Archaeology</option>
            
        
            
                <option value="INCH_CLS - Classical Studies">INCH_CLS - Classical Studies</option>
            
        
            
                <option value="INCH_CMM - Communication Studies">INCH_CMM - Communication Studies</option>
            
        
            
                <option value="INCH_CMP - Comparative Literature">INCH_CMP - Comparative Literature</option>
            
        
            
                <option value="INCH_COM - Computer Science">INCH_COM - Computer Science</option>
            
        
            
                <option value="INCH_DRA - Drama">INCH_DRA - Drama</option>
            
        
            
                <option value="INCH_DTH - Dutch">INCH_DTH - Dutch</option>
            
        
            
                <option value="INCH_ECL - Ecology">INCH_ECL - Ecology</option>
            
        
            
                <option value="INCH_ECO - Economics">INCH_ECO - Economics</option>
            
        
            
                <option value="INCH_EDU - Education">INCH_EDU - Education</option>
            
        
            
                <option value="INCH_ENG - English">INCH_ENG - English</option>
            
        
            
                <option value="INCH_ENS - Environmental Sci &amp; Studies">INCH_ENS - Environmental Sci &amp; Studies</option>
            
        
            
                <option value="INCH_ENV - Environmental Sciences">INCH_ENV - Environmental Sciences</option>
            
        
            
                <option value="INCH_EPD - Epidemiology">INCH_EPD - Epidemiology</option>
            
        
            
                <option value="INCH_EXS - Exercise and Sport Science">INCH_EXS - Exercise and Sport Science</option>
            
        
            
                <option value="INCH_FOL - Folklore">INCH_FOL - Folklore</option>
            
        
            
                <option value="INCH_FRN - French">INCH_FRN - French</option>
            
        
            
                <option value="INCH_GBS - Global Studies">INCH_GBS - Global Studies</option>
            
        
            
                <option value="INCH_GEG - Geography">INCH_GEG - Geography</option>
            
        
            
                <option value="INCH_GEO - Geology">INCH_GEO - Geology</option>
            
        
            
                <option value="INCH_GER - German">INCH_GER - German</option>
            
        
            
                <option value="INCH_GNT - GENETICS &amp; MOLECULAR BIOLOGY">INCH_GNT - GENETICS &amp; MOLECULAR BIOLOGY</option>
            
        
            
                <option value="INCH_GRK - Greek">INCH_GRK - Greek</option>
            
        
            
                <option value="INCH_HBH - Health Behavior &amp;  Education">INCH_HBH - Health Behavior &amp;  Education</option>
            
        
            
                <option value="INCH_HNR - Honors">INCH_HNR - Honors</option>
            
        
            
                <option value="INCH_HNU - Hindi-Urdu">INCH_HNU - Hindi-Urdu</option>
            
        
            
                <option value="INCH_HPA - Health Policy &amp; Administration">INCH_HPA - Health Policy &amp; Administration</option>
            
        
            
                <option value="INCH_HPM - Health Policy And Management">INCH_HPM - Health Policy And Management</option>
            
        
            
                <option value="INCH_HST - History">INCH_HST - History</option>
            
        
            
                <option value="INCH_HUN - Hungarian">INCH_HUN - Hungarian</option>
            
        
            
                <option value="INCH_INL - Information Library Science">INCH_INL - Information Library Science</option>
            
        
            
                <option value="INCH_ITA - Italian">INCH_ITA - Italian</option>
            
        
            
                <option value="INCH_JPN - Japanese">INCH_JPN - Japanese</option>
            
        
            
                <option value="INCH_LAW - Law">INCH_LAW - Law</option>
            
        
            
                <option value="INCH_LGL - LINGALA LANGUAGE">INCH_LGL - LINGALA LANGUAGE</option>
            
        
            
                <option value="INCH_LIN - Linguistics">INCH_LIN - Linguistics</option>
            
        
            
                <option value="INCH_LIT - Literature">INCH_LIT - Literature</option>
            
        
            
                <option value="INCH_LTN - Latin">INCH_LTN - Latin</option>
            
        
            
                <option value="INCH_MAC - Master of Accounting">INCH_MAC - Master of Accounting</option>
            
        
            
                <option value="INCH_MAS - Marine Science">INCH_MAS - Marine Science</option>
            
        
            
                <option value="INCH_MAY - Yucatec Maya">INCH_MAY - Yucatec Maya</option>
            
        
            
                <option value="INCH_MBA - Master of Business Admin">INCH_MBA - Master of Business Admin</option>
            
        
            
                <option value="INCH_MCB - Microbiology">INCH_MCB - Microbiology</option>
            
        
            
                <option value="INCH_MEJ - Media &amp; Journalism">INCH_MEJ - Media &amp; Journalism</option>
            
        
            
                <option value="INCH_MGT - Management">INCH_MGT - Management</option>
            
        
            
                <option value="INCH_MHC - Maternal and Child Health">INCH_MHC - Maternal and Child Health</option>
            
        
            
                <option value="INCH_MOR - Molecular Pharmaceutics">INCH_MOR - Molecular Pharmaceutics</option>
            
        
            
                <option value="INCH_MTH - Math">INCH_MTH - Math</option>
            
        
            
                <option value="INCH_MUS - Music">INCH_MUS - Music</option>
            
        
            
                <option value="INCH_NBI - Neurobiology">INCH_NBI - Neurobiology</option>
            
        
            
                <option value="INCH_NTR - Nutrition">INCH_NTR - Nutrition</option>
            
        
            
                <option value="INCH_NUR - Nursing">INCH_NUR - Nursing</option>
            
        
            
                <option value="INCH_OTI - OTI (UNC-CH)">INCH_OTI - OTI (UNC-CH)</option>
            
        
            
                <option value="INCH_PHA - Physical Activities">INCH_PHA - Physical Activities</option>
            
        
            
                <option value="INCH_PHC - Pharmacy">INCH_PHC - Pharmacy</option>
            
        
            
                <option value="INCH_PHL - Philosphy">INCH_PHL - Philosphy</option>
            
        
            
                <option value="INCH_PHN - Public Health Nursing">INCH_PHN - Public Health Nursing</option>
            
        
            
                <option value="INCH_PHS - Physiology">INCH_PHS - Physiology</option>
            
        
            
                <option value="INCH_PHY - Physics">INCH_PHY - Physics</option>
            
        
            
                <option value="INCH_PLH - Polish">INCH_PLH - Polish</option>
            
        
            
                <option value="INCH_PLN - Planning">INCH_PLN - Planning</option>
            
        
            
                <option value="INCH_PLY - Public Policy">INCH_PLY - Public Policy</option>
            
        
            
                <option value="INCH_POL - Political Science">INCH_POL - Political Science</option>
            
        
            
                <option value="INCH_POR - Portuguese">INCH_POR - Portuguese</option>
            
        
            
                <option value="INCH_PRN - Persian">INCH_PRN - Persian</option>
            
        
            
                <option value="INCH_PSY - Psychology">INCH_PSY - Psychology</option>
            
        
            
                <option value="INCH_PTH - Pathology">INCH_PTH - Pathology</option>
            
        
            
                <option value="INCH_PUA - Public Administration">INCH_PUA - Public Administration</option>
            
        
            
                <option value="INCH_PUH - Public Health">INCH_PUH - Public Health</option>
            
        
            
                <option value="INCH_PUP - Public Policy Analysis">INCH_PUP - Public Policy Analysis</option>
            
        
            
                <option value="INCH_PWD - Peace War &amp; Defense">INCH_PWD - Peace War &amp; Defense</option>
            
        
            
                <option value="INCH_REL - Religion">INCH_REL - Religion</option>
            
        
            
                <option value="INCH_RES - Russian &amp; East Euro Studies">INCH_RES - Russian &amp; East Euro Studies</option>
            
        
            
                <option value="INCH_ROM - Romance Languages">INCH_ROM - Romance Languages</option>
            
        
            
                <option value="INCH_RUS - Russian">INCH_RUS - Russian</option>
            
        
            
                <option value="INCH_SAN - Sanskrit">INCH_SAN - Sanskrit</option>
            
        
            
                <option value="INCH_SEC - Serb &amp; Croatian">INCH_SEC - Serb &amp; Croatian</option>
            
        
            
                <option value="INCH_SER - INCH_SER">INCH_SER - INCH_SER</option>
            
        
            
                <option value="INCH_SLV - Slavic Languages &amp; Literature">INCH_SLV - Slavic Languages &amp; Literature</option>
            
        
            
                <option value="INCH_SOC - Sociology">INCH_SOC - Sociology</option>
            
        
            
                <option value="INCH_SOW - Social Work">INCH_SOW - Social Work</option>
            
        
            
                <option value="INCH_SPA - Spanish">INCH_SPA - Spanish</option>
            
        
            
                <option value="INCH_SPH - Speech &amp; Hearing Sciences">INCH_SPH - Speech &amp; Hearing Sciences</option>
            
        
            
                <option value="INCH_STR - Stats &amp; Operations Research">INCH_STR - Stats &amp; Operations Research</option>
            
        
            
                <option value="INCH_SUS - SUSI (UNC-CH)">INCH_SUS - SUSI (UNC-CH)</option>
            
        
            
                <option value="INCH_SWA - Swahili">INCH_SWA - Swahili</option>
            
        
            
                <option value="INCH_TAM - Tamil">INCH_TAM - Tamil</option>
            
        
            
                <option value="INCH_TOX - Toxicology">INCH_TOX - Toxicology</option>
            
        
            
                <option value="INCH_VIT - Vietnamese">INCH_VIT - Vietnamese</option>
            
        
            
                <option value="INCH_WOL - Wolof Language">INCH_WOL - Wolof Language</option>
            
        
            
                <option value="INCH_WST - Women's Studies">INCH_WST - Women's Studies</option>
            
        
            
                <option value="INCS_ACC - Accounting">INCS_ACC - Accounting</option>
            
        
            
                <option value="INCS_ADN - Art and Design">INCS_ADN - Art and Design</option>
            
        
            
                <option value="INCS_AEC - Applied Ecology">INCS_AEC - Applied Ecology</option>
            
        
            
                <option value="INCS_ANS - Animal Science">INCS_ANS - Animal Science</option>
            
        
            
                <option value="INCS_ARC - Architecture">INCS_ARC - Architecture</option>
            
        
            
                <option value="INCS_ARE - Agricultural Economics">INCS_ARE - Agricultural Economics</option>
            
        
            
                <option value="INCS_BAE - BIOLOGICAL &amp; AGRIC ENGINEERING">INCS_BAE - BIOLOGICAL &amp; AGRIC ENGINEERING</option>
            
        
            
                <option value="INCS_BIO - Biological Sciences">INCS_BIO - Biological Sciences</option>
            
        
            
                <option value="INCS_BMA - Biomathematics">INCS_BMA - Biomathematics</option>
            
        
            
                <option value="INCS_BME - Biomedical Engineering">INCS_BME - Biomedical Engineering</option>
            
        
            
                <option value="INCS_BO - Botany">INCS_BO - Botany</option>
            
        
            
                <option value="INCS_BUS - Business Management">INCS_BUS - Business Management</option>
            
        
            
                <option value="INCS_CBS - Comparative Biomedical Science">INCS_CBS - Comparative Biomedical Science</option>
            
        
            
                <option value="INCS_CE - Civil Engineering">INCS_CE - Civil Engineering</option>
            
        
            
                <option value="INCS_CH - Chemistry">INCS_CH - Chemistry</option>
            
        
            
                <option value="INCS_CHE - Chemical Engineering">INCS_CHE - Chemical Engineering</option>
            
        
            
                <option value="INCS_COM - Communication Studies">INCS_COM - Communication Studies</option>
            
        
            
                <option value="INCS_CS - Crop Science">INCS_CS - Crop Science</option>
            
        
            
                <option value="INCS_CSC - Computer Science">INCS_CSC - Computer Science</option>
            
        
            
                <option value="INCS_EAC - Adult &amp; Higher Education">INCS_EAC - Adult &amp; Higher Education</option>
            
        
            
                <option value="INCS_EC - Economics  (Undergraduate)">INCS_EC - Economics  (Undergraduate)</option>
            
        
            
                <option value="INCS_ECE - Eletrical/Computer Engineering">INCS_ECE - Eletrical/Computer Engineering</option>
            
        
            
                <option value="INCS_ECG - Economics (Graduate)">INCS_ECG - Economics (Graduate)</option>
            
        
            
                <option value="INCS_ECI - Curriculum and Instruction">INCS_ECI - Curriculum and Instruction</option>
            
        
            
                <option value="INCS_EGR - Engineering">INCS_EGR - Engineering</option>
            
        
            
                <option value="INCS_ELP - Edu Leadershp &amp; Policy Studies">INCS_ELP - Edu Leadershp &amp; Policy Studies</option>
            
        
            
                <option value="INCS_ENG - English">INCS_ENG - English</option>
            
        
            
                <option value="INCS_ENT - Entomology">INCS_ENT - Entomology</option>
            
        
            
                <option value="INCS_FL - Foreign Language &amp; Literatures">INCS_FL - Foreign Language &amp; Literatures</option>
            
        
            
                <option value="INCS_FLG - Foreign Language-German">INCS_FLG - Foreign Language-German</option>
            
        
            
                <option value="INCS_FLN - Foreign Language - Hindi-Urdu">INCS_FLN - Foreign Language - Hindi-Urdu</option>
            
        
            
                <option value="INCS_FLP - Foreign Language - Portuguese">INCS_FLP - Foreign Language - Portuguese</option>
            
        
            
                <option value="INCS_FOR - Forestry">INCS_FOR - Forestry</option>
            
        
            
                <option value="INCS_FS - Food Science">INCS_FS - Food Science</option>
            
        
            
                <option value="INCS_FW - Fisheries &amp; Wildlife Sciences">INCS_FW - Fisheries &amp; Wildlife Sciences</option>
            
        
            
                <option value="INCS_GIS - Geographic Info Systems">INCS_GIS - Geographic Info Systems</option>
            
        
            
                <option value="INCS_GN - Genetics">INCS_GN - Genetics</option>
            
        
            
                <option value="INCS_HEA - HEALTH EXERCISE AQUATICS">INCS_HEA - HEALTH EXERCISE AQUATICS</option>
            
        
            
                <option value="INCS_HI - History">INCS_HI - History</option>
            
        
            
                <option value="INCS_HOR - Horticulture">INCS_HOR - Horticulture</option>
            
        
            
                <option value="INCS_ID - Industrial Design">INCS_ID - Industrial Design</option>
            
        
            
                <option value="INCS_IE - Industrial Engineering">INCS_IE - Industrial Engineering</option>
            
        
            
                <option value="INCS_IMM - IMMUNOLOGY">INCS_IMM - IMMUNOLOGY</option>
            
        
            
                <option value="INCS_ISE - Industrial &amp; Syst Engineering">INCS_ISE - Industrial &amp; Syst Engineering</option>
            
        
            
                <option value="INCS_LAR - Landscape Architecture">INCS_LAR - Landscape Architecture</option>
            
        
            
                <option value="INCS_LOG - Logic">INCS_LOG - Logic</option>
            
        
            
                <option value="INCS_MA - Mathematics">INCS_MA - Mathematics</option>
            
        
            
                <option value="INCS_MAE - Mechanical &amp; Aerospace Egr">INCS_MAE - Mechanical &amp; Aerospace Egr</option>
            
        
            
                <option value="INCS_MEA - Marine,Earth,&amp; Atmospheric Sci">INCS_MEA - Marine,Earth,&amp; Atmospheric Sci</option>
            
        
            
                <option value="INCS_MLS - Liberal Studies">INCS_MLS - Liberal Studies</option>
            
        
            
                <option value="INCS_MSE - Material Science &amp; Engineering">INCS_MSE - Material Science &amp; Engineering</option>
            
        
            
                <option value="INCS_MUS - Music">INCS_MUS - Music</option>
            
        
            
                <option value="INCS_NE - Nuclear Engineering">INCS_NE - Nuclear Engineering</option>
            
        
            
                <option value="INCS_NR - Natural Resources">INCS_NR - Natural Resources</option>
            
        
            
                <option value="INCS_NTR - Nutrition">INCS_NTR - Nutrition</option>
            
        
            
                <option value="INCS_OR - Operations Research">INCS_OR - Operations Research</option>
            
        
            
                <option value="INCS_PA - Public Administration">INCS_PA - Public Administration</option>
            
        
            
                <option value="INCS_PRT - Parks, Rec &amp;Tourism Management">INCS_PRT - Parks, Rec &amp;Tourism Management</option>
            
        
            
                <option value="INCS_PS - Political Science">INCS_PS - Political Science</option>
            
        
            
                <option value="INCS_PSY - Psychology">INCS_PSY - Psychology</option>
            
        
            
                <option value="INCS_PY - Physics">INCS_PY - Physics</option>
            
        
            
                <option value="INCS_REL - Religion">INCS_REL - Religion</option>
            
        
            
                <option value="INCS_SOC - Sociology">INCS_SOC - Sociology</option>
            
        
            
                <option value="INCS_SSC - Soil Science">INCS_SSC - Soil Science</option>
            
        
            
                <option value="INCS_ST - Statistics">INCS_ST - Statistics</option>
            
        
            
                <option value="INCS_TTM - Textile Technology Management">INCS_TTM - Textile Technology Management</option>
            
        
            
                <option value="INCS_VMP - Veterinary Science">INCS_VMP - Veterinary Science</option>
            
        
            
                <option value="INCS_WGS - Women's and Gender Studies">INCS_WGS - Women's and Gender Studies</option>
            
        
            
                <option value="INCS_ZOO - Zoology">INCS_ZOO - Zoology</option>
            
        
            
                <option value="INCU_ACC - Accounting">INCU_ACC - Accounting</option>
            
        
            
                <option value="INCU_ART - Art">INCU_ART - Art</option>
            
        
            
                <option value="INCU_BIO - Biology">INCU_BIO - Biology</option>
            
        
            
                <option value="INCU_CHM - Chemistry">INCU_CHM - Chemistry</option>
            
        
            
                <option value="INCU_CRJ - Criminal Justice">INCU_CRJ - Criminal Justice</option>
            
        
            
                <option value="INCU_CS - Computer Science">INCU_CS - Computer Science</option>
            
        
            
                <option value="INCU_DRA - Drama">INCU_DRA - Drama</option>
            
        
            
                <option value="INCU_ECO - Economics">INCU_ECO - Economics</option>
            
        
            
                <option value="INCU_ENG - English">INCU_ENG - English</option>
            
        
            
                <option value="INCU_FDN - Foods &amp; Nutrition">INCU_FDN - Foods &amp; Nutrition</option>
            
        
            
                <option value="INCU_FDS - Foods &amp; Nutrition">INCU_FDS - Foods &amp; Nutrition</option>
            
        
            
                <option value="INCU_GER - German">INCU_GER - German</option>
            
        
            
                <option value="INCU_HST - History">INCU_HST - History</option>
            
        
            
                <option value="INCU_LAW - Law">INCU_LAW - Law</option>
            
        
            
                <option value="INCU_MAT - Mathematics">INCU_MAT - Mathematics</option>
            
        
            
                <option value="INCU_MSC - Mass Communication">INCU_MSC - Mass Communication</option>
            
        
            
                <option value="INCU_MUS - Music">INCU_MUS - Music</option>
            
        
            
                <option value="INCU_PAD - Public Administration">INCU_PAD - Public Administration</option>
            
        
            
                <option value="INCU_PED - Physical Education">INCU_PED - Physical Education</option>
            
        
            
                <option value="INCU_PHY - Physics">INCU_PHY - Physics</option>
            
        
            
                <option value="INCU_PSY - Psychology">INCU_PSY - Psychology</option>
            
        
            
                <option value="INCU_SLD - Speech &amp; Language Disorders">INCU_SLD - Speech &amp; Language Disorders</option>
            
        
            
                <option value="INCU_SOC - Sociology">INCU_SOC - Sociology</option>
            
        
            
                <option value="IND - Interdisciplinary">IND - Interdisciplinary</option>
            
        
            
                <option value="INT - Internship">INT - Internship</option>
            
        
            
                <option value="INTERDIS - Interdisciplinary">INTERDIS - Interdisciplinary</option>
            
        
            
                <option value="INTERN - Internship">INTERN - Internship</option>
            
        
            
                <option value="INTERSES - INTERSESSION">INTERSES - INTERSESSION</option>
            
        
            
                <option value="INYU_AAL - INYU_AAL (Taught at NYU)">INYU_AAL - INYU_AAL (Taught at NYU)</option>
            
        
            
                <option value="INYU_AL - INYU_AL (Taught at NYU)">INYU_AL - INYU_AL (Taught at NYU)</option>
            
        
            
                <option value="INYU_AMI - INYU_AMI (Taught at NYU)">INYU_AMI - INYU_AMI (Taught at NYU)</option>
            
        
            
                <option value="INYU_AN - INYU_ANTHROPOL (Taught at NYU)">INYU_AN - INYU_ANTHROPOL (Taught at NYU)</option>
            
        
            
                <option value="INYU_ARB - INYU_ARB (Taught at NYU)">INYU_ARB - INYU_ARB (Taught at NYU)</option>
            
        
            
                <option value="INYU_ARH - INYU_ARH (Taught at NYU)">INYU_ARH - INYU_ARH (Taught at NYU)</option>
            
        
            
                <option value="INYU_ART - INYU_ART (Taught at NYU)">INYU_ART - INYU_ART (Taught at NYU)</option>
            
        
            
                <option value="INYU_ARV - INYU_ARV (Taught at NYU)">INYU_ARV - INYU_ARV (Taught at NYU)</option>
            
        
            
                <option value="INYU_AS - INYU_AFR STUDIES (Tght at NYU)">INYU_AS - INYU_AFR STUDIES (Tght at NYU)</option>
            
        
            
                <option value="INYU_BIO - INYU_BIO (Taught at NYU)">INYU_BIO - INYU_BIO (Taught at NYU)</option>
            
        
            
                <option value="INYU_BUS - INYU_BUS (Taught at NYU)">INYU_BUS - INYU_BUS (Taught at NYU)</option>
            
        
            
                <option value="INYU_CA - INYU_CA (Taught at NYU)">INYU_CA - INYU_CA (Taught at NYU)</option>
            
        
            
                <option value="INYU_CIN - INYU_CIN (Taught at NYU)">INYU_CIN - INYU_CIN (Taught at NYU)</option>
            
        
            
                <option value="INYU_CL - INYU_CL (Taught at NYU)">INYU_CL - INYU_CL (Taught at NYU)</option>
            
        
            
                <option value="INYU_CLS - INYU_CLASSICS (Taught at NYU)">INYU_CLS - INYU_CLASSICS (Taught at NYU)</option>
            
        
            
                <option value="INYU_CRW - INYU_CRW (Taught at NYU)">INYU_CRW - INYU_CRW (Taught at NYU)</option>
            
        
            
                <option value="INYU_CS - INYU_CS (Taught at NYU)">INYU_CS - INYU_CS (Taught at NYU)</option>
            
        
            
                <option value="INYU_DAN - INYU_DAN (Taught at NYU)">INYU_DAN - INYU_DAN (Taught at NYU)</option>
            
        
            
                <option value="INYU_DOC - INYU_DOC ST(Taught at NYU)">INYU_DOC - INYU_DOC ST(Taught at NYU)</option>
            
        
            
                <option value="INYU_DRL - INYU_DRL(Taught at NYU)">INYU_DRL - INYU_DRL(Taught at NYU)</option>
            
        
            
                <option value="INYU_ECN - INYU_ECN (Taught at NYU)">INYU_ECN - INYU_ECN (Taught at NYU)</option>
            
        
            
                <option value="INYU_ECO - INYU_ECO (Taught at NYU)">INYU_ECO - INYU_ECO (Taught at NYU)</option>
            
        
            
                <option value="INYU_EDU - INYU_EDU (Taught at NYU)">INYU_EDU - INYU_EDU (Taught at NYU)</option>
            
        
            
                <option value="INYU_ENG - INYU_ENG (Taught at NYU)">INYU_ENG - INYU_ENG (Taught at NYU)</option>
            
        
            
                <option value="INYU_ENV - INYU_ENV  (Taught at NYU)">INYU_ENV - INYU_ENV  (Taught at NYU)</option>
            
        
            
                <option value="INYU_FLM - INYU_FLM (Taught at NYU)">INYU_FLM - INYU_FLM (Taught at NYU)</option>
            
        
            
                <option value="INYU_FMI - INYU_FMI (Taught at NYU)">INYU_FMI - INYU_FMI (Taught at NYU)</option>
            
        
            
                <option value="INYU_FRN - INYU_FRN (Taught at NYU)">INYU_FRN - INYU_FRN (Taught at NYU)</option>
            
        
            
                <option value="INYU_FVD - INYU_FVD (Taught at NYU)">INYU_FVD - INYU_FVD (Taught at NYU)</option>
            
        
            
                <option value="INYU_GER - INYU_GER (Taught at NYU)">INYU_GER - INYU_GER (Taught at NYU)</option>
            
        
            
                <option value="INYU_GL - INTERMEDIATE GERMAN III">INYU_GL - INTERMEDIATE GERMAN III</option>
            
        
            
                <option value="INYU_GRK - INYU_GRK (Taught at NYU)">INYU_GRK - INYU_GRK (Taught at NYU)</option>
            
        
            
                <option value="INYU_GRL - GERMAN LANGUAGE/LITERATURE">INYU_GRL - GERMAN LANGUAGE/LITERATURE</option>
            
        
            
                <option value="INYU_HEB - INYU_HEB (Taught at NYU)">INYU_HEB - INYU_HEB (Taught at NYU)</option>
            
        
            
                <option value="INYU_HST - INYU_HST (Taught at NYU)">INYU_HST - INYU_HST (Taught at NYU)</option>
            
        
            
                <option value="INYU_IP - INYU_IP (Taught at NYU)">INYU_IP - INYU_IP (Taught at NYU)</option>
            
        
            
                <option value="INYU_IT - INYU_ITALIAN(Taught at NYU)">INYU_IT - INYU_ITALIAN(Taught at NYU)</option>
            
        
            
                <option value="INYU_ITL - INYU_ITL (Taught at NYU)">INYU_ITL - INYU_ITL (Taught at NYU)</option>
            
        
            
                <option value="INYU_JL - INYU_JL (Taught at NYU)">INYU_JL - INYU_JL (Taught at NYU)</option>
            
        
            
                <option value="INYU_JRL - INYU_JRL (Taught at NYU)">INYU_JRL - INYU_JRL (Taught at NYU)</option>
            
        
            
                <option value="INYU_JRN - INYU_JRNALISM (Taught at NYU)">INYU_JRN - INYU_JRNALISM (Taught at NYU)</option>
            
        
            
                <option value="INYU_LAS - INYU_LAS (Taught at NYU)">INYU_LAS - INYU_LAS (Taught at NYU)</option>
            
        
            
                <option value="INYU_LAW - INYU_LAW (Taught at NYU)">INYU_LAW - INYU_LAW (Taught at NYU)</option>
            
        
            
                <option value="INYU_LIN - INYU_LIN (Taught at NYU)">INYU_LIN - INYU_LIN (Taught at NYU)</option>
            
        
            
                <option value="INYU_LIT - INYU_LIT (Taught at NYU)">INYU_LIT - INYU_LIT (Taught at NYU)</option>
            
        
            
                <option value="INYU_MES - INYU_MES (Taught at NYU)">INYU_MES - INYU_MES (Taught at NYU)</option>
            
        
            
                <option value="INYU_MET - INYU_METRO ST (Taught at NYU)">INYU_MET - INYU_METRO ST (Taught at NYU)</option>
            
        
            
                <option value="INYU_MJL - INYU_MJL">INYU_MJL - INYU_MJL</option>
            
        
            
                <option value="INYU_MMS - INYU_MMS (Taught at NYU)">INYU_MMS - INYU_MMS (Taught at NYU)</option>
            
        
            
                <option value="INYU_MTH - INYU_MTH (Taught at NYU)">INYU_MTH - INYU_MTH (Taught at NYU)</option>
            
        
            
                <option value="INYU_MUS - INYU_MUS (Taught at NYU)">INYU_MUS - INYU_MUS (Taught at NYU)</option>
            
        
            
                <option value="INYU_NSC - INYU_NSC (Taught at NYU)">INYU_NSC - INYU_NSC (Taught at NYU)</option>
            
        
            
                <option value="INYU_OAR - INYU_OAR(Taught at NYU)">INYU_OAR - INYU_OAR(Taught at NYU)</option>
            
        
            
                <option value="INYU_PHE - INYU_PHYSEDU (Taught at NYU)">INYU_PHE - INYU_PHYSEDU (Taught at NYU)</option>
            
        
            
                <option value="INYU_PHL - INYU_PHL (Taught at NYU)">INYU_PHL - INYU_PHL (Taught at NYU)</option>
            
        
            
                <option value="INYU_PJ - INYU_PJ (Taught at NYU)">INYU_PJ - INYU_PJ (Taught at NYU)</option>
            
        
            
                <option value="INYU_PPS - INYU_PUBPOL (Taught at NYU)">INYU_PPS - INYU_PUBPOL (Taught at NYU)</option>
            
        
            
                <option value="INYU_PS - INYU_PS (Taught at NYU)">INYU_PS - INYU_PS (Taught at NYU)</option>
            
        
            
                <option value="INYU_PSY - INYU_PSY (Taught at NYU)">INYU_PSY - INYU_PSY (Taught at NYU)</option>
            
        
            
                <option value="INYU_PTG - INYU_PTG (Taught at NYU)">INYU_PTG - INYU_PTG (Taught at NYU)</option>
            
        
            
                <option value="INYU_REL - INYU_REL (Taught at NYU)">INYU_REL - INYU_REL (Taught at NYU)</option>
            
        
            
                <option value="INYU_RS - ROMANCE STUDIES">INYU_RS - ROMANCE STUDIES</option>
            
        
            
                <option value="INYU_SEM - INYU_SEM (Taught at NYU)">INYU_SEM - INYU_SEM (Taught at NYU)</option>
            
        
            
                <option value="INYU_SOC - INYU_SOC (Taught at NYU)">INYU_SOC - INYU_SOC (Taught at NYU)</option>
            
        
            
                <option value="INYU_SP - INYU_SPANISH (Taught at NYU)">INYU_SP - INYU_SPANISH (Taught at NYU)</option>
            
        
            
                <option value="INYU_STA - INYU_STA (Taught at NYU)">INYU_STA - INYU_STA (Taught at NYU)</option>
            
        
            
                <option value="INYU_SXL - INYU_SXL (Taught at NYU)">INYU_SXL - INYU_SXL (Taught at NYU)</option>
            
        
            
                <option value="INYU_THS - INYU_THS (Taught at NYU)">INYU_THS - INYU_THS (Taught at NYU)</option>
            
        
            
                <option value="INYU_TS - INYU-TS(Taught at NYU)">INYU_TS - INYU-TS(Taught at NYU)</option>
            
        
            
                <option value="INYU_VMS - INYU_VMS (Taught at NYU)">INYU_VMS - INYU_VMS (Taught at NYU)</option>
            
        
            
                <option value="INYU_WST - INYU_WST (Taught at NYU)">INYU_WST - INYU_WST (Taught at NYU)</option>
            
        
            
                <option value="ISIS - Inf Science and Inf Studies">ISIS - Inf Science and Inf Studies</option>
            
        
            
                <option value="ISP - Immunology Study Program">ISP - Immunology Study Program</option>
            
        
            
                <option value="ISS - Information Science + Studies">ISS - Information Science + Studies</option>
            
        
            
                <option value="ITALIAN - Italian">ITALIAN - Italian</option>
            
        
            
                <option value="IUSC-PSY - IUSC_PSYC (Taught at USC)">IUSC-PSY - IUSC_PSYC (Taught at USC)</option>
            
        
            
                <option value="IUSC_AME - IUSC_AME (Taught at USC)">IUSC_AME - IUSC_AME (Taught at USC)</option>
            
        
            
                <option value="IUSC_AMI - IUSC_AMI (Taught at USC)">IUSC_AMI - IUSC_AMI (Taught at USC)</option>
            
        
            
                <option value="IUSC_CE - IUSC_CE (Taught at USC)">IUSC_CE - IUSC_CE (Taught at USC)</option>
            
        
            
                <option value="IUSC_COM - IUSC_COM (Taught at USC)">IUSC_COM - IUSC_COM (Taught at USC)</option>
            
        
            
                <option value="IUSC_CSC - IUSC_CSC (Taught at USC)">IUSC_CSC - IUSC_CSC (Taught at USC)</option>
            
        
            
                <option value="IUSC_CTA - IUSC_CTA (Taught at USC)">IUSC_CTA - IUSC_CTA (Taught at USC)</option>
            
        
            
                <option value="IUSC_CTC - IUSC_CTC (Taught at USC)">IUSC_CTC - IUSC_CTC (Taught at USC)</option>
            
        
            
                <option value="IUSC_CTP - IUSC_CTP (Taught at USC)">IUSC_CTP - IUSC_CTP (Taught at USC)</option>
            
        
            
                <option value="IUSC_CTV - IUSC_CTV (Taught at USC)">IUSC_CTV - IUSC_CTV (Taught at USC)</option>
            
        
            
                <option value="IUSC_CTW - IUSC_CTW (Taught at USC)">IUSC_CTW - IUSC_CTW (Taught at USC)</option>
            
        
            
                <option value="IUSC_FA - IUSC_FA (Taught at USC)">IUSC_FA - IUSC_FA (Taught at USC)</option>
            
        
            
                <option value="IUSC_FVD - IUSC_FVD (Taught at USC)">IUSC_FVD - IUSC_FVD (Taught at USC)</option>
            
        
            
                <option value="IUSC_JRN - IUSC_JRN (Taught at USC)">IUSC_JRN - IUSC_JRN (Taught at USC)</option>
            
        
            
                <option value="IUSC_LIT - IUSC_LIT (Taught at USC)">IUSC_LIT - IUSC_LIT (Taught at USC)</option>
            
        
            
                <option value="IUSC_MUI - IUSC_MUI (Taught at USC)">IUSC_MUI - IUSC_MUI (Taught at USC)</option>
            
        
            
                <option value="IUSC_MUS - IUSC_MUS (Taught at USC)">IUSC_MUS - IUSC_MUS (Taught at USC)</option>
            
        
            
                <option value="IUSC_PE - IUSC_PE (Tuahgt at USC)">IUSC_PE - IUSC_PE (Tuahgt at USC)</option>
            
        
            
                <option value="IUSC_PJM - IUSC_PJMS (Taught at USC)">IUSC_PJM - IUSC_PJMS (Taught at USC)</option>
            
        
            
                <option value="IUSC_PPS - IUSC_PPS (Taught at USC)">IUSC_PPS - IUSC_PPS (Taught at USC)</option>
            
        
            
                <option value="IUSC_PS - IUSC_PS (Taught at USC)">IUSC_PS - IUSC_PS (Taught at USC)</option>
            
        
            
                <option value="IUSC_SOC - IUSC_SOC (Taught at USC)">IUSC_SOC - IUSC_SOC (Taught at USC)</option>
            
        
            
                <option value="IUSC_THT - IUSC_THT (Taught  at USC)">IUSC_THT - IUSC_THT (Taught  at USC)</option>
            
        
            
                <option value="IUSC_VIS - IUSC_ARTSVIS (Taught at USC)">IUSC_VIS - IUSC_ARTSVIS (Taught at USC)</option>
            
        
            
                <option value="JEWISHST - Jewish Studies">JEWISHST - Jewish Studies</option>
            
        
            
                <option value="JGER_ART - Art">JGER_ART - Art</option>
            
        
            
                <option value="JGER_CMM - Communication Studies">JGER_CMM - Communication Studies</option>
            
        
            
                <option value="JGER_CPL - Comparative Literature">JGER_CPL - Comparative Literature</option>
            
        
            
                <option value="JGER_CZH - Czech">JGER_CZH - Czech</option>
            
        
            
                <option value="JGER_ENG - English">JGER_ENG - English</option>
            
        
            
                <option value="JGER_FRE - French">JGER_FRE - French</option>
            
        
            
                <option value="JGER_GEG - Geography">JGER_GEG - Geography</option>
            
        
            
                <option value="JGER_GER - German">JGER_GER - German</option>
            
        
            
                <option value="JGER_GRK - Greek">JGER_GRK - Greek</option>
            
        
            
                <option value="JGER_HST - History">JGER_HST - History</option>
            
        
            
                <option value="JGER_JWS - Jewish Studies">JGER_JWS - Jewish Studies</option>
            
        
            
                <option value="JGER_LAT - Latin">JGER_LAT - Latin</option>
            
        
            
                <option value="JGER_LAW - Law">JGER_LAW - Law</option>
            
        
            
                <option value="JGER_PHA - Physical Activities">JGER_PHA - Physical Activities</option>
            
        
            
                <option value="JGER_PHL - Philosophy">JGER_PHL - Philosophy</option>
            
        
            
                <option value="JGER_PLN - City and Regional Planning">JGER_PLN - City and Regional Planning</option>
            
        
            
                <option value="JGER_PLS - Polish">JGER_PLS - Polish</option>
            
        
            
                <option value="JGER_REL - Religion">JGER_REL - Religion</option>
            
        
            
                <option value="JGER_SLV - Slavic Languages">JGER_SLV - Slavic Languages</option>
            
        
            
                <option value="JGER_SOC - Sociology">JGER_SOC - Sociology</option>
            
        
            
                <option value="JGER_WST - Women's Studies">JGER_WST - Women's Studies</option>
            
        
            
                <option value="JPN - Japanese">JPN - Japanese</option>
            
        
            
                <option value="KICHE - K’iche Mayan">KICHE - K’iche Mayan</option>
            
        
            
                <option value="KOREAN - Korean">KOREAN - Korean</option>
            
        
            
                <option value="LATAMER - Latin American Studies">LATAMER - Latin American Studies</option>
            
        
            
                <option value="LATIN - Latin">LATIN - Latin</option>
            
        
            
                <option value="LAW - Law">LAW - Law</option>
            
        
            
                <option value="LIBRARY - LIBRARY">LIBRARY - LIBRARY</option>
            
        
            
                <option value="LINGUIST - Linguistics">LINGUIST - Linguistics</option>
            
        
            
                <option value="LIT - Literature">LIT - Literature</option>
            
        
            
                <option value="LS - Liberal Studies">LS - Liberal Studies</option>
            
        
            
                <option value="LSGS - Latino Studies Global South">LSGS - Latino Studies Global South</option>
            
        
            
                <option value="LTS - Liturgical Studies">LTS - Liturgical Studies</option>
            
        
            
                <option value="MALS - Liberal Studies">MALS - Liberal Studies</option>
            
        
            
                <option value="MANAGEMT - Management">MANAGEMT - Management</option>
            
        
            
                <option value="MARKETNG - Marketing">MARKETNG - Marketing</option>
            
        
            
                <option value="MAT - Master of Arts in Teaching">MAT - Master of Arts in Teaching</option>
            
        
            
                <option value="MATH - Mathematics">MATH - Mathematics</option>
            
        
            
                <option value="MBP - Molecular Biophysics">MBP - Molecular Biophysics</option>
            
        
            
                <option value="MBS - Modeling Biological Systems">MBS - Modeling Biological Systems</option>
            
        
            
                <option value="MCH - MCH">MCH - MCH</option>
            
        
            
                <option value="MDP - Molecular Development">MDP - Molecular Development</option>
            
        
            
                <option value="ME - Mechanical Engr/Materials Sci">ME - Mechanical Engr/Materials Sci</option>
            
        
            
                <option value="MEDHUM - Medical Humanities Study Progr">MEDHUM - Medical Humanities Study Progr</option>
            
        
            
                <option value="MEDICINE - Medicine">MEDICINE - Medicine</option>
            
        
            
                <option value="MEDINFO - Medical Information Sciences">MEDINFO - Medical Information Sciences</option>
            
        
            
                <option value="MEDPHY - Medical Physics">MEDPHY - Medical Physics</option>
            
        
            
                <option value="MEDREN - Medieval and Renaissance">MEDREN - Medieval and Renaissance</option>
            
        
            
                <option value="MENG - Master of Engineering">MENG - Master of Engineering</option>
            
        
            
                <option value="MFAEDA - MFA in Experimental &amp; Doc Arts">MFAEDA - MFA in Experimental &amp; Doc Arts</option>
            
        
            
                <option value="MGM - Molec Genetics &amp; Microbiology">MGM - Molec Genetics &amp; Microbiology</option>
            
        
            
                <option value="MGMTCOM - Management Communications">MGMTCOM - Management Communications</option>
            
        
            
                <option value="MGP - Medical Genomics">MGP - Medical Genomics</option>
            
        
            
                <option value="MGRECON - Economics">MGRECON - Economics</option>
            
        
            
                <option value="MICROBIO - Microbiology">MICROBIO - Microbiology</option>
            
        
            
                <option value="MIDIP - MIDIP">MIDIP - MIDIP</option>
            
        
            
                <option value="MIDP - Micro and Infect Disease">MIDP - Micro and Infect Disease</option>
            
        
            
                <option value="MILITSCI - Military Science (Army ROTC)">MILITSCI - Military Science (Army ROTC)</option>
            
        
            
                <option value="MIS - Medical Information Sciences">MIS - Medical Information Sciences</option>
            
        
            
                <option value="MMCI - Mstrs in Manage in Cln Info">MMCI - Mstrs in Manage in Cln Info</option>
            
        
            
                <option value="MMS - Markets and Management Studies">MMS - Markets and Management Studies</option>
            
        
            
                <option value="MOLBPHY - Molecular Biophysics">MOLBPHY - Molecular Biophysics</option>
            
        
            
                <option value="MOLCAN - Molecular Cancer Biology">MOLCAN - Molecular Cancer Biology</option>
            
        
            
                <option value="MOLMED - Molecular Medicine">MOLMED - Molecular Medicine</option>
            
        
            
                <option value="MPS - MPS">MPS - MPS</option>
            
        
            
                <option value="MSIS - M of Sci of Info Sci Study Pro">MSIS - M of Sci of Info Sci Study Pro</option>
            
        
            
                <option value="MSLS - M of Sci of Lib Sci Study Pro">MSLS - M of Sci of Lib Sci Study Pro</option>
            
        
            
                <option value="MUSIC - Music">MUSIC - Music</option>
            
        
            
                <option value="NANOSCI - Nanosciences">NANOSCI - Nanosciences</option>
            
        
            
                <option value="NAVALSCI - Naval Science (Navy ROTC)">NAVALSCI - Naval Science (Navy ROTC)</option>
            
        
            
                <option value="NBP - Neurobiology Study Program">NBP - Neurobiology Study Program</option>
            
        
            
                <option value="NCS - Nonlinear and Complex Systems">NCS - Nonlinear and Complex Systems</option>
            
        
            
                <option value="NEURO - Neurology">NEURO - Neurology</option>
            
        
            
                <option value="NEUROBIO - Neurobiology">NEUROBIO - Neurobiology</option>
            
        
            
                <option value="NEUROSCI - Neuroscience">NEUROSCI - Neuroscience</option>
            
        
            
                <option value="NEUROSUR - Neurosurgery">NEUROSUR - Neurosurgery</option>
            
        
            
                <option value="NEWTEST - New Testament">NEWTEST - New Testament</option>
            
        
            
                <option value="NORTAMER - North American Studies">NORTAMER - North American Studies</option>
            
        
            
                <option value="NSS - Neurosciences Study Program">NSS - Neurosciences Study Program</option>
            
        
            
                <option value="NURSING - Nursing">NURSING - Nursing</option>
            
        
            
                <option value="OBG - Obstetrics and Gynecology">OBG - Obstetrics and Gynecology</option>
            
        
            
                <option value="OBGYN - Obstetrics and Gynecology">OBGYN - Obstetrics and Gynecology</option>
            
        
            
                <option value="OCR - Online Core-Clinical Research">OCR - Online Core-Clinical Research</option>
            
        
            
                <option value="OLDTEST - Old Testament">OLDTEST - Old Testament</option>
            
        
            
                <option value="OPERATNS - Operations">OPERATNS - Operations</option>
            
        
            
                <option value="OPHTHAL - Ophthalmology">OPHTHAL - Ophthalmology</option>
            
        
            
                <option value="OPTECH - Ophthalmic Medical Technician">OPTECH - Ophthalmic Medical Technician</option>
            
        
            
                <option value="OPTRS - Optional Research Studies">OPTRS - Optional Research Studies</option>
            
        
            
                <option value="ORTHO - Orthopaedics">ORTHO - Orthopaedics</option>
            
        
            
                <option value="OVS - Ophthalmology/Visual Sci St Pr">OVS - Ophthalmology/Visual Sci St Pr</option>
            
        
            
                <option value="PAP - Physician Assistant Program">PAP - Physician Assistant Program</option>
            
        
            
                <option value="PARISH - Care of Parish">PARISH - Care of Parish</option>
            
        
            
                <option value="PASHTO - Pashto">PASHTO - Pashto</option>
            
        
            
                <option value="PASTCARE - Pastoral Care">PASTCARE - Pastoral Care</option>
            
        
            
                <option value="PATHASST - Pathologist's Assistant Progr">PATHASST - Pathologist's Assistant Progr</option>
            
        
            
                <option value="PATHOL - Pathology">PATHOL - Pathology</option>
            
        
            
                <option value="PCLT - Primary Care Leadership Track">PCLT - Primary Care Leadership Track</option>
            
        
            
                <option value="PEDS - Pediatrics">PEDS - Pediatrics</option>
            
        
            
                <option value="PERSIAN - Persian">PERSIAN - Persian</option>
            
        
            
                <option value="PHARM - Pharm and Cancer Biology">PHARM - Pharm and Cancer Biology</option>
            
        
            
                <option value="PHIL - Philosophy">PHIL - Philosophy</option>
            
        
            
                <option value="PHYASST - Physician Assistant Program">PHYASST - Physician Assistant Program</option>
            
        
            
                <option value="PHYSEDU - Physical Education">PHYSEDU - Physical Education</option>
            
        
            
                <option value="PHYSICS - Physics">PHYSICS - Physics</option>
            
        
            
                <option value="PJMS - Policy Journalism and Media St">PJMS - Policy Journalism and Media St</option>
            
        
            
                <option value="PMT - Pharm &amp; Molecular Therapeutics">PMT - Pharm &amp; Molecular Therapeutics</option>
            
        
            
                <option value="POE - Practice-Oriented Education">POE - Practice-Oriented Education</option>
            
        
            
                <option value="POLISH - Polish">POLISH - Polish</option>
            
        
            
                <option value="POLSCI - Political Science">POLSCI - Political Science</option>
            
        
            
                <option value="POPHS - Population Health Sciences">POPHS - Population Health Sciences</option>
            
        
            
                <option value="PORTUGUE - Portuguese">PORTUGUE - Portuguese</option>
            
        
            
                <option value="PPE - Philosophy, Politics, and Econ">PPE - Philosophy, Politics, and Econ</option>
            
        
            
                <option value="PREACHNG - Preaching">PREACHNG - Preaching</option>
            
        
            
                <option value="PRIMATOL - Primatology">PRIMATOL - Primatology</option>
            
        
            
                <option value="PSC - Psychiatry">PSC - Psychiatry</option>
            
        
            
                <option value="PSP - Pathology Study Program">PSP - Pathology Study Program</option>
            
        
            
                <option value="PSY - Psychology">PSY - Psychology</option>
            
        
            
                <option value="PSYCHTRY - Psychiatry">PSYCHTRY - Psychiatry</option>
            
        
            
                <option value="PT - Physical Therapy">PT - Physical Therapy</option>
            
        
            
                <option value="PT-D - Physical Therapy - Doctorate">PT-D - Physical Therapy - Doctorate</option>
            
        
            
                <option value="PTA - Pathologist's Assistant Prgm">PTA - Pathologist's Assistant Prgm</option>
            
        
            
                <option value="PTH - Pathology">PTH - Pathology</option>
            
        
            
                <option value="PUBPOL - Public Policy">PUBPOL - Public Policy</option>
            
        
            
                <option value="QM - Quantitative Management">QM - Quantitative Management</option>
            
        
            
                <option value="QUECHUA - Quechua">QUECHUA - Quechua</option>
            
        
            
                <option value="R0BT_REL - ROBT_REL">R0BT_REL - ROBT_REL</option>
            
        
            
                <option value="RAD - Radiology">RAD - Radiology</option>
            
        
            
                <option value="RADIOL - Radiology">RADIOL - Radiology</option>
            
        
            
                <option value="RADONC - Radiation Oncology">RADONC - Radiation Oncology</option>
            
        
            
                <option value="REG - Registration">REG - Registration</option>
            
        
            
                <option value="RELIGION - Religion">RELIGION - Religion</option>
            
        
            
                <option value="RESEARCH - Research">RESEARCH - Research</option>
            
        
            
                <option value="RIGHTS - Human Rights">RIGHTS - Human Rights</option>
            
        
            
                <option value="ROBT_AAD - Afri, Afri-Amer, Diaspora Stds">ROBT_AAD - Afri, Afri-Amer, Diaspora Stds</option>
            
        
            
                <option value="ROBT_AFM - African American Studies">ROBT_AFM - African American Studies</option>
            
        
            
                <option value="ROBT_AFR - African Studies">ROBT_AFR - African Studies</option>
            
        
            
                <option value="ROBT_AMT - American Studies">ROBT_AMT - American Studies</option>
            
        
            
                <option value="ROBT_ANT - Anthropology">ROBT_ANT - Anthropology</option>
            
        
            
                <option value="ROBT_APL - Applied Sciences">ROBT_APL - Applied Sciences</option>
            
        
            
                <option value="ROBT_ARB - Arabic">ROBT_ARB - Arabic</option>
            
        
            
                <option value="ROBT_ARH - Art History">ROBT_ARH - Art History</option>
            
        
            
                <option value="ROBT_ART - Art">ROBT_ART - Art</option>
            
        
            
                <option value="ROBT_ARV - ARTS VIS">ROBT_ARV - ARTS VIS</option>
            
        
            
                <option value="ROBT_ASA - Asian Studies">ROBT_ASA - Asian Studies</option>
            
        
            
                <option value="ROBT_AST - Astronomy">ROBT_AST - Astronomy</option>
            
        
            
                <option value="ROBT_BIO - Biology">ROBT_BIO - Biology</option>
            
        
            
                <option value="ROBT_BST - Biostatistics">ROBT_BST - Biostatistics</option>
            
        
            
                <option value="ROBT_BUS - Business">ROBT_BUS - Business</option>
            
        
            
                <option value="ROBT_CDF - ROBT_CDF">ROBT_CDF - ROBT_CDF</option>
            
        
            
                <option value="ROBT_CHM - Chemistry">ROBT_CHM - Chemistry</option>
            
        
            
                <option value="ROBT_CHN - Chinese">ROBT_CHN - Chinese</option>
            
        
            
                <option value="ROBT_CLA - Classics">ROBT_CLA - Classics</option>
            
        
            
                <option value="ROBT_CLR - Classical Archeology">ROBT_CLR - Classical Archeology</option>
            
        
            
                <option value="ROBT_CML - Comparative Literature">ROBT_CML - Comparative Literature</option>
            
        
            
                <option value="ROBT_COM - Communications">ROBT_COM - Communications</option>
            
        
            
                <option value="ROBT_CPS - Computer Science">ROBT_CPS - Computer Science</option>
            
        
            
                <option value="ROBT_DRA - Drama">ROBT_DRA - Drama</option>
            
        
            
                <option value="ROBT_ECO - Economics">ROBT_ECO - Economics</option>
            
        
            
                <option value="ROBT_EDU - Education">ROBT_EDU - Education</option>
            
        
            
                <option value="ROBT_ENE - Environment &amp; Ecology">ROBT_ENE - Environment &amp; Ecology</option>
            
        
            
                <option value="ROBT_ENG - English">ROBT_ENG - English</option>
            
        
            
                <option value="ROBT_ENS - Environmental Studies">ROBT_ENS - Environmental Studies</option>
            
        
            
                <option value="ROBT_ENV - Environment Sciences">ROBT_ENV - Environment Sciences</option>
            
        
            
                <option value="ROBT_EPD - Epidemiology">ROBT_EPD - Epidemiology</option>
            
        
            
                <option value="ROBT_ESS - Exercise and Sport Science">ROBT_ESS - Exercise and Sport Science</option>
            
        
            
                <option value="ROBT_FOL - Folklore">ROBT_FOL - Folklore</option>
            
        
            
                <option value="ROBT_FRE - French">ROBT_FRE - French</option>
            
        
            
                <option value="ROBT_GBS - Global Studies">ROBT_GBS - Global Studies</option>
            
        
            
                <option value="ROBT_GEG - Geography">ROBT_GEG - Geography</option>
            
        
            
                <option value="ROBT_GEO - Geology">ROBT_GEO - Geology</option>
            
        
            
                <option value="ROBT_GLB - GLOBAL ISSUES">ROBT_GLB - GLOBAL ISSUES</option>
            
        
            
                <option value="ROBT_GRK - Greek">ROBT_GRK - Greek</option>
            
        
            
                <option value="ROBT_GRM - German">ROBT_GRM - German</option>
            
        
            
                <option value="ROBT_HNR - Honors">ROBT_HNR - Honors</option>
            
        
            
                <option value="ROBT_HNU - Hindi/Urdu">ROBT_HNU - Hindi/Urdu</option>
            
        
            
                <option value="ROBT_HPA - Health Policy &amp; Administration">ROBT_HPA - Health Policy &amp; Administration</option>
            
        
            
                <option value="ROBT_HPM - Health Policy &amp; Management">ROBT_HPM - Health Policy &amp; Management</option>
            
        
            
                <option value="ROBT_HST - History">ROBT_HST - History</option>
            
        
            
                <option value="ROBT_IDS - Inter-disciplinary Studies">ROBT_IDS - Inter-disciplinary Studies</option>
            
        
            
                <option value="ROBT_ILS - Information &amp; Library Science">ROBT_ILS - Information &amp; Library Science</option>
            
        
            
                <option value="ROBT_INT - International Studies">ROBT_INT - International Studies</option>
            
        
            
                <option value="ROBT_ITA - Italian">ROBT_ITA - Italian</option>
            
        
            
                <option value="ROBT_LIN - Linguistics">ROBT_LIN - Linguistics</option>
            
        
            
                <option value="ROBT_LIT - Literature">ROBT_LIT - Literature</option>
            
        
            
                <option value="ROBT_LTM - Latin American Studies">ROBT_LTM - Latin American Studies</option>
            
        
            
                <option value="ROBT_MEJ - Media and Journalism">ROBT_MEJ - Media and Journalism</option>
            
        
            
                <option value="ROBT_MTH - Math">ROBT_MTH - Math</option>
            
        
            
                <option value="ROBT_MUS - Music">ROBT_MUS - Music</option>
            
        
            
                <option value="ROBT_NTR - Health Nutrition">ROBT_NTR - Health Nutrition</option>
            
        
            
                <option value="ROBT_PBH - Public Health">ROBT_PBH - Public Health</option>
            
        
            
                <option value="ROBT_PHA - Physical Activities">ROBT_PHA - Physical Activities</option>
            
        
            
                <option value="ROBT_PHL - Philosophy">ROBT_PHL - Philosophy</option>
            
        
            
                <option value="ROBT_PHY - Physics">ROBT_PHY - Physics</option>
            
        
            
                <option value="ROBT_PLN - City and Regional Planning">ROBT_PLN - City and Regional Planning</option>
            
        
            
                <option value="ROBT_POL - Political Science">ROBT_POL - Political Science</option>
            
        
            
                <option value="ROBT_PRT - Portuguese">ROBT_PRT - Portuguese</option>
            
        
            
                <option value="ROBT_PSY - Psychology">ROBT_PSY - Psychology</option>
            
        
            
                <option value="ROBT_PUB - Public Policy">ROBT_PUB - Public Policy</option>
            
        
            
                <option value="ROBT_PWD - Peace, War, &amp; Defense">ROBT_PWD - Peace, War, &amp; Defense</option>
            
        
            
                <option value="ROBT_REL - Religion">ROBT_REL - Religion</option>
            
        
            
                <option value="ROBT_RUS - Russian">ROBT_RUS - Russian</option>
            
        
            
                <option value="ROBT_SOC - Sociology">ROBT_SOC - Sociology</option>
            
        
            
                <option value="ROBT_SPA - Spanish">ROBT_SPA - Spanish</option>
            
        
            
                <option value="ROBT_SPC - Exp &amp; Spl Studies">ROBT_SPC - Exp &amp; Spl Studies</option>
            
        
            
                <option value="ROBT_SPH - Speech &amp; Hearing Sciences">ROBT_SPH - Speech &amp; Hearing Sciences</option>
            
        
            
                <option value="ROBT_STR - Stats &amp; Oprtns Resrch">ROBT_STR - Stats &amp; Oprtns Resrch</option>
            
        
            
                <option value="ROBT_SW - Social Work">ROBT_SW - Social Work</option>
            
        
            
                <option value="ROBT_SWA - Swahili">ROBT_SWA - Swahili</option>
            
        
            
                <option value="ROBT_VIT - Vietnamese">ROBT_VIT - Vietnamese</option>
            
        
            
                <option value="ROBT_WGS - Women's and Gender Studies">ROBT_WGS - Women's and Gender Studies</option>
            
        
            
                <option value="ROBT_WST - Women's Studies">ROBT_WST - Women's Studies</option>
            
        
            
                <option value="ROMANIAN - Romanian">ROMANIAN - Romanian</option>
            
        
            
                <option value="ROMLANG - Romance Languages">ROMLANG - Romance Languages</option>
            
        
            
                <option value="ROMST - Romance Studies">ROMST - Romance Studies</option>
            
        
            
                <option value="RON - Radiation Oncology">RON - Radiation Oncology</option>
            
        
            
                <option value="RROMP - Radiology, RadOnc &amp; Med Physic">RROMP - Radiology, RadOnc &amp; Med Physic</option>
            
        
            
                <option value="RUSSIAN - Russian">RUSSIAN - Russian</option>
            
        
            
                <option value="SANSKRIT - SANSKRIT">SANSKRIT - SANSKRIT</option>
            
        
            
                <option value="SAS - South Asian Studies">SAS - South Asian Studies</option>
            
        
            
                <option value="SBB - Structural Bio &amp; Biophysics">SBB - Structural Bio &amp; Biophysics</option>
            
        
            
                <option value="SCISOC - Science &amp; Society">SCISOC - Science &amp; Society</option>
            
        
            
                <option value="SERBCRO - Serbian and Croatian">SERBCRO - Serbian and Croatian</option>
            
        
            
                <option value="SES - Slavic and Eurasian Studies">SES - Slavic and Eurasian Studies</option>
            
        
            
                <option value="SIGNATUR - Arts and Sci Signature Courses">SIGNATUR - Arts and Sci Signature Courses</option>
            
        
            
                <option value="SOCENT - Social Entrepreneurship">SOCENT - Social Entrepreneurship</option>
            
        
            
                <option value="SOCIOL - Sociology">SOCIOL - Sociology</option>
            
        
            
                <option value="SPANISH - Spanish">SPANISH - Spanish</option>
            
        
            
                <option value="SPIRIT - Spirituality">SPIRIT - Spirituality</option>
            
        
            
                <option value="STA - Statistical Science">STA - Statistical Science</option>
            
        
            
                <option value="STDYAWAY - Study Away">STDYAWAY - Study Away</option>
            
        
            
                <option value="STHV - Science, Tech and Human Values">STHV - Science, Tech and Human Values</option>
            
        
            
                <option value="STRATEGY - Strategy">STRATEGY - Strategy</option>
            
        
            
                <option value="SUR - Surgery">SUR - Surgery</option>
            
        
            
                <option value="SURGERY - Surgery">SURGERY - Surgery</option>
            
        
            
                <option value="SUSTAIN - Sustainability Engagement">SUSTAIN - Sustainability Engagement</option>
            
        
            
                <option value="SXL - Study of Sexualities">SXL - Study of Sexualities</option>
            
        
            
                <option value="THEATRST - Theater Studies">THEATRST - Theater Studies</option>
            
        
            
                <option value="THESIS - Thesis">THESIS - Thesis</option>
            
        
            
                <option value="TIBETAN - Tibetan">TIBETAN - Tibetan</option>
            
        
            
                <option value="TM - Transfusion Med">TM - Transfusion Med</option>
            
        
            
                <option value="TRAN - Transfer courses">TRAN - Transfer courses</option>
            
        
            
                <option value="TURKISH - Turkish">TURKISH - Turkish</option>
            
        
            
                <option value="UKRAIN - Ukrainian">UKRAIN - Ukrainian</option>
            
        
            
                <option value="UPE - University Program in Ecology">UPE - University Program in Ecology</option>
            
        
            
                <option value="UPGEN - University Program in Genetics">UPGEN - University Program in Genetics</option>
            
        
            
                <option value="USC_POLS - Interinstitutional POLSCI">USC_POLS - Interinstitutional POLSCI</option>
            
        
            
                <option value="UZBEK - Uzbek">UZBEK - Uzbek</option>
            
        
            
                <option value="VISUALST - Visual Studies">VISUALST - Visual Studies</option>
            
        
            
                <option value="VMS - Visual and Media Studies">VMS - Visual and Media Studies</option>
            
        
            
                <option value="WBA - Weekend Business Admin">WBA - Weekend Business Admin</option>
            
        
            
                <option value="WRITING - Writing">WRITING - Writing</option>
            
        
            
                <option value="WXTIAN - World Christianity">WXTIAN - World Christianity</option>
            
        
            
                <option value="XTIANEDU - Christian Education">XTIANEDU - Christian Education</option>
            
        
            
                <option value="XTIANETH - Christian Ethics">XTIANETH - Christian Ethics</option>
            
        
            
                <option value="XTIANPRC - MA in Christian Practice">XTIANPRC - MA in Christian Practice</option>
            
        
            
                <option value="XTIANSTU - MA in Christian Studies">XTIANSTU - MA in Christian Studies</option>
            
        
            
                <option value="XTIANTHE - Christian Theology">XTIANTHE - Christian Theology</option>
            
        
            
                <option value="YIDDISH - Yiddish">YIDDISH - Yiddish</option>
            
        
            
                <option value="ZOOLOGY - Zoology">ZOOLOGY - Zoology</option>
            
        
            
                <option value="ZZZ - Duke Equivalent Transfer Cred">ZZZ - Duke Equivalent Transfer Cred</option>
            
        
    </select>"""
    
split = classes.split("\n")
ignorespaces = []
oldData = """
{'code': 'ARABIC', 'name': 'Arabic'}
{'code': 'ARTHIST', 'name': 'Art History'}
{'code': 'BIOCHEM', 'name': 'Biochemistry'}
{'code': 'BIOLOGY', 'name': 'Biology'}
{'code': 'BME', 'name': 'Biomedical Engineering'}
{'code': 'CEE', 'name': 'Civil and Environmental Egr'}
{'code': 'CELLBIO', 'name': 'Cell Biology'}
{'code': 'CHEM', 'name': 'Chemistry'}
{'code': 'CHILDPOL', 'name': 'Child Policy'}
{'code': 'CHINESE', 'name': 'Chinese'}
{'code': 'CLST', 'name': 'Classical Studies'}
{'code': 'CMB', 'name': 'Cell and Molecular Biology'}
{'code': 'COMPSCI', 'name': 'Computer Science'}
{'code': 'CULANTH', 'name': 'Cultural Anthropology'}
{'code': 'DOCST', 'name': 'Documentary Studies'}
{'code': 'DRAMA', 'name': 'Drama'}
{'code': 'DUTCH', 'name': 'Dutch'}
{'code': 'ECE', 'name': 'Electrical &amp; Computer Egr'}
{'code': 'ECON', 'name': 'Economics'}
{'code': 'EDUC', 'name': 'Education'}
{'code': 'EGR', 'name': 'Engineering'}
{'code': 'ENERGY', 'name': 'Energy'}
{'code': 'ENGLISH', 'name': 'English'}
{'code': 'ENVIRON', 'name': 'Environment'}
{'code': 'EOS', 'name': 'Earth and Ocean Sciences'}
{'code': 'ETHICS', 'name': 'Study of Ethics'}
{'code': 'EVANTH', 'name': 'Evolutionary Anthropology'}
{'code': 'FINANCE', 'name': 'Finance'}
{'code': 'FRENCH', 'name': 'French'}
{'code': 'GERMAN', 'name': 'German'}
{'code': 'GLHLTH', 'name': 'Global Health'}
{'code': 'GREEK', 'name': 'Greek'}
{'code': 'GSF', 'name': 'Gender Sexuality &amp; Feminist St'}
{'code': 'HEBREW', 'name': 'Hebrew'}
{'code': 'HINDI', 'name': 'Hindi'}
{'code': 'HISTORY', 'name': 'History'}
{'code': 'HTHPOL', 'name': 'Health Policy'}
{'code': 'HUNGARN', 'name': 'Hungarian'}
{'code': 'ITALIAN', 'name': 'Italian'}
{'code': 'JEWISHST', 'name': 'Jewish Studies'}
{'code': 'JPN', 'name': 'Japanese'}
{'code': 'KOREAN', 'name': 'Korean'}
{'code': 'LATAMER', 'name': 'Latin American Studies'}
{'code': 'LATIN', 'name': 'Latin'}
{'code': 'LINGUIST', 'name': 'Linguistics'}
{'code': 'LIT', 'name': 'Literature'}
{'code': 'MANAGEMT', 'name': 'Management'}
{'code': 'MARKETNG', 'name': 'Marketing'}
{'code': 'MATH', 'name': 'Mathematics'}
{'code': 'MGRECON', 'name': 'Economics'}
{'code': 'MUSIC', 'name': 'Music'}
{'code': 'NEURO', 'name': 'Neurology'}
{'code': 'NEUROBIO', 'name': 'Neurobiology'}
{'code': 'NEUROSCI', 'name': 'Neuroscience'}
{'code': 'PHIL', 'name': 'Philosophy'}
{'code': 'PHYASST', 'name': 'Physician Assistant Program'}
{'code': 'PHYSEDU', 'name': 'Physical Education'}
{'code': 'PHYSICS', 'name': 'Physics'}
{'code': 'PJMS', 'name': 'Policy Journalism and Media St'}
{'code': 'POE', 'name': 'Practice-Oriented Education'}
{'code': 'POLISH', 'name': 'Polish'}
{'code': 'POLSCI', 'name': 'Political Science'}
{'code': 'PORTUGUE', 'name': 'Portuguese'}
{'code': 'PPE', 'name': 'Philosophy, Politics, and Econ'}
{'code': 'PSY', 'name': 'Psychology'}
{'code': 'PUBPOL', 'name': 'Public Policy'}
{'code': 'RELIGION', 'name': 'Religion'}
{'code': 'RESEARCH', 'name': 'Research'}
{'code': 'RIGHTS', 'name': 'Human Rights'}
{'code': 'ROMANIAN', 'name': 'Romanian'}
{'code': 'ROMLANG', 'name': 'Romance Languages'}
{'code': 'ROMST', 'name': 'Romance Studies'}
{'code': 'RUSSIAN', 'name': 'Russian'}
{'code': 'SOCENT', 'name': 'Social Entrepreneurship'}
{'code': 'SOCIOL', 'name': 'Sociology'}
{'code': 'SPANISH', 'name': 'Spanish'}
{'code': 'STA', 'name': 'Statistical Science'}
{'code': 'THEATRST', 'name': 'Theater Studies'}
{'code': 'THESIS', 'name': 'Thesis'}
{'code': 'VISUALST', 'name': 'Visual Studies'}
{'code': 'WRITING', 'name': 'Writing'}
"""
count = 0
for a in split:
    if ("<option" in a):
        a = a.split("\">")[1].split("</option>")[0]
        code = a.split(" - ")[0]
        name = a.split(" - ")[1]
        if ("ROBT" in code or "R0BT_REL" in code or "INYU" in code or "INCS" in code or
        "IUSC" in code or "JGER" in code or "INCH" in code or "INCU" in code or "@" in code or 
        "INCC" in code or "INCG" in code or (not code in oldData)):
            continue
        print(code)
        count += 1
        ignorespaces.append(a)
        
print(count)