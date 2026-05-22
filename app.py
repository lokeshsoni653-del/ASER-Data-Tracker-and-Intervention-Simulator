# =============================================================================
# ITA Education Emergency & ASER Data Tracker
# Portfolio Project for Parwaaz Internship — Idara-e-Taleem-o-Aagahi (ITA)
# Author: Portfolio Candidate
# Stack: Streamlit · Pandas · NumPy · Plotly · Folium · streamlit-folium
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG — Must be called first before any other Streamlit command
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ITA Education Emergency Tracker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# PREMIUM CUSTOM CSS — Corporate NGO Aesthetic
# Deep Blues (#003366) + Intervention Greens (#2CA02C) + Clean Light Theme
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ─────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── CSS Variables ────────────────────────────────────────────────────────── */
:root {
    --navy:       #003366;
    --navy-mid:   #004080;
    --navy-light: #0055a5;
    --green:      #2CA02C;
    --green-light:#3dbf3d;
    --green-pale: #e8f8e8;
    --amber:      #E8860A;
    --red:        #C0392B;
    --bg:         #F4F6FA;
    --surface:    #FFFFFF;
    --border:     #DDE3EE;
    --text-primary: #0D1B2A;
    --text-secondary: #4A5568;
    --text-muted:   #8A9BB0;
    --shadow-sm:  0 2px 8px rgba(0,51,102,0.08);
    --shadow-md:  0 6px 24px rgba(0,51,102,0.12);
    --shadow-lg:  0 16px 48px rgba(0,51,102,0.16);
    --radius:     12px;
    --radius-lg:  18px;
}

/* ── Global Reset & Body ──────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text-primary) !important;
}

.main .block-container {
    padding: 0 2rem 3rem 2rem !important;
    max-width: 1600px !important;
    background: var(--bg) !important;
}

/* Hide Streamlit default chrome */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }

/* ── Header Banner ────────────────────────────────────────────────────────── */
.ita-header {
    background: linear-gradient(135deg, var(--navy) 0%, var(--navy-mid) 60%, var(--navy-light) 100%);
    padding: 2.2rem 2.8rem;
    border-radius: 0 0 var(--radius-lg) var(--radius-lg);
    margin: -1rem -2rem 1.8rem -2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}

.ita-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 280px; height: 280px;
    background: rgba(44,160,44,0.15);
    border-radius: 50%;
    pointer-events: none;
}

.ita-header::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 40%;
    width: 200px; height: 200px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
    pointer-events: none;
}

.ita-header-eyebrow {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #7FB8FF;
    margin-bottom: 0.5rem;
}

.ita-header h1 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.1rem !important;
    font-weight: 400 !important;
    color: #FFFFFF !important;
    margin: 0 0 0.5rem 0 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.01em !important;
}

.ita-header-sub {
    font-size: 0.92rem;
    color: rgba(255,255,255,0.72);
    font-weight: 400;
    max-width: 680px;
    line-height: 1.6;
}

.ita-header-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(44,160,44,0.25);
    border: 1px solid rgba(44,160,44,0.5);
    color: #7EE87E;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 4px 12px;
    border-radius: 20px;
    margin-top: 1rem;
}

/* ── Filter / Control Row ─────────────────────────────────────────────────── */
.filter-bar {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem 1.4rem;
    margin-bottom: 1.6rem;
    box-shadow: var(--shadow-sm);
    display: flex;
    align-items: center;
    gap: 1rem;
}

.filter-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-muted);
    white-space: nowrap;
}

/* ── KPI Cards ────────────────────────────────────────────────────────────── */
.kpi-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.4rem 1.6rem;
    box-shadow: var(--shadow-sm);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    position: relative;
    overflow: hidden;
    height: 100%;
}

.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
}

.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: var(--radius) var(--radius) 0 0;
}

.kpi-card.red::before   { background: var(--red); }
.kpi-card.green::before { background: var(--green); }
.kpi-card.amber::before { background: var(--amber); }
.kpi-card.blue::before  { background: var(--navy-light); }

