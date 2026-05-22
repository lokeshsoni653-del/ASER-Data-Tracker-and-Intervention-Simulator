# =============================================================================
# ITA Education Emergency & ASER Data Tracker
# Portfolio Project — Parwaaz Internship Application
# Idara-e-Taleem-o-Aagahi (ITA)
# =============================================================================
# Architecture: Streamlit · Pandas · NumPy · Plotly · Folium
# Author: Parwaaz Applicant Portfolio
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

# ── Page config must be the very first Streamlit call ─────────────────────────
st.set_page_config(
    page_title="ITA Education Emergency & ASER Data Tracker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================================================================
# SECTION 0 — CUSTOM CSS (Premium NGO Aesthetic)
# Deep corporate blues (#003366) + intervention greens (#2CA02C)
# Light theme, elevated cards, smooth hover effects
# =============================================================================
st.markdown("""
<style>
/* ── Google Font Import ───────────────────────────────────────────────── */
@import url('[fonts.googleapis.com](https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap)');

/* ── Global Reset & Base ──────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F4F6FA;
    color: #1A1A2E;
}

/* ── Hide Streamlit Default Chrome ───────────────────────────────────── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 1.5rem 2.5rem 2rem 2.5rem;
    max-width: 1600px;
}

/* ── Hero Banner ─────────────────────────────────────────────────────── */
.hero-banner {
    background: linear-gradient(135deg, #003366 0%, #005599 60%, #0077CC 100%);
    border-radius: 16px;
    padding: 2.2rem 2.8rem;
    margin-bottom: 1.6rem;
    box-shadow: 0 8px 32px rgba(0, 51, 102, 0.25);
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -40%;
    right: -10%;
    width: 420px;
    height: 420px;
    background: radial-gradient(circle, rgba(255,255,255,0.07) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    color: #FFFFFF;
    font-size: 2rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin: 0 0 0.3rem 0;
}
.hero-subtitle {
    color: rgba(255,255,255,0.78);
    font-size: 0.95rem;
    font-weight: 400;
    margin: 0;
}
.hero-badge {
    display: inline-block;
    background: rgba(44, 160, 44, 0.85);
    color: #fff;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    margin-bottom: 0.8rem;
}

/* ── Filter Bar ──────────────────────────────────────────────────────── */
.filter-bar {
    background: #FFFFFF;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    margin-bottom: 1.6rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border: 1px solid #E8EDF5;
}
.filter-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #003366;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 0.3rem;
}

/* ── KPI Cards ───────────────────────────────────────────────────────── */
.kpi-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 4px 20px rgba(0, 51, 102, 0.10);
    border: 1px solid #E4EBF5;
    border-top: 4px solid #003366;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
    position: relative;
    overflow: hidden;
}
.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 32px rgba(0, 51, 102, 0.18);
}
.kpi-card.green { border-top-color: #2CA02C; }
.kpi-card.amber { border-top-color: #E07B00; }
.kpi-card.red   { border-top-color: #C0392B; }

.kpi-icon {
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
    display: block;
}
.kpi-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #6B7A99;
    text-transform: uppercase;
    letter-spacing: 0.9px;
    margin-bottom: 0.4rem;
}
.kpi-value {
    font-size: 2.1rem;
    font-weight: 800;
    color: #003366;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.kpi-value.green { color: #2CA02C; }
.kpi-value.amber { color: #E07B00; }
.kpi-value.red   { color: #C0392B; }
.kpi-delta {
    font-size: 0.78rem;
    font-weight: 500;
    color: #8896B0;
}

/* ── Section Headers ─────────────────────────────────────────────────── */
.section-header {
    font-size: 1.05rem;
    font-weight: 700;
    color: #003366;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #E4EBF5;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

/* ── Chart Container ─────────────────────────────────────────────────── */
.chart-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 4px 20px rgba(0, 51, 102, 0.08);
    border: 1px solid #E4EBF5;
}

/* ── Simulator Panel ─────────────────────────────────────────────────── */
.simulator-panel {
    background: linear-gradient(135deg, #003366 0%, #004F8B 100%);
    border-radius: 16px;
    padding: 2rem 2.4rem;
    margin-top: 1.6rem;
    box-shadow: 0 8px 32px rgba(0, 51, 102, 0.22);
}
.simulator-title {
    color: #FFFFFF;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}
.simulator-subtitle {
    color: rgba(255,255,255,0.65);
    font-size: 0.85rem;
    margin-bottom: 1.5rem;
}
.sim-result-box {
    background: rgba(255,255,255,0.10);
    border-radius: 12px;
    padding: 1.6rem;
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}
.sim-result-value {
    font-size: 3.5rem;
    font-weight: 800;
    color: #2CA02C;
    line-height: 1;
}
.sim-result-label {
    color: rgba(255,255,255,0.8);
    font-size: 0.88rem;
    margin-top: 0.4rem;
}
.sim-metric-row {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}
.sim-metric {
    flex: 1;
    background: rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    border: 1px solid rgba(255,255,255,0.12);
}
.sim-metric-val {
    font-size: 1.4rem;
    font-weight: 700;
    color: #FFFFFF;
}
.sim-metric-lbl {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.6);
    text-transform: uppercase;
    letter-spacing: 0.7px;
}

/* ── Streamlit widget overrides ───────────────────────────────────────── */
div[data-testid="stSelectbox"] > div:first-child,
div[data-testid="stMultiSelect"] > div:first-child {
    border-radius: 8px !important;
}
div[data-testid="stSlider"] .stSlider { padding: 0; }
.stRadio > label { color: rgba(255,255,255,0.85) !important; font-size: 0.88rem; }
.stRadio > div { gap: 1.2rem; }

/* ── Divider ─────────────────────────────────────────────────────────── */
.custom-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #D0DAF0, transparent);
    margin: 1.8rem 0;
}

/* ── Map container rounded corners ───────────────────────────────────── */
iframe { border-radius: 12px; }

</style>
""", unsafe_allow_html=True)


# =============================================================================
# SECTION 1 — SYNTHETIC DATA GENERATION
# High-fidelity, ASER-aligned district-level data for Pakistan
# Cached for performance — only regenerates on cache miss
# =============================================================================

@st.cache_data
def generate_district_data() -> pd.DataFrame:
    """
    Generate realistic synthetic education data for 20 Pakistani districts
    across all four provinces. Figures are calibrated against published
    ASER Pakistan reports (2021–2023) and Pakistan Social & Living Standards
    Measurement (PSLM) surveys.

    Returns:
        pd.DataFrame: One row per district with OOSC, literacy, infrastructure,
                      dropout, and geospatial columns.
    """
    np.random.seed(42)  # Reproducible synthetic data

    # ── District master list with realistic lat/lon centroids ──────────────
    districts = [
        # (District, Province, Zone, Latitude, Longitude)
        ("Karachi",       "Sindh",       "Urban",  24.8607,  67.0011),
        ("Hyderabad",     "Sindh",       "Urban",  25.3960,  68.3578),
        ("Sukkur",        "Sindh",       "Rural",  27.7052,  68.8574),
        ("Jacobabad",     "Sindh",       "Rural",  28.2769,  68.4514),
        ("Tharparkar",    "Sindh",       "Rural",  24.7161,  70.2433),
        ("Lahore",        "Punjab",      "Urban",  31.5204,  74.3587),
        ("Multan",        "Punjab",      "Urban",  30.1575,  71.5249),
        ("Rahim Yar Khan","Punjab",      "Rural",  28.4200,  70.2950),
        ("Muzaffargarh",  "Punjab",      "Rural",  30.0722,  71.1931),
        ("D.G. Khan",     "Punjab",      "Rural",  30.0489,  70.6341),
        ("Peshawar",      "KPK",         "Urban",  34.0151,  71.5249),
        ("Swat",          "KPK",         "Rural",  35.2227,  72.4258),
        ("D.I. Khan",     "KPK",         "Rural",  31.8314,  70.9017),
        ("Kohistan",      "KPK",         "Rural",  35.5000,  73.0000),
        ("Quetta",        "Balochistan", "Urban",  30.1798,  66.9750),
        ("Khuzdar",       "Balochistan", "Rural",  27.8118,  66.6173),
        ("Turbat",        "Balochistan", "Rural",  26.0025,  63.0422),
        ("Chaghai",       "Balochistan", "Rural",  29.0000,  64.7000),
        ("Killa Abdullah","Balochistan", "Rural",  30.6833,  66.5833),
        ("Lasbela",       "Balochistan", "Rural",  26.2000,  66.2167),
    ]

    records = []

    for district, province, zone, lat, lon in districts:

        # ── OOSC Rate: urban provinces lower, rural Balochistan/Sindh highest
        base_oosc = {
            ("Sindh",       "Urban"):  0.22,
            ("Sindh",       "Rural"):  0.42,
            ("Punjab",      "Urban"):  0.15,
            ("Punjab",      "Rural"):  0.32,
            ("KPK",         "Urban"):  0.20,
            ("KPK",         "Rural"):  0.48,
            ("Balochistan", "Urban"):  0.28,
            ("Balochistan", "Rural"):  0.62,
        }.get((province, zone), 0.35)

        oosc_rate = float(np.clip(np.random.normal(base_oosc, 0.05), 0.05, 0.80))

        # ── School-age population (5–16) in district — realistic range
        school_age_pop = int(np.random.randint(80_000, 650_000))
        oosc_count     = int(school_age_pop * oosc_rate)
        enrolled       = school_age_pop - oosc_count

        # ── Literacy rate (adults 15+) — inversely correlated with OOSC
        literacy_rate = float(np.clip(
            np.random.normal(0.82 - oosc_rate * 0.8, 0.04), 0.22, 0.90
        ))

        # ── Dropout rate: higher in rural, high-OOSC districts
        dropout_rate = float(np.clip(
            np.random.normal(oosc_rate * 0.55, 0.03), 0.04, 0.55
        ))

        # ── Infrastructure deficit: % of schools lacking basic facilities
        infra_deficit = float(np.clip(
            np.random.normal(oosc_rate * 0.75, 0.06), 0.05, 0.90
        ))

        # ── Teacher qualification rate
        teacher_qualified_rate = float(np.clip(
            np.random.normal(0.78 - oosc_rate * 0.4, 0.05), 0.30, 0.95
        ))

        # ── Primary school count in district
        school_count = int(np.random.randint(120, 1800))

        # ── Dropout causes (proportions that sum to 1.0)
        # Economic Hardship, Distance, Lack of Facilities, Child Labor, Other
        cause_weights = np.random.dirichlet(
            alpha=[3.5, 2.0, 1.8, 2.2, 0.5]
        )

        # ── Resource Optimization Score (0–100): composite metric
        ros = float(np.clip(
            (literacy_rate * 40)
            + ((1 - oosc_rate) * 30)
            + ((1 - infra_deficit) * 20)
            + (teacher_qualified_rate * 10),
            0, 100
        ))

        # ── Gender parity index (GPI) for enrollment
        gpi = float(np.clip(np.random.normal(0.88 - oosc_rate * 0.25, 0.06), 0.40, 1.05))

        records.append({
            "District":               district,
            "Province":               province,
            "Zone":                   zone,
            "Latitude":               lat,
            "Longitude":              lon,
            "School_Age_Population":  school_age_pop,
            "OOSC_Count":             oosc_count,
            "OOSC_Rate":              round(oosc_rate, 4),
            "Enrolled":               enrolled,
            "Literacy_Rate":          round(literacy_rate, 4),
            "Dropout_Rate":           round(dropout_rate, 4),
            "Infra_Deficit_Rate":     round(infra_deficit, 4),
            "Teacher_Qualified_Rate": round(teacher_qualified_rate, 4),
            "School_Count":           school_count,
            "GPI":                    round(gpi, 3),
            "ROS":                    round(ros, 2),
            # Dropout causes
            "Cause_Economic":         round(cause_weights[0], 3),
            "Cause_Distance":         round(cause_weights[1], 3),
            "Cause_Facilities":       round(cause_weights[2], 3),
            "Cause_ChildLabor":       round(cause_weights[3], 3),
            "Cause_Other":            round(cause_weights[4], 3),
        })

    df = pd.DataFrame(records)
    return df


# =============================================================================
# SECTION 2 — LOAD DATA
# =============================================================================
raw_df = generate_district_data()


# =============================================================================
# SECTION 3 — HERO BANNER
# =============================================================================
st.markdown("""
<div class="hero-banner">
    <span class="hero-badge">🇵🇰 Parwaaz Internship — Portfolio Flagship Project</span>
    <div class="hero-title">📚 ITA Education Emergency & ASER Data Tracker</div>
    <div class="hero-subtitle">
        Real-time district intelligence for Out-of-School Children · Literacy Outcomes ·
        Infrastructure Gaps · Intervention Simulation &nbsp;|&nbsp;
        <strong style="color:rgba(255,255,255,0.9)">Idara-e-Taleem-o-Aagahi (ITA)</strong>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================================================================
# SECTION 4 — GLOBAL FILTERS
# Province + Zone filter bar; all downstream visuals react to selection
# =============================================================================
st.markdown('<div class="filter-bar">', unsafe_allow_html=True)

f_col1, f_col2, f_col3 = st.columns([1, 1, 2])

with f_col1:
    st.markdown('<div class="filter-label">🏛️ Province</div>', unsafe_allow_html=True)
    province_options = ["All Provinces"] + sorted(raw_df["Province"].unique().tolist())
    selected_province = st.selectbox(
        "Province", province_options, label_visibility="collapsed"
    )

with f_col2:
    st.markdown('<div class="filter-label">🏙️ Zone</div>', unsafe_allow_html=True)
    zone_options = ["Urban & Rural", "Urban", "Rural"]
    selected_zone = st.selectbox(
        "Zone", zone_options, label_visibility="collapsed"
    )

with f_col3:
    st.markdown(
        '<div class="filter-label" style="padding-top:0.1rem;">ℹ️ Data Source</div>',
        unsafe_allow_html=True
    )
    st.caption(
        "Synthetic data calibrated against **ASER Pakistan 2021–2023**, "
        "PSLM surveys, and Pakistan Education Statistics. "
        "20 districts across Sindh, Punjab, KPK, Balochistan."
    )

st.markdown('</div>', unsafe_allow_html=True)


# ── Apply filters ──────────────────────────────────────────────────────────────
df = raw_df.copy()

if selected_province != "All Provinces":
    df = df[df["Province"] == selected_province]

if selected_zone != "Urban & Rural":
    df = df[df["Zone"] == selected_zone]

# Guard: if filters produce an empty DataFrame, surface a friendly message
if df.empty:
    st.warning(
        "⚠️ No districts match the selected filters. "
        "Try broadening your Province or Zone selection."
    )
    st.stop()


# =============================================================================
# SECTION 5 — STRATEGIC KPI ROW
# Four custom-styled metric cards
# =============================================================================
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

total_oosc      = df["OOSC_Count"].sum()
avg_literacy    = df["Literacy_Rate"].mean() * 100
infra_pct       = df["Infra_Deficit_Rate"].mean() * 100
avg_ros         = df["ROS"].mean()

# ── KPI 1: Total OOSC ─────────────────────────────────────────────────────────
with kpi1:
    st.markdown(f"""
    <div class="kpi-card red">
        <span class="kpi-icon">🚸</span>
        <div class="kpi-label">Total Simulated OOSC</div>
        <div class="kpi-value red">{total_oosc:,.0f}</div>
        <div class="kpi-delta">Out-of-School Children · Filtered View</div>
    </div>
    """, unsafe_allow_html=True)

# ── KPI 2: Avg Foundational Literacy ─────────────────────────────────────────
with kpi2:
    st.markdown(f"""
    <div class="kpi-card green">
        <span class="kpi-icon">📖</span>
        <div class="kpi-label">Avg Foundational Literacy</div>
        <div class="kpi-value green">{avg_literacy:.1f}%</div>
        <div class="kpi-delta">Adults 15+ · ASER Benchmark ≥ 80%</div>
    </div>
    """, unsafe_allow_html=True)

# ── KPI 3: Schools Lacking Infrastructure ────────────────────────────────────
with kpi3:
    st.markdown(f"""
    <div class="kpi-card amber">
        <span class="kpi-icon">🏚️</span>
        <div class="kpi-label">Schools: Infra Deficit</div>
        <div class="kpi-value amber">{infra_pct:.1f}%</div>
        <div class="kpi-delta">Lacking WASH, Electricity, or Boundary Wall</div>
    </div>
    """, unsafe_allow_html=True)

# ── KPI 4: Resource Optimization Score ───────────────────────────────────────
with kpi4:
    ros_color = "green" if avg_ros >= 60 else ("amber" if avg_ros >= 40 else "red")
    st.markdown(f"""
    <div class="kpi-card {ros_color}">
        <span class="kpi-icon">⚡</span>
        <div class="kpi-label">Resource Optimization Score</div>
        <div class="kpi-value {ros_color}">{avg_ros:.1f}<span style="font-size:1.1rem;font-weight:500"> /100</span></div>
        <div class="kpi-delta">Composite: Literacy + Enrollment + Infra</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-top:1.6rem'></div>", unsafe_allow_html=True)


# =============================================================================
# SECTION 6 — GEOSPATIAL INTELLIGENCE MAP
# Folium choropleth with color-coded severity circles per district
# Red = high OOSC severity → Green = optimal
# =============================================================================
st.markdown("""
<div class="section-header">
    🗺️ Geospatial Intelligence — District OOSC Severity Map
</div>
""", unsafe_allow_html=True)

# Compute map center from filtered data
map_center_lat = df["Latitude"].mean()
map_center_lon = df["Longitude"].mean()
zoom_start     = 6 if selected_province == "All Provinces" else 7

# Build Folium map
m = folium.Map(
    location=[map_center_lat, map_center_lon],
    zoom_start=zoom_start,
    tiles="CartoDB positron",          # Clean, minimal basemap
    attr="© OpenStreetMap, © CARTO",
)

# ── Color function: OOSC rate → hex color (red-orange-yellow-green gradient)
def oosc_to_color(rate: float) -> str:
    """Map OOSC rate [0, 1] to a color from green (low) to red (high)."""
    # Clamp
    r = max(0.0, min(1.0, rate))
    if r < 0.20:   return "#2CA02C"   # Green — optimal
    elif r < 0.35: return "#8DB600"   # Yellow-green
    elif r < 0.50: return "#E07B00"   # Amber — moderate concern
    elif r < 0.65: return "#D62728"   # Red — severe
    else:          return "#7B0000"   # Dark red — critical


for _, row in df.iterrows():
    color = oosc_to_color(row["OOSC_Rate"])

    # Circle radius proportional to OOSC count (visual weight = impact scale)
    radius = int(8000 + row["OOSC_Count"] / 20)

    popup_html = f"""
    <div style="font-family:Inter,sans-serif;min-width:220px;">
        <div style="background:#003366;color:#fff;padding:8px 12px;border-radius:6px 6px 0 0;
                    font-weight:700;font-size:13px;">
            {row['District']}, {row['Province']}
        </div>
        <div style="padding:10px 12px;background:#fff;border-radius:0 0 6px 6px;
                    border:1px solid #E4EBF5;">
            <table style="width:100%;border-collapse:collapse;font-size:12px;">
                <tr><td style="color:#6B7A99;padding:3px 0">Zone</td>
                    <td style="font-weight:600;text-align:right">{row['Zone']}</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">OOSC Count</td>
                    <td style="font-weight:700;color:#C0392B;text-align:right">
                        {row['OOSC_Count']:,}</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">OOSC Rate</td>
                    <td style="font-weight:600;text-align:right">
                        {row['OOSC_Rate']*100:.1f}%</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">Literacy Rate</td>
                    <td style="font-weight:600;color:#2CA02C;text-align:right">
                        {row['Literacy_Rate']*100:.1f}%</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">Infra Deficit</td>
                    <td style="font-weight:600;color:#E07B00;text-align:right">
                        {row['Infra_Deficit_Rate']*100:.1f}%</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">ROS Score</td>
                    <td style="font-weight:600;text-align:right">
                        {row['ROS']:.1f}/100</td></tr>
                <tr><td style="color:#6B7A99;padding:3px 0">Schools</td>
                    <td style="font-weight:600;text-align:right">
                        {row['School_Count']:,}</td></tr>
            </table>
        </div>
    </div>
    """

    folium.Circle(
        location=[row["Latitude"], row["Longitude"]],
        radius=radius,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.55,
        weight=2,
        popup=folium.Popup(popup_html, max_width=260),
        tooltip=folium.Tooltip(
            f"<b>{row['District']}</b> · OOSC: {row['OOSC_Rate']*100:.1f}%",
            sticky=True
        ),
    ).add_to(m)

    # District label marker
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        icon=folium.DivIcon(
            html=f'<div style="font-family:Inter,sans-serif;font-size:10px;'
                 f'font-weight:600;color:#003366;white-space:nowrap;'
                 f'text-shadow:1px 1px 2px #fff,-1px -1px 2px #fff;">'
                 f'{row["District"]}</div>',
            icon_size=(120, 20),
            icon_anchor=(60, 10),
        ),
    ).add_to(m)

# ── Render map ────────────────────────────────────────────────────────────────
st_folium(m, width=None, height=520, returned_objects=[])

# ── Map legend ────────────────────────────────────────────────────────────────
leg1, leg2, leg3, leg4, leg5 = st.columns(5)
legend_data = [
    ("#2CA02C", "< 20% OOSC", "Optimal"),
    ("#8DB600", "20–35% OOSC", "Moderate"),
    ("#E07B00", "35–50% OOSC", "Elevated"),
    ("#D62728", "50–65% OOSC", "Severe"),
    ("#7B0000", "> 65% OOSC",  "Critical"),
]
for col, (color, range_lbl, status) in zip(
    [leg1, leg2, leg3, leg4, leg5], legend_data
):
    with col:
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:8px;padding:6px 0;">'
            f'<div style="width:16px;height:16px;border-radius:50%;'
            f'background:{color};flex-shrink:0"></div>'
            f'<div><div style="font-size:0.75rem;font-weight:600;color:#1A1A2E">'
            f'{range_lbl}</div>'
            f'<div style="font-size:0.68rem;color:#6B7A99">{status}</div></div>'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)


