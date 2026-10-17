
import streamlit as st

st.set_page_config(
    page_title="The GOAT: Lionel Messi",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

* {
    box-sizing: border-box;
}

.stApp {
    background: #eef1f7;
    font-family: 'Inter', sans-serif;
    color: #222;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1400px;
    padding: 30px 30px 20px;
}

.hero {
    background: linear-gradient(135deg, #ff512f, #dd2476, #1c1c7c);
    border-radius: 24px;
    padding: 45px 20px;
    text-align: center;
    color: white;
    box-shadow: 0 8px 25px rgba(0,0,0,.15);
    transition: .3s;
}

.hero:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 30px rgba(0,0,0,.2);
}

.hero img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    object-position: center;
    border: 5px solid white;
    border-radius: 50%;
    background: #222;
    box-shadow: 0 6px 15px rgba(0,0,0,.2);
    transition: .3s;
}

.hero img:hover {
    transform: scale(1.05);
}

.hero h1 {
    color: white !important;
    font-size: 44px;
    font-weight: 800;
    margin: 18px 0 0;
    text-shadow: 2px 2px 5px rgba(0,0,0,.25);
}

.section {
    margin-top: 30px;
    padding: 35px;
    border: 2px solid white;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(102,126,234,.15);
}

.trophies {
    background: linear-gradient(135deg,#fff1eb,#e8eaff);
}

.performances {
    background: linear-gradient(135deg,#e8f4ff,#f4e8ff);
}

.section-title {
    text-align: center;
    font-size: 36px;
    font-weight: 800;
    margin: 0;
    color: #5b4bb7;
}

.performances .section-title {
    color: #633c9e;
}

.line {
    width: 35%;
    height: 4px;
    border-radius: 10px;
    margin: 15px auto;
    background: linear-gradient(90deg,#ff512f,#dd2476,#667eea);
}

.subtitle {
    text-align: center;
    font-size: 16px;
    color: #666;
    margin-bottom: 28px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(155px,1fr));
    gap: 18px;
}

.trophy-card {
    min-height: 140px;
    padding: 20px 12px;
    border: 2px solid #e2e4ff;
    border-radius: 16px;
    background: linear-gradient(145deg,#fff,#f1f3ff);
    box-shadow: 0 5px 15px rgba(102,126,234,.12);
    text-align: center;
    transition: .25s;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.trophy-card:hover {
    transform: translateY(-7px) scale(1.025);
    border-color: #667eea;
    box-shadow: 0 12px 25px rgba(102,126,234,.25);
}

.trophy-card h3 {
    color: #4b3ca7;
    font-size: 16px;
    margin: 0 0 13px;
}

.trophy-count {
    color: #dd2476;
    font-size: 24px;
    font-weight: 800;
}

.performance-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(245px,1fr));
    gap: 20px;
}

.performance-card {
    background: linear-gradient(145deg,#fff,#f5f0ff);
    border: 2px solid #e8ddff;
    border-radius: 17px;
    padding: 24px;
    text-align: left;
    box-shadow: 0 5px 15px rgba(118,75,162,.12);
    transition: .25s;
}

.performance-card:hover {
    transform: translateY(-7px);
    border-color: #764ba2;
    box-shadow: 0 12px 25px rgba(118,75,162,.22);
}

.performance-card h3 {
    color: #58348c;
    font-size: 19px;
    margin: 0 0 10px;
}

.performance-card .date {
    color: #dd2476;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 14px;
}

.performance-card p {
    color: #666;
    font-size: 14px;
    line-height: 1.7;
    margin: 0;
}

.footer {
    margin-top: 30px;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    background: linear-gradient(135deg,#1c1c7c,#764ba2,#dd2476);
    box-shadow: 0 8px 20px rgba(0,0,0,.15);
    transition: .3s;
}

.footer:hover {
    transform: translateY(-3px);
}

.footer h2 {
    color: white !important;
    margin: 0 0 8px;
}

.footer p {
    margin: 0;
    opacity: .9;
}

@media (max-width: 600px) {
    .block-container {
        padding: 15px 12px;
    }

    .hero {
        padding: 30px 12px;
    }

    .hero img {
        width: 155px;
        height: 155px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .section {
        padding: 22px 14px;
    }

    .section-title {
        font-size: 27px;
    }
}
</style>
""", unsafe_allow_html=True)


# HEADER

messi_image = (
    "https://encrypted-tbn0.gstatic.com/images"
    "?q=tbn:ANd9GcTCc9mFWHgvHeVAfXs-pkJV3V3cIRWkBbCYz1VBJO81Ax3-ro1K68b8fAo&s=10"
)

st.markdown(f"""
<div class="hero">
    <img src="{messi_image}" alt="Lionel Messi">
    <h1><i>Lionel Messi</i></h1>
</div>
""", unsafe_allow_html=True)


# TROPHIES

trophies = [
    ("La Liga", 10),
    ("Champions League", 4),
    ("Copa del Rey", 7),
    ("Spanish Super Cup", 8),
    ("UEFA Super Cup", 3),
    ("FIFA Club World Cup", 3),
    ("Ligue 1", 2),
    ("Trophée des Champions", 1),
    ("World Cup", 1),
    ("Copa América", 2),
    ("Finalissima", 1),
    ("Olympic Gold", 1),
    ("U-20 World Cup", 1),
    ("Leagues Cup", 1),
    ("Supporters' Shield", 1),
    ("Eastern Conference", 1),
    ("MLS Cup", 1),
]

trophy_html = "".join(
    f"""
    <div class="trophy-card">
        <h3>{name}</h3>
        <div class="trophy-count">
            {count} {"🥇" if name == "Olympic Gold" else "🏆"}
        </div>
    </div>
    """
    for name, count in trophies
)

st.markdown(f"""
<section class="section trophies">
    <h2 class="section-title">Trophies</h2>
    <div class="line"></div>
    <p class="subtitle">
        <i>Lionel Messi is praised for having the most trophies.</i>
    </p>
    <div class="cards">
        {trophy_html}
    </div>
</section>
""", unsafe_allow_html=True)


# BEST PERFORMANCES

performances = [
    (
        "Barcelona vs Real Madrid",
        "April 2017",
        "Messi scored twice, including a last-minute winner, "
        "to give Barcelona a dramatic 3–2 victory at the Bernabéu."
    ),
    (
        "Barcelona vs Arsenal",
        "April 2010",
        "Messi scored all four goals in a legendary Champions "
        "League performance as Barcelona won 4–1."
    ),
    (
        "Barcelona vs Bayern Munich",
        "May 2015",
        "Messi scored twice and helped create another goal in "
        "a famous 3–0 Champions League victory."
    ),
    (
        "Barcelona vs Getafe",
        "April 2007",
        "Messi scored an iconic solo goal after dribbling past "
        "multiple opponents in Barcelona's 5–2 victory."
    ),
    (
        "Argentina vs Ecuador",
        "October 2017",
        "Messi scored a hat-trick to send Argentina to the "
        "2018 World Cup."
    ),
    (
        "Argentina vs France",
        "December 2022",
        "Messi scored twice in the final and converted his "
        "penalty as Argentina won the World Cup."
    ),
    (
        "Barcelona vs Manchester United",
        "May 2009",
        "Messi scored a memorable header as Barcelona defeated "
        "Manchester United 2–0 in the Champions League final."
    ),
    (
        "Barcelona vs Manchester United",
        "May 2011",
        "Messi scored from outside the box and inspired "
        "Barcelona's 3–1 Champions League final victory."
    ),
]

performance_html = "".join(
    f"""
    <div class="performance-card">
        <h3>{title}</h3>
        <div class="date">{date}</div>
        <p>{description}</p>
    </div>
    """
    for title, date, description in performances
)

st.markdown(f"""
<section class="section performances">
    <h2 class="section-title">Best Ever Performances</h2>
    <div class="line"></div>
    <p class="subtitle">
        <i>Some of Lionel Messi's greatest individual performances.</i>
    </p>
    <div class="performance-grid">
        {performance_html}
    </div>
</section>
""", unsafe_allow_html=True)


# FOOTER

st.markdown("""
<div class="footer">
    <h2>🐐 Lionel Messi</h2>
    <p>The GOAT of Football</p>
</div>
""", unsafe_allow_html=True)
