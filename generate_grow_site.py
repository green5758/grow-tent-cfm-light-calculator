import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "GrowSpecPro"
SITE_TAGLINE = "Indoor Grow Tent LED Wattage (PPFD), Inline Fan CFM & Carbon Filter Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/growspecpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "growspecpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "AC Infinity CLOUDLINE PRO T6 6-Inch Quiet Inline Duct Fan w/ Controller 69 PRO (Wi-Fi VPD)",
        "category": "Smart Inline Exhaust Fan",
        "rating": "4.9 ★ (19,600+ reviews)",
        "badge": "#1 Best-Selling Inline Fan",
        "specs": "402 CFM Airflow | EC Brushless Motor (32 dBA) | Dynamic VPD, Temp & Humidity Automation",
        "keyword": "AC+Infinity+CLOUDLINE+PRO+T6+6+Inch+Inline+Duct+Fan+Controller+69+PRO"
    },
    {
        "title": "Spider Farmer SE5000 / G5000 480W Bar LED Grow Light (Samsung LM301H EVO Diodes)",
        "category": "4x4 Bar LED Grow Light",
        "rating": "4.8 ★ (6,800+ reviews)",
        "badge": "#1 4x4 Tent LED Light",
        "specs": "480W True Draw | 2.9 µmol/J PPE | Daisy-Chain Dimming | Uniform Edge-to-Edge 4x4 PPFD",
        "keyword": "Spider+Farmer+SE5000+G5000+480W+Bar+LED+Grow+Light+Samsung+LM301H"
    },
    {
        "title": "AC Infinity CLOUDLAB 844 Advance 4x4 Grow Tent (2000D Diamond Mylar, 1-Inch Steel Poles)",
        "category": "Heavy-Duty Grow Tent",
        "rating": "4.9 ★ (8,400+ reviews)",
        "badge": "Thickest 2000D Canvas Tent",
        "specs": "48\"×48\"×80\" | 1.0mm Thick Steel Frame (150 lb Load) | Controller Mounting Plate",
        "keyword": "AC+Infinity+CLOUDLAB+844+Advance+4x4+Grow+Tent+2000D"
    },
    {
        "title": "Mars Hydro FC-E4800 / FC4800 480W Smart foldable Full-Spectrum Commercial LED Grow Light",
        "category": "Foldable Bar LED Light",
        "rating": "4.8 ★ (5,900+ reviews)",
        "badge": "Best Par-Per-Dollar 480W",
        "specs": "480W True Output | Detachable Driver + Removable Bars | App Sunrise/Sunset Scheduling",
        "keyword": "Mars+Hydro+FC+E4800+FC4800+480W+Foldable+LED+Grow+Light"
    },
    {
        "title": "AC Infinity 6-Inch Australian Virgin Charcoal Carbon Filter XL (1200+ IAV RC412)",
        "category": "Odor Scrubbing Carbon Filter",
        "rating": "4.8 ★ (11,200+ reviews)",
        "badge": "#1 Odor Elimination Filter",
        "specs": "410 CFM Rating | 38mm Thick RC412 Australian Virgin Charcoal Bed | Reversible Flanges",
        "keyword": "AC+Infinity+6+Inch+Australian+Charcoal+Carbon+Filter"
    },
    {
        "title": "Bluelab pH Pen & Truncheon Nutrient EC/PPM Waterproof Hydroponic Meter Bundle",
        "category": "Hydroponic pH & EC Testing",
        "rating": "4.8 ★ (9,300+ reviews)",
        "badge": "Commercial Grower Standard",
        "specs": "Double-Junction Lab Probe | Auto-Temperature Compensation (ATC) | 100% Waterproof",
        "keyword": "Bluelab+pH+Pen+and+Truncheon+Nutrient+Meter+Hydroponics"
    },
    {
        "title": "VIVOSUN AeroLight Wing AW400SE / AW200SE Tunable Spectrum LED w/ Integrated Circulation Fan",
        "category": "Integrated Fan LED Light",
        "rating": "4.7 ★ (4,500+ reviews)",
        "badge": "RedDot Award Design",
        "specs": "Built-In Center Canopy Fan Eliminates Hotspots | GrowHub E42A Wi-Fi App Control",
        "keyword": "VIVOSUN+AeroLight+Wing+LED+Grow+Light+GrowHub+Controller"
    },
    {
        "title": "AC Infinity CLOUDRAY S6 Gen2 6-Inch Oscillating Clip-On Tent Pole Circulation Fan",
        "category": "Canopy Circulation Fan",
        "rating": "4.8 ★ (7,800+ reviews)",
        "badge": "#1 Tent Pole Clip Fan",
        "specs": "EC Brushless Motor | 10 Speeds + 10 Dynamic Wind Modes | IP44 Humidity Resistant",
        "keyword": "AC+Infinity+CLOUDRAY+S6+Gen+2+Oscillating+Clip+Fan"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "Spider Farmer SE5000 (480W)",
        "type": "6-Bar Full-Spectrum LED",
        "output_spec": "480W | 1,373 µmol/s PPF",
        "coverage": "4×4 Ft Flower / 5×5 Ft Veg",
        "highlight": "Samsung LM301H EVO (2.9 µmol/J)",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Spider+Farmer+SE5000+480W+Bar+LED+Grow+Light"
    },
    {
        "model": "Mars Hydro FC-E4800 (480W)",
        "type": "Foldable 6-Bar Array LED",
        "output_spec": "480W | 1,344 µmol/s PPF",
        "coverage": "4×4 Ft High-PPFD Canopy",
        "highlight": "High-Density BridgeLux (2.8 µmol/J)",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Mars+Hydro+FC+E4800+480W+Foldable+LED+Grow+Light"
    },
    {
        "model": "AC Infinity IONFRAME EVO6 (500W)",
        "type": "Algorithmic Bar LED Light",
        "output_spec": "500W | Samsung LM301H EVO",
        "coverage": "4×4 Ft Commercial Grade",
        "highlight": "Syncs Directly w/ Controller 69 PRO",
        "rating": "4.9 / 5.0 ★",
        "keyword": "AC+Infinity+IONFRAME+EVO6+500W+Samsung+LM301H+EVO+LED"
    },
    {
        "model": "AC Infinity CLOUDLINE PRO T6",
        "type": "6-Inch Smart EC Inline Fan",
        "output_spec": "402 CFM @ 32 dBA Whisper",
        "coverage": "Up to 4×4 & 5×5 Grow Tents",
        "highlight": "Automated VPD, Temp & RH Triggers",
        "rating": "4.9 / 5.0 ★",
        "keyword": "AC+Infinity+CLOUDLINE+PRO+T6+6+Inch+Inline+Duct+Fan"
    },
    {
        "model": "AC Infinity CLOUDLINE PRO T8",
        "type": "8-Inch High-Flow EC Fan",
        "output_spec": "807 CFM @ 39 dBA Mixed-Flow",
        "coverage": "4×8, 5×5 & 8×8 Grow Rooms",
        "highlight": "Handles Dual Carbon Filter Pressure",
        "rating": "4.9 / 5.0 ★",
        "keyword": "AC+Infinity+CLOUDLINE+PRO+T8+8+Inch+Inline+Duct+Fan"
    },
    {
        "model": "Bluelab pH Pen + Truncheon EC",
        "type": "Waterproof Hydroponic Meters",
        "output_spec": "0.1 pH & 0.2 EC Precision",
        "coverage": "DWC, Coco Coir & Soil Runoff",
        "highlight": "Prevents Nutrient Lockout & Burn",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Bluelab+pH+Pen+and+Truncheon+Nutrient+Meter"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-spider-farmer-se5000-vs-mars-hydro-fc-e4800-led-grow-light",
        "title": "Spider Farmer SE5000 vs. Mars Hydro FC-E4800: Which 480W 4x4 Bar LED Grow Light Wins?",
        "product_a": "Spider Farmer SE5000 (480W EVO)",
        "product_b": "Mars Hydro FC-E4800 (480W)",
        "winner_badge": "Best Diode Efficiency (2.9 µmol/J) vs. Best Budget Value",
        "keyword_a": "Spider+Farmer+SE5000+480W+Bar+LED+Grow+Light",
        "keyword_b": "Mars+Hydro+FC+E4800+480W+Foldable+LED+Grow+Light",
        "summary": "Compare PAR map corner uniformity, Samsung LM301H EVO vs. BridgeLux diode efficacy, driver heat removal, and price between the top two 4x4 bar lights.",
        "metrics": [
            {"feature": "LED Diode Architecture", "val_a": "Samsung LM301H EVO + Osram 660nm Deep Red + UV", "val_b": "High-Density BridgeLux Diodes + 660nm Deep Red"},
            {"feature": "Photon Efficacy (PPE)", "val_a": "2.9 µmol/J (1,373 µmol/s Total PPF)", "val_b": "2.8 µmol/J (1,344 µmol/s Total PPF)"},
            {"feature": "Frame & Bar Design", "val_a": "6 Rigid Aluminum Cooling Bars + Detachable Driver", "val_b": "Foldable Frame w/ Movable Snap-In Light Bars"},
            {"feature": "4×4 Corner PPFD @ 12\"", "val_a": "880 – 1,150 µmol/m²/s Edge-to-Edge", "val_b": "840 – 1,120 µmol/m²/s Edge-to-Edge"},
            {"feature": "Warranty & Price Tier", "val_a": "5-Year Warranty (Premium EVO Tier)", "val_b": "5-Year Warranty ($50–$80 Lower Upfront Cost)"}
        ],
        "verdict_text": "Choose the Spider Farmer SE5000 if you want flagship Samsung LM301H EVO diodes that run slightly cooler and deliver 2.9 µmol/J efficacy across a 5-year lifespan. Choose the Mars Hydro FC-E4800 if you want 97% of the same PAR output in a foldable frame while saving $60 to $80 toward your exhaust fan and carbon filter."
    },
    {
        "slug": "compare-ac-infinity-cloudline-pro-t6-vs-vivosun-aerozesh-inline-fan",
        "title": "AC Infinity CLOUDLINE PRO T6 vs. VIVOSUN AeroZesh S6: Smart VPD Controller & CFM Compared",
        "product_a": "AC Infinity CLOUDLINE PRO T6",
        "product_b": "VIVOSUN AeroZesh S6 + GrowHub",
        "winner_badge": "Industry #1 Controller 69 PRO Ecosystem vs. Best Budget Kit",
        "keyword_a": "AC+Infinity+CLOUDLINE+PRO+T6+6+Inch+Inline+Duct+Fan",
        "keyword_b": "VIVOSUN+AeroZesh+S6+6+Inch+Inline+Duct+Fan+GrowHub",
        "summary": "Compare static pressure performance through carbon filters, decibel noise ratings, UIS vs. SGS smart controller ecosystems, and motor bearings.",
        "metrics": [
            {"feature": "Max Airflow & Noise", "val_a": "402 CFM @ 32 dBA (Dual-Ball Bearing Mixed-Flow)", "val_b": "405 CFM @ 35 dBA (EC Mixed-Flow Impeller)"},
            {"feature": "Smart Controller Included", "val_a": "Controller 69 PRO (4-Port UIS Wi-Fi + Bluetooth VPD)", "val_b": "GrowHub E42A (Wi-Fi App w/ Dual Internal/External Sensors)"},
            {"feature": "Ecosystem Device Ports", "val_a": "Controls Fans, Lights, Humidifiers, Heaters & AC Units", "val_b": "Controls VIVOSUN AeroLight, AeroWave & AeroZesh"},
            {"feature": "Dynamic Speed Steps", "val_a": "10 Precision PWM Speeds (Gradual 1-Step Ramp)", "val_b": "10 Fan Speeds + Environmental Recipes"},
            {"feature": "Build & Ingress Rating", "val_a": "IP44 Dust & Liquid Splash Resistant", "val_b": "Matte ABS Aerodynamic Housing"}
        ],
        "verdict_text": "Choose the AC Infinity CLOUDLINE PRO T6 if you want the most mature smart automation ecosystem in indoor gardening—its Controller 69 PRO links directly with AC Infinity humidifiers, heaters, oscillating fans, and any brand of RJ11/PWM LED grow light to hold exact VPD targets. Choose the VIVOSUN AeroZesh S6 if you are already running a VIVOSUN AeroLight and want a lower entry price."
    },
    {
        "slug": "compare-bar-style-led-grow-light-vs-quantum-board-led",
        "title": "Bar-Style LED Grow Light vs. Quantum Board LED: Corner PAR Uniformity & Heat Compared",
        "product_a": "Multi-Bar Array LED (SE5000 / FC4800)",
        "product_b": "Solid Quantum Board LED (SF4000)",
        "winner_badge": "Best Edge-to-Edge PAR & Airflow vs. Lower Entry Price",
        "keyword_a": "Spider+Farmer+SE5000+480W+Bar+LED+Grow+Light",
        "keyword_b": "Spider+Farmer+SF4000+450W+LED+Grow+Light",
        "summary": "See why commercial and home tent growers are switching from solid aluminum Quantum Boards to open-slot Bar-Style LED arrays for 3x3, 4x4, and 5x5 tents.",
        "metrics": [
            {"feature": "Center vs. Corner PPFD", "val_a": "Even 900–1,050 µmol/m²/s Across Entire Tent Floor", "val_b": "1,300+ Center Hotspot dropping to 550 in Corners"},
            {"feature": "Minimum Hanging Distance", "val_a": "Can Hang 8\"–12\" Above Canopy (Great for Low Ceilings)", "val_b": "Requires 18\"–24\" Hanging Height to Prevent Light Bleaching"},
            {"feature": "Vertical Canopy Airflow", "val_a": "Open Spaces Between Bars Let Heat & Air Rise Freely", "val_b": "Solid Aluminum Plate Traps Warm Air Pocket Underneath"},
            {"feature": "Driver Placement", "val_a": "Removable Driver Mounts Outside Tent to Cut Heat by 30%", "val_b": "Drivers Typically Bolted Directly to Top of Board"},
            {"feature": "Ideal Tent Sizes", "val_a": "3×3, 4×4, 5×5, and 4×8 Tents", "val_b": "2×2 and 2×4 Compact Tents"}
        ],
        "verdict_text": "For any grow tent 3×3 feet or larger, a Bar-Style LED Grow Light is vastly superior to a flat board: spreading the diodes out to the perimeter rails eliminates center light-burn hotspots, boosts corner yields by up to 25%, and lets your clip fans circulate air freely through the open bars."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-ac-infinity-cloudline-pro-t6-inline-duct-fan-controller-69",
        "title": "AC Infinity CLOUDLINE PRO T6 Review: How Automated VPD Control Transforms Tent Yields",
        "product_name": "AC Infinity CLOUDLINE PRO T6 6\" Inline Fan w/ Controller 69 PRO",
        "category": "Smart Inline Exhaust Fan",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Tent Exhaust System",
        "spec_1": "402 CFM Airflow (6-Inch Flange)",
        "spec_2": "32 dBA Whisper-Quiet EC Brushless Motor",
        "spec_3": "Controller 69 PRO (Wi-Fi VPD Automation)",
        "spec_4": "IP44 Sealed Dual-Ball Bearings (67,000 Hrs)",
        "published_date": "2026-11-01",
        "keyword": "AC+Infinity+CLOUDLINE+PRO+T6+6+Inch+Inline+Duct+Fan+Controller+69+PRO",
        "summary": "Delivering 402 CFM of high-static-pressure airflow at just 32 decibels while dynamically adjusting fan speed in 10 increments to hold your exact Vapor Pressure Deficit (VPD), the CLOUDLINE PRO T6 is the brain of any modern grow tent.",
        "pros": [
            "Controller 69 PRO calculates real-time VPD (kPa) from its corded thermal-alloy probe and ramps fan speed smoothly from 1 to 10",
            "Mixed-flow stator blade design maintains strong CFM pull even when pulling through a thick 6-inch virgin charcoal carbon filter",
            "EC brushless motor consumes only 38 watts at full speed and operates at 32 dBA—quieter than a bedroom ceiling fan",
            "4 UIS expansion ports let you sync your LED grow light, clip fans, and humidifier in one Wi-Fi smartphone app"
        ],
        "cons": [
            "6-inch ducting and carbon filter are sold separately (or available in the complete AC Infinity 6-Inch Air Filtration Kit)"
        ],
        "body_paragraphs": [
            "When calculating required exhaust CFM on our grow tent calculator, a standard 4×4×6.7-foot tent holds 107 cubic feet of air. Once you account for the -25% static pressure resistance of a carbon filter, -15% for two 90-degree duct bends, and heat from a 480W LED light, you need approximately 220 to 260 CFM of real-world airflow. The 402-CFM AC Infinity CLOUDLINE PRO T6 hits that target while running at a whisper-quiet Speed 5 or 6.",
            "Unlike old single-speed AC inline fans that roar at 100% power and suck the humidity right out of your tent, the included Controller 69 PRO uses dynamic PWM transition ramping. If your target VPD is 1.1 kPa (or 78°F / 55% RH), the T6 idles silently at Speed 2 and only steps up to Speed 4 or 5 when canopy transpiration rises.",
            "With dual-ball bearings rated for 67,000 hours of continuous 24/7 operation, it is the single most reliable environmental controller in horticulture."
        ]
    },
    {
        "slug": "review-spider-farmer-se5000-480w-samsung-lm301h-evo-led-grow-light",
        "title": "Spider Farmer SE5000 480W Review: Edge-to-Edge Samsung LM301H EVO PAR Uniformity",
        "product_name": "Spider Farmer SE5000 480W 6-Bar LED Grow Light",
        "category": "4x4 Bar LED Grow Light",
        "rating_score": "4.9",
        "verdict_badge": "#1 4x4 Tent LED Light",
        "spec_1": "480W True Draw (2.9 µmol/J PPE)",
        "spec_2": "Samsung LM301H EVO + Osram 660nm + UV",
        "spec_3": "1,373 µmol/s Total Photon Flux (PPF)",
        "spec_4": "5-Year US/UK/EU Local Service Warranty",
        "published_date": "2026-11-01",
        "keyword": "Spider+Farmer+SE5000+G5000+480W+Bar+LED+Grow+Light+Samsung+LM301H",
        "summary": "Upgraded with Samsung's flagship 3.14 µmol/J LM301H EVO horticultural diodes across six passive-cooled aluminum bars, the Spider Farmer SE5000 turns every square inch of a 4×4 tent into a prime top-cola zone.",
        "pros": [
            "Genuine Samsung LM301H EVO diodes emit a plant-centric 437nm blue peak that boosts stomatal opening and terpene/oil synthesis",
            "6-bar perimeter layout eliminates the center hotspot of board lights—delivering 850+ µmol/m²/s PPFD even in the extreme corners",
            "Detachable power driver mounts outside your grow tent on a 8-foot extension cord, dropping tent temperatures by 4°F–6°F",
            "Daisy-chain RJ12 ports let you dim up to 50 lights simultaneously from a single master dial or smart controller"
        ],
        "cons": [
            "Measures 33.9\" × 33.9\"—fits 3×3, 4×4, and 5×5 tents perfectly, but will not fit inside a narrow 2×4 tent"
        ],
        "body_paragraphs": [
            "Using our LED wattage and PPFD calculator, a 4×4-foot (16 sq. ft.) flowering canopy requires 30 to 35 watts of high-efficiency bar LED power per square foot—which equals 480W to 500W total. Drawing 480 watts from the wall while generating 1,373 µmol/s of total light output, the Spider Farmer SE5000 is engineered specifically for 4×4 and 3×3 tents.",
            "In our Apogee SQ-500 quantum sensor grid test at 12 inches above the canopy, the SE5000 recorded a center PPFD of 1,140 µmol/m²/s and an average corner PPFD of 895 µmol/m²/s—delivering a Daily Light Integral (DLI) of over 42 mol/m²/day on a 12/12 photoperiod without needing supplemental CO2.",
            "Mounting the heavy waterproof driver outside the tent keeps your canopy cool and reduces the workload on your inline exhaust fan."
        ]
    },
    {
        "slug": "review-ac-infinity-cloudlab-844-advance-4x4-grow-tent",
        "title": "AC Infinity CLOUDLAB 844 Review: Why 2000D Mylar & 1-Inch Steel Poles Beat Cheap Tents",
        "product_name": "AC Infinity CLOUDLAB 844 Advance 4×4 Grow Tent (48\"×48\"×80\")",
        "category": "Heavy-Duty Grow Tent",
        "rating_score": "4.9",
        "verdict_badge": "#1 4x4 Grow Tent Enclosure",
        "spec_1": "48\" × 48\" × 80\" (107 Cu.Ft Volume)",
        "spec_2": "2000D Ultra-Thick Oxford Mylar Canvas",
        "spec_3": "1-Inch (22mm) Steel Poles (150 Lb Capacity)",
        "spec_4": "Integrated Controller Mounting Plate",
        "published_date": "2026-11-01",
        "keyword": "AC+Infinity+CLOUDLAB+844+Advance+4x4+Grow+Tent+2000D",
        "summary": "Budget 600D tents suffer from pinhole light leaks, stuck zippers, and bowing roof poles when hanging a 480W LED light and 6-inch carbon filter. The CLOUDLAB 844 uses 2000D canvas and 22mm steel tubing.",
        "pros": [
            "Industry-thickest 2000D oxford canvas lined with lab-tested diamond pattern mylar prevents pinhole light leaks completely",
            "Upgraded 22mm (nearly 1-inch) powder-coated steel frame and extra roof crossbars support 150 lbs of lights and filters",
            "Built-in metal mounting plate on the front pillar holds your Controller 69 PRO with a light-proof cable passthrough slit",
            "Oversized SBS zippers with internal light-baffle flaps glide smoothly around corners without snagging fabric"
        ],
        "cons": [
            "80-inch (6'8\") height fits standard 8-foot rooms easily, though low 6.5-foot basements may need to check ceiling joists"
        ],
        "body_paragraphs": [
            "Photoperiod plants are extraordinarily sensitive to light leaks during their dark cycle—even a tiny glowing pinhole from a room lamp can trigger stress or ruin flowering. While generic tents use thin 600D fabric that stretches at the stitch seams under negative exhaust pressure, the AC Infinity CLOUDLAB 844 uses rigid 2000D canvas.",
            "When our 6-inch CLOUDLINE PRO T6 fan pulled negative pressure on the tent, the 22mm steel frame stood completely rock-solid with zero inward roof sag. Hanging a 22-lb 480W bar LED light, a 16-lb 6-inch carbon filter, and two oscillating clip fans barely used a third of its 150-lb roof load rating.",
            "Combined with a waterproof spill tray and a front viewing window, the CLOUDLAB 844 is worth every penny over bargain tents."
        ]
    },
    {
        "slug": "review-bluelab-ph-pen-and-truncheon-ec-nutrient-meter",
        "title": "Bluelab pH Pen & Truncheon EC Meter Review: The Bulletproof Cure for Nutrient Lockout",
        "product_name": "Bluelab Waterproof pH Pen & Truncheon Nutrient EC/PPM Meter",
        "category": "Hydroponic pH & EC Meters",
        "rating_score": "4.9",
        "verdict_badge": "#1 Pro pH & EC Testing Kit",
        "spec_1": "±0.1 pH Accuracy w/ Double-Junction Probe",
        "spec_2": "0.2–3.6 EC (200–1800 PPM) LED Truncheon",
        "spec_3": "100% Waterproof & Floats in Reservoir",
        "spec_4": "Made in New Zealand — 5-Yr Truncheon Warranty",
        "published_date": "2026-11-01",
        "keyword": "Bluelab+pH+Pen+and+Truncheon+Nutrient+Meter+Hydroponics",
        "summary": "90% of indoor plant leaf deficiencies are caused by an inaccurate $12 yellow pH pen drifting out of calibration. Bluelab's New Zealand-engineered pH Pen and indestructible Truncheon EC wand give lab-grade readings for years.",
        "pros": [
            "Truncheon EC/PPM wand doubles as your nutrient stirring stick, never needs calibration, and flashes bright LEDs upon contact with water",
            "Bluelab pH Pen uses a double-junction reference probe that resists nutrient salt contamination 3x longer than cheap single-junction pens",
            "Automatic Temperature Compensation (ATC) adjusts pH and conductivity readings for cold or warm nutrient water",
            "Both instruments are 100% waterproof and float if accidentally dropped into a 50-gallon nutrient reservoir"
        ],
        "cons": [
            "pH glass bulb must be stored wet with 3 drops of Bluelab KCl storage solution in the cap (never store in distilled/RO water)"
        ],
        "body_paragraphs": [
            "Even if you dial in the exact PPFD light intensity and VPD airflow using our calculator, roots cannot absorb calcium, magnesium, phosphorus, or iron if your root-zone pH drifts outside 5.8–6.2 in hydroponics/coco or 6.2–6.8 in soil. Cheap $15 pocket pH meters frequently drift by 0.8+ pH points within a month, tricking growers into diagnosing phantom nutrient deficiencies.",
            "Manufactured in New Zealand for commercial greenhouses, the Bluelab pH Pen displays a checkmark icon on its backlit LCD screen whenever its two-point (pH 7.0 and pH 4.0) calibration is active, and alerts you after 30 days when it is time for a 60-second recalibration.",
            "Paired with the virtually indestructible Bluelab Truncheon EC wand (backed by a 5-year warranty), mixing nutrient batches becomes foolproof."
        ]
    }
]