# =============================================================================
# SECTION 7 — DIAGNOSTIC ANALYTICS
# Left: Enrollment vs. Dropout stacked bar | Right: Dropout Causes donut
# =============================================================================
st.markdown("""
<div class="section-header">
    📊 Diagnostic Analytics — Enrollment, Dropout & Causal Breakdown
</div>
""", unsafe_allow_html=True)

chart_left, chart_right = st.columns([3, 2], gap="large")

# ── LEFT: Stacked Bar — Enrolled vs. OOSC across districts ───────────────────
with chart_left:
    # Sort by OOSC_Count descending, take top 10 for readability
    top_districts = df.nlargest(10, "OOSC_Count").copy()
    top_districts = top_districts.sort_values("OOSC_Count")  # ascending for horizontal

    bar_fig = go.Figure()

    bar_fig.add_trace(go.Bar(
        name="Enrolled Children",
        y=top_districts["District"],
        x=top_districts["Enrolled"],
        orientation="h",
        marker_color="#003366",
        hovertemplate="<b>%{y}</b><br>Enrolled: %{x:,.0f}<extra></extra>",
    ))

    bar_fig.add_trace(go.Bar(
        name="Out-of-School (OOSC)",
        y=top_districts["District"],
        x=top_districts["OOSC_Count"],
        orientation="h",
        marker_color="#C0392B",
        hovertemplate="<b>%{y}</b><br>OOSC: %{x:,.0f}<extra></extra>",
    ))

    bar_fig.update_layout(
        barmode="stack",
        title={
            "text": "Enrollment vs. Out-of-School Children",
            "font": {"family": "Inter", "size": 14, "color": "#003366"},
            "x": 0.0, "xanchor": "left",
        },
        xaxis_title="Children (5–16 years)",
        yaxis_title="",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",,
        plot_bgcolor="#FFFFFF",
        font={"family": "Inter", "size": 11, "color": "#4A4A6A"},
        legend={
            "orientation": "h", "y": -0.18, "x": 0,
            "font": {"size": 11},
        },
        xaxis={
            "gridcolor": "#F0F0F5",
            "zerolinecolor": "#E4EBF5",
            "tickformat": ",.0f",
        },
        yaxis={"gridcolor": "#F0F0F5"},
        margin={"l": 10, "r": 20, "t": 50, "b": 60},
        height=420,
        hoverlabel={"bgcolor": "#003366", "font_color": "#fff", "font_family": "Inter"},
    )

    st.plotly_chart(bar_fig, use_container_width=True)

