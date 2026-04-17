from typing import Dict, List


def get_school_list() -> List[Dict[str, str]]:
    """
    U.S. News National Liberal Arts Colleges list, formatted for Niche scraping.

    Source for school names/rank membership:
    Andrew Reiter historical U.S. News dataset (updated through 2026).
    Live U.S. News pages are blocked in this environment, so this file was generated
    from the public historical dataset instead.

    Note: the 2026 dataset contains 201 ranked schools.
    """

    return [
        {
            "name": 'Williams College',
            "url": 'https://www.niche.com/colleges/williams-college/'
        },
        {
            "name": 'Amherst College',
            "url": 'https://www.niche.com/colleges/amherst-college/'
        },
        {
            "name": 'United States Naval Academy',
            "url": 'https://www.niche.com/colleges/united-states-naval-academy/'
        },
        {
            "name": 'Swarthmore College',
            "url": 'https://www.niche.com/colleges/swarthmore-college/'
        },
        {
            "name": 'Bowdoin College',
            "url": 'https://www.niche.com/colleges/bowdoin-college/'
        },
        {
            "name": 'United States Air Force Academy',
            "url": 'https://www.niche.com/colleges/united-states-air-force-academy/'
        },
        {
            "name": 'Pomona College',
            "url": 'https://www.niche.com/colleges/pomona-college/'
        },
        {
            "name": 'Wellesley College',
            "url": 'https://www.niche.com/colleges/wellesley-college/'
        },
        {
            "name": 'Claremont McKenna College',
            "url": 'https://www.niche.com/colleges/claremont-mckenna-college/'
        },
        {
            "name": 'United States Military Academy',
            "url": 'https://www.niche.com/colleges/united-states-military-academy/'
        },
        {
            "name": 'Carleton College',
            "url": 'https://www.niche.com/colleges/carleton-college/'
        },
        {
            "name": 'Harvey Mudd College',
            "url": 'https://www.niche.com/colleges/harvey-mudd-college/'
        },
        {
            "name": 'Vassar College',
            "url": 'https://www.niche.com/colleges/vassar-college/'
        },
        {
            "name": 'Barnard College',
            "url": 'https://www.niche.com/colleges/barnard-college/'
        },
        {
            "name": 'Wesleyan University',
            "url": 'https://www.niche.com/colleges/wesleyan-university/'
        },
        {
            "name": 'Davidson College',
            "url": 'https://www.niche.com/colleges/davidson-college/'
        },
        {
            "name": 'Hamilton College',
            "url": 'https://www.niche.com/colleges/hamilton-college/'
        },
        {
            "name": 'Smith College',
            "url": 'https://www.niche.com/colleges/smith-college/'
        },
        {
            "name": 'Grinnell College',
            "url": 'https://www.niche.com/colleges/grinnell-college/'
        },
        {
            "name": 'Middlebury College',
            "url": 'https://www.niche.com/colleges/middlebury-college/'
        },
        {
            "name": 'Washington and Lee University',
            "url": 'https://www.niche.com/colleges/washington-and-lee-university/'
        },
        {
            "name": 'Colgate University',
            "url": 'https://www.niche.com/colleges/colgate-university/'
        },
        {
            "name": 'University of Richmond',
            "url": 'https://www.niche.com/colleges/university-of-richmond/'
        },
        {
            "name": 'Haverford College',
            "url": 'https://www.niche.com/colleges/haverford-college/'
        },
        {
            "name": 'Colby College',
            "url": 'https://www.niche.com/colleges/colby-college/'
        },
        {
            "name": 'Bates College',
            "url": 'https://www.niche.com/colleges/bates-college/'
        },
        {
            "name": 'College of the Holy Cross',
            "url": 'https://www.niche.com/colleges/college-of-the-holy-cross/'
        },
        {
            "name": 'Macalester College',
            "url": 'https://www.niche.com/colleges/macalester-college/'
        },
        {
            "name": 'Mount Holyoke College',
            "url": 'https://www.niche.com/colleges/mount-holyoke-college/'
        },
        {
            "name": 'Colorado College',
            "url": 'https://www.niche.com/colleges/colorado-college/'
        },
        {
            "name": 'Bryn Mawr College',
            "url": 'https://www.niche.com/colleges/bryn-mawr-college/'
        },
        {
            "name": 'Bucknell University',
            "url": 'https://www.niche.com/colleges/bucknell-university/'
        },
        {
            "name": 'Lafayette College',
            "url": 'https://www.niche.com/colleges/lafayette-college/'
        },
        {
            "name": 'Denison University',
            "url": 'https://www.niche.com/colleges/denison-university/'
        },
        {
            "name": 'Franklin and Marshall College',
            "url": 'https://www.niche.com/colleges/franklin-and-marshall-college/'
        },
        {
            "name": 'Occidental College',
            "url": 'https://www.niche.com/colleges/occidental-college/'
        },
        {
            "name": 'Skidmore College',
            "url": 'https://www.niche.com/colleges/skidmore-college/'
        },
        {
            "name": 'Pitzer College',
            "url": 'https://www.niche.com/colleges/pitzer-college/'
        },
        {
            "name": 'Trinity College',
            "url": 'https://www.niche.com/colleges/trinity-college/'
        },
        {
            "name": 'Spelman College',
            "url": 'https://www.niche.com/colleges/spelman-college/'
        },
        {
            "name": 'Trinity University',
            "url": 'https://www.niche.com/colleges/trinity-university/'
        },
        {
            "name": 'Scripps College',
            "url": 'https://www.niche.com/colleges/scripps-college/'
        },
        {
            "name": 'Soka University of America',
            "url": 'https://www.niche.com/colleges/soka-university-of-america/'
        },
        {
            "name": 'Union College',
            "url": 'https://www.niche.com/colleges/union-college/'
        },
        {
            "name": 'Berea College',
            "url": 'https://www.niche.com/colleges/berea-college/'
        },
        {
            "name": 'Kenyon College',
            "url": 'https://www.niche.com/colleges/kenyon-college/'
        },
        {
            "name": 'Dickinson College',
            "url": 'https://www.niche.com/colleges/dickinson-college/'
        },
        {
            "name": 'Furman University',
            "url": 'https://www.niche.com/colleges/furman-university/'
        },
        {
            "name": 'Sewanee: The University of the South',
            "url": 'https://www.niche.com/colleges/sewanee-the-university-of-the-south/'
        },
        {
            "name": 'Hillsdale College',
            "url": 'https://www.niche.com/colleges/hillsdale-college/'
        },
        {
            "name": 'St. Olaf College',
            "url": 'https://www.niche.com/colleges/st-olaf-college/'
        },
        {
            "name": 'Wheaton College',
            "url": 'https://www.niche.com/colleges/wheaton-college/'
        },
        {
            "name": 'Connecticut College',
            "url": 'https://www.niche.com/colleges/connecticut-college/'
        },
        {
            "name": 'Wabash College',
            "url": 'https://www.niche.com/colleges/wabash-college/'
        },
        {
            "name": 'Centre College',
            "url": 'https://www.niche.com/colleges/centre-college/'
        },
        {
            "name": 'Rhodes College',
            "url": 'https://www.niche.com/colleges/rhodes-college/'
        },
        {
            "name": 'Thomas Aquinas College',
            "url": 'https://www.niche.com/colleges/thomas-aquinas-college/'
        },
        {
            "name": 'DePauw University',
            "url": 'https://www.niche.com/colleges/depauw-university/'
        },
        {
            "name": 'Whitman College',
            "url": 'https://www.niche.com/colleges/whitman-college/'
        },
        {
            "name": 'Oberlin College and Conservatory',
            "url": 'https://www.niche.com/colleges/oberlin-college-and-conservatory/'
        },
        {
            "name": 'Gettysburg College',
            "url": 'https://www.niche.com/colleges/gettysburg-college/'
        },
        {
            "name": 'St. Lawrence University',
            "url": 'https://www.niche.com/colleges/st-lawrence-university/'
        },
        {
            "name": 'Reed College',
            "url": 'https://www.niche.com/colleges/reed-college/'
        },
        {
            "name": 'Principia College',
            "url": 'https://www.niche.com/colleges/principia-college/'
        },
        {
            "name": 'Virginia Military Institute',
            "url": 'https://www.niche.com/colleges/virginia-military-institute/'
        },
        {
            "name": 'Lawrence University',
            "url": 'https://www.niche.com/colleges/lawrence-university/'
        },
        {
            "name": 'Agnes Scott College',
            "url": 'https://www.niche.com/colleges/agnes-scott-college/'
        },
        {
            "name": 'Wofford College',
            "url": 'https://www.niche.com/colleges/wofford-college/'
        },
        {
            "name": 'Kalamazoo College',
            "url": 'https://www.niche.com/colleges/kalamazoo-college/'
        },
        {
            "name": 'Gustavus Adolphus College',
            "url": 'https://www.niche.com/colleges/gustavus-adolphus-college/'
        },
        {
            "name": 'Bard College',
            "url": 'https://www.niche.com/colleges/bard-college/'
        },
        {
            "name": 'Muhlenberg College',
            "url": 'https://www.niche.com/colleges/muhlenberg-college/'
        },
        {
            "name": 'College of St. Benedict',
            "url": 'https://www.niche.com/colleges/college-of-st-benedict/'
        },
        {
            "name": 'Hobart and William Smith Colleges',
            "url": 'https://www.niche.com/colleges/hobart-and-william-smith-colleges/'
        },
        {
            "name": 'Lake Forest College',
            "url": 'https://www.niche.com/colleges/lake-forest-college/'
        },
        {
            "name": 'Wheaton College',
            "url": 'https://www.niche.com/colleges/wheaton-college/'
        },
        {
            "name": 'Earlham College',
            "url": 'https://www.niche.com/colleges/earlham-college/'
        },
        {
            "name": 'College of Wooster',
            "url": 'https://www.niche.com/colleges/college-of-wooster/'
        },
        {
            "name": 'Willamette University',
            "url": 'https://www.niche.com/colleges/willamette-university/'
        },
        {
            "name": 'Allegheny College',
            "url": 'https://www.niche.com/colleges/allegheny-college/'
        },
        {
            "name": 'Knox College',
            "url": 'https://www.niche.com/colleges/knox-college/'
        },
        {
            "name": "St. John's University",
            "url": 'https://www.niche.com/colleges/st-johns-university/'
        },
        {
            "name": 'Stonehill College',
            "url": 'https://www.niche.com/colleges/stonehill-college/'
        },
        {
            "name": "Saint Mary's College",
            "url": 'https://www.niche.com/colleges/saint-marys-college/'
        },
        {
            "name": "St. John's College",
            "url": 'https://www.niche.com/colleges/st-johns-college/'
        },
        {
            "name": 'Ursinus College',
            "url": 'https://www.niche.com/colleges/ursinus-college/'
        },
        {
            "name": 'Southwestern University',
            "url": 'https://www.niche.com/colleges/southwestern-university/'
        },
        {
            "name": 'Austin College',
            "url": 'https://www.niche.com/colleges/austin-college/'
        },
        {
            "name": 'Drew University',
            "url": 'https://www.niche.com/colleges/drew-university/'
        },
        {
            "name": 'Washington and Jefferson College',
            "url": 'https://www.niche.com/colleges/washington-and-jefferson-college/'
        },
        {
            "name": 'Hope College',
            "url": 'https://www.niche.com/colleges/hope-college/'
        },
        {
            "name": 'Juniata College',
            "url": 'https://www.niche.com/colleges/juniata-college/'
        },
        {
            "name": 'Beloit College',
            "url": 'https://www.niche.com/colleges/beloit-college/'
        },
        {
            "name": 'Washington College',
            "url": 'https://www.niche.com/colleges/washington-college/'
        },
        {
            "name": 'Whittier College',
            "url": 'https://www.niche.com/colleges/whittier-college/'
        },
        {
            "name": 'Saint Anselm College',
            "url": 'https://www.niche.com/colleges/saint-anselm-college/'
        },
        {
            "name": 'University of Puget Sound',
            "url": 'https://www.niche.com/colleges/university-of-puget-sound/'
        },
        {
            "name": 'Morehouse College',
            "url": 'https://www.niche.com/colleges/morehouse-college/'
        },
        {
            "name": "St. Mary's College of Maryland",
            "url": 'https://www.niche.com/colleges/st-marys-college-of-maryland/'
        },
        {
            "name": 'Augustana College',
            "url": 'https://www.niche.com/colleges/augustana-college/'
        },
        {
            "name": 'Lycoming College',
            "url": 'https://www.niche.com/colleges/lycoming-college/'
        },
        {
            "name": 'Lewis & Clark College',
            "url": 'https://www.niche.com/colleges/lewis-and-clark-college/'
        },
        {
            "name": 'Randolph-Macon College',
            "url": 'https://www.niche.com/colleges/randolph-macon-college/'
        },
        {
            "name": 'Susquehanna University',
            "url": 'https://www.niche.com/colleges/susquehanna-university/'
        },
        {
            "name": "St. John's College",
            "url": 'https://www.niche.com/colleges/st-johns-college/'
        },
        {
            "name": 'Hendrix College',
            "url": 'https://www.niche.com/colleges/hendrix-college/'
        },
        {
            "name": 'Hampden-Sydney College',
            "url": 'https://www.niche.com/colleges/hampden-sydney-college/'
        },
        {
            "name": 'Patrick Henry College',
            "url": 'https://www.niche.com/colleges/patrick-henry-college/'
        },
        {
            "name": 'Sarah Lawrence College',
            "url": 'https://www.niche.com/colleges/sarah-lawrence-college/'
        },
        {
            "name": 'Transylvania University',
            "url": 'https://www.niche.com/colleges/transylvania-university/'
        },
        {
            "name": 'St. Norbert College',
            "url": 'https://www.niche.com/colleges/st-norbert-college/'
        },
        {
            "name": 'Linfield College',
            "url": 'https://www.niche.com/colleges/linfield-college/'
        },
        {
            "name": 'Luther College',
            "url": 'https://www.niche.com/colleges/luther-college/'
        },
        {
            "name": 'Illinois College',
            "url": 'https://www.niche.com/colleges/illinois-college/'
        },
        {
            "name": 'Hanover College',
            "url": 'https://www.niche.com/colleges/hanover-college/'
        },
        {
            "name": 'Westmont College',
            "url": 'https://www.niche.com/colleges/westmont-college/'
        },
        {
            "name": 'Massachusetts College of Liberal Arts',
            "url": 'https://www.niche.com/colleges/massachusetts-college-of-liberal-arts/'
        },
        {
            "name": "Saint Michael's College",
            "url": 'https://www.niche.com/colleges/saint-michaels-college/'
        },
        {
            "name": 'University of Minnesota Morris',
            "url": 'https://www.niche.com/colleges/university-of-minnesota-morris/'
        },
        {
            "name": 'Meredith College',
            "url": 'https://www.niche.com/colleges/meredith-college/'
        },
        {
            "name": 'Westminster College',
            "url": 'https://www.niche.com/colleges/westminster-college/'
        },
        {
            "name": 'Bennington College',
            "url": 'https://www.niche.com/colleges/bennington-college/'
        },
        {
            "name": 'Saint Vincent College',
            "url": 'https://www.niche.com/colleges/saint-vincent-college/'
        },
        {
            "name": 'Ohio Wesleyan University',
            "url": 'https://www.niche.com/colleges/ohio-wesleyan-university/'
        },
        {
            "name": 'Cornell College',
            "url": 'https://www.niche.com/colleges/cornell-college/'
        },
        {
            "name": 'Covenant College',
            "url": 'https://www.niche.com/colleges/covenant-college/'
        },
        {
            "name": 'Roanoke College',
            "url": 'https://www.niche.com/colleges/roanoke-college/'
        },
        {
            "name": 'Goucher College',
            "url": 'https://www.niche.com/colleges/goucher-college/'
        },
        {
            "name": 'Coe College',
            "url": 'https://www.niche.com/colleges/coe-college/'
        },
        {
            "name": 'College of the Atlantic',
            "url": 'https://www.niche.com/colleges/college-of-the-atlantic/'
        },
        {
            "name": 'Albion College',
            "url": 'https://www.niche.com/colleges/albion-college/'
        },
        {
            "name": 'Central College',
            "url": 'https://www.niche.com/colleges/central-college/'
        },
        {
            "name": 'University of Mary Washington',
            "url": 'https://www.niche.com/colleges/university-of-mary-washington/'
        },
        {
            "name": 'State University of New York at Purchase College',
            "url": 'https://www.niche.com/colleges/state-university-of-new-york-at-purchase-college/'
        },
        {
            "name": 'New College of Florida',
            "url": 'https://www.niche.com/colleges/new-college-of-florida/'
        },
        {
            "name": 'Eckerd College',
            "url": 'https://www.niche.com/colleges/eckerd-college/'
        },
        {
            "name": 'Concordia College at Moorhead',
            "url": 'https://www.niche.com/colleges/concordia-college-at-moorhead/'
        },
        {
            "name": 'University of North Carolina at Asheville',
            "url": 'https://www.niche.com/colleges/university-of-north-carolina-at-asheville/'
        },
        {
            "name": 'Hollins University',
            "url": 'https://www.niche.com/colleges/hollins-university/'
        },
        {
            "name": 'Emmanuel College',
            "url": 'https://www.niche.com/colleges/emmanuel-college/'
        },
        {
            "name": 'University of New Hampshire at Manchester',
            "url": 'https://www.niche.com/colleges/university-of-new-hampshire-at-manchester/'
        },
        {
            "name": 'Claflin University',
            "url": 'https://www.niche.com/colleges/claflin-university/'
        },
        {
            "name": 'Salem College',
            "url": 'https://www.niche.com/colleges/salem-college/'
        },
        {
            "name": 'Centenary College of Louisiana',
            "url": 'https://www.niche.com/colleges/centenary-college-of-louisiana/'
        },
        {
            "name": 'Ripon College',
            "url": 'https://www.niche.com/colleges/ripon-college/'
        },
        {
            "name": 'Millsaps College',
            "url": 'https://www.niche.com/colleges/millsaps-college/'
        },
        {
            "name": 'Franklin College',
            "url": 'https://www.niche.com/colleges/franklin-college/'
        },
        {
            "name": 'Aquinas College',
            "url": 'https://www.niche.com/colleges/aquinas-college/'
        },
        {
            "name": 'Houghton College',
            "url": 'https://www.niche.com/colleges/houghton-college/'
        },
        {
            "name": 'New Saint Andrews College',
            "url": 'https://www.niche.com/colleges/new-saint-andrews-college/'
        },
        {
            "name": 'Hartwick College',
            "url": 'https://www.niche.com/colleges/hartwick-college/'
        },
        {
            "name": 'Ouachita Baptist University',
            "url": 'https://www.niche.com/colleges/ouachita-baptist-university/'
        },
        {
            "name": 'University of Puerto Rico in Cayey',
            "url": 'https://www.niche.com/colleges/university-of-puerto-rico-in-cayey/'
        },
        {
            "name": 'Monmouth College',
            "url": 'https://www.niche.com/colleges/monmouth-college/'
        },
        {
            "name": 'Bethany Lutheran College',
            "url": 'https://www.niche.com/colleges/bethany-lutheran-college/'
        },
        {
            "name": 'Hampshire College',
            "url": 'https://www.niche.com/colleges/hampshire-college/'
        },
        {
            "name": 'Dillard University',
            "url": 'https://www.niche.com/colleges/dillard-university/'
        },
        {
            "name": 'Oglethorpe University',
            "url": 'https://www.niche.com/colleges/oglethorpe-university/'
        },
        {
            "name": 'Fisk University',
            "url": 'https://www.niche.com/colleges/fisk-university/'
        },
        {
            "name": 'Wartburg College',
            "url": 'https://www.niche.com/colleges/wartburg-college/'
        },
        {
            "name": 'Gordon College',
            "url": 'https://www.niche.com/colleges/gordon-college/'
        },
        {
            "name": 'Randolph College',
            "url": 'https://www.niche.com/colleges/randolph-college/'
        },
        {
            "name": 'Presbyterian College',
            "url": 'https://www.niche.com/colleges/presbyterian-college/'
        },
        {
            "name": 'Wittenberg University',
            "url": 'https://www.niche.com/colleges/wittenberg-university/'
        },
        {
            "name": 'Westminster College',
            "url": 'https://www.niche.com/colleges/westminster-college/'
        },
        {
            "name": 'Sweet Briar College',
            "url": 'https://www.niche.com/colleges/sweet-briar-college/'
        },
        {
            "name": 'Bridgewater College',
            "url": 'https://www.niche.com/colleges/bridgewater-college/'
        },
        {
            "name": 'Lyon College',
            "url": 'https://www.niche.com/colleges/lyon-college/'
        },
        {
            "name": "University of Virginia's College at Wise",
            "url": 'https://www.niche.com/colleges/university-of-virginias-college-at-wise/'
        },
        {
            "name": 'Albright College',
            "url": 'https://www.niche.com/colleges/albright-college/'
        },
        {
            "name": 'Maryville College',
            "url": 'https://www.niche.com/colleges/maryville-college/'
        },
        {
            "name": 'Guilford College',
            "url": 'https://www.niche.com/colleges/guilford-college/'
        },
        {
            "name": 'Johnson C. Smith University',
            "url": 'https://www.niche.com/colleges/johnson-c-smith-university/'
        },
        {
            "name": 'Simpson University',
            "url": 'https://www.niche.com/colleges/simpson-university/'
        },
        {
            "name": 'Ava Maria University',
            "url": 'https://www.niche.com/colleges/ava-maria-university/'
        },
        {
            "name": 'Medgar Evers College-CUNY',
            "url": 'https://www.niche.com/colleges/medgar-evers-college-cuny/'
        },
        {
            "name": 'Providence Christian College',
            "url": 'https://www.niche.com/colleges/providence-christian-college/'
        },
        {
            "name": 'Virginia Wesleyan University',
            "url": 'https://www.niche.com/colleges/virginia-wesleyan-university/'
        },
        {
            "name": 'Marymount Manhattan College',
            "url": 'https://www.niche.com/colleges/marymount-manhattan-college/'
        },
        {
            "name": 'Georgetown College',
            "url": 'https://www.niche.com/colleges/georgetown-college/'
        },
        {
            "name": 'Bryn Athyn College of the New Church',
            "url": 'https://www.niche.com/colleges/bryn-athyn-college-of-the-new-church/'
        },
        {
            "name": 'Tougaloo College',
            "url": 'https://www.niche.com/colleges/tougaloo-college/'
        },
        {
            "name": 'Antioch College',
            "url": 'https://www.niche.com/colleges/antioch-college/'
        },
        {
            "name": 'Oakwood University',
            "url": 'https://www.niche.com/colleges/oakwood-university/'
        },
        {
            "name": 'Bethune-Cookman University',
            "url": 'https://www.niche.com/colleges/bethune-cookman-university/'
        },
        {
            "name": 'Holy Cross College at Notre Dame, Indiana',
            "url": 'https://www.niche.com/colleges/holy-cross-college-at-notre-dame-indiana/'
        },
        {
            "name": 'Southern Virginia University',
            "url": 'https://www.niche.com/colleges/southern-virginia-university/'
        },
        {
            "name": 'Bennett College',
            "url": 'https://www.niche.com/colleges/bennett-college/'
        },
        {
            "name": 'Allen University',
            "url": 'https://www.niche.com/colleges/allen-university/'
        },
        {
            "name": 'Bethany College',
            "url": 'https://www.niche.com/colleges/bethany-college/'
        },
        {
            "name": 'Cheyney University of Pennsylvania',
            "url": 'https://www.niche.com/colleges/cheyney-university-of-pennsylvania/'
        },
        {
            "name": 'East-West University',
            "url": 'https://www.niche.com/colleges/east-west-university/'
        },
        {
            "name": 'Hebrew Theological College',
            "url": 'https://www.niche.com/colleges/hebrew-theological-college/'
        },
        {
            "name": 'Lane College',
            "url": 'https://www.niche.com/colleges/lane-college/'
        },
        {
            "name": 'Rust College',
            "url": 'https://www.niche.com/colleges/rust-college/'
        },
        {
            "name": 'University of Pittsburgh at Greensburg',
            "url": 'https://www.niche.com/colleges/university-of-pittsburgh-at-greensburg/'
        },
        {
            "name": 'University of Science and Arts of Oklahoma',
            "url": 'https://www.niche.com/colleges/university-of-science-and-arts-of-oklahoma/'
        },
        {
            "name": 'Virginia Union University',
            "url": 'https://www.niche.com/colleges/virginia-union-university/'
        },
        {
            "name": 'Warren Wilson College',
            "url": 'https://www.niche.com/colleges/warren-wilson-college/'
        },
        {
            "name": 'Young Harris College',
            "url": 'https://www.niche.com/colleges/young-harris-college/'
        },
        {
            "name": 'Pennsylvania State University at Brandywine',
            "url": 'https://www.niche.com/colleges/pennsylvania-state-university-at-brandywine/'
        },
    ]