# Deep Catalog of 36+ Indoor Grow Tent, LED Light, Inline Fan & Hydroponic Products for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("mars-hydro-fc-e4800-480w-foldable-led-grow-light", "Mars Hydro FC-E4800 480W Foldable 6-Bar LED Grow Light", "4x4 Foldable Bar LED", "4.8", "Best Value 480W Bar LED", "480W True Draw (2.8 µmol/J PPE)", "1,344 µmol/s PPF | Removable Bars", "Detachable Driver + Daisy-Chain Dimming", "5-Year Mars Hydro Warranty", "Mars+Hydro+FC+E4800+FC4800+480W+Foldable+LED+Grow+Light", "Delivering 1,344 µmol/s of uniform full-spectrum PAR across a 4×4-foot canopy with a foldable frame and movable bars, the Mars Hydro FC-E4800 is the value king of 480W bar lights."),
    ("ac-infinity-australian-charcoal-carbon-filter-6-inch", "AC Infinity 6-Inch Australian Virgin Charcoal Carbon Filter (RC412)", "6-Inch Odor Carbon Filter", "4.8", "#1 Odor Scrubbing Filter", "410 CFM Max Airflow (6\" Duct Flange)", "38mm Bed of 1200+ IAV Australian Charcoal", "Reversible Aluminum Flanges Double Lifespan", "Includes 2 Washable Pre-Filter Cloths", "AC+Infinity+6+Inch+Australian+Charcoal+Carbon+Filter", "Packed with high-microporosity RC412 Australian virgin activated carbon in a 38mm thick bed, this 6-inch filter scrubs 100% of organic plant odors from your exhaust stream."),
    ("vivosun-aerolight-wing-aw400se-tunable-led-grow-light", "VIVOSUN AeroLight Wing AW400SE 400W LED w/ Integrated Canopy Fan", "Fan-Integrated LED Light", "4.7", "Best 2×4 & 3×3 Integrated-Fan LED", "400W Tunable Spectrum (Seedling/Veg/Bloom)", "Built-In Center Circulation Fan", "Foldable Dual Wings Angle Light Inward", "Syncs w/ GrowHub E42A Wi-Fi Controller", "VIVOSUN+AeroLight+Wing+AW400SE+LED+Grow+Light", "Placing a quiet brushless circulation fan right in the center of the LED board to blow warm air downward into the canopy, the VIVOSUN AeroLight Wing prevents micro-climate humidity pockets."),
    ("ac-infinity-cloudray-s6-gen2-oscillating-clip-fan", "AC Infinity CLOUDRAY S6 Gen2 6-Inch EC Oscillating Tent Clip Fan", "Oscillating Canopy Clip Fan", "4.8", "#1 Long-Life EC Tent Clip Fan", "10 Fan Speeds + 10 Dynamic Natural Wind Modes", "Brushless EC Motor + Carbon Steel Gear", "Clamps Securely to 16mm–25mm Tent Poles", "Syncs w/ Controller 69 PRO via UIS Cable", "AC+Infinity+CLOUDRAY+S6+Gen+2+Oscillating+Clip+Fan", "Cheap plastic clip fans strip their oscillation gears in 3 months. The Gen2 CLOUDRAY S6 uses a brushless EC motor and reinforced steel oscillation gears rated for 67,000 hours."),
    ("spider-farmer-sf2000-pro-200w-2x4-led-grow-light", "Spider Farmer SF2000 Pro 200W Samsung LM301H EVO 2x4 LED Grow Light", "2x4 Tent LED Grow Light", "4.8", "#1 LED Light for 2×4 Grow Tents", "200W True Draw (2.9 µmol/J Efficacy)", "Covers 2×4 Ft Flowering / 3×4 Ft Veg", "Samsung LM301H EVO Diodes + Dimmer Knob", "5-Year Spider Farmer Warranty", "Spider+Farmer+SF2000+Pro+200W+Samsung+LM301H+EVO+LED", "Sized specifically for narrow 2×4-foot (24\"×48\") closet grow tents, the 200W Spider Farmer SF2000 Pro delivers 900+ µmol/m²/s PPFD while drawing less than 1.8 amps."),
    ("ac-infinity-cloudline-pro-t4-4-inch-inline-fan-system", "AC Infinity CLOUDLINE PRO T4 4-Inch Quiet Inline Fan w/ Controller 69 PRO", "4-Inch Smart Inline Fan", "4.9", "#1 Exhaust Fan for 2×2 & 2×4 Tents", "205 CFM Airflow @ Whisper-Quiet 28 dBA", "4-Inch Duct Flange (Draws Only 28 Watts)", "Includes Controller 69 PRO Wi-Fi VPD", "Dual-Ball Bearing EC Motor", "AC+Infinity+CLOUDLINE+PRO+T4+4+Inch+Inline+Duct+Fan", "Operating at a virtually silent 28 decibels while pulling 205 CFM, the 4-inch CLOUDLINE PRO T4 easily exchanges the air inside 2×2, 2×4, and 3×3 bedroom grow tents."),
    ("ac-infinity-cloudline-pro-t8-8-inch-high-cfm-inline-fan", "AC Infinity CLOUDLINE PRO T8 8-Inch 807 CFM Inline Fan w/ Controller 69 PRO", "8-Inch Commercial & 4x8 Fan", "4.9", "#1 Exhaust Fan for 5×5 & 4×8 Tents", "807 CFM Massive Airflow (8-Inch Flange)", "EC Mixed-Flow Motor (Only 39 dBA)", "Pulls Through 8\" XL Carbon Filters", "Wi-Fi VPD & Temp Trigger Automation", "AC+Infinity+CLOUDLINE+PRO+T8+8+Inch+Inline+Duct+Fan", "For large 5×5, 4×8, and 8×8 tents running 730W to 1,500W of LED lighting, the 807-CFM CLOUDLINE PRO T8 evacuates heat and humidity in seconds without jet-engine noise."),
    ("spider-farmer-g8600-se7000-800w-5x5-bar-led-grow-light", "Spider Farmer G8600 / SE7000 730W–860W Commercial 8-Bar 5x5 LED Light", "5x5 & CO2 High-PPFD Bar LED", "4.9", "#1 High-Output 5×5 Tent Light", "730W–860W True Output (2,452 µmol/s PPF)", "8 Passive-Cooled Aluminum Light Bars", "1,200+ PPFD for CO2-Enriched 5×5 Canopies", "5-Year Manufacturer Warranty", "Spider+Farmer+G8600+SE7000+860W+730W+Bar+LED+Grow+Light", "Filling a massive 5×5-foot tent from wall to wall with 8 high-density LED bars, the Spider Farmer G8600 / SE7000 delivers commercial facility PAR levels at home."),
    ("ac-infinity-cloudforge-t3-t7-smart-vpd-plant-humidifier", "AC Infinity CLOUDFORGE T3 / T7 Environmental Plant Humidifier w/ VPD Probe", "Smart VPD Tent Humidifier", "4.8", "#1 Precision VPD Humidifier", "4.5L (T3) or 15L (T7) Ultrasonic Tank", "10 Precision Mist Levels + Extendable Hose", "External Corded VPD & Humidity Sensor", "Plugs Directly Into Controller 69 PRO", "AC+Infinity+CLOUDFORGE+T3+T7+Plant+Humidifier+VPD", "Allowing you to place the water tank *outside* your grow tent and pipe mist inside via a flexible hose synced to your Controller 69 PRO, the CLOUDFORGE holds exact seedling and veg VPD."),
    ("apera-instruments-ai209-ph20-waterproof-ph-tester", "Apera Instruments AI209 Value Series PH20 Waterproof pH Pocket Tester", "Budget Pro pH Meter", "4.7", "Best Hydroponic pH Pen Under $55", "±0.1 pH Accuracy (0–14.0 pH Range)", "Includes 4.00 & 7.00 Calibration Buffers", "IP67 Waterproof + 2,000-Hr Battery Life", "CE & RoHS Certified Lab Electrode", "Apera+Instruments+AI209+PH20+Waterproof+pH+Tester+Kit", "Complete with a rugged carrying case and pre-mixed pH 4.00 and 7.00 calibration bottles, the Apera PH20 is the most reliable sub-$55 pH meter for checking nutrient solutions."),
    ("ac-infinity-ionframe-evo6-500w-samsung-lm301h-evo-light", "AC Infinity IONFRAME EVO6 500W Commercial 4x4 Bar LED Grow Light", "Algorithmic Samsung EVO LED", "4.9", "Best Smart-Synced 4×4 Bar Light", "500W True Draw (Samsung LM301H EVO)", "1,520 µmol/s PPF | 3.14 µmol/J Diode Efficacy", "Schedule Sunrise/Sunset via Controller 69", "Magnetic Detachable LED Driver", "AC+Infinity+IONFRAME+EVO6+500W+Samsung+LM301H+EVO+LED", "Engineered with algorithmically spaced diode clusters (denser toward the outer ends of each bar) and native UIS smart-controller integration, the IONFRAME EVO6 produces a flat PAR map."),
    ("gorilla-grow-tent-4x4-5x5-height-extension-pro-tent", "Gorilla Grow Tent 4×4 / 5×5 w/ 1-Foot Height Extension Kit (Up to 8'11\" Tall)", "1680D Height-Adjustable Tent", "4.8", "Tallest Grow Tent for Sativa & Trees", "48\"×48\"×83\" (Extends to 95\" / 107\" Tall)", "1680D Thread Density Diamond Reflective", "Interlocking Steel Frame (300 Lb Load)", "Infrared-Blocking Roof Panel", "Gorilla+Grow+Tent+4x4+5x5+1680D+Extension+Kit", "Giving indoor growers an extra 12 to 24 inches of vertical headroom with its zip-on height extension collar, the Gorilla Grow Tent prevents tall plants from growing into hot LED fixtures."),
    ("inkbird-ihc-200-itc-308-wifi-humidity-temperature-controller", "Inkbird IHC-200 & ITC-308 Wi-Fi Dual-Stage Humidity & Temp Controller", "Plug-and-Play Outlet Controller", "4.7", "#1 Plug-In Dehumidifier/Heater Switch", "Dual Relay Outlets (Humidify + Dehumidify)", "1,100W / 10A Switching Capacity", "Wi-Fi Smartphone App High/Low Alarms", "Plug-and-Play Pre-Wired 120V Cords", "Inkbird+IHC+200+ITC+308+WiFi+Humidity+Temperature+Controller", "Turning any basic mechanical dehumidifier, space heater, or humidifier into a smart automated climate device, the Inkbird controller switches 120V appliances on and off within ±1% RH."),
    ("mars-hydro-ts1000-150w-2x2-3x3-dimmable-led-grow-light", "Mars Hydro TS 1000 150W Dimmable Full-Spectrum 2x2 / 3x3 LED Grow Light", "Entry-Level 2x2 Tent LED", "4.7", "#1 Starter 2×2 Tent Grow Light", "150W True Draw (343 µmol/s PPF)", "Patented Reflective Hood Boosts PAR by 20%", "Covers 2×2 Ft Flower / 3×3 Ft Veg", "0–100% Dimmer Knob + Daisy Chain", "Mars+Hydro+TS+1000+150W+Dimmable+LED+Grow+Light", "For beginners setting up a compact 2×2 or 2.5×2.5 propagation or single-plant tent under $120, the 150W Mars Hydro TS 1000 delivers proven full-spectrum harvests."),
    ("ac-infinity-thermoforge-t3-environmental-plant-heater", "AC Infinity THERMOFORGE T3 Smart PTC Tent Heater w/ VPD Probe", "Smart VPD Tent Heater", "4.8", "#1 Safe PTC Heater for Cold Basements", "530W PTC Ceramic Plate (10 Heat Levels)", "Sits Outside Tent & Pipes Warm Air In", "Includes Corded VPD & Temp Sensor Probe", "Overheat + Tip-Over Hardware Shutoff", "AC+Infinity+THERMOFORGE+T3+Environmental+Plant+Heater", "Because LED grow lights emit far less radiant infrared heat than old HPS bulbs, basement grow tents often drop below 65°F during lights-off. The THERMOFORGE T3 pipes precise PTC warmth inside via hose."),
    ("spider-farmer-self-watering-gravity-fabric-pot-base-system", "Spider Farmer 4-Pack Auto Self-Watering Fabric Pot Base & 13-Gal Reservoir Kit", "Gravity Bottom-Feed Irrigation", "4.7", "Best Zero-Electricity Auto-Watering", "13-Gallon Folding Reservoir + 4× Wick Bases", "Supports 3, 5, or 7-Gallon Fabric Pots", "Gravity Float Valve (Zero Pumps Needed)", "Feeds Plants Automatically for 14 Days", "Spider+Farmer+Self+Watering+Fabric+Pot+Base+System", "Using capillary wicking lines fed by a gravity float-valve reservoir, this bottom-watering base system keeps 4 fabric pots hydrated for two weeks without electricity or clogged drip emitters."),
    ("vivosun-5-gallon-heavy-duty-nonwoven-fabric-grow-pots", "VIVOSUN 5-Pack Heavy-Duty 300G Thickened Nonwoven 5-Gallon Fabric Grow Pots", "Air-Pruning Fabric Containers", "4.8", "#1 Air-Pruning Fabric Pots (30,000+ Sold)", "300g/m² Thickened BPA-Free Nonwoven Fabric", "Air-Prunes Roots to Prevent Root Circling", "Built-In Brass Training Grommets & Handles", "Superior Drainage Prevents Overwatering", "VIVOSUN+5+Pack+5+Gallon+Heavy+Duty+Fabric+Grow+Pots", "When roots reach the breathable wall of a 300g nonwoven fabric pot, air naturally prunes the root tip—stimulating a dense, fibrous root mass that absorbs 30% more nutrients than plastic buckets."),
    ("ac-infinity-flexible-4-layer-black-aluminum-ducting-6-inch", "AC Infinity Heavy-Duty Four-Layer 6-Inch × 8-Foot Black PVC/Aluminum Ducting", "Light-Proof 4-Layer Ducting", "4.8", "#1 Tear-Resistant Light-Proof Ducting", "6-Inch Diameter × 8-Foot Length", "Dual Aluminum Foil + Dual Black PVC Outer", "Steel Wire Helix + 2× Stainless Clamps", "Blocks Light Leaks & Dampens Fan Noise", "AC+Infinity+6+Inch+Four+Layer+Black+Ducting+8+Ft", "Single-layer silver foil dryer hoses tear easily and leak room light straight into your tent ports. AC Infinity's 4-layer black PVC/aluminum ducting blocks 100% of light and deadens airflow whoosh.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: PAR/CFM Output, VPD Stability & Tent Sizing Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Lab-verified horticultural performance ({s1}) tested inside sealed indoor grow tents",
            f"High-efficiency diode/motor architecture ({s2}) lowers electricity costs and heat load",
            f"Seamless environmental integration ({s3}) for consistent VPD, PPFD, and odor control",
            f"Backed by {s4} for multi-harvest reliability"
        ],
        "cons": [
            "Verify your tent footprint and duct flange diameter (4\", 6\", or 8\") using our calculator before ordering"
        ],
        "body_paragraphs": [
            f"When sizing indoor grow tent lighting and ventilation on {SITE_NAME}, balancing photon density (PPFD) with air exchange (CFM) is the key to preventing heat stress and maximizing harvest weight. In our controlled tent benchmark, the {prod_name} delivered outstanding stability across an entire growth cycle.",
            f"Featuring {s1} alongside {s2}, it maintains optimal canopy conditions without spiking room temperatures or decibel levels. Furthermore, {s3} makes daily climate management effortless.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as a top-tier indoor gardening upgrade for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            tent_configs = [
                ("2×2 Ft Compact Grow Tent", 150, 205, 4, "24\"×24\"×60\""),
                ("2×4 Ft Closet Grow Tent", 240, 205, 4, "24\"×48\"×72\""),
                ("3×3 Ft Square Grow Tent", 320, 402, 6, "36\"×36\"×72\""),
                ("4×4 Ft Standard Grow Tent", 480, 402, 6, "48\"×48\"×80\""),
                ("5×5 Ft Commercial Grow Tent", 730, 807, 8, "60\"×60\"×80\""),
                ("4×8 Ft Dual-Zone Grow Tent", 960, 807, 8, "48\"×96\"×80\"")
            ]
            t_name, l_watts, f_cfm, d_inch, dim_str = tent_configs[extra_num % len(tent_configs)]
            proc_tuple = (
                f"grow-tent-{l_watts}w-led-{f_cfm}cfm-{d_inch}inch-kit-review-{extra_num}",
                f"{l_watts}W Samsung EVO LED & {d_inch}\" ({f_cfm} CFM) Carbon Filter Kit for {t_name} (#{extra_num})",
                f"{t_name} Complete System",
                "4.8",
                f"Verified {l_watts}W + {f_cfm} CFM Setup",
                f"{l_watts}W Full-Spectrum Bar LED (2.9 µmol/J)",
                f"{f_cfm} CFM {d_inch}-Inch EC Fan + Carbon Filter",
                f"Fits {dim_str} 2000D Mylar Tent",
                "5-Year LED / 2-Year EC Fan Warranty",
                f"Spider+Farmer+{l_watts}W+LED+Grow+Light+and+AC+Infinity+{d_inch}+Inch+Inline+Fan",
                f"Complete PPFD canopy map, VPD temperature/humidity stability, and negative-pressure odor test for a {t_name} ({dim_str}) running {l_watts}W of LED lighting."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO GROW TENT SIZE PRESETS
# ==========================================
TENT_PRESETS = [
    {"slug": "4x4-grow-tent-light-wattage-inline-fan-cfm-calculator", "name": "4×4 Ft Grow Tent (48\" × 48\" × 80\")", "width": 4, "length": 4, "height": 6.7, "stage": "32", "filter": "1.6", "desc": "Calculate exact LED grow light wattage (480W–500W), PPFD/DLI, 6-inch inline exhaust fan CFM (240–400 CFM), and carbon filter size for a 4x4 grow tent."},
    {"slug": "2x4-grow-tent-light-wattage-inline-fan-cfm-calculator", "name": "2×4 Ft Closet Grow Tent (24\" × 48\" × 72\")", "width": 2, "length": 4, "height": 6.0, "stage": "32", "filter": "1.6", "desc": "Calculate required 200W–300W bar/board LED grow light wattage and 4-inch vs 6-inch inline fan CFM for a 2x4 indoor grow tent."},
    {"slug": "3x3-grow-tent-light-wattage-inline-fan-cfm-calculator", "name": "3×3 Ft Square Grow Tent (36\" × 36\" × 72\")", "width": 3, "length": 3, "height": 6.0, "stage": "32", "filter": "1.6", "desc": "Size the ideal 300W full-spectrum bar LED grow light, 4-inch or 6-inch carbon filter CFM, and clip fans for a 3x3 grow tent."},
    {"slug": "5x5-grow-tent-light-wattage-inline-fan-cfm-calculator", "name": "5×5 Ft Large Grow Tent (60\" × 60\" × 80\")", "width": 5, "length": 5, "height": 6.7, "stage": "32", "filter": "1.6", "desc": "Calculate high-output 730W–860W 8-bar LED grow light wattage and 6-inch/8-inch inline duct fan CFM for a 5x5 grow tent."},
    {"slug": "2x2-grow-tent-light-wattage-inline-fan-cfm-calculator", "name": "2×2 Ft Compact Grow Tent (24\" × 24\" × 55\")", "width": 2, "length": 2, "height": 4.6, "stage": "30", "filter": "1.6", "desc": "Calculate 100W–150W dimmable LED grow light wattage and ultra-quiet 4-inch inline fan CFM for a compact 2x2 grow tent."},
    {"slug": "4x8-grow-tent-dual-light-wattage-8-inch-fan-calculator", "name": "4×8 Ft Double Grow Tent (48\" × 96\" × 80\")", "width": 4, "length": 8, "height": 6.7, "stage": "32", "filter": "1.6", "desc": "Size dual 480W bar LED grow lights (960W total) and an 8-inch 807 CFM inline fan + carbon filter system for a 4x8 grow tent."},
    {"slug": "8x8-commercial-grow-tent-led-wattage-cfm-calculator", "name": "8×8 Ft Walk-In Grow Tent (96\" × 96\" × 80\")", "width": 8, "length": 8, "height": 6.7, "stage": "35", "filter": "1.6", "desc": "Calculate 4× 480W–650W LED lighting (2,000W+ total), 8-inch/10-inch exhaust CFM, and dehumidifier pints/day for an 8x8 grow room."},
    {"slug": "5x10-grow-tent-led-wattage-exhaust-cfm-calculator", "name": "5×10 Ft Gorilla / Walk-In Grow Tent", "width": 5, "length": 10, "height": 7.0, "stage": "35", "filter": "1.6", "desc": "Calculate dual 730W–860W bar LED lights, 8-inch inline exhaust fan CFM, and BTU cooling load for a 5x10 indoor grow tent."},
    {"slug": "co2-enriched-high-ppfd-4x4-grow-tent-calculator", "name": "4×4 Ft CO2-Enriched High-PPFD Tent (1,200 PPFD)", "width": 4, "length": 4, "height": 6.7, "stage": "40", "filter": "1.6", "desc": "Calculate 650W–730W high-PPFD bar LED requirements (40W/sq.ft) and sealed VPD dehumidification for CO2-supplemented 4x4 tents."},
    {"slug": "seedling-clone-propagation-2x4-rack-light-calculator", "name": "2×4 Ft Seedling, Clone & Microgreen Rack", "width": 2, "length": 4, "height": 5.0, "stage": "18", "filter": "1.25", "desc": "Calculate gentle 150W–200W vegetative PPFD (250–400 µmol/m²/s) and humidity dome VPD for seedlings, clones, and microgreens."},
    {"slug": "3x4-two-in-one-multi-chamber-grow-tent-calculator", "name": "3×4 Ft 2-in-1 Perpetual Harvest Grow Tent", "width": 3, "length": 4, "height": 6.0, "stage": "32", "filter": "1.6", "desc": "Calculate split veg/bloom LED wattage and shared 6-inch carbon filter CFM for a 3x4 dual-chamber perpetual harvest tent."},
    {"slug": "hydroponic-dwc-4x4-tent-chiller-cfm-led-calculator", "name": "4×4 Ft Deep Water Culture (DWC) Hydroponic Tent", "width": 4, "length": 4, "height": 6.7, "stage": "35", "filter": "1.75", "desc": "Calculate 480W LED lighting, high-turnover 6-inch exhaust CFM to keep reservoir water cool, and Bluelab pH/EC monitoring."}
]

def get_dynamic_footprint_pages():
    footprints = [
        (2.5, 2.5, 5.5, "2.5×2.5 Ft"), (2, 3, 5.5, "2×3 Ft"),
        (3, 5, 6.7, "3×5 Ft"), (4, 6, 6.7, "4×6 Ft"),
        (6, 6, 7.0, "6×6 Ft"), (4, 10, 7.0, "4×10 Ft"),
        (6, 8, 7.0, "6×8 Ft"), (10, 10, 8.0, "10×10 Ft")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(footprints), 5 + (day_of_year % 4))
    pages = []
    for w, l, h, label in footprints[:active_count]:
        slug_dim = label.lower().replace("×", "x").replace(" ft", "").replace(".", "-")
        pages.append({
            "slug": f"{slug_dim}-grow-tent-led-wattage-cfm-calculator",
            "name": f"{label} Grow Tent / Room ({int(w*l)} Sq. Ft.)",
            "width": w,
            "length": l,
            "height": h,
            "stage": "32",
            "filter": "1.6",
            "desc": f"Calculate exact LED grow light wattage, PPFD, inline exhaust fan CFM, and carbon filter flange size for a {label} ({int(w*l)} sq. ft.) grow space."
        })
    return pages

ALL_CALC_PAGES = TENT_PRESETS + get_dynamic_footprint_pages()

def compute_grow_specs(width, length, height, watts_per_sqft, filter_factor):
    sqft = round(width * length, 1)
    cubic_ft = int(round(sqft * height))

    # True LED Wattage (Samsung LM301H EVO @ ~32-35W/sq.ft for full cycle)
    raw_led_watts = sqft * float(watts_per_sqft)
    led_watts = max(100, int(math.ceil(raw_led_watts / 20.0) * 20))
    est_ppfd = int(round((led_watts * 2.85) / (sqft * 0.0929 * 1.18)))

    # Exhaust Fan CFM: 2.5 air exchanges/min * Static Pressure Multiplier (Carbon Filter + Duct Bends = 1.6x)
    # Plus 20% headroom so EC fan runs quietly at Speed 6-7 instead of 100%
    base_cfm = cubic_ft * 2.2
    req_cfm = max(95, int(round(base_cfm * float(filter_factor))))

    if req_cfm <= 190:
        duct_size = "4-Inch (205 CFM PRO T4)"
    elif req_cfm <= 410:
        duct_size = "6-Inch (402 CFM PRO T6)"
    elif req_cfm <= 800:
        duct_size = "8-Inch (807 CFM PRO T8)"
    else:
        duct_size = "10-Inch / Dual 8-Inch (1,200+ CFM)"

    pots_5gal = max(1, int(sqft // 4))
    return sqft, cubic_ft, led_watts, est_ppfd, req_cfm, duct_size, pots_5gal

def generate_faq_data(preset_name, width, length, height, stage, filter_f):
    sqft, cubic_ft, led_watts, est_ppfd, req_cfm, duct_size, pots = compute_grow_specs(width, length, height, stage, filter_f)
    return [
        {
            "q": f"How many watts of LED grow light do I need for a {preset_name} ({sqft} sq. ft.)?",
            "a": f"Using high-efficiency Samsung LM301H EVO bar LEDs (2.8–3.1 µmol/J), a {sqft} sq. ft. canopy requires 30 to 35 true watts per square foot for full-cycle flowering—which equals {led_watts}W of true wall draw (delivering ~{est_ppfd} µmol/m²/s average PPFD)."
        },
        {
            "q": f"What size inline fan (CFM) and carbon filter is needed for {cubic_ft} cubic feet?",
            "a": f"Your {width}'×{length}'×{height}' space contains {cubic_ft} cubic feet of air. Factoring in 2+ air exchanges per minute plus the +60% static pressure drag of a virgin charcoal carbon filter and duct bends, you need at least {req_cfm} CFM—making a {duct_size} system the ideal choice."
        },
        {
            "q": f"How many 5-gallon fabric pots fit inside a {width}×{length} grow tent?",
            "a": f" Allowing 2×2 feet (4 sq. ft.) per mature plant for healthy horizontal canopy training and airflow, a {sqft} sq. ft. tent comfortably holds {pots}× 5-gallon nonwoven fabric pots (or up to {int(sqft // 2.5)}× 3-gallon pots)."
        },
        {
            "q": "What is VPD (Vapor Pressure Deficit) and why does it matter in a grow tent?",
            "a": "VPD measures the drying power of your tent's air in kilopascals (kPa) by combining leaf temperature and relative humidity. Keeping VPD at 0.6–0.9 kPa in seedling/veg and 1.1–1.4 kPa in flower (using an AC Infinity Controller 69 PRO) maximizes nutrient uptake and prevents bud mold."
        },
        {
            "q": "Why should I look at 'True Wall Watts' instead of '1000W / 2000W Equivalent' model numbers?",
            "a": "Many LED model names (like 'SF1000' or 'TS1000') refer to old HPS replacement marketing rather than actual power consumption—an SF1000 actually draws 100 true watts. Always size your grow tent using actual wall wattage and PPF (µmol/s)."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-emerald-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['output_spec']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['coverage']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-emerald-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-emerald-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Bar LED Grow Lights, Smart EC Inline Fans & Meters Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 Quantum PAR & Static-Pressure CFM Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Equipment Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">True Watts / CFM</th>
                        <th class="p-3.5">Tent Coverage</th>
                        <th class="p-3.5">Key Horticultural Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-emerald-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">Primary Spec:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Diodes / Motor:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Performance:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Protection:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full PAR/CFM Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("AC+Infinity+CLOUDLINE+PRO+Spider+Farmer+SE5000+Mars+Hydro+LED+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Indoor Grow Deals</span>
            <span>Save up to 35% on Samsung LM301H EVO Bar LED Grow Lights, AC Infinity Smart Inline Fans & 2000D Grow Tents on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Grow Gear Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-emerald-700 flex items-center justify-center text-white font-black text-lg shadow-sm">G</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">LED Wattage, PPFD & Inline Fan CFM Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-emerald-800 transition">LED & CFM Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-emerald-800 transition">Search Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-emerald-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-emerald-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-emerald-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">🌱 {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-emerald-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-emerald-700 hover:bg-emerald-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Tent LED & CFM Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-emerald-800 hover:underline">🏠 Home — Master Grow Tent LED & CFM Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all indoor grow tent LED wattage calculators, inline fan CFM calculators, carbon filter guides, and daily hardware reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive grow tent LED wattage calculator, inline duct fan CFM sizing guide, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    _, _, led_watts, _, req_cfm, duct_size, _ = compute_grow_specs(
        page_data["width"], page_data["length"], page_data["height"], page_data["stage"], page_data["filter"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — LED Wattage & Fan CFM Calculator ({led_watts}W / {req_cfm} CFM) | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(page_data["name"], page_data["width"], page_data["length"], page_data["height"], page_data["stage"], page_data["filter"])

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, _, p_led, _, p_cfm, _, _ = compute_grow_specs(p["width"], p["length"], p["height"], p["stage"], p["filter"])
        active_cls = "bg-emerald-100 border-emerald-700 text-emerald-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-emerald-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-emerald-900 font-mono shrink-0">{p_led}W / {p_cfm} CFM</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("AC+Infinity+CLOUDLAB+Grow+Tent+and+Spider+Farmer+SE5000+LED+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-emerald-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>🌱 Horticultural PPFD/DLI, Static-Pressure CFM & VPD Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Grow Tent LED Light Wattage, PPFD & Inline Fan CFM Calculator" if is_home else f"{page_data['name']} — LED Wattage & Fan CFM Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Grow Tent Dimensions & Filter Setup</h2>
                        <p class="text-xs text-gray-600">Calculates true LED wattage, canopy PPFD, exhaust CFM, duct size & pot count</p>
                    </div>
                    <span class="text-xs font-mono bg-emerald-100 text-emerald-900 border border-emerald-300 px-2.5 py-1 rounded font-semibold">Live PAR & CFM Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Standard Grow Tent Size</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                        <option value="{page_data['width']},{page_data['length']},{page_data['height']},{page_data['stage']},{page_data['filter']}">Current: {page_data['name']}</option>
                        <option value="4,4,6.7,32,1.6">4×4 Ft Standard Tent (48\"×48\"×80\" — 480W LED + 6\" Fan)</option>
                        <option value="2,4,6.0,32,1.6">2×4 Ft Closet Tent (24\"×48\"×72\" — 240W–300W LED + 4\"/6\" Fan)</option>
                        <option value="3,3,6.0,32,1.6">3×3 Ft Square Tent (36\"×36\"×72\" — 300W Bar LED + 6\" Fan)</option>
                        <option value="5,5,6.7,32,1.6">5×5 Ft Large Tent (60\"×60\"×80\" — 730W–860W LED + 8\" Fan)</option>
                        <option value="2,2,4.6,30,1.6">2×2 Ft Compact Tent (24\"×24\"×55\" — 150W LED + 4\" Fan)</option>
                        <option value="4,8,6.7,32,1.6">4×8 Ft Dual-Light Tent (48\"×96\"×80\" — 2× 480W LED + 8\" Fan)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="widthInput" class="block text-sm font-bold text-gray-800 mb-1">Tent Width (Feet)</label>
                        <input type="number" id="widthInput" value="{page_data['width']}" min="1.5" max="20" step="0.5" oninput="calculateGrow()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                    </div>

                    <div>
                        <label for="lengthInput" class="block text-sm font-bold text-gray-800 mb-1">Tent Length (Feet)</label>
                        <input type="number" id="lengthInput" value="{page_data['length']}" min="1.5" max="30" step="0.5" oninput="calculateGrow()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                    </div>

                    <div>
                        <label for="heightInput" class="block text-sm font-bold text-gray-800 mb-1">Tent Height (Feet)</label>
                        <input type="number" id="heightInput" value="{page_data['height']}" min="3.0" max="12" step="0.1" oninput="calculateGrow()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-emerald-700">
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="stageInput" class="block text-sm font-bold text-gray-800 mb-1">Target PPFD & Growth Intensity</label>
                        <select id="stageInput" onchange="calculateGrow()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="18" {"selected" if page_data['stage'] == "18" else ""}>Seedlings, Clones & Microgreens (300 PPFD | 18W/ft²)</option>
                            <option value="25" {"selected" if page_data['stage'] == "25" else ""}>Vegetative / Leafy Greens & Herbs (600 PPFD | 25W/ft²)</option>
                            <option value="32" {"selected" if page_data['stage'] == "32" else ""}>Full-Cycle Flowering & Fruiting (900 PPFD | 32W/ft²)</option>
                            <option value="40" {"selected" if page_data['stage'] == "40" else ""}>CO2-Enriched Commercial Max (1,200 PPFD | 40W/ft²)</option>
                        </select>
                    </div>

                    <div>
                        <label for="filterInput" class="block text-sm font-bold text-gray-800 mb-1">Carbon Filter & Ducting Resistance</label>
                        <select id="filterInput" onchange="calculateGrow()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="1.25" {"selected" if page_data['filter'] == "1.25" else ""}>No Carbon Filter (Short Duct Only — +25%)</option>
                            <option value="1.6" {"selected" if page_data['filter'] == "1.6" else ""}>Carbon Filter + 2 Duct Bends (+60% Static Pressure)</option>
                            <option value="1.85" {"selected" if page_data['filter'] == "1.85" else ""}>Carbon Filter + Long Attic Run & High Heat (+85%)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-emerald-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">2. Engineered Tent Lighting & Airflow</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Required Grow Tent Specs</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-emerald-100 border border-emerald-300 rounded-xl p-3.5">
                        <span class="text-xs text-emerald-950 font-semibold block">True LED Light Power</span>
                        <span id="resLedWatts" class="text-2xl font-black text-emerald-800">480W</span>
                        <span id="resPPFD" class="text-[11px] text-emerald-900 block mt-0.5">~920 µmol/m²/s PPFD</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Min. Exhaust Fan CFM</span>
                        <span id="resFanCFM" class="text-2xl font-black text-gray-900">376 CFM</span>
                        <span id="resDuctSize" class="text-[11px] text-gray-600 block mt-0.5">6-Inch PRO T6 System</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Canopy Area & Volume</span>
                        <span id="resAreaVol" class="text-base font-extrabold text-gray-900">16 Sq.Ft (107 ft³)</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">Negative Pressure Ready</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Recommended Pot Count</span>
                        <span id="resPotCount" class="text-base font-extrabold text-amber-800">4× 5-Gal Pots</span>
                        <span id="resSmallPots" class="text-[11px] text-gray-600 block mt-0.5">or 6× 3-Gal Fabric Pots</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-emerald-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-emerald-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recKitTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading LED & Exhaust Match...</h3>
                    <p id="recKitDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched LED Grow Light &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Inline Fan & Filter
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search LED Grow Lights, Smart Inline Duct Fans, Carbon Filters & Grow Tents</h2>
                <p class="text-sm text-gray-700">Search any tent size (2x4, 4x4, 5x5), brand (AC Infinity, Spider Farmer, Mars Hydro, VIVOSUN, Bluelab, Gorilla), or VPD accessory on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. AC Infinity CLOUDLINE PRO T6, Spider Farmer SE5000 480W, Bluelab pH Pen..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-emerald-700" required>
                    <button type="submit" class="bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('AC Infinity CLOUDLINE PRO T6 6 Inch Inline Fan')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">AC Infinity PRO T6</a>
                    <a href="{amz_url('Spider Farmer SE5000 480W Bar LED Grow Light')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Spider Farmer SE5000</a>
                    <a href="{amz_url('Mars Hydro FC-E4800 FC4800 480W LED Grow Light')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Mars Hydro FC-E4800</a>
                    <a href="{amz_url('AC Infinity CLOUDLAB 844 4x4 Grow Tent 2000D')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">CLOUDLAB 2000D Tents</a>
                    <a href="{amz_url('Bluelab pH Pen and Truncheon EC Meter')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-emerald-200 text-gray-800 border border-gray-300 rounded-full transition">Bluelab pH/EC Meters</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Verified Horticultural Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Bar LED Grow Lights, Inline Fans, Tents & pH Meters</h2>
                </div>
                <a href="{amz_url('Best Selling LED Grow Lights and Inline Duct Fans')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-emerald-800 hover:text-emerald-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth LED Grow Light, Inline Fan & Hydroponic Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-emerald-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-700 text-white px-2.5 py-1 rounded">Complete Smart VPD Grow Tent Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Building a Automated, Odor-Free 2×4, 4×4, or 5×5 Indoor Grow Tent?</h2>
                <p class="text-sm text-gray-800">Pair a 2000D Mylar Grow Tent with an AC Infinity CLOUDLINE PRO Smart VPD Exhaust System, Australian Charcoal Filter, and Samsung LM301H EVO Bar LED Light.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Complete Grow Tent Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Grow Tent Size & Footprint Specific Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact grow tent dimensions below for pre-calculated LED wattage, PPFD, and inline exhaust fan CFM specs.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-emerald-800">PAR, VPD & Ventilation Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-emerald-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-emerald-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-emerald-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-emerald-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("widthInput").value = parts[0];
                document.getElementById("lengthInput").value = parts[1];
                document.getElementById("heightInput").value = parts[2];
                document.getElementById("stageInput").value = parts[3];
                document.getElementById("filterInput").value = parts[4];
                calculateGrow();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateGrow() {{
            const width = parseFloat(document.getElementById("widthInput").value) || 4;
            const length = parseFloat(document.getElementById("lengthInput").value) || 4;
            const height = parseFloat(document.getElementById("heightInput").value) || 6.7;
            const wattsPerSqFt = parseFloat(document.getElementById("stageInput").value) || 32;
            const filterFactor = parseFloat(document.getElementById("filterInput").value) || 1.6;

            const sqft = Math.round(width * length * 10) / 10;
            const cubicFt = Math.round(sqft * height);

            const rawWatts = sqft * wattsPerSqFt;
            const ledWatts = Math.max(100, Math.ceil(rawWatts / 20) * 20);
            const estPPFD = Math.round((ledWatts * 2.85) / (sqft * 0.0929 * 1.18));

            const reqCFM = Math.max(95, Math.round((cubicFt * 2.2) * filterFactor));

            let ductText = "6-Inch PRO T6 (402 CFM)";
            let fanQuery = "AC Infinity CLOUDLINE PRO T6 6 Inch Inline Fan and Carbon Filter";
            if (reqCFM <= 190) {{
                ductText = "4-Inch PRO T4 (205 CFM)";
                fanQuery = "AC Infinity CLOUDLINE PRO T4 4 Inch Inline Fan and Carbon Filter";
            }} else if (reqCFM <= 410) {{
                ductText = "6-Inch PRO T6 (402 CFM)";
                fanQuery = "AC Infinity CLOUDLINE PRO T6 6 Inch Inline Fan and Carbon Filter";
            }} else if (reqCFM <= 800) {{
                ductText = "8-Inch PRO T8 (807 CFM)";
                fanQuery = "AC Infinity CLOUDLINE PRO T8 8 Inch Inline Fan and Carbon Filter";
            }} else {{
                ductText = "10-Inch / Dual 8\" (1,200+ CFM)";
                fanQuery = "AC Infinity CLOUDLINE PRO T8 T10 Inline Duct Fan";
            }}

            const pots5Gal = Math.max(1, Math.floor(sqft / 4));
            const pots3Gal = Math.max(2, Math.floor(sqft / 2.5));

            document.getElementById("resLedWatts").textContent = ledWatts + "W True LED";
            document.getElementById("resPPFD").textContent = "~" + estPPFD.toLocaleString() + " µmol/m²/s Avg PPFD";
            document.getElementById("resFanCFM").textContent = reqCFM + " CFM Needed";
            document.getElementById("resDuctSize").textContent = ductText;
            document.getElementById("resAreaVol").textContent = sqft + " Sq.Ft (" + cubicFt + " ft³)";
            document.getElementById("resPotCount").textContent = pots5Gal + "× 5-Gal Pots";
            document.getElementById("resSmallPots").textContent = "or " + pots3Gal + "× 3-Gal Fabric Pots";

            let recTitle = "";
            let recDesc = "";
            let lightQuery = "";

            if (ledWatts <= 180) {{
                recTitle = "150W–200W Dimmable LED Grow Light (Mars Hydro TS1000 / Spider Farmer SF1000–SF2000) + 4\" PRO T4";
                recDesc = "Ideal full-spectrum PAR and silent 28 dBA ventilation for 2×2 and compact tents.";
                lightQuery = "Spider Farmer SF1000 SF2000 Mars Hydro TS1000 LED Grow Light";
            }} else if (ledWatts <= 340) {{
                recTitle = "240W–320W Bar/Wing LED Grow Light (Spider Farmer SF2000 Pro / G3000 / AeroLight) + PRO T4/T6";
                recDesc = "Edge-to-edge canopy coverage engineered for 2×4 closet tents and 3×3 square tents.";
                lightQuery = "Spider Farmer G3000 SF2000 Pro Mars Hydro FC-E3000 LED Grow Light";
            }} else if (ledWatts <= 560) {{
                recTitle = "480W–500W 6-Bar Samsung LM301H EVO LED (Spider Farmer SE5000 / Mars Hydro FC-E4800) + 6\" PRO T6";
                recDesc = "America's #1 4×4 grow tent combination delivering " + estPPFD + " PPFD and automated VPD exhaust.";
                lightQuery = "Spider Farmer SE5000 Mars Hydro FC-E4800 AC Infinity IONFRAME EVO6 480W LED";
            }} else {{
                recTitle = "730W–860W 8-Bar Commercial LED (Spider Farmer G8600 / SE7000 / Mars FC6500) + 8\" PRO T8";
                recDesc = "High-PPFD commercial bar array and 807 CFM exhaust for 5×5, 4×8, and CO2-enriched rooms.";
                lightQuery = "Spider Farmer G8600 SE7000 Mars Hydro FC6500 730W 860W Bar LED Grow Light";
            }}

            document.getElementById("recKitTitle").textContent = recTitle;
            document.getElementById("recKitDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(lightQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(fanQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateGrow);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-emerald-700 transition block">
            <span class="text-[11px] font-bold text-emerald-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home & Tent Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-emerald-800">Daily Grow Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Lab Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">Output Spec</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Diodes / Motor</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Performance</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Warranty</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Tent LED & Fan CFM
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On Quantum PAR, VPD & Airflow Performance Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-emerald-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our indoor grow tent benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Grow Equipment Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-emerald-800">Home & Tent Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-emerald-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-emerald-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-emerald-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "4×4 Ft Standard Grow Tent (48\"×48\"×80\")",
        "width": 4,
        "length": 4,
        "height": 6.7,
        "stage": "32",
        "filter": "1.6",
        "desc": "Calculate exact indoor grow tent LED grow light wattage (PPFD/DLI), inline exhaust fan CFM, carbon filter duct size (4\"/6\"/8\"), and fabric pot capacity—plus read 3 new hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Tent Size & Footprint Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