# ── RIGHT: Donut — Primary Causes of Dropout ─────────────────────────────────
with chart_right:
    # Aggregate dropout causes across filtered districts (weighted avg)
    cause_cols = [
        "Cause_Economic", "Cause_Distance",
        "Cause_Facilities", "Cause_ChildLabor", "Cause_Other"
    ]
    cause_labels = [
        "Economic Hardship", "School Distance",
        "Lack of Facilities", "Child Labor", "Other"
    ]
    cause_colors = ["#C0392B", "#E07B00", "#003366", "#8B008B", "#6B7A99"]

    # Weighted by dropout count in each district
    df_cause = df.copy()
    df_cause["dropout_count"] = df_cause["School_Age_Population"] * df_cause["Dropout_Rate"]
    total_dropouts = df_cause["dropout_count"].sum()

    cause_totals = []
    for col in cause_cols:
        weighted = (df_cause[col] * df_cause["dropout_count"]).sum()
        cause_totals.append(weighted)

    donut_fig = go.Figure(go.Pie(
        labels=cause_labels,
        values=cause_totals,
        hole=0.55,
        marker={
            "colors": cause_colors,
            "line": {"color": "#FFFFFF", "width": 2},
        },
        hovertemplate="<b>%{label}</b><br>Share: %{percent}<br>Count: %{value:,.0f}<extra></extra>",
        textfont={"family": "Inter", "size": 11},
    ))

    donut_fig.add_annotation(
        text="Dropout<br>Causes",
        x=0.5, y=0.5,
        font={"family": "Inter", "size": 13, "color": "#003366"},
        showarrow=False,
    )

    donut_fig.update_layout(
        title={
            "text": "Primary Causes of Student Dropout",
            "font": {"family": "Inter", "size": 14, "color": "#003366"},
            "x": 0.0, "xanchor": "left",
        },
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",,
        font={"family": "Inter", "size": 11, "color": "#4A4A6A"},
        legend={
            "font": {"size": 11},
            "itemsizing": "constant",
        },
        margin={"l": 10, "r": 10, "t": 50, "b": 20},
        height=420,
        hoverlabel={"bgcolor": "#003366", "font_color": "#fff", "font_family": "Inter"},
        showlegend=True,
    )

    st.plotly_chart(donut_fig, use_container_width=True)