.kpi-icon {
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
    display: block;
}

.kpi-label {
    font-size: 0.73rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 0.4rem;
}

.kpi-value {
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1;
    margin-bottom: 0.5rem;
    font-variant-numeric: tabular-nums;
}

.kpi-value.red   { color: var(--red); }
.kpi-value.green { color: var(--green); }
.kpi-value.amber { color: var(--amber); }
.kpi-value.blue  { color: var(--navy-light); }

.kpi-delta {
    font-size: 0.78rem;
    color: var(--text-muted);
    display: flex;
    align-items: center;
    gap: 4px;
}

.kpi-delta.up   { color: var(--green); }
.kpi-delta.down { color: var(--red); }

/* ── Section Headers ──────────────────────────────────────────────────────── */
.section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.8rem 0 1rem 0;
}

.section-header h2 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 1.3rem !important;
    font-weight: 400 !important;
    color: var(--navy) !important;
    margin: 0 !important;
}

.section-pill {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    background: var(--green-pale);
    color: var(--green);
    border: 1px solid rgba(44,160,44,0.25);
    padding: 3px 10px;
    border-radius: 20px;
}

/* ── Chart / Map Containers ───────────────────────────────────────────────── */
.chart-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.2rem;
    box-shadow: var(--shadow-sm);
    height: 100%;
}

.chart-title {
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--text-secondary);
    margin-bottom: 0.8rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid var(--border);
}

/* ── Simulator Panel ──────────────────────────────────────────────────────── */
.simulator-panel {
    background: linear-gradient(135deg, var(--navy) 0%, #001f4d 100%);
    border-radius: var(--radius-lg);
    padding: 2rem 2.4rem;
    box-shadow: var(--shadow-lg);
    margin-top: 0.5rem;
    position: relative;
    overflow: hidden;
}

.simulator-panel::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 250px; height: 250px;
    background: rgba(44,160,44,0.08);
    border-radius: 50%;
}

.simulator-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.45rem;
    font-weight: 400;
    color: #FFFFFF;
    margin-bottom: 0.3rem;
}

.simulator-subtitle {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.6);
    margin-bottom: 1.6rem;
}

.sim-result-box {
    background: rgba(44,160,44,0.15);
    border: 1px solid rgba(44,160,44,0.4);
    border-radius: var(--radius);
    padding: 1.4rem 2rem;
    text-align: center;
}

.sim-result-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #7EE87E;
    margin-bottom: 0.5rem;
}

.sim-result-value {
    font-size: 3rem;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1;
    font-variant-numeric: tabular-nums;
}

.sim-result-unit {
    font-size: 1rem;
    color: rgba(255,255,255,0.7);
    margin-top: 0.3rem;
}

.sim-reach-item {
    background: rgba(255,255,255,0.06);
    border-radius: 8px;
    padding: 0.8rem 1rem;
    margin-bottom: 0.6rem;
}

.sim-reach-label {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.55);
    margin-bottom: 0.25rem;
}

.sim-reach-value {
    font-size: 1.05rem;
    font-weight: 600;
    color: #FFFFFF;
}

/* ── Streamlit Component Overrides ───────────────────────────────────────── */
div[data-testid="stSelectbox"] > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text-primary) !important;
}

div[data-testid="stSlider"] > div > div > div {
    background: var(--navy-light) !important;
}

div[data-testid="stSlider"] [data-testid="stThumbValue"] {
    background: var(--navy) !important;
    color: white !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.75rem !important;
}

.stRadio > div {
    gap: 8px !important;
}

.stRadio > div > label {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 0.6rem 1.2rem !important;
    cursor: pointer !important;
    transition: all 0.15s ease !important;
    color: var(--text-secondary) !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
}

.stRadio > div > label:hover {
    border-color: var(--navy-light) !important;
    color: var(--navy) !important;
}

/* Mono font for data values */
.mono { font-family: 'IBM Plex Mono', monospace !important; }

/* Divider */
.ita-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0;
}

