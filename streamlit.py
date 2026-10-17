
import streamlit as st
from html import escape

st.set_page_config(
    page_title="The GOAT: Lionel Messi",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

TROPHIES = [
    ("La Liga", "10"),
    ("Champions League", "4"),
    ("Copa del Rey", "7"),
    ("Spanish Super Cup", "8"),
    ("UEFA Super Cup", "3"),
    ("FIFA Club World Cup", "3"),
    ("Ligue 1", "2"),
    ("Trophée des Champions", "1"),
    ("World Cup", "1"),
    ("Copa América", "2"),
    ("Finalissima", "1"),
    ("Olympic Gold", "1"),
    ("U-20 World Cup", "1"),
    ("Leagues Cup", "1"),
    ("Supporters' Shield", "1"),
    ("Eastern Conference", "1"),
    ("MLS Cup", "1"),
]

PERFORMANCES = [
    {
        "match": "Barcelona vs Real Madrid",
        "date": "April 2017",
        "result": "3–2",
        "description": (
            "Messi scored twice in a dramatic El Clásico victory "
            "at the Santiago Bernabéu, including a stoppage-time winner."
        ),
    },
    {
        "match": "Barcelona vs Arsenal",
        "date": "April 2010",
        "result": "4–1",
        "description": (
            "Messi scored all four goals in a sensational Champions "
            "League quarter-final performance at Camp Nou."
        ),
    },
    {
        "match": "Barcelona vs Bayern Munich",
        "date": "May 2015",
        "result": "3–0",
        "description": (
            "Messi scored twice and helped create the third goal "
            "in a memorable Champions League semi-final first leg."
        ),
    },
    {
        "match": "Barcelona vs Getafe",
        "date": "April 2007",
        "result": "5–2",
        "description": (
            "Messi scored an extraordinary solo goal, dribbling past "
            "multiple defenders in a run often compared to Maradona's."
        ),
    },
    {
        "match": "Argentina vs Ecuador",
        "date": "October 2017",
        "result": "3–1",
        "description": (
            "Messi scored a hat-trick to secure Argentina's place "
            "at the 2018 FIFA World Cup."
        ),
    },
    {
        "match": "Argentina vs France",
        "date": "December 2022",
        "result": "4–2 on penalties",
        "description": (
            "Messi scored twice in the World Cup final and converted "
            "his penalty as Argentina won the trophy."
        ),
    },
    {
        "match": "Barcelona vs Manchester United",
        "date": "May 2011",
        "result": "3–1",
        "description": (
            "Messi scored a brilliant long-range goal in the Champions "
            "League final as Barcelona dominated Manchester United."
        ),
    },
    {
        "match": "Argentina vs Croatia",
        "date": "December 2022",
        "result": "3–0",
        "description": (
            "Messi scored a penalty and produced a stunning run and "
            "assist for Julián Álvarez in the World Cup semi-final."
        ),
    },
]

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    box-sizing: border-box;
}

.stApp {
    background: #eef1f7;
    font-family: 'Inter', Arial, sans-serif;
    color: #222;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"],
[data-testid="stDecoration"],
footer {
    display: none !important;
}

.block-container {
    max-width: 1500px;
    padding: 30px 30px 25px !important;
}

.hero {
    position: relative;
    overflow: hidden;
    text-align: center;
    color: white;
    background: linear-gradient(135deg, #ff512f, #dd2476, #1c1c7c);
    border-radius: 22px;
    padding: 42px 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,.15);
    transition: transform .3s, box-shadow .3s;
}

.hero:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 28px rgba(0,0,0,.19);
}

.hero img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    object-position: center;
    border-radius: 50%;
    background: #222;
    border: 5px solid white;
    box-shadow: 0 6px 18px rgba(0,0,0,.25);
    transition: transform .3s;
}

.hero img:hover {
    transform: scale(1.05);
}

.hero h1 {
    color: white;
    font-size: clamp(32px, 5vw, 48px);
    font-weight: 800;
    letter-spacing: 1px;
    margin: 20px 0 5px;
    text-shadow: 2px 2px 5px rgba(0,0,0,.25);
}

.hero p {
    margin: 8px 0 0;
    font-size: 16px;
    color: rgba(255,255,255,.9);
}

.section {
    margin-top: 30px;
    padding: 35px;
    border: 2px solid white;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(102,126,234,.16);
    text-align: center;
}