st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)


# =============================================================================
# SECTION 8 — SUPPLEMENTARY ANALYTICS
# Scatter: Literacy vs. OOSC Rate | Bar: Teacher Qualification by Province
# =============================================================================
st.markdown("""
<div class="section-header">
    🔍 Deep-Dive Analytics — Literacy Correlations & Teacher Workforce
</div>
""", unsafe_allow_html=True)

deep_left, deep_right = st.columns(2, gap="large")

# ── Scatter: Literacy Rate vs OOSC Rate ──────────────────────────────────────
with deep_left:
    scatter_fig = px.scatter(
        df,
        x="OOSC_Rate",
        y="Literacy_Rate",
        size="School_Age_Population",
        color="Province",
        hover_name="District",
        hover_data={
            "OOSC_Rate": ":.1%",
            "Literacy_Rate": ":.1%",
            "School_Age_Population": ":,",
            "Zone": True,
        },
        color_discrete_map={
            "Sindh":       "#C0392B",
            "Punjab":      "#003366",
            "KPK":         "#2CA02C",
            "Balochistan": "#E07B00",
        },
        title="Literacy Rate vs. OOSC Rate (bubble = school-age population)",
        labels={
            "OOSC_Rate":    "OOSC Rate",
            "Literacy_Rate": "Adult Literacy Rate",
        },
        size_max=40,
    )

    scatter_fig.update_traces(
        marker_opacity=0.75,
        marker_line_width=1.5,
        marker_line_color="white",
    )

    scatter_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",,
        plot_bgcolor="#FFFFFF",
        font={"family": "Inter", "size": 11},
        xaxis={
            "tickformat": ".0%",
            "gridcolor": "#F0F0F5",
            "title_font_color": "#003366",
        },
        yaxis={
            "tickformat": ".0%",
            "gridcolor": "#F0F0F5",
            "title_font_color": "#003366",
        },
        title_font={"family": "Inter", "size": 13, "color": "#003366"},
        margin={"l": 10, "r": 10, "t": 50, "b": 20},
        height=380,
        hoverlabel={"bgcolor": "#003366", "font_color": "#fff", "font_family": "Inter"},
    )

    st.plotly_chart(scatter_fig, use_container_width=True)