/* Map container */
.map-container {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.5rem;
    box-shadow: var(--shadow-sm);
    overflow: hidden;
}

/* Streamlit metric override */
[data-testid="metric-container"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SYNTHETIC DATA GENERATION
# Highly realistic district-level education data for 15+ Pakistani districts
# Cached with @st.cache_data for performance — only runs once per session
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data
def generate_education_data() -> pd.DataFrame:
    """
    Generates a high-fidelity synthetic dataset modeling education metrics
    for 18 Pakistani districts across 4 provinces. Values are calibrated
    against real ASER Pakistan and UNICEF OOSC reports for plausibility.

    Returns:
        pd.DataFrame: District-level education metrics with lat/lon coordinates.
    """
    np.random.seed(42)  # Reproducibility

    districts = [
        # (name, province, zone, lat, lon, base_oosc_pct, base_literacy, infra_gap)
        ("Karachi Central",  "Sindh",       "Urban", 24.860, 67.010, 0.21, 0.68, 0.35),
        ("Larkana",          "Sindh",       "Rural", 27.559, 68.215, 0.49, 0.38, 0.72),
        ("Tharparkar",       "Sindh",       "Rural", 24.739, 69.793, 0.62, 0.28, 0.85),
        ("Hyderabad",        "Sindh",       "Urban", 25.396, 68.374, 0.29, 0.58, 0.42),
        ("Sukkur",           "Sindh",       "Rural", 27.705, 68.857, 0.44, 0.41, 0.65),

        ("Lahore",           "Punjab",      "Urban", 31.548, 74.343, 0.14, 0.77, 0.22),
        ("Multan",           "Punjab",      "Urban", 30.157, 71.524, 0.22, 0.62, 0.38),
        ("Rahim Yar Khan",   "Punjab",      "Rural", 28.420, 70.295, 0.38, 0.47, 0.58),
        ("D.G. Khan",        "Punjab",      "Rural", 30.048, 70.635, 0.41, 0.44, 0.62),
        ("Bahawalpur",       "Punjab",      "Rural", 29.395, 71.678, 0.33, 0.51, 0.52),

        ("Peshawar",         "KPK",         "Urban", 34.009, 71.678, 0.18, 0.71, 0.28),
        ("Swat",             "KPK",         "Rural", 35.221, 72.421, 0.35, 0.49, 0.55),
        ("Khyber",           "KPK",         "Rural", 34.100, 71.085, 0.45, 0.39, 0.68),

        ("Quetta",           "Balochistan", "Urban", 30.183, 67.007, 0.31, 0.52, 0.48),
        ("Turbat",           "Balochistan", "Rural", 26.003, 63.058, 0.58, 0.31, 0.79),
        ("Khuzdar",          "Balochistan", "Rural", 27.812, 66.620, 0.54, 0.34, 0.76),
        ("Gwadar",           "Balochistan", "Rural", 25.122, 62.325, 0.47, 0.39, 0.70),
        ("Loralai",          "Balochistan", "Rural", 30.372, 68.592, 0.50, 0.36, 0.74),
    ]

    rows = []
    for d in districts:
        name, province, zone, lat, lon, oosc_base, lit_base, infra_gap = d

        # Add realistic noise to base values
        noise = np.random.normal(0, 0.03)

        total_children    = int(np.random.uniform(80_000, 420_000))
        oosc_pct          = np.clip(oosc_base + noise, 0.05, 0.90)
        oosc_count        = int(total_children * oosc_pct)
        enrolled          = total_children - oosc_count
        dropout_rate      = np.clip(np.random.uniform(0.08, 0.30) + (oosc_pct * 0.2), 0.05, 0.45)
        literacy_rate     = np.clip(lit_base + np.random.normal(0, 0.04), 0.15, 0.92)
        infra_lacking_pct = np.clip(infra_gap + np.random.normal(0, 0.05), 0.10, 0.95)
        teacher_ratio     = np.random.randint(28, 72)  # students per teacher
        schools_total     = int(np.random.uniform(150, 900))
        schools_no_water  = int(schools_total * np.random.uniform(0.1, 0.55))
        schools_no_toilet = int(schools_total * np.random.uniform(0.15, 0.60))

        # Dropout cause breakdown (sums to 100)
        economic  = np.random.uniform(0.25, 0.45)
        distance  = np.random.uniform(0.15, 0.30)
        child_lab = np.random.uniform(0.10, 0.25)
        no_fac    = 1.0 - economic - distance - child_lab

        # Composite resource optimization score (0–100, higher = better)
        opt_score = round(
            (literacy_rate * 0.35 +
             (1 - oosc_pct) * 0.35 +
             (1 - infra_lacking_pct) * 0.30) * 100, 1
        )

        rows.append({
            "District":            name,
            "Province":            province,
            "Zone":                zone,
            "Latitude":            lat,
            "Longitude":           lon,
            "Total_Children":      total_children,
            "OOSC_Count":          oosc_count,
            "OOSC_Pct":            round(oosc_pct * 100, 1),
            "Enrolled":            enrolled,
            "Dropout_Rate":        round(dropout_rate * 100, 1),
            "Literacy_Rate":       round(literacy_rate * 100, 1),
            "Infra_Lacking_Pct":   round(infra_lacking_pct * 100, 1),
            "Teacher_Ratio":       teacher_ratio,
            "Schools_Total":       schools_total,
            "Schools_No_Water":    schools_no_water,
            "Schools_No_Toilet":   schools_no_toilet,
            "Cause_Economic":      round(economic * 100, 1),
            "Cause_Distance":      round(distance * 100, 1),
            "Cause_ChildLabor":    round(child_lab * 100, 1),
            "Cause_NoFacilities":  round(no_fac * 100, 1),
            "Opt_Score":           opt_score,
        })

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────────────────────────────────────
# HELPER: KPI Card HTML
# ─────────────────────────────────────────────────────────────────────────────
def kpi_card(icon: str, label: str, value: str, delta: str, color: str) -> str:
    """Returns styled HTML for a single KPI metric card."""
    delta_class = "up" if "▲" in delta else ("down" if "▼" in delta else "")
    return f"""
    <div class="kpi-card {color}">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value {color} mono">{value}</div>
        <div class="kpi-delta {delta_class}">{delta}</div>
    </div>
    """


# ─────────────────────────────────────────────────────────────────────────────
# HELPER: Folium Map Builder
# ─────────────────────────────────────────────────────────────────────────────
def build_folium_map(df: pd.DataFrame) -> folium.Map:
    """
    Constructs an interactive Folium choropleth-style map with color-coded
    heat circles per district. Circle color encodes OOSC severity.
    Red = high burden, Yellow = moderate, Green = low burden.
    """
    # Center map on Pakistan
    m = folium.Map(
        location=[29.5, 68.5],
        zoom_start=5,
        tiles="CartoDB positron",
        control_scale=True,
    )

    # Color scale: green → yellow → red based on OOSC percentage
    def oosc_to_color(pct: float) -> str:
        if pct < 25:   return "#2CA02C"   # green  — low severity
        elif pct < 40: return "#E8860A"   # amber  — moderate
        elif pct < 55: return "#D62728"   # red    — high
        else:          return "#7B0D1E"   # deep red — critical

    for _, row in df.iterrows():
        color  = oosc_to_color(row["OOSC_Pct"])
        radius = int(row["OOSC_Pct"] * 700)  # scale circle to severity

        popup_html = f"""
        <div style="font-family:DM Sans,sans-serif;min-width:220px;padding:4px;">
            <div style="font-size:13px;font-weight:700;color:#003366;border-bottom:2px solid #003366;padding-bottom:6px;margin-bottom:8px;">
                📍 {row['District']}
            </div>
            <table style="width:100%;font-size:11.5px;border-collapse:collapse;">
                <tr><td style="color:#666;padding:3px 0;">Province</td>
                    <td style="font-weight:600;text-align:right;">{row['Province']}</td></tr>
                <tr><td style="color:#666;padding:3px 0;">Zone</td>
                    <td style="font-weight:600;text-align:right;">{row['Zone']}</td></tr>
                <tr style="background:#fff3f3;"><td style="color:#C0392B;padding:3px 4px;font-weight:600;">OOSC</td>
                    <td style="font-weight:700;color:#C0392B;text-align:right;">{row['OOSC_Count']:,} ({row['OOSC_Pct']}%)</td></tr>
                <tr><td style="color:#666;padding:3px 0;">Literacy Rate</td>
                    <td style="font-weight:600;text-align:right;">{row['Literacy_Rate']}%</td></tr>
                <tr><td style="color:#666;padding:3px 0;">Dropout Rate</td>
                    <td style="font-weight:600;text-align:right;">{row['Dropout_Rate']}%</td></tr>
                <tr><td style="color:#666;padding:3px 0;">Infra Gap</td>
                    <td style="font-weight:600;text-align:right;">{row['Infra_Lacking_Pct']}%</td></tr>
                <tr style="background:#f0f8f0;"><td style="color:#2CA02C;padding:3px 4px;font-weight:600;">Opt. Score</td>
                    <td style="font-weight:700;color:#2CA02C;text-align:right;">{row['Opt_Score']}/100</td></tr>
            </table>
        </div>
        """

        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=max(12, min(radius // 100, 40)),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.55,
            weight=2,
            popup=folium.Popup(popup_html, max_width=260),
            tooltip=f"<b>{row['District']}</b> — OOSC: {row['OOSC_Pct']}%",
        ).add_to(m)

    # Custom legend
    legend_html = """
    <div style="position:fixed;bottom:24px;left:24px;z-index:1000;
                background:white;padding:12px 16px;border-radius:10px;
                box-shadow:0 4px 16px rgba(0,0,0,0.15);
                font-family:DM Sans,sans-serif;font-size:11.5px;">
        <div style="font-weight:700;color:#003366;margin-bottom:8px;font-size:12px;">
            OOSC Severity Index
        </div>
        <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px;">
            <div style="width:14px;height:14px;border-radius:50%;background:#2CA02C;"></div>
            <span style="color:#444;">Low (&lt;25%)</span>
        </div>
        <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px;">
            <div style="width:14px;height:14px;border-radius:50%;background:#E8860A;"></div>
            <span style="color:#444;">Moderate (25–40%)</span>
        </div>
        <div style="display:flex;align-items:center;gap:7px;margin-bottom:5px;">
            <div style="width:14px;height:14px;border-radius:50%;background:#D62728;"></div>
            <span style="color:#444;">High (40–55%)</span>
        </div>
        <div style="display:flex;align-items:center;gap:7px;">
            <div style="width:14px;height:14px;border-radius:50%;background:#7B0D1E;"></div>
            <span style="color:#444;">Critical (&gt;55%)</span>
        </div>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    return m


# ─────────────────────────────────────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────────────────────────────────────
def main():
    # ── Load Data ─────────────────────────────────────────────────────────────
    raw_df = generate_education_data()

    # ── Header Banner ─────────────────────────────────────────────────────────
    st.markdown("""
    <div class="ita-header">
        <div class="ita-header-eyebrow">Idara-e-Taleem-o-Aagahi (ITA) · Parwaaz Fellowship</div>
        <h1>Education Emergency &amp; ASER Data Tracker</h1>
        <div class="ita-header-sub">
            An interactive intelligence platform for monitoring out-of-school children,
            foundational literacy outcomes, and infrastructure deficits across Pakistan's districts.
            Built on ASER-calibrated synthetic indicators for evidence-based policymaking.
        </div>
        <div class="ita-header-badge">⚡ Live Dashboard · 18 Districts · 4 Provinces</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Global Filters ─────────────────────────────────────────────────────────
    st.markdown('<div class="filter-label">🎛️ &nbsp;Global Filters</div>', unsafe_allow_html=True)

    filter_col1, filter_col2, filter_col3 = st.columns([2, 2, 4])

    with filter_col1:
        province_opts = ["All Provinces"] + sorted(raw_df["Province"].unique().tolist())
        selected_province = st.selectbox("Province", province_opts, key="province_filter")

    with filter_col2:
        zone_opts = ["All Zones", "Urban", "Rural"]
        selected_zone = st.selectbox("Zone", zone_opts, key="zone_filter")

    with filter_col3:
        st.markdown("")  # spacer

    # ── Apply Filters ──────────────────────────────────────────────────────────
    df = raw_df.copy()
    if selected_province != "All Provinces":
        df = df[df["Province"] == selected_province]
    if selected_zone != "All Zones":
        df = df[df["Zone"] == selected_zone]

    # Graceful empty-state handler
    if df.empty:
        st.warning("⚠️ No data matches the current filter combination. Please adjust your selections.")
        st.stop()

    # ── KPI Computations ───────────────────────────────────────────────────────
    total_oosc       = df["OOSC_Count"].sum()
    avg_literacy     = df["Literacy_Rate"].mean()
    avg_infra_gap    = df["Infra_Lacking_Pct"].mean()
    avg_opt_score    = df["Opt_Score"].mean()
    total_children   = df["Total_Children"].sum()
    oosc_national    = (total_oosc / total_children * 100) if total_children > 0 else 0

    # ── KPI Row ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
        <h2>Strategic Overview</h2>
        <span class="section-pill">Key Performance Indicators</span>
    </div>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.markdown(kpi_card(
            icon="👧🏽",
            label="Total OOSC (Filtered)",
            value=f"{total_oosc:,.0f}",
            delta=f"▼ {oosc_national:.1f}% of child population",
            color="red"
        ), unsafe_allow_html=True)

    with k2:
        lit_delta = "▲ Above target" if avg_literacy >= 60 else "▼ Below 60% benchmark"
        st.markdown(kpi_card(
            icon="📖",
            label="Avg Foundational Literacy",
            value=f"{avg_literacy:.1f}%",
            delta=lit_delta,
            color="green" if avg_literacy >= 60 else "amber"
        ), unsafe_allow_html=True)

    with k3:
        st.markdown(kpi_card(
            icon="🏫",
            label="Schools w/ Infra Deficit",
            value=f"{avg_infra_gap:.1f}%",
            delta="▼ Lacking water or sanitation",
            color="amber"
        ), unsafe_allow_html=True)

    with k4:
        st.markdown(kpi_card(
            icon="📊",
            label="Resource Optimization Score",
            value=f"{avg_opt_score:.1f}",
            delta="/ 100 composite index",
            color="blue"
        ), unsafe_allow_html=True)

    st.markdown("<hr class='ita-divider'>", unsafe_allow_html=True)

    # ── Geospatial Intelligence Map ────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
        <h2>Geospatial Intelligence</h2>
        <span class="section-pill">District Heat Map</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    folium_map = build_folium_map(df)
    st_folium(folium_map, width=None, height=480, returned_objects=[])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr class='ita-divider'>", unsafe_allow_html=True)

    # ── Diagnostic Analytics ───────────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
        <h2>Diagnostic Analytics</h2>
        <span class="section-pill">Enrollment · Dropout · Causes</span>
    </div>
    """, unsafe_allow_html=True)

    chart_left, chart_right = st.columns([3, 2])

    # ── Left: Stacked Bar — Enrollment vs Dropout ──────────────────────────────
    with chart_left:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">📊 Enrollment vs. Active Dropout by District</div>', unsafe_allow_html=True)

        bar_df = df.copy()
        bar_df["Active_Dropout"] = (bar_df["Enrolled"] * bar_df["Dropout_Rate"] / 100).astype(int)
        bar_df["Net_Enrolled"]   = bar_df["Enrolled"] - bar_df["Active_Dropout"]
        bar_df_sorted = bar_df.nlargest(12, "OOSC_Count")

        fig_bar = go.Figure()

        fig_bar.add_trace(go.Bar(
            name="Net Enrolled",
            x=bar_df_sorted["District"],
            y=bar_df_sorted["Net_Enrolled"],
            marker_color="#003366",
            marker_line_width=0,
        ))
        fig_bar.add_trace(go.Bar(
            name="Active Dropout",
            x=bar_df_sorted["District"],
            y=bar_df_sorted["Active_Dropout"],
            marker_color="#E8860A",
            marker_line_width=0,
        ))
        fig_bar.add_trace(go.Bar(
            name="Out-of-School",
            x=bar_df_sorted["District"],
            y=bar_df_sorted["OOSC_Count"],
            marker_color="#C0392B",
            marker_line_width=0,
        ))

        fig_bar.update_layout(
            barmode="stack",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=8, b=0),
            height=360,
            legend=dict(
                orientation="h", yanchor="bottom", y=1.01,
                xanchor="left", x=0,
                font=dict(size=11, family="DM Sans"),
                bgcolor="rgba(0,0,0,0)",
            ),
            xaxis=dict(
                tickangle=-35,
                tickfont=dict(size=10, family="DM Sans"),
                gridcolor="rgba(0,0,0,0)",
                linecolor="#DDE3EE",
            ),
            yaxis=dict(
                tickfont=dict(size=10, family="DM Sans"),
                gridcolor="#F0F2F8",
                linecolor="rgba(0,0,0,0)",
                tickformat=",",
            ),
            font=dict(family="DM Sans"),
            hoverlabel=dict(font_size=12, font_family="DM Sans"),
        )

        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Right: Donut — Primary Dropout Causes ─────────────────────────────────
    with chart_right:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title">🔍 Primary Causes of Dropout</div>', unsafe_allow_html=True)

        cause_values = [
            df["Cause_Economic"].mean(),
            df["Cause_Distance"].mean(),
            df["Cause_ChildLabor"].mean(),
            df["Cause_NoFacilities"].mean(),
        ]
        cause_labels = ["Economic Hardship", "Distance to School", "Child Labour", "Lack of Facilities"]
        cause_colors = ["#003366", "#2CA02C", "#C0392B", "#E8860A"]

        fig_donut = go.Figure(go.Pie(
            labels=cause_labels,
            values=cause_values,
            hole=0.55,
            marker=dict(colors=cause_colors, line=dict(color="white", width=2)),
            textinfo="percent",
            textfont=dict(size=11, family="DM Sans"),
            hovertemplate="<b>%{label}</b><br>Avg Share: %{value:.1f}%<extra></extra>",
        ))

        fig_donut.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=8, b=0),
            height=360,
            showlegend=True,
            legend=dict(
                orientation="v",
                font=dict(size=11, family="DM Sans"),
                bgcolor="rgba(0,0,0,0)",
                itemsizing="constant",
            ),
            annotations=[dict(
                text="<b>Causes</b>",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=14, family="DM Serif Display", color="#003366"),
            )],
            hoverlabel=dict(font_size=12, font_family="DM Sans"),
        )

        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<hr class='ita-divider'>", unsafe_allow_html=True)

    # ── Intervention Simulator ─────────────────────────────────────────────────
    st.markdown("""
    <div class="section-header">
        <h2>Intervention Simulator</h2>
        <span class="section-pill">Policymaker Tool</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="simulator-panel">', unsafe_allow_html=True)
    st.markdown("""
        <div class="simulator-title">💡 Budget Allocation Engine</div>
        <div class="simulator-subtitle">
            Simulate the projected impact of monthly budget allocations on OOSC reduction.
            Adjust parameters below to model different intervention strategies.
        </div>
    """, unsafe_allow_html=True)

    sim_col1, sim_col2, sim_col3 = st.columns([2, 2, 2])

    with sim_col1:
        # Budget slider — styled via CSS override above
        budget_pkr = st.slider(
            "Simulated Monthly Budget (PKR)",
            min_value=500_000,
            max_value=50_000_000,
            value=10_000_000,
            step=500_000,
            format="PKR %d",
            key="budget_slider",
            help="Set monthly intervention budget in Pakistani Rupees",
        )

    with sim_col2:
        strategy = st.radio(
            "Investment Strategy",
            options=["🏗️ Infrastructure Upgrades", "👩‍🏫 Targeted Teacher Training"],
            key="strategy_radio",
            help="Choose how the budget is primarily allocated",
        )

    # ── Simulator Logic ────────────────────────────────────────────────────────
    # Infrastructure: high capital cost per school; each school fixed reduces
    # dropout by eliminating distance/facility barriers (~0.8% OOSC reduction
    # per 10M PKR at base rate)
    # Teacher Training: lower unit cost, scalable; improves retention and
    # quality indicators (~1.2% OOSC reduction per 10M PKR at base rate)

    base_oosc_rate   = df["OOSC_Pct"].mean()          # % of children OOSC
    budget_in_crore  = budget_pkr / 10_000_000         # normalize to 10M PKR units

    if "Infrastructure" in strategy:
        efficiency_per_unit = 0.72    # % OOSC reduction per 10M PKR unit
        cost_per_school     = 3_500_000  # PKR per school upgraded
        cost_per_teacher    = 0
        schools_reached     = int(budget_pkr / cost_per_school)
        teachers_reached    = 0
    else:
        efficiency_per_unit = 1.15    # Teacher training is more cost-efficient
        cost_per_school     = 0
        cost_per_teacher    = 85_000   # PKR per teacher trained (monthly)
        schools_reached     = 0
        teachers_reached    = int(budget_pkr / cost_per_teacher)

    # Diminishing returns: log scale dampening for large budgets
    raw_reduction       = efficiency_per_unit * budget_in_crore
    diminished_reduction = raw_reduction / (1 + 0.04 * budget_in_crore)
    projected_reduction = min(diminished_reduction, base_oosc_rate * 0.65)  # cap at 65% of base
    projected_new_oosc  = int(total_oosc * (1 - projected_reduction / 100))
    children_reached    = max(0, total_oosc - projected_new_oosc)

    with sim_col3:
        st.markdown(f"""
        <div class="sim-result-box">
            <div class="sim-result-label">Projected OOSC Reduction</div>
            <div class="sim-result-value">{projected_reduction:.1f}<span style="font-size:1.4rem">%</span></div>
            <div class="sim-result-unit">≈ {children_reached:,} children re-enrolled</div>
        </div>
        """, unsafe_allow_html=True)

    # Detail metrics row
    d1, d2, d3, d4 = st.columns(4)

    budget_fmt = f"PKR {budget_pkr/1_000_000:.1f}M"

    metrics = [
        ("Monthly Budget",        budget_fmt,                    "💰"),
        ("Schools Upgraded" if schools_reached else "Teachers Trained",
         f"{schools_reached:,}" if schools_reached else f"{teachers_reached:,}", "🏫" if schools_reached else "👩‍🏫"),
        ("Post-Intervention OOSC", f"{projected_new_oosc:,}",    "📉"),
        ("Cost per Child Reached", f"PKR {int(budget_pkr / max(children_reached, 1)):,}", "🎯"),
    ]

    for col, (label, value, icon) in zip([d1, d2, d3, d4], metrics):
        with col:
            st.markdown(f"""
            <div class="sim-reach-item">
                <div class="sim-reach-label">{icon} {label}</div>
                <div class="sim-reach-value mono">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # close simulator-panel

    # ── Footer ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:2.5rem 0 1rem 0;color:#8A9BB0;font-size:0.78rem;line-height:1.8;">
        <strong style="color:#003366;">ITA Education Emergency &amp; ASER Data Tracker</strong>
        &nbsp;·&nbsp; Built for the Parwaaz Internship Application
        &nbsp;·&nbsp; Data is synthetic, ASER-calibrated for demonstration purposes
        <br>
        Framework: Streamlit · Plotly · Folium · Pandas · NumPy
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
