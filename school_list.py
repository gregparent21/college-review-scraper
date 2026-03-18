from typing import Dict, List


def get_school_list() -> List[Dict[str, str]]:
    """
    Central definition of all schools to scrape.

    Each entry must have:
    - name: human-readable school name
    - url: Niche college URL

    You can freely extend or modify this list.
    """
    
    return [
    {
        "name": "Abilene Christian University",
        "url": "https://www.niche.com/colleges/abilene-christian-university/"
    },
    {
        "name": "Adelphi University",
        "url": "https://www.niche.com/colleges/adelphi-university/"
    },
    {
        "name": "Alabama State University",
        "url": "https://www.niche.com/colleges/alabama-state-university/"
    },
    {
        "name": "Albizu University--Miami",
        "url": "https://www.niche.com/colleges/albizu-university-miami/"
    },
    {
        "name": "Alliant International University",
        "url": "https://www.niche.com/colleges/alliant-international-university/"
    },
    {
        "name": "Alvernia University",
        "url": "https://www.niche.com/colleges/alvernia-university/"
    },
    {
        "name": "American International College",
        "url": "https://www.niche.com/colleges/american-international-college/"
    },
    {
        "name": "American University",
        "url": "https://www.niche.com/colleges/american-university/"
    },
    {
        "name": "Andrews University",
        "url": "https://www.niche.com/colleges/andrews-university/"
    },
    {
        "name": "Arizona State University",
        "url": "https://www.niche.com/colleges/arizona-state-university/"
    },
    {
        "name": "Arkansas State University",
        "url": "https://www.niche.com/colleges/arkansas-state-university/"
    },
    {
        "name": "Auburn University",
        "url": "https://www.niche.com/colleges/auburn-university/"
    },
    {
        "name": "Augusta University",
        "url": "https://www.niche.com/colleges/augusta-university/"
    },
    {
        "name": "Aurora University",
        "url": "https://www.niche.com/colleges/aurora-university/"
    },
    {
        "name": "Azusa Pacific University",
        "url": "https://www.niche.com/colleges/azusa-pacific-university/"
    },
    {
        "name": "Baker University",
        "url": "https://www.niche.com/colleges/baker-university/"
    },
    {
        "name": "Ball State University",
        "url": "https://www.niche.com/colleges/ball-state-university/"
    },
    {
        "name": "Barry University",
        "url": "https://www.niche.com/colleges/barry-university/"
    },
    {
        "name": "Baylor University",
        "url": "https://www.niche.com/colleges/baylor-university/"
    },
    {
        "name": "Belhaven University",
        "url": "https://www.niche.com/colleges/belhaven-university/"
    },
    {
        "name": "Bellarmine University",
        "url": "https://www.niche.com/colleges/bellarmine-university/"
    },
    {
        "name": "Belmont University",
        "url": "https://www.niche.com/colleges/belmont-university/"
    },
    {
        "name": "Bethel University (MN)",
        "url": "https://www.niche.com/colleges/bethel-university-mn/"
    },
    {
        "name": "Binghamton University--SUNY",
        "url": "https://www.niche.com/colleges/binghamton-university-suny/"
    },
    {
        "name": "Biola University",
        "url": "https://www.niche.com/colleges/biola-university/"
    },
    {
        "name": "Boise State University",
        "url": "https://www.niche.com/colleges/boise-state-university/"
    },
    {
        "name": "Boston College",
        "url": "https://www.niche.com/colleges/boston-college/"
    },
    {
        "name": "Boston University",
        "url": "https://www.niche.com/colleges/boston-university/"
    },
    {
        "name": "Bowling Green State University",
        "url": "https://www.niche.com/colleges/bowling-green-state-university/"
    },
    {
        "name": "Bradley University",
        "url": "https://www.niche.com/colleges/bradley-university/"
    },
    {
        "name": "Brandeis University",
        "url": "https://www.niche.com/colleges/brandeis-university/"
    },
    {
        "name": "Brenau University",
        "url": "https://www.niche.com/colleges/brenau-university/"
    },
    {
        "name": "Briar Cliff University",
        "url": "https://www.niche.com/colleges/briar-cliff-university/"
    },
    {
        "name": "Brigham Young University",
        "url": "https://www.niche.com/colleges/brigham-young-university/"
    },
    {
        "name": "Brown University",
        "url": "https://www.niche.com/colleges/brown-university/"
    },
    {
        "name": "CUNY--City College",
        "url": "https://www.niche.com/colleges/cuny-city-college/"
    },
    {
        "name": "California Institute of Technology",
        "url": "https://www.niche.com/colleges/california-institute-of-technology/"
    },
    {
        "name": "California State University--East Bay",
        "url": "https://www.niche.com/colleges/california-state-university-east-bay/"
    },
    {
        "name": "California State University--Fresno",
        "url": "https://www.niche.com/colleges/california-state-university-fresno/"
    },
    {
        "name": "California State University--Fullerton",
        "url": "https://www.niche.com/colleges/california-state-university-fullerton/"
    },
    {
        "name": "California State University--Long Beach",
        "url": "https://www.niche.com/colleges/california-state-university-long-beach/"
    },
    {
        "name": "California State University--San Bernardino",
        "url": "https://www.niche.com/colleges/california-state-university-san-bernardino/"
    },
    {
        "name": "Campbell University",
        "url": "https://www.niche.com/colleges/campbell-university/"
    },
    {
        "name": "Capitol Technology University",
        "url": "https://www.niche.com/colleges/capitol-technology-university/"
    },
    {
        "name": "Carnegie Mellon University",
        "url": "https://www.niche.com/colleges/carnegie-mellon-university/"
    },
    {
        "name": "Carson-Newman University",
        "url": "https://www.niche.com/colleges/carson-newman-university/"
    },
    {
        "name": "Case Western Reserve University",
        "url": "https://www.niche.com/colleges/case-western-reserve-university/"
    },
    {
        "name": "Central Michigan University",
        "url": "https://www.niche.com/colleges/central-michigan-university/"
    },
    {
        "name": "Chapman University",
        "url": "https://www.niche.com/colleges/chapman-university/"
    },
    {
        "name": "Chatham University",
        "url": "https://www.niche.com/colleges/chatham-university/"
    },
    {
        "name": "Clark Atlanta University",
        "url": "https://www.niche.com/colleges/clark-atlanta-university/"
    },
    {
        "name": "Clark University",
        "url": "https://www.niche.com/colleges/clark-university/"
    },
    {
        "name": "Clarke University",
        "url": "https://www.niche.com/colleges/clarke-university/"
    },
    {
        "name": "Clarkson University",
        "url": "https://www.niche.com/colleges/clarkson-university/"
    },
    {
        "name": "Clemson University",
        "url": "https://www.niche.com/colleges/clemson-university/"
    },
    {
        "name": "Cleveland State University",
        "url": "https://www.niche.com/colleges/cleveland-state-university/"
    },
    {
        "name": "Colorado School of Mines",
        "url": "https://www.niche.com/colleges/colorado-school-of-mines/"
    },
    {
        "name": "Colorado State University",
        "url": "https://www.niche.com/colleges/colorado-state-university/"
    },
    {
        "name": "Colorado Technical University",
        "url": "https://www.niche.com/colleges/colorado-technical-university/"
    },
    {
        "name": "Columbia University",
        "url": "https://www.niche.com/colleges/columbia-university/"
    },
    {
        "name": "Concordia University Irvine",
        "url": "https://www.niche.com/colleges/concordia-university-irvine/"
    },
    {
        "name": "Concordia University Wisconsin",
        "url": "https://www.niche.com/colleges/concordia-university-wisconsin/"
    },
    {
        "name": "Cornell University",
        "url": "https://www.niche.com/colleges/cornell-university/"
    },
    {
        "name": "Creighton University",
        "url": "https://www.niche.com/colleges/creighton-university/"
    },
    {
        "name": "D'Youville University",
        "url": "https://www.niche.com/colleges/dyouville-university/"
    },
    {
        "name": "Daemen University",
        "url": "https://www.niche.com/colleges/daemen-university/"
    },
    {
        "name": "Dallas Baptist University",
        "url": "https://www.niche.com/colleges/dallas-baptist-university/"
    },
    {
        "name": "Dartmouth College",
        "url": "https://www.niche.com/colleges/dartmouth-college/"
    },
    {
        "name": "DePaul University",
        "url": "https://www.niche.com/colleges/depaul-university/"
    },
    {
        "name": "DeSales University",
        "url": "https://www.niche.com/colleges/desales-university/"
    },
    {
        "name": "Dominican University New York",
        "url": "https://www.niche.com/colleges/dominican-university-new-york/"
    },
    {
        "name": "Drake University",
        "url": "https://www.niche.com/colleges/drake-university/"
    },
    {
        "name": "Drexel University",
        "url": "https://www.niche.com/colleges/drexel-university/"
    },
    {
        "name": "Duke University",
        "url": "https://www.niche.com/colleges/duke-university/"
    },
    {
        "name": "Duquesne University",
        "url": "https://www.niche.com/colleges/duquesne-university/"
    },
    {
        "name": "East Carolina University",
        "url": "https://www.niche.com/colleges/east-carolina-university/"
    },
    {
        "name": "East Tennessee State University",
        "url": "https://www.niche.com/colleges/east-tennessee-state-university/"
    },
    {
        "name": "East Texas A&M University",
        "url": "https://www.niche.com/colleges/east-texas-a-and-m-university/"
    },
    {
        "name": "Eastern Kentucky University",
        "url": "https://www.niche.com/colleges/eastern-kentucky-university/"
    },
    {
        "name": "Eastern Michigan University",
        "url": "https://www.niche.com/colleges/eastern-michigan-university/"
    },
    {
        "name": "Edgewood College",
        "url": "https://www.niche.com/colleges/edgewood-college/"
    },
    {
        "name": "Elon University",
        "url": "https://www.niche.com/colleges/elon-university/"
    },
    {
        "name": "Emory University",
        "url": "https://www.niche.com/colleges/emory-university/"
    },
    {
        "name": "Fairfield University",
        "url": "https://www.niche.com/colleges/fairfield-university/"
    },
    {
        "name": "Ferris State University",
        "url": "https://www.niche.com/colleges/ferris-state-university/"
    },
    {
        "name": "Florida A&M University",
        "url": "https://www.niche.com/colleges/florida-a-and-m-university/"
    },
    {
        "name": "Florida Atlantic University",
        "url": "https://www.niche.com/colleges/florida-atlantic-university/"
    },
    {
        "name": "Florida Gulf Coast University",
        "url": "https://www.niche.com/colleges/florida-gulf-coast-university/"
    },
    {
        "name": "Florida Institute of Technology",
        "url": "https://www.niche.com/colleges/florida-institute-of-technology/"
    },
    {
        "name": "Florida International University",
        "url": "https://www.niche.com/colleges/florida-international-university/"
    },
    {
        "name": "Florida State University",
        "url": "https://www.niche.com/colleges/florida-state-university/"
    },
    {
        "name": "Fordham University",
        "url": "https://www.niche.com/colleges/fordham-university/"
    },
    {
        "name": "Gallaudet University",
        "url": "https://www.niche.com/colleges/gallaudet-university/"
    },
    {
        "name": "Gannon University",
        "url": "https://www.niche.com/colleges/gannon-university/"
    },
    {
        "name": "Gardner-Webb University",
        "url": "https://www.niche.com/colleges/gardner-webb-university/"
    },
    {
        "name": "George Fox University",
        "url": "https://www.niche.com/colleges/george-fox-university/"
    },
    {
        "name": "George Mason University",
        "url": "https://www.niche.com/colleges/george-mason-university/"
    },
    {
        "name": "George Washington University",
        "url": "https://www.niche.com/colleges/george-washington-university/"
    },
    {
        "name": "Georgetown University",
        "url": "https://www.niche.com/colleges/georgetown-university/"
    },
    {
        "name": "Georgia Institute of Technology",
        "url": "https://www.niche.com/colleges/georgia-institute-of-technology/"
    },
    {
        "name": "Georgia Southern University",
        "url": "https://www.niche.com/colleges/georgia-southern-university/"
    },
    {
        "name": "Georgia State University",
        "url": "https://www.niche.com/colleges/georgia-state-university/"
    },
    {
        "name": "Gonzaga University",
        "url": "https://www.niche.com/colleges/gonzaga-university/"
    },
    {
        "name": "Grand Canyon University",
        "url": "https://www.niche.com/colleges/grand-canyon-university/"
    },
    {
        "name": "Grand Valley State University",
        "url": "https://www.niche.com/colleges/grand-valley-state-university/"
    },
    {
        "name": "Gwynedd Mercy University",
        "url": "https://www.niche.com/colleges/gwynedd-mercy-university/"
    },
    {
        "name": "Hampton University",
        "url": "https://www.niche.com/colleges/hampton-university/"
    },
    {
        "name": "Hardin-Simmons University",
        "url": "https://www.niche.com/colleges/hardin-simmons-university/"
    },
    {
        "name": "Harding University",
        "url": "https://www.niche.com/colleges/harding-university/"
    },
    {
        "name": "Harvard University",
        "url": "https://www.niche.com/colleges/harvard-university/"
    },
    {
        "name": "Hofstra University",
        "url": "https://www.niche.com/colleges/hofstra-university/"
    },
    {
        "name": "Howard University",
        "url": "https://www.niche.com/colleges/howard-university/"
    },
    {
        "name": "Husson University",
        "url": "https://www.niche.com/colleges/husson-university/"
    },
    {
        "name": "Idaho State University",
        "url": "https://www.niche.com/colleges/idaho-state-university/"
    },
    {
        "name": "Illinois Institute of Technology",
        "url": "https://www.niche.com/colleges/illinois-institute-of-technology/"
    },
    {
        "name": "Illinois State University",
        "url": "https://www.niche.com/colleges/illinois-state-university/"
    },
    {
        "name": "Immaculata University",
        "url": "https://www.niche.com/colleges/immaculata-university/"
    },
    {
        "name": "Indiana State University",
        "url": "https://www.niche.com/colleges/indiana-state-university/"
    },
    {
        "name": "Indiana University Indianapolis",
        "url": "https://www.niche.com/colleges/indiana-university-indianapolis/"
    },
    {
        "name": "Indiana University of Pennsylvania",
        "url": "https://www.niche.com/colleges/indiana-university-of-pennsylvania/"
    },
    {
        "name": "Indiana University--Bloomington",
        "url": "https://www.niche.com/colleges/indiana-university-bloomington/"
    },
    {
        "name": "Iowa State University of Science and Technology",
        "url": "https://www.niche.com/colleges/iowa-state-university-of-science-and-technology/"
    },
    {
        "name": "Jackson State University",
        "url": "https://www.niche.com/colleges/jackson-state-university/"
    },
    {
        "name": "James Madison University",
        "url": "https://www.niche.com/colleges/james-madison-university/"
    },
    {
        "name": "Johns Hopkins University",
        "url": "https://www.niche.com/colleges/johns-hopkins-university/"
    },
    {
        "name": "Judson College at Southeastern",
        "url": "https://www.niche.com/colleges/judson-college-at-southeastern/"
    },
    {
        "name": "Kansas State University",
        "url": "https://www.niche.com/colleges/kansas-state-university/"
    },
    {
        "name": "Kean University",
        "url": "https://www.niche.com/colleges/kean-university/"
    },
    {
        "name": "Keiser University",
        "url": "https://www.niche.com/colleges/keiser-university/"
    },
    {
        "name": "Kennesaw State University",
        "url": "https://www.niche.com/colleges/kennesaw-state-university/"
    },
    {
        "name": "Kent State University",
        "url": "https://www.niche.com/colleges/kent-state-university/"
    },
    {
        "name": "La Salle University",
        "url": "https://www.niche.com/colleges/la-salle-university/"
    },
    {
        "name": "Lamar University",
        "url": "https://www.niche.com/colleges/lamar-university/"
    },
    {
        "name": "Lehigh University",
        "url": "https://www.niche.com/colleges/lehigh-university/"
    },
    {
        "name": "Lesley University",
        "url": "https://www.niche.com/colleges/lesley-university/"
    },
    {
        "name": "Liberty University",
        "url": "https://www.niche.com/colleges/liberty-university/"
    },
    {
        "name": "Lincoln Memorial University",
        "url": "https://www.niche.com/colleges/lincoln-memorial-university/"
    },
    {
        "name": "Lipscomb University",
        "url": "https://www.niche.com/colleges/lipscomb-university/"
    },
    {
        "name": "Long Island University",
        "url": "https://www.niche.com/colleges/long-island-university/"
    },
    {
        "name": "Louisiana State University--Baton Rouge",
        "url": "https://www.niche.com/colleges/louisiana-state-university-baton-rouge/"
    },
    {
        "name": "Louisiana Tech University",
        "url": "https://www.niche.com/colleges/louisiana-tech-university/"
    },
    {
        "name": "Loyola Marymount University",
        "url": "https://www.niche.com/colleges/loyola-marymount-university/"
    },
    {
        "name": "Loyola University Chicago",
        "url": "https://www.niche.com/colleges/loyola-university-chicago/"
    },
    {
        "name": "Loyola University New Orleans",
        "url": "https://www.niche.com/colleges/loyola-university-new-orleans/"
    },
    {
        "name": "Marian University (IN)",
        "url": "https://www.niche.com/colleges/marian-university-in/"
    },
    {
        "name": "Marquette University",
        "url": "https://www.niche.com/colleges/marquette-university/"
    },
    {
        "name": "Marshall University",
        "url": "https://www.niche.com/colleges/marshall-university/"
    },
    {
        "name": "Mary Baldwin University",
        "url": "https://www.niche.com/colleges/mary-baldwin-university/"
    },
    {
        "name": "Marymount University",
        "url": "https://www.niche.com/colleges/marymount-university/"
    },
    {
        "name": "Maryville University of St. Louis",
        "url": "https://www.niche.com/colleges/maryville-university-of-st-louis/"
    },
    {
        "name": "Massachusetts Institute of Technology",
        "url": "https://www.niche.com/colleges/massachusetts-institute-of-technology/"
    },
    {
        "name": "Mercer University",
        "url": "https://www.niche.com/colleges/mercer-university/"
    },
    {
        "name": "Miami University--Oxford",
        "url": "https://www.niche.com/colleges/miami-university-oxford/"
    },
    {
        "name": "Michigan State University",
        "url": "https://www.niche.com/colleges/michigan-state-university/"
    },
    {
        "name": "Michigan Technological University",
        "url": "https://www.niche.com/colleges/michigan-technological-university/"
    },
    {
        "name": "Middle Tennessee State University",
        "url": "https://www.niche.com/colleges/middle-tennessee-state-university/"
    },
    {
        "name": "Misericordia University",
        "url": "https://www.niche.com/colleges/misericordia-university/"
    },
    {
        "name": "Mississippi College",
        "url": "https://www.niche.com/colleges/mississippi-college/"
    },
    {
        "name": "Mississippi State University",
        "url": "https://www.niche.com/colleges/mississippi-state-university/"
    },
    {
        "name": "Missouri State University",
        "url": "https://www.niche.com/colleges/missouri-state-university/"
    },
    {
        "name": "Missouri University of Science and Technology",
        "url": "https://www.niche.com/colleges/missouri-university-of-science-and-technology/"
    },
    {
        "name": "Montana State University",
        "url": "https://www.niche.com/colleges/montana-state-university/"
    },
    {
        "name": "Montclair State University",
        "url": "https://www.niche.com/colleges/montclair-state-university/"
    },
    {
        "name": "Morgan State University",
        "url": "https://www.niche.com/colleges/morgan-state-university/"
    },
    {
        "name": "Mount St. Joseph University",
        "url": "https://www.niche.com/colleges/mount-st-joseph-university/"
    },
    {
        "name": "National Louis University",
        "url": "https://www.niche.com/colleges/national-louis-university/"
    },
    {
        "name": "New Jersey Institute of Technology",
        "url": "https://www.niche.com/colleges/new-jersey-institute-of-technology/"
    },
    {
        "name": "New Mexico State University",
        "url": "https://www.niche.com/colleges/new-mexico-state-university/"
    },
    {
        "name": "New York University",
        "url": "https://www.niche.com/colleges/new-york-university/"
    },
    {
        "name": "North Carolina Agricultural and Technical State University",
        "url": "https://www.niche.com/colleges/north-carolina-agricultural-and-technical-state-university/"
    },
    {
        "name": "North Carolina State University",
        "url": "https://www.niche.com/colleges/north-carolina-state-university/"
    },
    {
        "name": "North Dakota State University",
        "url": "https://www.niche.com/colleges/north-dakota-state-university/"
    },
    {
        "name": "Northeastern University",
        "url": "https://www.niche.com/colleges/northeastern-university/"
    },
    {
        "name": "Northern Arizona University",
        "url": "https://www.niche.com/colleges/northern-arizona-university/"
    },
    {
        "name": "Northern Illinois University",
        "url": "https://www.niche.com/colleges/northern-illinois-university/"
    },
    {
        "name": "Northern Kentucky University",
        "url": "https://www.niche.com/colleges/northern-kentucky-university/"
    },
    {
        "name": "Northwestern University",
        "url": "https://www.niche.com/colleges/northwestern-university/"
    },
    {
        "name": "Nova Southeastern University",
        "url": "https://www.niche.com/colleges/nova-southeastern-university/"
    },
    {
        "name": "Oakland City University",
        "url": "https://www.niche.com/colleges/oakland-city-university/"
    },
    {
        "name": "Oakland University",
        "url": "https://www.niche.com/colleges/oakland-university/"
    },
    {
        "name": "Ohio University",
        "url": "https://www.niche.com/colleges/ohio-university/"
    },
    {
        "name": "Oklahoma City University",
        "url": "https://www.niche.com/colleges/oklahoma-city-university/"
    },
    {
        "name": "Oklahoma State University",
        "url": "https://www.niche.com/colleges/oklahoma-state-university/"
    },
    {
        "name": "Old Dominion University",
        "url": "https://www.niche.com/colleges/old-dominion-university/"
    },
    {
        "name": "Oregon State University",
        "url": "https://www.niche.com/colleges/oregon-state-university/"
    },
    {
        "name": "Our Lady of the Lake University",
        "url": "https://www.niche.com/colleges/our-lady-of-the-lake-university/"
    },
    {
        "name": "Pace University",
        "url": "https://www.niche.com/colleges/pace-university/"
    },
    {
        "name": "Pacific University",
        "url": "https://www.niche.com/colleges/pacific-university/"
    },
    {
        "name": "Palm Beach Atlantic University",
        "url": "https://www.niche.com/colleges/palm-beach-atlantic-university/"
    },
    {
        "name": "Pepperdine University",
        "url": "https://www.niche.com/colleges/pepperdine-university/"
    },
    {
        "name": "Point Park University",
        "url": "https://www.niche.com/colleges/point-park-university/"
    },
    {
        "name": "Pontifical Catholic University of Puerto Rico--Arecibo",
        "url": "https://www.niche.com/colleges/pontifical-catholic-university-of-puerto-rico-arecibo/"
    },
    {
        "name": "Pontifical Catholic University of Puerto Rico--Ponce",
        "url": "https://www.niche.com/colleges/pontifical-catholic-university-of-puerto-rico-ponce/"
    },
    {
        "name": "Portland State University",
        "url": "https://www.niche.com/colleges/portland-state-university/"
    },
    {
        "name": "Prairie View A&M University",
        "url": "https://www.niche.com/colleges/prairie-view-a-and-m-university/"
    },
    {
        "name": "Princeton University",
        "url": "https://www.niche.com/colleges/princeton-university/"
    },
    {
        "name": "Purdue University--Main Campus",
        "url": "https://www.niche.com/colleges/purdue-university-main-campus/"
    },
    {
        "name": "Quinnipiac University",
        "url": "https://www.niche.com/colleges/quinnipiac-university/"
    },
    {
        "name": "Radford University",
        "url": "https://www.niche.com/colleges/radford-university/"
    },
    {
        "name": "Regent University",
        "url": "https://www.niche.com/colleges/regent-university/"
    },
    {
        "name": "Regis University",
        "url": "https://www.niche.com/colleges/regis-university/"
    },
    {
        "name": "Rensselaer Polytechnic Institute",
        "url": "https://www.niche.com/colleges/rensselaer-polytechnic-institute/"
    },
    {
        "name": "Rice University",
        "url": "https://www.niche.com/colleges/rice-university/"
    },
    {
        "name": "Robert Morris University",
        "url": "https://www.niche.com/colleges/robert-morris-university/"
    },
    {
        "name": "Rochester Institute of Technology",
        "url": "https://www.niche.com/colleges/rochester-institute-of-technology/"
    },
    {
        "name": "Roosevelt University",
        "url": "https://www.niche.com/colleges/roosevelt-university/"
    },
    {
        "name": "Rowan University",
        "url": "https://www.niche.com/colleges/rowan-university/"
    },
    {
        "name": "Russell Sage College",
        "url": "https://www.niche.com/colleges/russell-sage-college/"
    },
    {
        "name": "Rutgers University--Camden",
        "url": "https://www.niche.com/colleges/rutgers-university-camden/"
    },
    {
        "name": "Rutgers University--New Brunswick",
        "url": "https://www.niche.com/colleges/rutgers-university-new-brunswick/"
    },
    {
        "name": "Rutgers University--Newark",
        "url": "https://www.niche.com/colleges/rutgers-university-newark/"
    },
    {
        "name": "SUNY College of Environmental Science and Forestry",
        "url": "https://www.niche.com/colleges/suny-college-of-environmental-science-and-forestry/"
    },
    {
        "name": "Sacred Heart University",
        "url": "https://www.niche.com/colleges/sacred-heart-university/"
    },
    {
        "name": "Saint Leo University",
        "url": "https://www.niche.com/colleges/saint-leo-university/"
    },
    {
        "name": "Saint Louis University",
        "url": "https://www.niche.com/colleges/saint-louis-university/"
    },
    {
        "name": "Saint Mary's University of Minnesota",
        "url": "https://www.niche.com/colleges/saint-marys-university-of-minnesota/"
    },
    {
        "name": "Sam Houston State University",
        "url": "https://www.niche.com/colleges/sam-houston-state-university/"
    },
    {
        "name": "Samford University",
        "url": "https://www.niche.com/colleges/samford-university/"
    },
    {
        "name": "San Diego State University",
        "url": "https://www.niche.com/colleges/san-diego-state-university/"
    },
    {
        "name": "San Francisco State University",
        "url": "https://www.niche.com/colleges/san-francisco-state-university/"
    },
    {
        "name": "Santa Clara University",
        "url": "https://www.niche.com/colleges/santa-clara-university/"
    },
    {
        "name": "Seattle Pacific University",
        "url": "https://www.niche.com/colleges/seattle-pacific-university/"
    },
    {
        "name": "Seattle University",
        "url": "https://www.niche.com/colleges/seattle-university/"
    },
    {
        "name": "Seton Hall University",
        "url": "https://www.niche.com/colleges/seton-hall-university/"
    },
    {
        "name": "Shenandoah University",
        "url": "https://www.niche.com/colleges/shenandoah-university/"
    },
    {
        "name": "Simmons University",
        "url": "https://www.niche.com/colleges/simmons-university/"
    },
    {
        "name": "South College",
        "url": "https://www.niche.com/colleges/south-college/"
    },
    {
        "name": "South Dakota State University",
        "url": "https://www.niche.com/colleges/south-dakota-state-university/"
    },
    {
        "name": "Southeastern University",
        "url": "https://www.niche.com/colleges/southeastern-university/"
    },
    {
        "name": "Southern Illinois University Edwardsville",
        "url": "https://www.niche.com/colleges/southern-illinois-university-edwardsville/"
    },
    {
        "name": "Southern Illinois University--Carbondale",
        "url": "https://www.niche.com/colleges/southern-illinois-university-carbondale/"
    },
    {
        "name": "Southern Methodist University",
        "url": "https://www.niche.com/colleges/southern-methodist-university/"
    },
    {
        "name": "Southern University and A & M College",
        "url": "https://www.niche.com/colleges/southern-university-and-a-and-m-college/"
    },
    {
        "name": "Springfield College",
        "url": "https://www.niche.com/colleges/springfield-college/"
    },
    {
        "name": "St. Ambrose University",
        "url": "https://www.niche.com/colleges/st-ambrose-university/"
    },
    {
        "name": "St. Catherine University",
        "url": "https://www.niche.com/colleges/st-catherine-university/"
    },
    {
        "name": "St. John Fisher University",
        "url": "https://www.niche.com/colleges/st-john-fisher-university/"
    },
    {
        "name": "St. John's University (NY)",
        "url": "https://www.niche.com/colleges/st-johns-university-ny/"
    },
    {
        "name": "St. Thomas University",
        "url": "https://www.niche.com/colleges/st-thomas-university/"
    },
    {
        "name": "Stanford University",
        "url": "https://www.niche.com/colleges/stanford-university/"
    },
    {
        "name": "Stevens Institute of Technology",
        "url": "https://www.niche.com/colleges/stevens-institute-of-technology/"
    },
    {
        "name": "Stockton University",
        "url": "https://www.niche.com/colleges/stockton-university/"
    },
    {
        "name": "Stony Brook University--SUNY",
        "url": "https://www.niche.com/colleges/stony-brook-university-suny/"
    },
    {
        "name": "Suffolk University",
        "url": "https://www.niche.com/colleges/suffolk-university/"
    },
    {
        "name": "Syracuse University",
        "url": "https://www.niche.com/colleges/syracuse-university/"
    },
    {
        "name": "Tarleton State University",
        "url": "https://www.niche.com/colleges/tarleton-state-university/"
    },
    {
        "name": "Temple University",
        "url": "https://www.niche.com/colleges/temple-university/"
    },
    {
        "name": "Tennessee State University",
        "url": "https://www.niche.com/colleges/tennessee-state-university/"
    },
    {
        "name": "Tennessee Tech University",
        "url": "https://www.niche.com/colleges/tennessee-tech-university/"
    },
    {
        "name": "Texas A & M University-Kingsville",
        "url": "https://www.niche.com/colleges/texas-a-and-m-university-kingsville/"
    },
    {
        "name": "Texas A&M University",
        "url": "https://www.niche.com/colleges/texas-a-and-m-university/"
    },
    {
        "name": "Texas A&M University--Corpus Christi",
        "url": "https://www.niche.com/colleges/texas-a-and-m-university-corpus-christi/"
    },
    {
        "name": "Texas Christian University",
        "url": "https://www.niche.com/colleges/texas-christian-university/"
    },
    {
        "name": "Texas Southern University",
        "url": "https://www.niche.com/colleges/texas-southern-university/"
    },
    {
        "name": "Texas State University",
        "url": "https://www.niche.com/colleges/texas-state-university/"
    },
    {
        "name": "Texas Tech University",
        "url": "https://www.niche.com/colleges/texas-tech-university/"
    },
    {
        "name": "Texas Wesleyan University",
        "url": "https://www.niche.com/colleges/texas-wesleyan-university/"
    },
    {
        "name": "Texas Woman's University",
        "url": "https://www.niche.com/colleges/texas-womans-university/"
    },
    {
        "name": "The Catholic University of America",
        "url": "https://www.niche.com/colleges/the-catholic-university-of-america/"
    },
    {
        "name": "The College of St. Scholastica",
        "url": "https://www.niche.com/colleges/the-college-of-st-scholastica/"
    },
    {
        "name": "The Master's University and Seminary",
        "url": "https://www.niche.com/colleges/the-masters-university-and-seminary/"
    },
    {
        "name": "The New School",
        "url": "https://www.niche.com/colleges/the-new-school/"
    },
    {
        "name": "The Ohio State University",
        "url": "https://www.niche.com/colleges/the-ohio-state-university/"
    },
    {
        "name": "The Pennsylvania State University--University Park",
        "url": "https://www.niche.com/colleges/the-pennsylvania-state-university-university-park/"
    },
    {
        "name": "The University of Akron",
        "url": "https://www.niche.com/colleges/the-university-of-akron/"
    },
    {
        "name": "The University of Alabama",
        "url": "https://www.niche.com/colleges/the-university-of-alabama/"
    },
    {
        "name": "The University of Oklahoma",
        "url": "https://www.niche.com/colleges/the-university-of-oklahoma/"
    },
    {
        "name": "The University of Texas at Tyler",
        "url": "https://www.niche.com/colleges/the-university-of-texas-at-tyler/"
    },
    {
        "name": "The University of Texas--Arlington",
        "url": "https://www.niche.com/colleges/the-university-of-texas-arlington/"
    },
    {
        "name": "The University of Texas--Austin",
        "url": "https://www.niche.com/colleges/the-university-of-texas-austin/"
    },
    {
        "name": "The University of Texas--Dallas",
        "url": "https://www.niche.com/colleges/the-university-of-texas-dallas/"
    },
    {
        "name": "The University of Texas--El Paso",
        "url": "https://www.niche.com/colleges/the-university-of-texas-el-paso/"
    },
    {
        "name": "The University of Texas--Rio Grande Valley",
        "url": "https://www.niche.com/colleges/the-university-of-texas-rio-grande-valley/"
    },
    {
        "name": "The University of Texas--San Antonio",
        "url": "https://www.niche.com/colleges/the-university-of-texas-san-antonio/"
    },
    {
        "name": "The University of Toledo",
        "url": "https://www.niche.com/colleges/the-university-of-toledo/"
    },
    {
        "name": "Thomas Jefferson University",
        "url": "https://www.niche.com/colleges/thomas-jefferson-university/"
    },
    {
        "name": "Touro University",
        "url": "https://www.niche.com/colleges/touro-university/"
    },
    {
        "name": "Trevecca Nazarene University",
        "url": "https://www.niche.com/colleges/trevecca-nazarene-university/"
    },
    {
        "name": "Trinity International University",
        "url": "https://www.niche.com/colleges/trinity-international-university/"
    },
    {
        "name": "Tufts University",
        "url": "https://www.niche.com/colleges/tufts-university/"
    },
    {
        "name": "Tulane University of Louisiana",
        "url": "https://www.niche.com/colleges/tulane-university-of-louisiana/"
    },
    {
        "name": "Union University",
        "url": "https://www.niche.com/colleges/union-university/"
    },
    {
        "name": "Universidad Ana G. Mendez--Gurabo Campus",
        "url": "https://www.niche.com/colleges/universidad-ana-g-mendez-gurabo-campus/"
    },
    {
        "name": "University at Albany--SUNY",
        "url": "https://www.niche.com/colleges/university-at-albany-suny/"
    },
    {
        "name": "University at Buffalo--SUNY",
        "url": "https://www.niche.com/colleges/university-at-buffalo-suny/"
    },
    {
        "name": "University of Alabama at Birmingham",
        "url": "https://www.niche.com/colleges/university-of-alabama-at-birmingham/"
    },
    {
        "name": "University of Alabama at Huntsville",
        "url": "https://www.niche.com/colleges/university-of-alabama-at-huntsville/"
    },
    {
        "name": "University of Alaska Fairbanks",
        "url": "https://www.niche.com/colleges/university-of-alaska-fairbanks/"
    },
    {
        "name": "University of Arizona",
        "url": "https://www.niche.com/colleges/university-of-arizona/"
    },
    {
        "name": "University of Arkansas",
        "url": "https://www.niche.com/colleges/university-of-arkansas/"
    },
    {
        "name": "University of Arkansas--Little Rock",
        "url": "https://www.niche.com/colleges/university-of-arkansas-little-rock/"
    },
    {
        "name": "University of Bridgeport",
        "url": "https://www.niche.com/colleges/university-of-bridgeport/"
    },
    {
        "name": "University of California, Berkeley",
        "url": "https://www.niche.com/colleges/university-of-california-berkeley/"
    },
    {
        "name": "University of California, Davis",
        "url": "https://www.niche.com/colleges/university-of-california-davis/"
    },
    {
        "name": "University of California, Merced",
        "url": "https://www.niche.com/colleges/university-of-california-merced/"
    },
    {
        "name": "University of California, Riverside",
        "url": "https://www.niche.com/colleges/university-of-california-riverside/"
    },
    {
        "name": "University of California, San Diego",
        "url": "https://www.niche.com/colleges/university-of-california-san-diego/"
    },
    {
        "name": "University of California, Santa Barbara",
        "url": "https://www.niche.com/colleges/university-of-california-santa-barbara/"
    },
    {
        "name": "University of California, Santa Cruz",
        "url": "https://www.niche.com/colleges/university-of-california-santa-cruz/"
    },
    {
        "name": "University of California--Irvine",
        "url": "https://www.niche.com/colleges/university-of-california-irvine/"
    },
    {
        "name": "University of California--Los Angeles",
        "url": "https://www.niche.com/colleges/university-of-california-los-angeles/"
    },
    {
        "name": "University of Central Arkansas",
        "url": "https://www.niche.com/colleges/university-of-central-arkansas/"
    },
    {
        "name": "University of Central Florida",
        "url": "https://www.niche.com/colleges/university-of-central-florida/"
    },
    {
        "name": "University of Charleston",
        "url": "https://www.niche.com/colleges/university-of-charleston/"
    },
    {
        "name": "University of Chicago",
        "url": "https://www.niche.com/colleges/university-of-chicago/"
    },
    {
        "name": "University of Cincinnati",
        "url": "https://www.niche.com/colleges/university-of-cincinnati/"
    },
    {
        "name": "University of Colorado Boulder",
        "url": "https://www.niche.com/colleges/university-of-colorado-boulder/"
    },
    {
        "name": "University of Colorado Denver",
        "url": "https://www.niche.com/colleges/university-of-colorado-denver/"
    },
    {
        "name": "University of Colorado--Colorado Springs",
        "url": "https://www.niche.com/colleges/university-of-colorado-colorado-springs/"
    },
    {
        "name": "University of Connecticut",
        "url": "https://www.niche.com/colleges/university-of-connecticut/"
    },
    {
        "name": "University of Dayton",
        "url": "https://www.niche.com/colleges/university-of-dayton/"
    },
    {
        "name": "University of Delaware",
        "url": "https://www.niche.com/colleges/university-of-delaware/"
    },
    {
        "name": "University of Denver",
        "url": "https://www.niche.com/colleges/university-of-denver/"
    },
    {
        "name": "University of Detroit Mercy",
        "url": "https://www.niche.com/colleges/university-of-detroit-mercy/"
    },
    {
        "name": "University of Findlay",
        "url": "https://www.niche.com/colleges/university-of-findlay/"
    },
    {
        "name": "University of Florida",
        "url": "https://www.niche.com/colleges/university-of-florida/"
    },
    {
        "name": "University of Georgia",
        "url": "https://www.niche.com/colleges/university-of-georgia/"
    },
    {
        "name": "University of Hartford",
        "url": "https://www.niche.com/colleges/university-of-hartford/"
    },
    {
        "name": "University of Hawaii at Hilo",
        "url": "https://www.niche.com/colleges/university-of-hawaii-at-hilo/"
    },
    {
        "name": "University of Hawaii at Manoa",
        "url": "https://www.niche.com/colleges/university-of-hawaii-at-manoa/"
    },
    {
        "name": "University of Houston",
        "url": "https://www.niche.com/colleges/university-of-houston/"
    },
    {
        "name": "University of Houston--Clear Lake",
        "url": "https://www.niche.com/colleges/university-of-houston-clear-lake/"
    },
    {
        "name": "University of Idaho",
        "url": "https://www.niche.com/colleges/university-of-idaho/"
    },
    {
        "name": "University of Illinois Chicago",
        "url": "https://www.niche.com/colleges/university-of-illinois-chicago/"
    },
    {
        "name": "University of Illinois Urbana-Champaign",
        "url": "https://www.niche.com/colleges/university-of-illinois-urbana-champaign/"
    },
    {
        "name": "University of Indianapolis",
        "url": "https://www.niche.com/colleges/university-of-indianapolis/"
    },
    {
        "name": "University of Iowa",
        "url": "https://www.niche.com/colleges/university-of-iowa/"
    },
    {
        "name": "University of Kansas",
        "url": "https://www.niche.com/colleges/university-of-kansas/"
    },
    {
        "name": "University of Kentucky",
        "url": "https://www.niche.com/colleges/university-of-kentucky/"
    },
    {
        "name": "University of La Verne",
        "url": "https://www.niche.com/colleges/university-of-la-verne/"
    },
    {
        "name": "University of Louisiana at Lafayette",
        "url": "https://www.niche.com/colleges/university-of-louisiana-at-lafayette/"
    },
    {
        "name": "University of Louisiana at Monroe",
        "url": "https://www.niche.com/colleges/university-of-louisiana-at-monroe/"
    },
    {
        "name": "University of Louisville",
        "url": "https://www.niche.com/colleges/university-of-louisville/"
    },
    {
        "name": "University of Lynchburg",
        "url": "https://www.niche.com/colleges/university-of-lynchburg/"
    },
    {
        "name": "University of Maine",
        "url": "https://www.niche.com/colleges/university-of-maine/"
    },
    {
        "name": "University of Mary",
        "url": "https://www.niche.com/colleges/university-of-mary/"
    },
    {
        "name": "University of Mary Hardin-Baylor",
        "url": "https://www.niche.com/colleges/university-of-mary-hardin-baylor/"
    },
    {
        "name": "University of Maryland Baltimore County",
        "url": "https://www.niche.com/colleges/university-of-maryland-baltimore-county/"
    },
    {
        "name": "University of Maryland Eastern Shore",
        "url": "https://www.niche.com/colleges/university-of-maryland-eastern-shore/"
    },
    {
        "name": "University of Maryland, College Park",
        "url": "https://www.niche.com/colleges/university-of-maryland-college-park/"
    },
    {
        "name": "University of Massachusetts--Amherst",
        "url": "https://www.niche.com/colleges/university-of-massachusetts-amherst/"
    },
    {
        "name": "University of Massachusetts--Boston",
        "url": "https://www.niche.com/colleges/university-of-massachusetts-boston/"
    },
    {
        "name": "University of Massachusetts--Dartmouth",
        "url": "https://www.niche.com/colleges/university-of-massachusetts-dartmouth/"
    },
    {
        "name": "University of Massachusetts--Lowell",
        "url": "https://www.niche.com/colleges/university-of-massachusetts-lowell/"
    },
    {
        "name": "University of Memphis",
        "url": "https://www.niche.com/colleges/university-of-memphis/"
    },
    {
        "name": "University of Miami",
        "url": "https://www.niche.com/colleges/university-of-miami/"
    },
    {
        "name": "University of Michigan--Ann Arbor",
        "url": "https://www.niche.com/colleges/university-of-michigan-ann-arbor/"
    },
    {
        "name": "University of Michigan--Flint",
        "url": "https://www.niche.com/colleges/university-of-michigan-flint/"
    },
    {
        "name": "University of Minnesota--Twin Cities",
        "url": "https://www.niche.com/colleges/university-of-minnesota-twin-cities/"
    },
    {
        "name": "University of Mississippi",
        "url": "https://www.niche.com/colleges/university-of-mississippi/"
    },
    {
        "name": "University of Missouri",
        "url": "https://www.niche.com/colleges/university-of-missouri/"
    },
    {
        "name": "University of Missouri--Kansas City",
        "url": "https://www.niche.com/colleges/university-of-missouri-kansas-city/"
    },
    {
        "name": "University of Missouri--St. Louis",
        "url": "https://www.niche.com/colleges/university-of-missouri-st-louis/"
    },
    {
        "name": "University of Montana",
        "url": "https://www.niche.com/colleges/university-of-montana/"
    },
    {
        "name": "University of Nebraska -- Lincoln",
        "url": "https://www.niche.com/colleges/university-of-nebraska-lincoln/"
    },
    {
        "name": "University of Nebraska Omaha",
        "url": "https://www.niche.com/colleges/university-of-nebraska-omaha/"
    },
    {
        "name": "University of Nevada--Las Vegas",
        "url": "https://www.niche.com/colleges/university-of-nevada-las-vegas/"
    },
    {
        "name": "University of Nevada--Reno",
        "url": "https://www.niche.com/colleges/university-of-nevada-reno/"
    },
    {
        "name": "University of New England",
        "url": "https://www.niche.com/colleges/university-of-new-england/"
    },
    {
        "name": "University of New Hampshire",
        "url": "https://www.niche.com/colleges/university-of-new-hampshire/"
    },
    {
        "name": "University of New Mexico",
        "url": "https://www.niche.com/colleges/university-of-new-mexico/"
    },
    {
        "name": "University of New Orleans",
        "url": "https://www.niche.com/colleges/university-of-new-orleans/"
    },
    {
        "name": "University of North Carolina at Charlotte",
        "url": "https://www.niche.com/colleges/university-of-north-carolina-at-charlotte/"
    },
    {
        "name": "University of North Carolina--Chapel Hill",
        "url": "https://www.niche.com/colleges/university-of-north-carolina-chapel-hill/"
    },
    {
        "name": "University of North Carolina--Greensboro",
        "url": "https://www.niche.com/colleges/university-of-north-carolina-greensboro/"
    },
    {
        "name": "University of North Carolina--Wilmington",
        "url": "https://www.niche.com/colleges/university-of-north-carolina-wilmington/"
    },
    {
        "name": "University of North Dakota",
        "url": "https://www.niche.com/colleges/university-of-north-dakota/"
    },
    {
        "name": "University of North Florida",
        "url": "https://www.niche.com/colleges/university-of-north-florida/"
    },
    {
        "name": "University of North Texas",
        "url": "https://www.niche.com/colleges/university-of-north-texas/"
    },
    {
        "name": "University of Northern Colorado",
        "url": "https://www.niche.com/colleges/university-of-northern-colorado/"
    },
    {
        "name": "University of Notre Dame",
        "url": "https://www.niche.com/colleges/university-of-notre-dame/"
    },
    {
        "name": "University of Oregon",
        "url": "https://www.niche.com/colleges/university-of-oregon/"
    },
    {
        "name": "University of Pennsylvania",
        "url": "https://www.niche.com/colleges/university-of-pennsylvania/"
    },
    {
        "name": "University of Pikeville",
        "url": "https://www.niche.com/colleges/university-of-pikeville/"
    },
    {
        "name": "University of Pittsburgh",
        "url": "https://www.niche.com/colleges/university-of-pittsburgh/"
    },
    {
        "name": "University of Puerto Rico--Rio Piedras",
        "url": "https://www.niche.com/colleges/university-of-puerto-rico-rio-piedras/"
    },
    {
        "name": "University of Rhode Island",
        "url": "https://www.niche.com/colleges/university-of-rhode-island/"
    },
    {
        "name": "University of Rochester",
        "url": "https://www.niche.com/colleges/university-of-rochester/"
    },
    {
        "name": "University of San Diego",
        "url": "https://www.niche.com/colleges/university-of-san-diego/"
    },
    {
        "name": "University of San Francisco",
        "url": "https://www.niche.com/colleges/university-of-san-francisco/"
    },
    {
        "name": "University of South Alabama",
        "url": "https://www.niche.com/colleges/university-of-south-alabama/"
    },
    {
        "name": "University of South Carolina",
        "url": "https://www.niche.com/colleges/university-of-south-carolina/"
    },
    {
        "name": "University of South Dakota",
        "url": "https://www.niche.com/colleges/university-of-south-dakota/"
    },
    {
        "name": "University of South Florida",
        "url": "https://www.niche.com/colleges/university-of-south-florida/"
    },
    {
        "name": "University of Southern California",
        "url": "https://www.niche.com/colleges/university-of-southern-california/"
    },
    {
        "name": "University of Southern Mississippi",
        "url": "https://www.niche.com/colleges/university-of-southern-mississippi/"
    },
    {
        "name": "University of St. Francis",
        "url": "https://www.niche.com/colleges/university-of-st-francis/"
    },
    {
        "name": "University of St. Thomas (MN)",
        "url": "https://www.niche.com/colleges/university-of-st-thomas-mn/"
    },
    {
        "name": "University of St. Thomas (TX)",
        "url": "https://www.niche.com/colleges/university-of-st-thomas-tx/"
    },
    {
        "name": "University of Tennessee at Chattanooga",
        "url": "https://www.niche.com/colleges/university-of-tennessee-at-chattanooga/"
    },
    {
        "name": "University of Tennessee--Knoxville",
        "url": "https://www.niche.com/colleges/university-of-tennessee-knoxville/"
    },
    {
        "name": "University of Tulsa",
        "url": "https://www.niche.com/colleges/university-of-tulsa/"
    },
    {
        "name": "University of Utah",
        "url": "https://www.niche.com/colleges/university-of-utah/"
    },
    {
        "name": "University of Vermont",
        "url": "https://www.niche.com/colleges/university-of-vermont/"
    },
    {
        "name": "University of Virginia",
        "url": "https://www.niche.com/colleges/university-of-virginia/"
    },
    {
        "name": "University of Washington",
        "url": "https://www.niche.com/colleges/university-of-washington/"
    },
    {
        "name": "University of West Georgia",
        "url": "https://www.niche.com/colleges/university-of-west-georgia/"
    },
    {
        "name": "University of Wisconsin--Madison",
        "url": "https://www.niche.com/colleges/university-of-wisconsin-madison/"
    },
    {
        "name": "University of Wisconsin--Milwaukee",
        "url": "https://www.niche.com/colleges/university-of-wisconsin-milwaukee/"
    },
    {
        "name": "University of Wisconsin-Oshkosh",
        "url": "https://www.niche.com/colleges/university-of-wisconsin-oshkosh/"
    },
    {
        "name": "University of Wyoming",
        "url": "https://www.niche.com/colleges/university-of-wyoming/"
    },
    {
        "name": "University of the Cumberlands",
        "url": "https://www.niche.com/colleges/university-of-the-cumberlands/"
    },
    {
        "name": "University of the Incarnate Word",
        "url": "https://www.niche.com/colleges/university-of-the-incarnate-word/"
    },
    {
        "name": "University of the Pacific",
        "url": "https://www.niche.com/colleges/university-of-the-pacific/"
    },
    {
        "name": "Utah State University",
        "url": "https://www.niche.com/colleges/utah-state-university/"
    },
    {
        "name": "Valdosta State University",
        "url": "https://www.niche.com/colleges/valdosta-state-university/"
    },
    {
        "name": "Valparaiso University",
        "url": "https://www.niche.com/colleges/valparaiso-university/"
    },
    {
        "name": "Vanderbilt University",
        "url": "https://www.niche.com/colleges/vanderbilt-university/"
    },
    {
        "name": "Villanova University",
        "url": "https://www.niche.com/colleges/villanova-university/"
    },
    {
        "name": "Virginia Commonwealth University",
        "url": "https://www.niche.com/colleges/virginia-commonwealth-university/"
    },
    {
        "name": "Virginia Tech",
        "url": "https://www.niche.com/colleges/virginia-tech/"
    },
    {
        "name": "Wake Forest University",
        "url": "https://www.niche.com/colleges/wake-forest-university/"
    },
    {
        "name": "Walsh University",
        "url": "https://www.niche.com/colleges/walsh-university/"
    },
    {
        "name": "Washington State University",
        "url": "https://www.niche.com/colleges/washington-state-university/"
    },
    {
        "name": "Washington University in St. Louis",
        "url": "https://www.niche.com/colleges/washington-university-in-st-louis/"
    },
    {
        "name": "Wayne State University",
        "url": "https://www.niche.com/colleges/wayne-state-university/"
    },
    {
        "name": "West Chester University of Pennsylvania",
        "url": "https://www.niche.com/colleges/west-chester-university-of-pennsylvania/"
    },
    {
        "name": "West Virginia University",
        "url": "https://www.niche.com/colleges/west-virginia-university/"
    },
    {
        "name": "Western Carolina University",
        "url": "https://www.niche.com/colleges/western-carolina-university/"
    },
    {
        "name": "Western Kentucky University",
        "url": "https://www.niche.com/colleges/western-kentucky-university/"
    },
    {
        "name": "Western Michigan University",
        "url": "https://www.niche.com/colleges/western-michigan-university/"
    },
    {
        "name": "Western New England University",
        "url": "https://www.niche.com/colleges/western-new-england-university/"
    },
    {
        "name": "Wichita State University",
        "url": "https://www.niche.com/colleges/wichita-state-university/"
    },
    {
        "name": "Widener University",
        "url": "https://www.niche.com/colleges/widener-university/"
    },
    {
        "name": "Wilkes University",
        "url": "https://www.niche.com/colleges/wilkes-university/"
    },
    {
        "name": "William & Mary",
        "url": "https://www.niche.com/colleges/william-and-mary/"
    },
    {
        "name": "William Carey University",
        "url": "https://www.niche.com/colleges/william-carey-university/"
    },
    {
        "name": "William Woods University",
        "url": "https://www.niche.com/colleges/william-woods-university/"
    },
    {
        "name": "Wilmington University",
        "url": "https://www.niche.com/colleges/wilmington-university/"
    },
    {
        "name": "Wingate University",
        "url": "https://www.niche.com/colleges/wingate-university/"
    },
    {
        "name": "Winston-Salem State University",
        "url": "https://www.niche.com/colleges/winston-salem-state-university/"
    },
    {
        "name": "Worcester Polytechnic Institute",
        "url": "https://www.niche.com/colleges/worcester-polytechnic-institute/"
    },
    {
        "name": "Wright State University",
        "url": "https://www.niche.com/colleges/wright-state-university/"
    },
    {
        "name": "Xavier University",
        "url": "https://www.niche.com/colleges/xavier-university/"
    },
    {
        "name": "Yale University",
        "url": "https://www.niche.com/colleges/yale-university/"
    },
    {
        "name": "Yeshiva University",
        "url": "https://www.niche.com/colleges/yeshiva-university/"
    }
]