# ── Bar: Avg Teacher Qualification Rate by Province ──────────────────────────
with deep_right:
    tq_df = (
        df.groupby("Province")["Teacher_Qualified_Rate"]
        .mean()
        .reset_index()
        .sort_values("Teacher_Qualified_Rate")
    )
    tq_df["Pct"] = tq_df["Teacher_Qualified_Rate"] * 100

    tq_colors = {
        "Balochistan": "#C0392B",
        "Sindh":       "#E07B00",
        "KPK":         "#8DB600",
        "Punjab":      "#2CA02C",
    }

    tq_fig = go.Figure(go.Bar(
        x=tq_df["Pct"],
        y=tq_df["Province"],
        orientation="h",
        marker_color=[tq_colors.get(p, "#003366") for p in tq_df["Province"]],
        text=[f"{v:.1f}%" for v in tq_df["Pct"]],
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Qualified Teachers: %{x:.1f}%<extra></extra>",
    ))

    # Add benchmark line at 80%
    tq_fig.add_vline(
        x=80,
        line_dash="dash",
        line_color="#003366",
        line_width=1.5,
        annotation_text="80% Target",
        annotation_position="top",
        annotation_font={"color": "#003366", "size": 10},
    )

    tq_fig.update_layout(
        title={
            "text": "Avg Teacher Qualification Rate by Province",
            "font": {"family": "Inter", "size": 13, "color": "#003366"},
            "x": 0.0, "xanchor": "left",
        },
        xaxis={
            "range": [0, 105],
            "gridcolor": "#F0F0F5",
            "ticksuffix": "%",
        },
        yaxis={"gridcolor": "#F0F0F5"},
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",,
        plot_bgcolor="#FFFFFF",
        font={"family": "Inter", "size": 11},
        margin={"l": 10, "r": 30, "t": 50, "b": 20},
        height=380,
        showlegend=False,
        hoverlabel={"bgcolor": "#003366", "font_color": "#fff", "font_family": "Inter"},
    )

    st.plotly_chart(tq_fig, use_container_width=True)