.trophies {
    background: linear-gradient(135deg, #fff1eb, #e8eaff);
}

.performances {
    background: linear-gradient(135deg, #e8f4ff, #f4e8ff);
}

.section-title {
    margin: 0;
    font-size: clamp(27px, 4vw, 39px);
    font-weight: 800;
    line-height: 1.25;
}

.trophies .section-title {
    color: #5b4bb7;
}

.performances .section-title {
    color: #633c9e;
}

.line {
    width: min(250px, 45%);
    height: 4px;
    border-radius: 10px;
    margin: 17px auto;
    background: linear-gradient(90deg, #ff512f, #dd2476, #667eea);
}

.subtitle {
    font-size: 16px;
    color: #666;
    line-height: 1.7;
    margin: 12px 0 0;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.trophy-card {
    min-height: 145px;
    padding: 23px 15px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: linear-gradient(145deg, #fff, #f1f3ff);
    border: 2px solid #e2e4ff;
    border-radius: 17px;
    box-shadow: 0 5px 15px rgba(102,126,234,.14);
    transition: transform .3s, box-shadow .3s, border-color .3s;
}

.trophy-card:hover {
    transform: translateY(-8px) scale(1.025);
    border-color: #667eea;
    box-shadow: 0 13px 25px rgba(102,126,234,.24);
}

.trophy-card h3 {
    color: #4b3ca7;
    font-size: 17px;
    font-weight: 700;
    line-height: 1.45;
    margin: 0 0 13px;
}

.trophy-count {
    color: #dd2476;
    font-size: 25px;
    font-weight: 800;
}

.trophy-symbol {
    font-size: 20px;
}

.performance-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 30px;
    text-align: left;
}

.performance-card {
    display: flex;
    flex-direction: column;
    min-height: 225px;
    padding: 24px;
    background: linear-gradient(145deg, #fff, #f5f0ff);
    border: 2px solid #e8ddff;
    border-radius: 17px;
    box-shadow: 0 5px 15px rgba(118,75,162,.12);
    transition: transform .3s, box-shadow .3s, border-color .3s;
}

.performance-card:hover {
    transform: translateY(-8px);
    border-color: #764ba2;
    box-shadow: 0 13px 25px rgba(118,75,162,.24);
}

.performance-card h3 {
    font-size: 19px;
    font-weight: 800;
    line-height: 1.45;
    color: #58348c;
    margin: 0 0 9px;
}

.performance-date {
    color: #dd2476;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 14px;
}

.performance-result {
    align-self: flex-start;
    background: #eee6ff;
    color: #58348c;
    padding: 5px 10px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 800;
    margin-bottom: 14px;
}

.performance-card p {
    color: #666;
    font-size: 14px;
    line-height: 1.75;
    margin: 0;
}

.site-footer {
    margin-top: 30px;
    padding: 28px 20px;
    text-align: center;
    color: white;
    background: linear-gradient(135deg, #1c1c7c, #764ba2, #dd2476);
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,.15);
    transition: transform .3s, box-shadow .3s;
}

.site-footer:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(0,0,0,.2);
}

.site-footer h2 {
    color: white;
    font-size: 25px;
    font-weight: 800;
    margin: 0 0 10px;
}

.site-footer p {
    color: rgba(255,255,255,.9);
    font-size: 14px;
    margin: 6px 0;
    line-height: 1.6;
}

@media (max-width: 600px) {
    .block-container {
        padding: 15px 12px 20px !important;
    }

    .hero {
        padding: 30px 12px;
        border-radius: 17px;
    }

    .hero img {
        width: 155px;
        height: 155px;
    }

    .section {
        padding: 25px 14px;
        margin-top: 20px;
        border-radius: 17px;
    }

    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 12px;
    }

    .trophy-card {
        min-height: 130px;
        padding: 17px 10px;
    }

    .trophy-card h3 {
        font-size: 15px;
    }

    .performance-grid {
        grid-template-columns: 1fr;
        gap: 14px;
    }

    .performance-card {
        min-height: auto;
        padding: 21px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        transition-duration: 0.01ms !important;
    }
}
</style>
""")

st.html("""
<header class="hero">
    <img
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCc9mFWHgvHeVAfXs-pkJV3V3cIRWkBbCYz1VBJO81Ax3-ro1K68b8fAo&s=10"
        alt="Lionel Messi"
    >
    <h1><i>Lionel Messi</i></h1>
    <p>Legend. Champion. The GOAT.</p>
</header>
""")

trophy_cards = "".join(
    f"""
    <article class="trophy-card">
        <h3>{escape(name)}</h3>
        <div class="trophy-count">
            {escape(count)}
            <span class="trophy-symbol">{"🥇" if name == "Olympic Gold" else "🏆"}</span>
        </div>
    </article>
    """
    for name, count in TROPHIES
)

st.html(f"""
<section class="section trophies">
    <h2 class="section-title">Trophies</h2>
    <div class="line"></div>
    <p class="subtitle">
        <i>A legendary collection of team honours from Messi's career.</i>
    </p>
    <div class="cards">
        {trophy_cards}
    </div>
</section>
""")

performance_cards = "".join(
    f"""
    <article class="performance-card">
        <h3>{escape(item["match"])}</h3>
        <div class="performance-date">{escape(item["date"])}</div>
        <div class="performance-result">
            {escape(item["result"])}
        </div>
        <p>{escape(item["description"])}</p>
    </article>
    """
    for item in PERFORMANCES
)

st.html(f"""
<section class="section performances">
    <h2 class="section-title">Best Ever Performances</h2>
    <div class="line"></div>
    <p class="subtitle">
        <i>Some of Lionel Messi's most memorable performances.</i>
    </p>
    <div class="performance-grid">
        {performance_cards}
    </div>
</section>
""")


st.html("""
<footer class="site-footer">
    <h2>The GOAT: Lionel Messi</h2>
    <p>A career that inspired millions around the world.</p>
    <p>Football history. Legendary moments. Eternal greatness.</p>
</footer>
""")