# =============================================================================
# SECTION 9 — THE INTERVENTION SIMULATOR
# Interactive policy tool: budget allocation → projected OOSC reduction
# =============================================================================
st.markdown("""
<div class="simulator-panel">
    <div class="simulator-title">🎯 Policy Intervention Simulator</div>
    <div class="simulator-subtitle">
        Allocate simulated budget and select intervention strategy to project
        the expected reduction in the OOSC rate across filtered districts.
    </div>
""", unsafe_allow_html=True)

sim_left, sim_right = st.columns([2, 1], gap="large")

with sim_left:
    # ── Budget Slider ─────────────────────────────────────────────────────────
    st.markdown(
        '<div style="color:rgba(255,255,255,0.85);font-size:0.82rem;'
        'font-weight:600;margin-bottom:0.4rem;">💰 Simulated Monthly Budget (PKR)</div>',
        unsafe_allow_html=True
    )
    monthly_budget = st.slider(
        "Budget",
        min_value=1_000_000,
        max_value=100_000_000,
        value=25_000_000,
        step=500_000,
        format="PKR %d",
        label_visibility="collapsed",
    )

    # ── Strategy Radio ────────────────────────────────────────────────────────
    st.markdown(
        '<div style="color:rgba(255,255,255,0.85);font-size:0.82rem;'
        'font-weight:600;margin-bottom:0.4rem;margin-top:1rem;">🔧 Intervention Strategy</div>',
        unsafe_allow_html=True
    )
    strategy = st.radio(
        "Strategy",
        options=["Infrastructure Upgrades", "Targeted Teacher Training", "Blended (50/50)"],
        horizontal=True,
        label_visibility="collapsed",
    )

    # ── Simulator Logic ───────────────────────────────────────────────────────
    # Evidence-based elasticity coefficients (simplified linear model):
    #   Infrastructure: PKR 1M → 0.012% OOSC reduction (construction, WASH, etc.)
    #   Teacher Training: PKR 1M → 0.019% OOSC reduction (higher ROI, lower cost)
    #   Blended: average of both, with a 10% synergy bonus

    budget_millions = monthly_budget / 1_000_000  # Express in millions for scaling

    if strategy == "Infrastructure Upgrades":
        elasticity         = 0.012
        strategy_icon      = "🏗️"
        strategy_color     = "#E07B00"
        schools_affected   = int(budget_millions * 2.8)
        teachers_affected  = 0
        notes              = "WASH facilities, boundary walls, electricity & classrooms"

    elif strategy == "Targeted Teacher Training":
        elasticity         = 0.019
        strategy_icon      = "👩‍🏫"
        strategy_color     = "#2CA02C"
        schools_affected   = int(budget_millions * 1.2)
        teachers_affected  = int(budget_millions * 18)
        notes              = "In-service training, mentoring & pedagogical coaching"

    else:  # Blended
        elasticity         = ((0.012 + 0.019) / 2) * 1.10   # 10% synergy bonus
        strategy_icon      = "⚖️"
        strategy_color     = "#0077CC"
        schools_affected   = int(budget_millions * 2.0)
        teachers_affected  = int(budget_millions * 9)
        notes              = "Combined infrastructure + training — synergy premium applied"

    # Projected OOSC reduction (%)
    # We cap the reduction at 35% to maintain realism for a single-month cycle
    projected_reduction_pct = min(budget_millions * elasticity, 35.0)

    # Projected children re-enrolled
    current_oosc       = df["OOSC_Count"].sum()
    children_reached   = int(current_oosc * (projected_reduction_pct / 100))
    annual_budget      = monthly_budget * 12
    cost_per_child     = (annual_budget / children_reached) if children_reached > 0 else 0

    # Display budget in human-readable form
    if monthly_budget >= 10_000_000:
        budget_display = f"PKR {monthly_budget/1_000_000:.1f}M"
    else:
        budget_display = f"PKR {monthly_budget/1_000:,.0f}K"

# ── RIGHT: Result Box ─────────────────────────────────────────────────────────
with sim_right:
    st.markdown(f"""
    <div class="sim-result-box">
        <div style="font-size:1.8rem;margin-bottom:0.3rem">{strategy_icon}</div>
        <div class="sim-result-value">{projected_reduction_pct:.2f}%</div>
        <div class="sim-result-label">Projected OOSC Rate Reduction<br>per month · {strategy}</div>

        <div class="sim-metric-row">
            <div class="sim-metric">
                <div class="sim-metric-val">{children_reached:,}</div>
                <div class="sim-metric-lbl">Children Re-enrolled</div>
            </div>
            <div class="sim-metric">
                <div class="sim-metric-val">{budget_display}</div>
                <div class="sim-metric-lbl">Monthly Investment</div>
            </div>
        </div>

        <div class="sim-metric-row">
            <div class="sim-metric">
                <div class="sim-metric-val">{schools_affected:,}</div>
                <div class="sim-metric-lbl">Schools Impacted</div>
            </div>
            <div class="sim-metric">
                <div class="sim-metric-val">PKR {cost_per_child:,.0f}</div>
                <div class="sim-metric-lbl">Annual Cost / Child</div>
            </div>
        </div>

        <div style="margin-top:1rem;font-size:0.72rem;color:rgba(255,255,255,0.5);
                    text-align:left;line-height:1.5;">
            <em>{notes}</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Close simulator panel div
st.markdown("</div>", unsafe_allow_html=True)


# ── Simulator Progress Visual ─────────────────────────────────────────────────
st.markdown("<div style='margin-top:1rem'></div>", unsafe_allow_html=True)

progress_fig = go.Figure()

# Before intervention
progress_fig.add_trace(go.Bar(
    name="Current OOSC Rate",
    x=df["District"],
    y=df["OOSC_Rate"] * 100,
    marker_color="rgba(192, 57, 43, 0.7)",
    hovertemplate="<b>%{x}</b><br>Current OOSC: %{y:.1f}%<extra></extra>",
))

# After intervention
projected_rates = df["OOSC_Rate"] * (1 - projected_reduction_pct / 100) * 100
progress_fig.add_trace(go.Bar(
    name=f"Projected OOSC Rate (after {strategy})",
    x=df["District"],
    y=projected_rates,
    marker_color="rgba(44, 160, 44, 0.75)",
    hovertemplate="<b>%{x}</b><br>Projected OOSC: %{y:.1f}%<extra></extra>",
))

progress_fig.update_layout(
    barmode="group",
    title={
        "text": f"District-Level OOSC Rate: Before vs. After Intervention — {strategy} | Budget: {budget_display}/month",
        "font": {"family": "Inter", "size": 13, "color": "#003366"},
        "x": 0.0, "xanchor": "left",
    },
    xaxis_title="District",
    yaxis_title="OOSC Rate (%)",
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",,
    plot_bgcolor="#FFFFFF",
    font={"family": "Inter", "size": 11, "color": "#4A4A6A"},
    legend={
        "orientation": "h", "y": -0.22, "x": 0,
        "font": {"size": 11},
    },
    xaxis={"gridcolor": "#F0F0F5", "tickangle": -35},
    yaxis={"gridcolor": "#F0F0F5", "ticksuffix": "%"},
    margin={"l": 10, "r": 20, "t": 60, "b": 80},
    height=380,
    hoverlabel={"bgcolor": "#003366", "font_color": "#fff", "font_family": "Inter"},
)

st.plotly_chart(progress_fig, use_container_width=True)


# =============================================================================
# SECTION 10 — DATA TABLE (Expandable)
# Full district-level data table for analysts and policymakers
# =============================================================================
with st.expander("📋 View Full District Dataset", expanded=False):
    display_df = df[[
        "District", "Province", "Zone",
        "School_Age_Population", "OOSC_Count", "OOSC_Rate",
        "Literacy_Rate", "Dropout_Rate", "Infra_Deficit_Rate",
        "Teacher_Qualified_Rate", "School_Count", "GPI", "ROS"
    ]].copy()

    # Format percentages for readability
    for col in ["OOSC_Rate", "Literacy_Rate", "Dropout_Rate",
                "Infra_Deficit_Rate", "Teacher_Qualified_Rate"]:
        display_df[col] = display_df[col].apply(lambda x: f"{x*100:.1f}%")

    display_df["GPI"]  = display_df["GPI"].apply(lambda x: f"{x:.2f}")
    display_df["ROS"]  = display_df["ROS"].apply(lambda x: f"{x:.1f}")

    display_df.columns = [
        "District", "Province", "Zone",
        "School-Age Pop.", "OOSC Count", "OOSC Rate",
        "Literacy Rate", "Dropout Rate", "Infra Deficit",
        "Teacher Qual. Rate", "Schools", "GPI", "ROS /100"
    ]

    st.dataframe(display_df, use_container_width=True, hide_index=True)


# =============================================================================
# SECTION 11 — FOOTER
# =============================================================================
st.markdown("""
<div style="text-align:center;padding:2rem 0 1rem;color:#8896B0;font-size:0.78rem;">
    <div style="font-weight:600;color:#003366;margin-bottom:0.3rem;">
        ITA Education Emergency & ASER Data Tracker
    </div>
    Synthetic data calibrated against ASER Pakistan (2021–2023) &amp; PSLM surveys ·
    Built for the <strong>Parwaaz Internship</strong> application ·
    <strong>Idara-e-Taleem-o-Aagahi (ITA)</strong>
    <br><br>
    <em>All figures are simulated for analytical demonstration.
    Intervention projections use simplified linear elasticity models.</em>
</div>
""", unsafe_allow_html=True)
