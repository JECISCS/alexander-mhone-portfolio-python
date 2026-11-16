from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "static" / "images" / "projects" / "artwork"
WIDTH = 1440
HEIGHT = 760


def text(x, y, value, size=16, color="#26332E", weight=400, extra=""):
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'
    )


def rect(x, y, width, height, fill, radius=0, extra=""):
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="{radius}" fill="{fill}" {extra}/>'
    )


def civic_shell(title, subtitle, page):
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F2F4F1"),
        rect(0, 0, 228, HEIGHT, "#183A32"),
        text(34, 50, "CIVIC", 18, "#FFFFFF", 700, 'letter-spacing="2"'),
        text(34, 73, "SCORE", 11, "#9BD4B7", 700, 'letter-spacing="3"'),
        rect(29, 100, 170, 1, "#36574F"),
    ]
    links = ["Overview", "Scorecards", "District map", "Reports", "Analytics", "Community"]
    for index, label in enumerate(links):
        y = 145 + index * 49
        active = label.lower() in page.lower()
        if active:
            parts.append(rect(14, y - 25, 200, 39, "#2B554A", 8))
            parts.append(rect(14, y - 25, 3, 39, "#8FD5AD", 2))
        parts.append(text(43, y, label, 14, "#FFFFFF" if active else "#AFC5BC", 400))
    parts += [
        rect(24, 676, 180, 55, "#22463D", 10),
        text(40, 699, "MANGOCHI DISTRICT", 10, "#9BD4B7", 700, 'letter-spacing="1"'),
        text(40, 718, "Community workspace", 11, "#FFFFFF"),
        rect(228, 0, 1212, 78, "#FFFFFF"),
        text(265, 33, "Mangochi District  /  Malawi", 13, "#63736C"),
        text(265, 56, "Social accountability workspace", 11, "#9AA59F"),
        rect(1223, 20, 178, 38, "#F2F6F3", 19),
        text(1243, 44, "●  DATA UPDATED", 10, "#327A56", 700, 'letter-spacing="1"'),
        text(265, 126, title, 30, "#20352D", 700),
        text(265, 153, subtitle, 13, "#738078"),
        text(265, 730, "CIVICSCORE  /  COMMUNITY-LED ACCOUNTABILITY", 10, "#92A097", 700, 'letter-spacing="1"'),
        text(1305, 730, f"{page.upper()}  /  0{civic_pages.index(page) + 1}", 10, "#92A097", 700, 'text-anchor="end" letter-spacing="1"'),
    ]
    return parts


civic_pages = [
    "Overview",
    "Scorecards",
    "District map",
    "Reports",
    "Analytics",
    "Community",
    "Institutions",
    "Follow-up",
    "Evidence library",
]


def civic_art(index):
    page = civic_pages[index - 1]
    titles = [
        ("District overview", "A clear view of community priorities and public service performance."),
        ("Community scorecards", "Compare reported experiences across essential public services."),
        ("Mangochi service map", "Explore feedback and follow-up by community and service area."),
        ("Community reports", "Review issues raised by residents and track the next action."),
        ("Performance insights", "Spot patterns in service delivery and emerging community needs."),
        ("Community voices", "See the latest feedback shared by residents and local groups."),
        ("Institution directory", "Connect each service concern to the responsible institution."),
        ("Action follow-up", "Keep commitments visible from first report to resolution."),
        ("Evidence library", "Organise supporting documents and field evidence in one place."),
    ]
    title, subtitle = titles[index - 1]
    parts = civic_shell(title, subtitle, page)

    def card(x, y, w, h, heading, value=None, detail=None):
        parts.append(rect(x, y, w, h, "#FFFFFF", 12, 'stroke="#E5EBE6" stroke-width="1"'))
        parts.append(text(x + 20, y + 29, heading, 12, "#728078", 600))
        if value is not None:
            parts.append(text(x + 20, y + 69, value, 26, "#213A30", 700))
        if detail is not None:
            parts.append(text(x + 20, y + h - 17, detail, 10, "#538567", 600))

    if index == 1:
        card(265, 180, 260, 108, "REPORTS RECEIVED", "1,284", "↑ 12% this quarter")
        card(541, 180, 260, 108, "COMMUNITY SCORE", "78 / 100", "↑ 6 points this year")
        card(817, 180, 260, 108, "ACTIONS IN PROGRESS", "36", "Across 8 service areas")
        card(1093, 180, 275, 108, "RESOLVED THIS MONTH", "84%", "↑ 9% since last month")
        card(265, 309, 690, 366, "SERVICE DELIVERY  /  COMMUNITY SCORE")
        parts.append(text(290, 371, "Community score", 12, "#7D8983"))
        parts.append(text(290, 415, "78", 34, "#263D32", 700))
        parts.append(text(340, 415, "out of 100  ·  Improving steadily", 12, "#5E8B6D"))
        for i, h in enumerate([77, 114, 94, 143, 125, 172, 151, 196, 179, 218, 198, 238]):
            x = 302 + i * 48
            parts.append(rect(x, 628 - h, 23, h, "#76B58F" if i > 7 else "#C7DFD0", 5))
            parts.append(text(x + 11, 649, ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"][i], 9, "#91A097", 400, 'text-anchor="middle"'))
        card(974, 309, 394, 366, "LATEST COMMUNITY UPDATES")
        for i, (name, line) in enumerate([
            ("Water access", "New borehole feedback · 2h ago"),
            ("Primary education", "School facility review · 5h ago"),
            ("Local health services", "Community response received · 1d ago"),
            ("Road maintenance", "Follow-up scheduled · 2d ago"),
        ]):
            y = 381 + i * 66
            parts += [rect(997, y - 20, 34, 34, ["#E1F1E7", "#F5EEDC", "#E6E9F5", "#E1F1E7"][i], 10),
                      text(1014, y + 2, ["W", "E", "H", "R"][i], 13, "#3D7755", 700, 'text-anchor="middle"'),
                      text(1044, y - 1, name, 13, "#304139", 600),
                      text(1044, y + 19, line, 10, "#89958E")]
    elif index == 2:
        card(265, 181, 1103, 494, "SCORECARD COMPARISON")
        parts += [
            text(294, 246, "SERVICE AREA", 10, "#8A958F", 700, 'letter-spacing="1"'),
            text(795, 246, "COMMUNITY SCORE", 10, "#8A958F", 700, 'letter-spacing="1"'),
            text(1124, 246, "TREND", 10, "#8A958F", 700, 'letter-spacing="1"'),
        ]
        rows = [("Water & sanitation", 84, "↑ 8"), ("Primary education", 78, "↑ 4"),
                ("Community health", 73, "↑ 6"), ("Road access", 67, "↓ 2"),
                ("Agriculture support", 61, "↑ 3")]
        for i, (name, score, trend) in enumerate(rows):
            y = 295 + i * 70
            parts += [rect(288, y + 18, 1054, 1, "#EDF0ED"),
                      text(294, y, name, 14, "#34453D", 600),
                      rect(795, y - 12, 260, 13, "#ECF1ED", 7),
                      rect(795, y - 12, score * 2.6, 13, "#67A981", 7),
                      text(1070, y, f"{score} / 100", 12, "#34453D", 700),
                      text(1200, y, trend, 12, "#4B9366", 600)]
    elif index == 3:
        card(265, 181, 770, 494, "COMMUNITY FEEDBACK BY AREA")
        # Abstract district regions make a clear, illustrative map rather than a false geographic boundary.
        regions = [
            ("#D2E8D8", "Makanjira", 380, 290, "M"),
            ("#9BCBA9", "Monkey Bay", 520, 278, "M"),
            ("#E4EEDB", "Mangochi Town", 660, 300, "M"),
            ("#B6D9BE", "Chilipa", 430, 410, "C"),
            ("#E6EEDF", "Namwera", 590, 420, "N"),
            ("#7FBA91", "Nankumba", 740, 410, "N"),
            ("#C4DFC9", "Chiponde", 550, 525, "C"),
        ]
        for fill, label, x, y, initial in regions:
            parts += [rect(x, y, 122, 74, fill, 20, 'stroke="#FFFFFF" stroke-width="4"'),
                      text(x + 61, y + 31, initial, 13, "#356B4B", 700, 'text-anchor="middle"'),
                      text(x + 61, y + 53, label, 10, "#45624F", 600, 'text-anchor="middle"')]
        card(1054, 181, 314, 230, "REPORTS BY SERVICE")
        for i, (label, amount, color) in enumerate([("Water", "38%", "#5C9D75"), ("Education", "27%", "#85B994"), ("Health", "21%", "#B1D0B8"), ("Other", "14%", "#D9E7DC")]):
            y = 245 + i * 37
            parts += [rect(1076, y - 11, 10, 10, color, 3),
                      text(1095, y, label, 12, "#536159"),
                      text(1338, y, amount, 12, "#304138", 700, 'text-anchor="end"')]
        card(1054, 430, 314, 245, "AREA TO WATCH", "Road access", "22 open community reports")
    elif index == 4:
        card(265, 181, 1103, 494, "RECENT COMMUNITY REPORTS")
        parts += [text(294, 246, "REPORT / SERVICE", 10, "#8A958F", 700, 'letter-spacing="1"'),
                  text(790, 246, "COMMUNITY", 10, "#8A958F", 700, 'letter-spacing="1"'),
                  text(1040, 246, "STATUS", 10, "#8A958F", 700, 'letter-spacing="1"'),
                  text(1240, 246, "UPDATED", 10, "#8A958F", 700, 'letter-spacing="1"')]
        rows = [("Limited water access", "Water & sanitation", "Makanjira", "In review", "Today"),
                ("Classroom materials", "Primary education", "Monkey Bay", "Assigned", "Yesterday"),
                ("Clinic opening hours", "Community health", "Mangochi Town", "Responded", "12 Nov"),
                ("Road surface damage", "Road access", "Namwera", "In review", "11 Nov"),
                ("Crop support request", "Agriculture", "Chilipa", "Resolved", "10 Nov")]
        for i, row in enumerate(rows):
            y = 303 + i * 67
            parts += [rect(288, y + 17, 1054, 1, "#EDF0ED"),
                      text(294, y - 3, row[0], 13, "#34453D", 600),
                      text(294, y + 16, row[1], 10, "#87928C"),
                      text(790, y + 4, row[2], 12, "#536159"),
                      rect(1038, y - 13, 105, 25, "#E4F1E8", 12),
                      text(1090, y + 4, row[3], 10, "#417A55", 600, 'text-anchor="middle"'),
                      text(1240, y + 4, row[4], 11, "#68756E")]
    elif index == 5:
        card(265, 181, 690, 494, "COMMUNITY PRIORITIES  /  LAST 6 MONTHS")
        for i, (label, value) in enumerate([("Water access", 84), ("Education quality", 70), ("Health services", 64), ("Road access", 53), ("Agriculture", 41)]):
            y = 270 + i * 73
            parts += [text(292, y, label, 13, "#48584F", 600),
                      rect(292, y + 14, 600, 16, "#ECF1ED", 8),
                      rect(292, y + 14, value * 6, 16, "#6DA982", 8),
                      text(916, y + 28, f"{value}%", 11, "#4C785B", 700, 'text-anchor="end"')]
        card(974, 181, 394, 224, "REPORT RESPONSE TIME", "4.2 days", "↓ 1.1 days faster this quarter")
        for i, h in enumerate([53, 78, 64, 106, 88, 123, 108]):
            parts.append(rect(1004 + i * 43, 372 - h, 22, h, "#8AC19A" if i > 4 else "#D0E5D5", 5))
        card(974, 424, 394, 251, "RESOLUTION BY SERVICE")
        for i, (label, value) in enumerate([("Water & sanitation", "82%"), ("Education", "76%"), ("Health", "71%")]):
            y = 496 + i * 50
            parts += [text(998, y, label, 12, "#526158"),
                      text(1340, y, value, 12, "#356B4B", 700, 'text-anchor="end"'),
                      rect(998, y + 12, 340, 6, "#EAF0EB", 3),
                      rect(998, y + 12, int(value[:-1]) * 3.4, 6, "#75B488", 3)]
    elif index == 6:
        for i, (name, location, score, initials) in enumerate([
            ("Grace M.", "Makanjira · Water access", "“Our village has reliable water this month.”", "G"),
            ("Peter K.", "Monkey Bay · Education", "“The new classroom materials arrived.”", "P"),
            ("Esther N.", "Mangochi Town · Health", "“We shared our clinic feedback with the team.”", "E"),
        ]):
            x = 265 + i * 374
            card(x, 181, 348, 494, "COMMUNITY UPDATE")
            parts += [rect(x + 25, 236, 55, 55, ["#D8EBDD", "#F0E7D2", "#E3E4F1"][i], 18),
                      text(x + 52, 271, initials, 18, "#3C7151", 700, 'text-anchor="middle"'),
                      text(x + 96, 258, name, 15, "#31443A", 700),
                      text(x + 96, 279, location, 10, "#849088"),
                      text(x + 25, 344, score, 18, "#42554A", 500),
                      rect(x + 25, 385, 298, 1, "#E9EEEA"),
                      text(x + 25, 421, "STATUS", 10, "#8A958F", 700, 'letter-spacing="1"'),
                      rect(x + 25, 443, 105, 27, "#E3F1E7", 13),
                      text(x + 78, 461, ["Follow-up", "Resolved", "Responded"][i], 10, "#417A55", 600, 'text-anchor="middle"'),
                      text(x + 25, 527, "COMMUNITY SCORE", 10, "#8A958F", 700, 'letter-spacing="1"'),
                      text(x + 25, 580, ["82", "76", "89"][i], 34, "#2E6747", 700),
                      text(x + 77, 580, "/ 100", 12, "#87928C")]
    elif index == 7:
        card(265, 181, 1103, 494, "SERVICE INSTITUTIONS")
        institutions = [("Mangochi District Council", "Local infrastructure · public services", "12 open items", "MDC"),
                        ("District Health Office", "Health facilities · community care", "8 open items", "DHO"),
                        ("District Education Office", "Schools · learning resources", "6 open items", "DEO"),
                        ("Water Development Office", "Water access · sanitation", "4 open items", "WDO")]
        for i, (name, detail, status, short) in enumerate(institutions):
            y = 295 + i * 83
            parts += [rect(292, y - 29, 48, 48, "#E5F1E8", 13),
                      text(316, y, short, 10, "#3F7853", 700, 'text-anchor="middle"'),
                      text(363, y - 5, name, 14, "#34453D", 600),
                      text(363, y + 17, detail, 10, "#87928C"),
                      rect(1054, y - 15, 188, 28, "#F1F5F2", 14),
                      text(1148, y + 4, status, 10, "#52715C", 600, 'text-anchor="middle"')]
    elif index == 8:
        card(265, 181, 1103, 494, "FOLLOW-UP TRACKER")
        cases = [("Water point repair", "Makanjira community", 82, "IN PROGRESS"),
                 ("School materials request", "Monkey Bay community", 55, "ASSIGNED"),
                 ("Clinic access feedback", "Mangochi Town community", 100, "COMPLETED")]
        for i, (name, location, progress, state) in enumerate(cases):
            y = 280 + i * 120
            parts += [text(297, y, name, 15, "#304238", 700),
                      text(297, y + 24, location, 11, "#88938D"),
                      rect(297, y + 42, 700, 9, "#EAF0EB", 5),
                      rect(297, y + 42, progress * 7, 9, "#6BA881", 5),
                      text(1020, y + 12, f"{progress}% complete", 11, "#4E795B", 600),
                      rect(1173, y - 8, 147, 28, "#E3F1E7", 14),
                      text(1246, y + 11, state, 9, "#417A55", 700, 'text-anchor="middle" letter-spacing="1"')]
    else:
        card(265, 181, 1103, 494, "FIELD EVIDENCE")
        for i, (label, kind) in enumerate([("Water point review", "FIELD NOTE"), ("Community meeting", "PHOTO RECORD"), ("School visit", "ASSESSMENT"), ("Health centre", "FIELD NOTE")]):
            x = 291 + i * 267
            parts += [rect(x, 239, 244, 208, ["#D8E6DA", "#E9E2D2", "#DBE3E8", "#E2DDD4"][i], 9),
                      rect(x + 17, 256, 210, 174, ["#B7D3BF", "#DACDAF", "#B6CCD6", "#C9BDAA"][i], 6),
                      rect(x + 39, 280, 164, 78, "#FFFFFF", 4, 'opacity=".72"'),
                      rect(x + 39, 370, 130, 8, "#FFFFFF", 4, 'opacity=".75"'),
                      rect(x + 39, 388, 95, 6, "#FFFFFF", 3, 'opacity=".55"'),
                      text(x, 480, label, 13, "#35473C", 600),
                      text(x, 503, kind, 9, "#8A958F", 700, 'letter-spacing="1"')]

    return svg_doc(parts)


def mindsafe_art(index):
    titles = [
        ("A little support,\nright when you need it.", "A calmer space to check in, find guidance and take one small step."),
        ("Check in with yourself.", "Notice how today feels. Every answer is welcome here."),
        ("Small steps count.", "Gentle, practical tools for the moments that feel heavy."),
        ("You don't have to\nfigure it out alone.", "Find a trusted person and make a plan to reach out."),
        ("Take a moment\nto reset.", "A quiet breathing exercise you can do at your own pace."),
        ("Support that stays\nwithin reach.", "Save helpful guidance for whenever you need a reminder."),
    ]
    title, subtitle = titles[index - 1]
    purple = "#6856B5"
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F5F3FA"),
        rect(0, 0, WIDTH, 82, "#FFFFFF"),
        text(70, 50, "mindsafe", 25, "#302C43", 700),
        rect(70, 61, 82, 3, "#8878D0", 2),
        text(1090, 48, "HOME     YOUR WELLBEING     GET SUPPORT", 11, "#737088", 600, 'letter-spacing="1"'),
        rect(1288, 22, 105, 38, "#EEEAF9", 19),
        text(1340, 46, "MY SPACE", 10, purple, 700, 'text-anchor="middle" letter-spacing="1"'),
        text(75, 141, "MINDSAFE MALAWI  /  WELLBEING", 11, purple, 700, 'letter-spacing="2"'),
    ]
    lines = title.split("\n")
    y = 228
    for line in lines:
        parts.append(text(75, y, line, 52, "#302C43", 700, 'letter-spacing="-1"'))
        y += 59
    subtitle_y = y + 11
    parts += [
        text(78, subtitle_y, subtitle, 15, "#77748A"),
        rect(78, subtitle_y + 34, 176, 46, purple, 23),
        text(166, subtitle_y + 63, ["Explore support", "Start check-in", "Try a tool", "Make a plan", "Begin breathing", "Browse guidance"][index - 1], 12, "#FFFFFF", 700, 'text-anchor="middle"'),
        text(78, subtitle_y + 119, "Private by design  ·  Works at your pace", 11, "#89869B"),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(75, 739, "A SAFE SPACE TO TAKE YOUR NEXT SMALL STEP", 10, "#89869B", 600, 'letter-spacing="1"'),
        text(1362, 739, f"MINDSAFE  /  0{index}", 10, "#89869B", 700, 'text-anchor="end" letter-spacing="1"'),
    ]

    # Give each gallery slide its own full-height, edge-to-edge app surface.
    if index == 1:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 199, "YOUR DAILY CHECK-IN", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 244, "How are you feeling today?", 22, "#302C43", 700),
                  text(884, 271, "There is no right or wrong answer.", 11, "#89869B")]
        for i, (emoji, feeling) in enumerate([("☀", "Good"), ("◒", "Okay"), ("☁", "Low"), ("♡", "Unsure")]):
            x = 880 + i * 105
            parts += [rect(x, 304, 90, 106, "#F5F2FC" if i == 1 else "#F8F7FB", 16),
                      text(x + 45, 352, emoji, 24, ["#E29F53", "#8170C4", "#678FAA", "#C27B9D"][i], 700, 'text-anchor="middle"'),
                      text(x + 45, 384, feeling, 11, "#5F5B73", 600, 'text-anchor="middle"')]
        parts += [text(884, 455, "TODAY'S GENTLE REMINDER", 10, purple, 700, 'letter-spacing="1"'),
                  text(884, 490, "You deserve care, even on", 16, "#302C43", 600),
                  text(884, 514, "the days when things feel hard.", 16, "#302C43", 600),
                  rect(884, 549, 190, 43, "#EEEAF9", 21),
                  text(979, 576, "See support options  →", 11, purple, 700, 'text-anchor="middle"')]
    elif index == 2:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 199, "WELLBEING CHECK-IN", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 248, "How has your week felt?", 23, "#302C43", 700),
                  text(884, 277, "Choose anything that feels close.", 12, "#89869B")]
        for i, (label, val) in enumerate([("Calm", 76), ("Connected", 54), ("Rested", 68), ("Hopeful", 82)]):
            yy = 335 + i * 61
            parts += [text(885, yy, label, 12, "#5F5B73", 600),
                      rect(990, yy - 10, 250, 12, "#F0EDF7", 6),
                      rect(990, yy - 10, int(250 * val / 100), 12, ["#7B6AC6", "#78A9A1", "#D5AA6B", "#9486D4"][i], 6),
                      text(1261, yy, f"{val}%", 11, "#79758C", 600)]
        parts += [rect(884, 582, 405, 1, "#EEEAF4"),
                  text(884, 606, "Your check-ins are private to you.", 11, "#89869B")]
    elif index == 3:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 198, "TOOLS FOR RIGHT NOW", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 242, "Choose one small step.", 22, "#302C43", 700)]
        for i, (label, detail, icon, color) in enumerate([
            ("Grounding exercise", "Notice five things around you", "5", "#E7E1F6"),
            ("Make space to write", "Get thoughts out of your head", "✎", "#E6F0EC"),
            ("Reach someone", "A conversation can make a difference", "♡", "#F5EBDD"),
        ]):
            yy = 282 + i * 98
            parts += [rect(880, yy, 420, 78, "#FBFAFD", 14, 'stroke="#EFECF4" stroke-width="1"'),
                      rect(896, yy + 14, 48, 48, color, 15),
                      text(920, yy + 45, icon, 18, purple, 700, 'text-anchor="middle"'),
                      text(961, yy + 32, label, 13, "#3B364D", 700),
                      text(961, yy + 53, detail, 10, "#89869B"),
                      text(1277, yy + 45, "→", 17, purple, 500, 'text-anchor="middle"')]
        parts.append(text(884, 610, "Move at your own pace. Skip anything you don't need.", 10, "#89869B"))
    elif index == 4:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 199, "YOUR SUPPORT CIRCLE", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 243, "Who feels safe to talk to?", 22, "#302C43", 700),
                  text(884, 271, "Start with one person you trust.", 11, "#89869B")]
        for i, (name, relation, initial) in enumerate([("A trusted friend", "Someone who listens", "F"),
                                                       ("Family member", "Someone you feel safe with", "M"),
                                                       ("Support service", "Confidential help is available", "+")]):
            yy = 304 + i * 80
            parts += [rect(884, yy, 416, 62, "#FBFAFD", 13, 'stroke="#EFECF4" stroke-width="1"'),
                      rect(899, yy + 9, 44, 44, ["#EAE4F7", "#E6F0EC", "#F5EBDD"][i], 15),
                      text(921, yy + 37, initial, 15, purple, 700, 'text-anchor="middle"'),
                      text(958, yy + 27, name, 12, "#3B364D", 700),
                      text(958, yy + 45, relation, 10, "#89869B"),
                      text(1275, yy + 38, "→", 16, purple, 500, 'text-anchor="middle"')]
        parts += [rect(884, 559, 416, 38, "#F4F1FA", 19),
                  text(1092, 584, "You choose what to share.", 10, purple, 600, 'text-anchor="middle"')]
    elif index == 5:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 199, "A MOMENT TO RESET", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 244, "Breathe in. Breathe out.", 22, "#302C43", 700),
                  text(884, 274, "Follow the circle for one slow breath.", 11, "#89869B"),
                  rect(1002, 319, 185, 185, "#F2EFFA", 92),
                  rect(1021, 338, 147, 147, "#DDD6F2", 74),
                  rect(1041, 358, 107, 107, "#8978CE", 54),
                  text(1094, 412, "IN", 12, "#FFFFFF", 700, 'text-anchor="middle" letter-spacing="2"'),
                  text(1094, 435, "4", 24, "#FFFFFF", 600, 'text-anchor="middle"'),
                  text(884, 552, "INHALE", 10, purple, 700, 'letter-spacing="2"'),
                  rect(884, 565, 416, 5, "#EEEAF5", 3),
                  rect(884, 565, 182, 5, "#8573C9", 3),
                  text(884, 598, "No rush. Stop whenever you're ready.", 10, "#89869B")]
    else:
        parts += [rect(815, 121, 555, 535, "#EAE6F7", 30),
                  rect(850, 155, 485, 468, "#FFFFFF", 20),
                  text(884, 199, "YOUR SAVED SUPPORT", 10, "#8C86A5", 700, 'letter-spacing="1"'),
                  text(884, 242, "A few things to keep close.", 22, "#302C43", 700)]
        guidance = [("When feelings feel big", "A reminder that emotions change.", "#EAE4F7"),
                    ("Reach out to someone", "You can ask for company or a chat.", "#E4F0EA"),
                    ("Take care of the basics", "Water, rest and a little fresh air.", "#F5EBDD"),
                    ("Find urgent support", "Contact local emergency services.", "#F4E4E9")]
        for i, (label, detail, color) in enumerate(guidance):
            yy = 282 + i * 71
            parts += [rect(884, yy, 416, 57, "#FBFAFD", 12, 'stroke="#EFECF4" stroke-width="1"'),
                      rect(898, yy + 10, 38, 38, color, 12),
                      text(917, yy + 35, ["♡", "↗", "＋", "!"][i], 15, purple, 700, 'text-anchor="middle"'),
                      text(951, yy + 24, label, 12, "#3B364D", 700),
                      text(951, yy + 42, detail, 10, "#89869B")]

    return svg_doc(parts)


def tibhu_art(index):
    titles = [
        ("Find your next ride.", "Book a seat and get moving with TibhuKeBus."),
        ("Choose the trip that works.", "Compare routes, departure times and available seats."),
        ("Pick your seat.", "Choose a comfortable spot before confirming your journey."),
        ("Add passenger details.", "Review your booking and continue to ticket payment."),
        ("Your ticket, ready to go.", "Keep your booking details close for the journey."),
    ]
    title, subtitle = titles[index - 1]
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F3F4EF"),
        rect(0, 0, WIDTH, 78, "#FFFFFF"),
        text(66, 50, "TIBHU", 24, "#1D3932", 700, 'letter-spacing="1"'),
        text(155, 50, "KE BUS", 14, "#68A27B", 700, 'letter-spacing="2"'),
        text(925, 47, "BOOK A TRIP      MY BOOKINGS      HELP", 11, "#64736B", 600, 'letter-spacing="1"'),
        rect(1289, 20, 95, 38, "#E4F0E7", 19),
        text(1336, 44, "SIGN IN", 10, "#34724D", 700, 'text-anchor="middle" letter-spacing="1"'),
        text(72, 131, "TIBHUKEBUS  /  BUS BOOKING", 10, "#4E8B64", 700, 'letter-spacing="2"'),
        text(72, 189, title, 39, "#1E342C", 700, 'letter-spacing="-1"'),
        text(74, 222, subtitle, 13, "#76827B"),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(70, 739, "A SIMPLER WAY TO PLAN YOUR JOURNEY", 10, "#87928B", 600, 'letter-spacing="1"'),
        text(1368, 739, f"TIBHUKEBUS  /  0{index}", 10, "#87928B", 700, 'text-anchor="end" letter-spacing="1"'),
    ]
    if index == 1:
        parts += [
            rect(735, 111, 640, 205, "#DDEBE0", 22),
            rect(777, 155, 484, 100, "#1E3931", 19),
            rect(803, 174, 178, 52, "#DCEBE0", 9),
            rect(994, 174, 110, 52, "#BBD6C3", 9),
            rect(1118, 174, 115, 52, "#E7EDE5", 9),
            rect(827, 265, 332, 12, "#1D3932", 6),
            rect(848, 286, 286, 7, "#75947F", 4),
            '<circle cx="850" cy="265" r="20" fill="#263C34"/>',
            '<circle cx="1186" cy="265" r="20" fill="#263C34"/>',
            text(72, 285, "Lilongwe", 12, "#527160", 600),
            text(72, 307, "Easy booking. A seat is waiting.", 12, "#849088"),
            rect(72, 356, 795, 117, "#FFFFFF", 14, 'stroke="#E5EAE4" stroke-width="1"'),
            text(99, 386, "FROM", 9, "#8B968F", 700, 'letter-spacing="1"'),
            text(99, 427, "Lilongwe", 18, "#293D33", 600),
            text(344, 386, "TO", 9, "#8B968F", 700, 'letter-spacing="1"'),
            text(344, 427, "Blantyre", 18, "#293D33", 600),
            text(568, 386, "TRAVEL DATE", 9, "#8B968F", 700, 'letter-spacing="1"'),
            text(568, 427, "Select a date", 15, "#68776E"),
            rect(735, 391, 106, 45, "#38784F", 22),
            text(788, 419, "Search", 12, "#FFFFFF", 700, 'text-anchor="middle"'),
            text(72, 526, "POPULAR ROUTES", 10, "#71907B", 700, 'letter-spacing="1"'),
        ]
        for i, (route, time, price) in enumerate([
            ("Lilongwe → Blantyre", "Daily departures", "From MWK 25,000"),
            ("Blantyre → Zomba", "Multiple departures", "From MWK 12,000"),
            ("Lilongwe → Mzuzu", "Selected travel days", "From MWK 30,000"),
        ]):
            x = 72 + i * 435
            parts += [rect(x, 546, 405, 111, "#FFFFFF", 13, 'stroke="#E5EAE4" stroke-width="1"'),
                      text(x + 19, 578, route, 14, "#2B4035", 700),
                      text(x + 19, 602, time, 10, "#859089"),
                      text(x + 19, 633, price, 11, "#4E8B64", 700)]
    elif index == 2:
        parts += [text(72, 278, "AVAILABLE DEPARTURES", 10, "#71907B", 700, 'letter-spacing="1"'),
                  text(72, 315, "Lilongwe  →  Blantyre", 22, "#1E342C", 700),
                  text(72, 340, "3 options for your selected travel date", 11, "#849088")]
        for i, (operator, departure, arrival, fare, seats) in enumerate([
            ("Capital Express", "07:30", "13:45", "MWK 28,000", "12 seats left"),
            ("Green Line Coach", "09:00", "15:20", "MWK 25,000", "8 seats left"),
            ("Lakeview Travel", "11:15", "17:40", "MWK 30,000", "16 seats left"),
        ]):
            y = 371 + i * 95
            parts += [rect(72, y, 980, 78, "#FFFFFF", 12, 'stroke="#E5EAE4" stroke-width="1"'),
                      text(95, y + 29, operator, 13, "#34483C", 700),
                      text(95, y + 52, "AC • Reclining seats • Luggage", 10, "#88928C"),
                      text(440, y + 31, departure, 17, "#2A4035", 700),
                      text(494, y + 31, "→", 15, "#8C998F"),
                      text(530, y + 31, arrival, 17, "#2A4035", 700),
                      text(440, y + 54, "Lilongwe", 9, "#89958D"),
                      text(530, y + 54, "Blantyre", 9, "#89958D"),
                      text(740, y + 30, fare, 14, "#36764C", 700),
                      text(740, y + 52, seats, 10, "#88928C"),
                      rect(922, y + 18, 106, 41, "#38784F", 20),
                      text(975, y + 44, "Choose", 11, "#FFFFFF", 700, 'text-anchor="middle"')]
        parts += [rect(1082, 371, 286, 268, "#E5EEE5", 16),
                  text(1107, 407, "YOUR SEARCH", 10, "#65826E", 700, 'letter-spacing="1"'),
                  text(1107, 451, "Lilongwe", 17, "#2C4135", 700),
                  text(1107, 477, "Blantyre", 17, "#2C4135", 700),
                  rect(1107, 495, 233, 1, "#CBDACE"),
                  text(1107, 527, "Travel date", 10, "#839087"),
                  text(1107, 550, "Selected date", 13, "#34483C", 600),
                  text(1107, 602, "Change search  →", 11, "#4E8B64", 700)]
    elif index == 3:
        parts += [rect(72, 266, 810, 386, "#FFFFFF", 14, 'stroke="#E5EAE4" stroke-width="1"'),
                  text(103, 307, "SELECT YOUR SEAT", 10, "#71907B", 700, 'letter-spacing="1"'),
                  text(103, 337, "Choose from available seats on the coach", 12, "#7D8982"),
                  rect(128, 364, 390, 244, "#F6F8F5", 15),
                  text(323, 394, "FRONT OF COACH", 9, "#8A958D", 700, 'text-anchor="middle" letter-spacing="1"')]
        for row in range(4):
            for col in range(4):
                x = 175 + col * 78
                y = 422 + row * 42
                color = "#7CB48A" if (row, col) == (1, 2) else ("#E4EAE4" if (row + col) % 4 else "#D2DAD3")
                parts.append(rect(x, y, 48, 30, color, 8))
                parts.append(text(x + 24, y + 20, f"{row * 4 + col + 1:02}", 9, "#FFFFFF" if color == "#7CB48A" else "#718077", 600, 'text-anchor="middle"'))
        parts += [rect(556, 381, 12, 12, "#7CB48A", 4), text(577, 392, "Selected", 10, "#6E7D73"),
                  rect(661, 381, 12, 12, "#E4EAE4", 4), text(682, 392, "Available", 10, "#6E7D73"),
                  rect(785, 381, 12, 12, "#D2DAD3", 4), text(806, 392, "Unavailable", 10, "#6E7D73"),
                  rect(920, 266, 448, 386, "#E5EEE5", 16),
                  text(951, 307, "TRIP SUMMARY", 10, "#65826E", 700, 'letter-spacing="1"'),
                  text(951, 357, "Lilongwe  →  Blantyre", 17, "#2C4135", 700),
                  text(951, 388, "Capital Express  ·  07:30", 11, "#77847B"),
                  rect(951, 416, 384, 1, "#CBDACE"),
                  text(951, 455, "Selected seat", 11, "#819087"),
                  text(951, 480, "Seat 07", 14, "#34483C", 700),
                  text(951, 521, "Fare", 11, "#819087"),
                  text(1334, 521, "MWK 28,000", 14, "#34483C", 700, 'text-anchor="end"'),
                  rect(951, 557, 384, 46, "#38784F", 23),
                  text(1143, 586, "Continue to booking", 12, "#FFFFFF", 700, 'text-anchor="middle"')]
    elif index == 4:
        parts += [rect(72, 266, 800, 374, "#FFFFFF", 16, 'stroke="#E5EAE4" stroke-width="1"'),
                  text(106, 307, "PASSENGER DETAILS", 10, "#65826E", 700, 'letter-spacing="1"'),
                  text(106, 348, "Who is travelling?", 22, "#293E33", 700),
                  text(106, 377, "Enter the passenger information for this ticket.", 11, "#7C8981")]
        for label, x, y, value in [
            ("FULL NAME", 106, 427, "Passenger name"),
            ("PHONE NUMBER", 472, 427, "+265"),
            ("EMAIL ADDRESS", 106, 518, "name@example.com"),
        ]:
            parts += [text(x, y, label, 9, "#8B968F", 700, 'letter-spacing="1"'),
                      rect(x, y + 13, 332, 45, "#FAFBF9", 8, 'stroke="#E5EAE4" stroke-width="1"'),
                      text(x + 14, y + 42, value, 11, "#818C84")]
        parts += [rect(814, 402, 58, 45, "#38784F", 22),
                  text(843, 430, "→", 16, "#FFFFFF", 700, 'text-anchor="middle"'),
                  rect(918, 266, 450, 374, "#E5EEE5", 16),
                  text(951, 307, "BOOKING SUMMARY", 10, "#65826E", 700, 'letter-spacing="1"'),
                  text(951, 356, "Lilongwe  →  Blantyre", 17, "#2C4135", 700),
                  text(951, 385, "Capital Express  ·  07:30", 11, "#77847B"),
                  rect(951, 408, 384, 1, "#CBDACE"),
                  text(951, 447, "Selected seat", 11, "#819087"),
                  text(951, 472, "Seat 07  ·  Window", 13, "#34483C", 700),
                  text(951, 513, "Ticket total", 11, "#819087"),
                  text(1334, 513, "MWK 28,000", 14, "#34483C", 700, 'text-anchor="end"'),
                  rect(951, 551, 384, 46, "#38784F", 23),
                  text(1143, 580, "Continue to payment", 12, "#FFFFFF", 700, 'text-anchor="middle"')]
    else:
        parts += [rect(72, 266, 810, 374, "#FFFFFF", 16, 'stroke="#E5EAE4" stroke-width="1"'),
                  rect(72, 266, 810, 77, "#1E3931", 16),
                  text(108, 310, "TIBHUKEBUS  /  E-TICKET", 11, "#D4E8D8", 700, 'letter-spacing="1"'),
                  rect(108, 366, 365, 219, "#F5F8F4", 14),
                  text(138, 407, "BOARDING PASS", 10, "#65826E", 700, 'letter-spacing="1"'),
                  text(138, 449, "Lilongwe  →  Blantyre", 19, "#293E33", 700),
                  text(138, 485, "DEPARTURE", 9, "#8B968F", 700, 'letter-spacing="1"'),
                  text(138, 512, "07:30  ·  Selected date", 13, "#4B5D51", 600),
                  text(138, 550, "CAPITAL EXPRESS  ·  SEAT 07", 10, "#68776E", 700, 'letter-spacing="1"'),
                  rect(504, 366, 340, 219, "#E5EEE5", 14),
                  text(534, 407, "PASSENGER", 9, "#819087", 700, 'letter-spacing="1"'),
                  text(534, 436, "Your booking name", 14, "#34483C", 700),
                  text(534, 477, "BOOKING REFERENCE", 9, "#819087", 700, 'letter-spacing="1"'),
                  text(534, 506, "TKB · 0482 · 19", 17, "#34483C", 700),
                  text(534, 550, "Keep this ticket for boarding.", 10, "#6E8373"),
                  rect(918, 266, 450, 374, "#DDEBE0", 16),
                  text(960, 316, "YOUR JOURNEY", 10, "#65826E", 700, 'letter-spacing="1"'),
                  '<circle cx="1003" cy="382" r="15" fill="#4B9366"/>',
                  '<circle cx="1003" cy="500" r="15" fill="#4B9366"/>',
                  '<path d="M1003 397 L1003 485" stroke="#78AA85" stroke-width="4" stroke-dasharray="6 7"/>',
                  text(1040, 377, "LILONGWE", 10, "#839087", 700, 'letter-spacing="1"'),
                  text(1040, 405, "Departure point", 16, "#2C4135", 700),
                  text(1040, 495, "BLANTYRE", 10, "#839087", 700, 'letter-spacing="1"'),
                  text(1040, 523, "Arrival destination", 16, "#2C4135", 700),
                  text(960, 588, "Ticket details stay together in one place.", 10, "#6E8373")]
    return svg_doc(parts)


def school_art(index):
    titles = [
        "A clearer view of school.",
        "Student records, together.",
        "Attendance at a glance.",
        "Progress made visible.",
    ]
    title = titles[index - 1]
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F3F5F8"),
        rect(0, 0, 228, HEIGHT, "#203653"),
        text(32, 48, "SCHOOL", 17, "#FFFFFF", 700, 'letter-spacing="2"'),
        text(32, 70, "DESK", 10, "#ADC7E3", 700, 'letter-spacing="3"'),
        rect(28, 99, 170, 1, "#3D5673"),
    ]
    menu = ["Overview", "Students", "Attendance", "Classes", "Academics", "Reports"]
    active = ["Overview", "Students", "Attendance", "Academics"][index - 1]
    for i, label in enumerate(menu):
        y = 145 + i * 48
        if label == active:
            parts += [rect(13, y - 25, 201, 39, "#334E70", 8),
                      rect(13, y - 25, 3, 39, "#87B5E5", 2)]
        parts.append(text(42, y, label, 13, "#FFFFFF" if label == active else "#B8C6D7", 400))
    parts += [
        rect(228, 0, 1212, 76, "#FFFFFF"),
        text(264, 34, "School workspace", 12, "#64758B"),
        text(264, 55, "Administration  /  Academic year", 10, "#98A3B1"),
        rect(1222, 19, 183, 38, "#EDF2F8", 19),
        text(1242, 43, "DEMO DATA", 10, "#48688D", 700, 'letter-spacing="1"'),
        text(265, 126, title, 28, "#243A55", 700),
        text(265, 151, "School management concept  ·  Sample interface", 12, "#76869A"),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(72, 739, "STUDENT INFORMATION  ·  ATTENDANCE  ·  ACADEMIC PROGRESS", 9, "#8795A5", 600, 'letter-spacing="1"'),
        text(1368, 739, f"SCHOOL DESK  /  0{index}", 10, "#8795A5", 700, 'text-anchor="end" letter-spacing="1"'),
    ]

    def card(x, y, w, h, heading):
        parts.extend([rect(x, y, w, h, "#FFFFFF", 12, 'stroke="#E5EAF0" stroke-width="1"'),
                      text(x + 20, y + 28, heading, 11, "#7C8BA0", 600)])

    if index == 1:
        for i, (label, value, detail, color) in enumerate([
            ("ENROLLED STUDENTS", "842", "Across all classes", "#5B88B6"),
            ("ATTENDANCE TODAY", "94%", "Sample overview", "#5A9B82"),
            ("CLASSES", "24", "Academic year", "#8A78B9"),
            ("REPORTS READY", "18", "Term summaries", "#C18B59"),
        ]):
            x = 265 + i * 280
            card(x, 182, 260, 105, label)
            parts += [text(x + 20, 236, value, 26, "#263D59", 700),
                      text(x + 20, 270, detail, 10, color, 600)]
        card(265, 308, 689, 357, "ATTENDANCE OVERVIEW  /  SAMPLE DATA")
        for i, h in enumerate([99, 137, 108, 166, 148, 193, 172, 212, 190, 237, 205, 225]):
            x = 300 + i * 48
            parts.append(rect(x, 601 - h, 23, h, "#8FB5DA" if i > 7 else "#D2E0EF", 5))
            parts.append(text(x + 11, 626, ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"][i], 9, "#95A1AF", 400, 'text-anchor="middle"'))
        card(974, 308, 394, 357, "RECENT SCHOOL ACTIVITY")
        for i, (name, detail) in enumerate([
            ("Class 8 attendance", "Register updated · 10:24"),
            ("Term assessment", "Scores entered · Yesterday"),
            ("Student records", "4 profile updates · Yesterday"),
            ("Parent meeting", "Schedule shared · 2 days ago"),
        ]):
            y = 377 + i * 62
            parts += [rect(996, y - 18, 34, 34, ["#E1ECF7", "#E6F1EB", "#EEE8F6", "#F5EBDD"][i], 10),
                      text(1013, y + 4, ["A", "T", "S", "P"][i], 12, "#4C729A", 700, 'text-anchor="middle"'),
                      text(1044, y - 1, name, 12, "#344B67", 600),
                      text(1044, y + 19, detail, 9, "#8996A5")]
    elif index == 2:
        card(265, 181, 1103, 484, "STUDENT DIRECTORY  /  SAMPLE RECORDS")
        parts += [text(291, 244, "STUDENT", 9, "#8A96A4", 700, 'letter-spacing="1"'),
                  text(710, 244, "CLASS", 9, "#8A96A4", 700, 'letter-spacing="1"'),
                  text(887, 244, "GUARDIAN CONTACT", 9, "#8A96A4", 700, 'letter-spacing="1"'),
                  text(1190, 244, "STATUS", 9, "#8A96A4", 700, 'letter-spacing="1"')]
        for i, (name, code, clas, contact, status) in enumerate([
            ("Chisomo Banda", "ST-2041", "Form 2A", "+265 99X XXX 101", "Active"),
            ("Thoko Phiri", "ST-2042", "Form 1B", "+265 88X XXX 202", "Active"),
            ("Tapiwa Mbewe", "ST-2043", "Form 3A", "+265 99X XXX 303", "Active"),
            ("Lindiwe Nkhoma", "ST-2044", "Form 2B", "+265 88X XXX 404", "Review"),
            ("Yamikani Zulu", "ST-2045", "Form 4A", "+265 99X XXX 505", "Active"),
        ]):
            y = 300 + i * 66
            parts += [rect(286, y + 16, 1058, 1, "#EDF0F4"),
                      rect(292, y - 12, 35, 35, ["#E1ECF7", "#E6F1EB", "#EEE8F6", "#F5EBDD", "#E2ECF4"][i], 12),
                      text(309, y + 11, name[0], 12, "#4C729A", 700, 'text-anchor="middle"'),
                      text(340, y + 1, name, 12, "#364B65", 600),
                      text(340, y + 20, code, 9, "#8A96A4"),
                      text(710, y + 8, clas, 11, "#52647A"),
                      text(887, y + 8, contact, 11, "#52647A"),
                      rect(1183, y - 6, 82, 24, "#E8F2EB", 12),
                      text(1224, y + 10, status, 9, "#4C8064", 600, 'text-anchor="middle"')]
    elif index == 3:
        card(265, 181, 700, 484, "WEEKLY ATTENDANCE  /  ILLUSTRATIVE")
        parts += [text(292, 251, "Attendance by class", 15, "#364B65", 700)]
        for i, (label, value) in enumerate([("Form 1", 88), ("Form 2", 94), ("Form 3", 79), ("Form 4", 91), ("Form 5", 85)]):
            y = 309 + i * 64
            parts += [text(294, y, label, 12, "#52647A", 600),
                      rect(400, y - 12, 439, 13, "#EDF1F5", 7),
                      rect(400, y - 12, int(value * 4.1), 13, "#78A98F", 7),
                      text(873, y, f"{value}%", 11, "#527C67", 700, 'text-anchor="end"')]
        card(987, 181, 381, 211, "REGISTER STATUS")
        parts += [text(1010, 266, "18", 35, "#2B4563", 700),
                  text(1053, 266, "of 24 classes submitted", 11, "#718197"),
                  rect(1010, 298, 327, 9, "#ECF0F5", 5),
                  rect(1010, 298, 245, 9, "#78A98F", 5),
                  text(1010, 338, "6 registers still to review", 10, "#8592A1")]
        card(987, 411, 381, 254, "RECENT REGISTER UPDATES")
        for i, (name, time) in enumerate([("Form 2A", "Today · 10:24"), ("Form 1B", "Today · 09:51"), ("Form 3A", "Yesterday")]):
            y = 478 + i * 52
            parts += [text(1011, y, name, 12, "#3F536B", 600),
                      text(1338, y, time, 10, "#8995A3", 400, 'text-anchor="end"')]
    else:
        card(265, 181, 705, 484, "ACADEMIC PROGRESS  /  SAMPLE DATA")
        for i, (subject, value) in enumerate([("Mathematics", 74), ("English", 81), ("Science", 68), ("Social studies", 77), ("Chichewa", 85)]):
            y = 270 + i * 69
            parts += [text(294, y, subject, 12, "#52647A", 600),
                      rect(430, y - 12, 430, 14, "#EDF1F5", 7),
                      rect(430, y - 12, int(value * 4.1), 14, "#779FC7", 7),
                      text(884, y, f"{value}%", 11, "#486B91", 700, 'text-anchor="end"')]
        card(991, 181, 377, 222, "TERM SUMMARY")
        parts += [text(1016, 268, "76%", 37, "#2B4563", 700),
                  text(1123, 265, "sample cohort average", 10, "#76869A"),
                  text(1016, 325, "Assessment period", 10, "#8995A3"),
                  text(1016, 347, "Term 2  ·  Illustrative data", 12, "#52647A", 600)]
        card(991, 422, 377, 243, "PROGRESS TREND")
        for i, h in enumerate([61, 93, 82, 117, 101, 140, 123, 166, 149]):
            parts.append(rect(1020 + i * 35, 624 - h, 19, h, "#82A9CE" if i > 5 else "#D3E1EF", 4))

    return svg_doc(parts)


def dzikolens_art(index):
    pages = [
        ("Malawi, seen in new ways.", "A conceptual view of environmental change across the landscape."),
        ("Follow the growing season.", "Illustrative vegetation trends for agricultural monitoring."),
        ("Keep an eye on forest change.", "Explore forest cover patterns over time with satellite imagery."),
        ("See fire signals sooner.", "A conceptual view of fire monitoring and changing conditions."),
        ("Prepare for water extremes.", "Explore rainfall, flood and drought indicators together."),
    ]
    title, subtitle = pages[index - 1]
    green = "#376C52"
    mint = "#B9D7B5"
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F2F5EF"),
        rect(0, 0, WIDTH, 76, "#FFFFFF"),
        text(68, 49, "dzikolens", 22, "#1F3D2D", 700, 'letter-spacing="1"'),
        text(231, 49, "EARTH OBSERVATION  /  MALAWI", 9, "#748776", 700, 'letter-spacing="1"'),
        text(939, 47, "OVERVIEW     AGRICULTURE     FORESTS     HAZARDS", 10, "#66776B", 600, 'letter-spacing="1"'),
        rect(0, 76, WIDTH, 40, "#E2EBDD"),
        text(69, 101, "UPCOMING PROJECT  ·  CONCEPTUAL MONITORING VIEW  ·  NO LIVE DATA", 9, "#507054", 700, 'letter-spacing="1"'),
        text(69, 161, "DZIKOLENS  /  ENVIRONMENTAL INTELLIGENCE", 10, green, 700, 'letter-spacing="2"'),
        text(69, 207, title, 34, "#22392B", 700, 'letter-spacing="-1"'),
        text(71, 233, subtitle, 12, "#78877A"),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(70, 739, "FREE SATELLITE IMAGERY  ·  AI  ·  ENVIRONMENTAL DATA", 9, "#7E8C7F", 600, 'letter-spacing="1"'),
        text(1370, 739, f"DZIKOLENS  /  0{index}", 10, "#7E8C7F", 700, 'text-anchor="end" letter-spacing="1"'),
    ]

    def panel(x, y, w, h, label):
        parts.extend([rect(x, y, w, h, "#FFFFFF", 12, 'stroke="#E2E8DF" stroke-width="1"'),
                      text(x + 18, y + 27, label, 10, "#758575", 700, 'letter-spacing="1"')])

    if index == 1:
        for i, (label, value, tint) in enumerate([
            ("AGRICULTURE", "Crop conditions", "#D7E9CA"),
            ("FORESTS", "Cover change", "#A9C6A0"),
            ("FIRE", "Thermal signals", "#F0D8B8"),
            ("WATER", "Flood & drought", "#C8DDE2"),
        ]):
            x = 70 + i * 337
            panel(x, 264, 315, 88, label)
            parts += [text(x + 18, 328, value, 16, "#344735", 600),
                      rect(x + 255, 292, 37, 37, tint, 13),
                      text(x + 273, 316, ["A", "F", "!", "W"][i], 12, green, 700, 'text-anchor="middle"')]
        panel(70, 374, 767, 300, "MALAWI  /  ILLUSTRATIVE LANDSCAPE LAYERS")
        parts += [rect(94, 420, 719, 213, "#E7EEE2", 8),
                  '<path d="M398 430 L451 439 L472 459 L495 465 L506 486 L487 506 L492 524 L472 538 L480 556 L452 579 L439 606 L418 610 L404 591 L398 566 L381 552 L375 531 L385 515 L377 496 L386 478 L382 458 Z" fill="#7B9D75" stroke="#FFFFFF" stroke-width="5"/>',
                  '<path d="M405 455 L433 448 L453 460 L449 480 L422 486 L397 478 Z" fill="#B6CF8D"/>',
                  '<path d="M405 495 L438 487 L470 502 L459 526 L426 535 L391 518 Z" fill="#95B77D"/>',
                  '<path d="M416 543 L455 533 L473 550 L449 577 L424 583 L405 563 Z" fill="#C5D79C"/>',
                  '<path d="M424 474 C449 489 425 507 448 521 C466 536 437 555 457 570" fill="none" stroke="#6DA6B3" stroke-width="4" opacity=".8"/>',
                  '<circle cx="447" cy="477" r="6" fill="#C38B4A"/><circle cx="425" cy="535" r="6" fill="#7BAA67"/><circle cx="456" cy="563" r="6" fill="#739DB0"/>',
                  text(120, 454, "SATELLITE LAYER PREVIEW", 9, "#7D897A", 700, 'letter-spacing="1"'),
                  text(510, 482, "AGRICULTURE", 9, "#537451", 700, 'letter-spacing="1"'),
                  text(510, 546, "FOREST COVER", 9, "#537451", 700, 'letter-spacing="1"'),
                  text(510, 597, "WATER SIGNALS", 9, "#537451", 700, 'letter-spacing="1"')]
        panel(858, 374, 512, 300, "ENVIRONMENTAL INDICATORS  /  CONCEPT")
        for i, (label, color, heights) in enumerate([
            ("VEGETATION INDEX", "#79A56A", [34, 51, 42, 63, 53, 78, 70, 94, 80]),
            ("RAINFALL SIGNAL", "#719DA7", [69, 50, 82, 61, 92, 75, 101, 84, 112]),
        ]):
            y = 451 + i * 110
            parts.append(text(883, y, label, 9, "#728172", 700, 'letter-spacing="1"'))
            for j, height in enumerate(heights):
                parts.append(rect(883 + j * 47, y + 66 - height / 2, 23, height / 2, color if j > 5 else "#D7E5D2", 4))
    elif index == 2:
        panel(70, 264, 801, 397, "AGRICULTURE MONITORING  /  CONCEPTUAL LAYER")
        parts += [rect(94, 308, 753, 312, "#E8EFE0", 8)]
        for i in range(7):
            for j in range(5):
                colors = ["#9BB97E", "#BED29A", "#7EAA71", "#D2D9A6", "#A9C88A"]
                parts.append(rect(121 + i * 99, 336 + j * 49, 80, 34, colors[(i * 3 + j * 2 + index) % len(colors)], 7))
        parts += [text(119, 345, "VEGETATION INDEX", 9, "#F7FAF4", 700, 'letter-spacing="1"'),
                  text(119, 603, "Illustrative field and crop-health layer · No live readings", 9, "#758575")]
        panel(892, 264, 478, 180, "SEASONAL VEGETATION TREND  /  ILLUSTRATIVE")
        for i, height in enumerate([26, 35, 41, 52, 48, 62, 70, 81, 77, 93, 102]):
            x = 920 + i * 37
            parts.append(rect(x, 406 - height, 20, height, "#7EA76B" if i > 6 else "#D5E4CE", 4))
        panel(892, 463, 478, 198, "POTENTIAL SIGNALS")
        for i, label in enumerate(["Crop growth patterns", "Seasonal change", "Areas for field review"]):
            y = 526 + i * 39
            parts += [rect(916, y - 12, 9, 9, ["#86A967", "#C4A267", "#7E9FAD"][i], 4),
                      text(938, y - 3, label, 11, "#4C5F4D")]
    elif index == 3:
        panel(70, 264, 801, 397, "FOREST COVER CHANGE  /  CONCEPTUAL COMPARISON")
        parts += [rect(94, 308, 753, 312, "#E9EEE6", 8)]
        for i in range(10):
            for j in range(5):
                x, y = 119 + i * 68, 337 + j * 48
                size = 10 + ((i * 7 + j * 5 + index) % 12)
                tone = ["#456D4E", "#6C925C", "#8EAD74", "#B6C999"][(i * 3 + j * 2) % 4]
                parts.append(f'<circle cx="{x}" cy="{y}" r="{size}" fill="{tone}" opacity=".88"/>')
        parts += [rect(578, 333, 244, 44, "#FFFFFF", 9, 'opacity=".92"'),
                  text(596, 360, "TREE-COVER LAYER  /  PREVIEW", 9, "#476549", 700, 'letter-spacing="1"'),
                  text(119, 602, "Illustrative forest mosaic for comparing imagery over time", 9, "#758575")]
        panel(892, 264, 478, 180, "CHANGE DETECTION  /  CONCEPT")
        parts += [text(920, 342, "Compare", 24, "#344735", 700),
                  text(1024, 342, "two periods", 15, "#647564"),
                  text(920, 382, "Surface change signals for review", 10, "#758575"),
                  rect(920, 404, 183, 6, "#DDE8D8", 3),
                  rect(920, 404, 113, 6, "#6C965B", 3)]
        panel(892, 463, 478, 198, "POTENTIAL FOREST INDICATORS")
        for i, label in enumerate(["Canopy change", "New clearing signals", "Regrowth patterns"]):
            y = 526 + i * 39
            parts += [rect(916, y - 12, 9, 9, ["#52794C", "#C08C4D", "#88A971"][i], 4),
                      text(938, y - 3, label, 11, "#4C5F4D")]
    elif index == 4:
        panel(70, 264, 801, 397, "FIRE MONITORING  /  CONCEPTUAL SIGNALS")
        parts += [rect(94, 308, 753, 312, "#ECEDE3", 8),
                  '<path d="M175 500 C213 433 268 447 305 397 C356 464 407 419 451 464 C501 400 566 434 603 390 C649 444 705 418 769 468 L803 620 L119 620 Z" fill="#AEBF8C"/>',
                  '<path d="M174 551 C257 511 297 545 368 502 C442 467 505 521 573 489 C652 463 709 510 803 477" fill="none" stroke="#668C5E" stroke-width="10" opacity=".8"/>',
                  '<circle cx="302" cy="414" r="13" fill="#D8794E"/><circle cx="604" cy="411" r="13" fill="#DB9856"/>',
                  '<circle cx="302" cy="414" r="24" fill="none" stroke="#D8794E" stroke-width="2" opacity=".55"/>',
                  '<circle cx="604" cy="411" r="24" fill="none" stroke="#DB9856" stroke-width="2" opacity=".55"/>',
                  text(119, 345, "THERMAL SIGNAL LAYER  /  ILLUSTRATIVE", 9, "#758575", 700, 'letter-spacing="1"'),
                  text(119, 600, "Concept illustration · Not a live alert or mapped incident", 9, "#758575")]
        panel(892, 264, 478, 180, "POTENTIAL FIRE-WEATHER INPUTS")
        for i, (label, value) in enumerate([("Temperature", "Satellite-derived"), ("Vegetation dryness", "Environmental data"), ("Thermal anomaly", "AI-assisted review")]):
            y = 325 + i * 38
            parts += [text(920, y, label, 11, "#4C5F4D", 600),
                      text(1339, y, value, 9, "#758575", 400, 'text-anchor="end"')]
        panel(892, 463, 478, 198, "EARLY AWARENESS WORKFLOW")
        parts += [text(920, 529, "Satellite imagery", 11, "#4C5F4D", 600),
                  text(1059, 529, "→", 13, "#789078", 600),
                  text(1081, 529, "Change signal", 11, "#4C5F4D", 600),
                  text(920, 565, "Environmental context", 11, "#4C5F4D", 600),
                  text(1085, 565, "→", 13, "#789078", 600),
                  text(1107, 565, "Human review", 11, "#4C5F4D", 600),
                  text(920, 619, "Designed to support monitoring, not replace emergency services.", 9, "#758575")]
    else:
        panel(70, 264, 801, 397, "WATER EXTREMES  /  CONCEPTUAL OVERVIEW")
        parts += [rect(94, 308, 753, 312, "#E8EFEB", 8),
                  '<path d="M94 483 C173 457 228 464 283 481 C354 505 407 491 476 472 C544 454 602 460 661 482 C724 504 782 489 847 467 L847 620 L94 620 Z" fill="#B6D7D8"/>',
                  '<path d="M94 529 C172 510 222 519 293 533 C358 548 418 534 480 513 C548 490 614 505 672 527 C733 550 783 533 847 513" fill="none" stroke="#729DA5" stroke-width="3"/>',
                  '<path d="M94 568 C163 552 221 556 286 571 C358 587 429 566 491 548 C556 529 611 538 674 562 C735 585 795 564 847 548" fill="none" stroke="#8CB0B2" stroke-width="2"/>',
                  text(119, 345, "RAIN / FLOOD / DROUGHT LAYERS", 9, "#5C7F7E", 700, 'letter-spacing="1"'),
                  text(119, 602, "Illustrative hydrology and rainfall signals · No live readings", 9, "#758575")]
        panel(892, 264, 478, 180, "ENVIRONMENTAL DATA INPUTS")
        for i, (label, color) in enumerate([("Rainfall patterns", "#6D9AA3"), ("Surface-water change", "#82B2B4"), ("Soil moisture", "#96A974")]):
            y = 325 + i * 39
            parts += [rect(920, y - 10, 10, 10, color, 4),
                      text(941, y, label, 11, "#4C5F4D")]
        panel(892, 463, 478, 198, "POTENTIAL MONITORING FOCUS")
        for i, label in enumerate(["Flood extent and change", "Dry-season conditions", "Areas to investigate"]):
            y = 526 + i * 39
            parts += [rect(916, y - 12, 9, 9, ["#729DA5", "#C4A267", "#7E9FAD"][i], 4),
                      text(938, y - 3, label, 11, "#4C5F4D")]
    return svg_doc(parts)


def job_monitor_art(index):
    titles = [
        "ICT opportunities, in one place.",
        "Monitor. Filter. Find relevant roles.",
        "Get notified when a match appears.",
    ]
    parts = [
        rect(0, 0, WIDTH, HEIGHT, "#F3F5F8"),
        rect(0, 0, 228, HEIGHT, "#203653"),
        text(32, 48, "ROLE", 18, "#FFFFFF", 700, 'letter-spacing="2"'),
        text(32, 70, "RADAR", 10, "#AAC7E5", 700, 'letter-spacing="3"'),
        rect(28, 99, 170, 1, "#3D5673"),
    ]
    menu = ["Overview", "Job listings", "Saved filters", "Notifications"]
    active = menu[index - 1]
    for i, label in enumerate(menu):
        y = 145 + i * 49
        if label == active:
            parts += [rect(13, y - 25, 201, 39, "#334E70", 8),
                      rect(13, y - 25, 3, 39, "#87B5E5", 2)]
        parts.append(text(42, y, label, 13, "#FFFFFF" if label == active else "#B8C6D7", 400))
    parts += [
        rect(228, 0, 1212, 76, "#FFFFFF"),
        text(264, 34, "ICT vacancy monitor", 12, "#64758B"),
        text(264, 55, "Malawi  /  Automated job discovery", 10, "#98A3B1"),
        rect(1220, 19, 185, 38, "#EDF2F8", 19),
        text(1240, 43, "ILLUSTRATIVE UI", 9, "#48688D", 700, 'letter-spacing="1"'),
        text(265, 126, titles[index - 1], 28, "#243A55", 700),
        text(265, 151, "Concept visuals based on the CV project description · Sample listings only", 11, "#76869A"),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(72, 739, "WEBSITE MONITORING  ·  VACANCY FILTERING  ·  NOTIFICATIONS", 9, "#8795A5", 600, 'letter-spacing="1"'),
        text(1368, 739, f"ICT VACANCY MONITOR  /  0{index}", 9, "#8795A5", 700, 'text-anchor="end" letter-spacing="1"'),
    ]

    def card(x, y, w, h, heading):
        parts.extend([rect(x, y, w, h, "#FFFFFF", 12, 'stroke="#E5EAF0" stroke-width="1"'),
                      text(x + 20, y + 28, heading, 10, "#7C8BA0", 700, 'letter-spacing="1"')])

    if index == 1:
        card(265, 181, 250, 100, "SOURCES MONITORED")
        parts += [text(287, 246, "Job websites", 22, "#2B4563", 700),
                  text(287, 269, "Automated checks", 10, "#7B8C9E")]
        card(531, 181, 250, 100, "FILTER")
        parts += [text(553, 246, "ICT roles", 22, "#2B4563", 700),
                  text(553, 269, "Relevant listings", 10, "#7B8C9E")]
        card(797, 181, 250, 100, "MATCHING")
        parts += [text(819, 246, "Review", 22, "#2B4563", 700),
                  text(819, 269, "Matches for review", 10, "#7B8C9E")]
        card(1063, 181, 305, 100, "DELIVERY")
        parts += [text(1085, 246, "Notifications", 22, "#2B4563", 700),
                  text(1085, 269, "When relevant vacancies appear", 9, "#7B8C9E")]
        card(265, 302, 700, 363, "RECENTLY DETECTED  /  SAMPLE LISTINGS")
        for i, (title, category, source) in enumerate([
            ("ICT Support Officer", "Technical support", "Example source listing"),
            ("Database Assistant", "Databases & information systems", "Example source listing"),
            ("Network Technician", "Networking", "Example source listing"),
            ("Web Developer", "Software development", "Example source listing"),
        ]):
            y = 367 + i * 67
            parts += [rect(285, y + 17, 657, 1, "#EDF0F4"),
                      rect(292, y - 11, 34, 34, ["#E1ECF7", "#E6F1EB", "#EEE8F6", "#F5EBDD"][i], 11),
                      text(309, y + 12, ["I", "D", "N", "W"][i], 12, "#4C729A", 700, 'text-anchor="middle"'),
                      text(340, y, title, 12, "#364B65", 600),
                      text(340, y + 20, category, 10, "#8290A0"),
                      text(740, y + 6, source, 9, "#8996A5", 400, 'text-anchor="end"')]
        card(985, 302, 383, 363, "MONITORING WORKFLOW")
        for i, (label, detail) in enumerate([
            ("Scan", "Check selected job websites"),
            ("Extract", "Collect vacancy information"),
            ("Filter", "Identify relevant ICT roles"),
            ("Notify", "Send an alert for a match"),
        ]):
            y = 370 + i * 67
            parts += [rect(1008, y - 18, 33, 33, "#E4EDF6", 11),
                      text(1024, y + 4, f"0{i+1}", 10, "#4C729A", 700, 'text-anchor="middle"'),
                      text(1056, y - 1, label, 12, "#364B65", 600),
                      text(1056, y + 20, detail, 9, "#8290A0")]
    elif index == 2:
        card(265, 181, 730, 484, "SAVED ICT VACANCY FILTER")
        parts += [text(294, 250, "Role keywords", 10, "#8491A0", 700, 'letter-spacing="1"'),
                  rect(292, 263, 666, 46, "#FAFBFC", 8, 'stroke="#E4EAF0" stroke-width="1"'),
                  text(310, 292, "ICT · software · database · network", 12, "#52647A"),
                  text(294, 351, "Listing criteria", 10, "#8491A0", 700, 'letter-spacing="1"')]
        for i, (label, chosen) in enumerate([
            ("Search vacancy titles and descriptions", True),
            ("Include software and database roles", True),
            ("Review source links for each match", True),
            ("Send a notification for relevant listings", False),
        ]):
            y = 391 + i * 53
            parts += [rect(294, y - 13, 17, 17, "#5C8F72" if chosen else "#FFFFFF", 4,
                          'stroke="#AAB8C8" stroke-width="1"'),
                      text(302, y, "✓" if chosen else "", 11, "#FFFFFF", 700, 'text-anchor="middle"'),
                      text(328, y, label, 11, "#4A5F75")]
        parts += [rect(294, 596, 177, 42, "#416D8E", 21),
                  text(382, 622, "Save filter", 11, "#FFFFFF", 700, 'text-anchor="middle"')]
        card(1015, 181, 353, 484, "HOW MATCHING WORKS")
        for i, (label, detail) in enumerate([
            ("01  Scan", "Check public job pages"),
            ("02  Extract", "Collect listing details"),
            ("03  Match", "Filter for ICT vacancies"),
            ("04  Alert", "Notify when relevant"),
        ]):
            y = 270 + i * 83
            parts += [text(1040, y, label, 13, "#364B65", 700),
                      text(1040, y + 23, detail, 10, "#8290A0")]
            if i < 3:
                parts.append(rect(1041, y + 39, 1, 25, "#D7E0E9"))
        parts.append(text(1040, 620, "Illustrative workflow", 9, "#8996A5"))
    else:
        card(265, 181, 695, 484, "NOTIFICATION PREVIEW  /  SAMPLE")
        parts += [rect(292, 239, 640, 365, "#F7F9FB", 12),
                  rect(292, 239, 640, 62, "#E8EEF5", 12),
                  text(318, 276, "NEW ICT VACANCY MATCH", 10, "#4C729A", 700, 'letter-spacing="1"'),
                  rect(318, 325, 586, 100, "#FFFFFF", 10, 'stroke="#E5EAF0" stroke-width="1"'),
                  text(341, 357, "Sample ICT vacancy", 15, "#364B65", 700),
                  text(341, 383, "Matched from a monitored Malawi job website", 10, "#8290A0"),
                  text(341, 407, "Example listing — not a current vacancy", 9, "#9AA5B2"),
                  rect(318, 448, 586, 1, "#E4EAF0"),
                  text(318, 480, "The monitor can send a notification when a relevant", 11, "#52647A"),
                  text(318, 502, "ICT opportunity is identified.", 11, "#52647A"),
                  rect(318, 537, 168, 40, "#416D8E", 20),
                  text(402, 562, "Review source listing", 10, "#FFFFFF", 700, 'text-anchor="middle"')]
        card(982, 181, 386, 484, "NOTIFICATION SETTINGS")
        parts += [text(1008, 252, "Delivery preference", 10, "#8491A0", 700, 'letter-spacing="1"'),
                  rect(1007, 268, 333, 52, "#F7F9FB", 9),
                  text(1024, 300, "Email notification", 12, "#52647A", 600),
                  rect(1292, 284, 31, 18, "#6B9D7C", 9),
                  '<circle cx="1312" cy="293" r="7" fill="#FFFFFF"/>',
                  text(1008, 363, "MATCH RELEVANCE", 9, "#8491A0", 700, 'letter-spacing="1"'),
                  text(1008, 397, "ICT roles only", 14, "#364B65", 600),
                  rect(1008, 415, 322, 1, "#E4EAF0"),
                  text(1008, 457, "SOURCE LINK", 9, "#8491A0", 700, 'letter-spacing="1"'),
                  text(1008, 486, "Always review the original", 11, "#52647A"),
                  text(1008, 507, "listing before applying.", 11, "#52647A"),
                  rect(1008, 545, 322, 60, "#EDF2F7", 10),
                  text(1024, 570, "Illustrative interface", 10, "#4C729A", 700),
                  text(1024, 588, "Sample content, not live vacancies", 9, "#8290A0")]
    return svg_doc(parts)


def mlimisense_art(index):
    scenes = [
        ("A clearer view of your field.", "Local crop guidance, designed around the farmer."),
        ("Start with what you can see.", "A photo can begin a check — not replace an expert."),
        ("Advice that speaks your language.", "Practical next steps in English and Chichewa."),
        ("Bring farmers and experts together.", "Keep field notes and prepare a question for an extension officer."),
    ]
    title, subtitle = scenes[index - 1]
    green = "#285D45"
    ink = "#253B30"
    muted = "#748276"
    canvas = "#F2F5EF"
    card_fill = "#FFFFFF"
    line = "#E3EAE1"
    parts = [
        rect(0, 0, WIDTH, HEIGHT, canvas),
        rect(0, 0, 228, HEIGHT, "#214B39"),
        text(31, 47, "MLIMI", 18, "#FFFFFF", 700, 'letter-spacing="2"'),
        text(31, 69, "SENSE  /  AI", 10, "#B8D7B3", 700, 'letter-spacing="2"'),
        rect(28, 94, 172, 1, "#3A654D"),
    ]
    menu = ["My farm", "Check a crop", "Local advice", "Field notes"]
    active = menu[index - 1]
    for i, label in enumerate(menu):
        y = 143 + i * 48
        if label == active:
            parts += [
                rect(13, y - 25, 201, 38, "#35644A", 8),
                rect(13, y - 25, 3, 38, "#C2DD83", 2),
            ]
        parts.append(text(42, y, label, 13, "#FFFFFF" if label == active else "#BCD0C0", 400))
    parts += [
        rect(22, 659, 184, 75, "#2B5740", 10),
        text(38, 685, "WORKS OFFLINE", 9, "#D5E4B9", 700, 'letter-spacing="1"'),
        text(38, 706, "Sync when connected", 10, "#FFFFFF"),
        rect(228, 0, 1212, 74, "#FFFFFF"),
        text(263, 32, "MlimiSense  /  Farm workspace", 12, "#617267", 600),
        text(263, 53, "DEMO EXPERIENCE  ·  SAMPLE FARM INFORMATION", 9, "#96A197", 600, 'letter-spacing=".8"'),
        rect(1200, 18, 174, 38, "#EEF4EA", 18),
        text(1287, 42, "CHICHEWA  /  EN", 9, green, 700, 'text-anchor="middle" letter-spacing="1"'),
        text(265, 120, title, 28, ink, 700),
        text(265, 147, subtitle, 12, muted),
        rect(0, 706, WIDTH, 54, "#FFFFFF"),
        text(70, 739, "AI-ASSISTED CROP CHECKS  ·  LOCAL GUIDANCE  ·  HUMAN REVIEW", 9, "#819083", 600, 'letter-spacing=".6"'),
        text(1368, 739, f"MLIMISENSE  /  0{index}", 9, "#819083", 700, 'text-anchor="end" letter-spacing="1"'),
    ]

    def card(x, y, w, h, heading):
        parts.extend([
            rect(x, y, w, h, card_fill, 12, f'stroke="{line}" stroke-width="1"'),
            text(x + 18, y + 26, heading, 10, muted, 700, 'letter-spacing=".7"'),
        ])

    if index == 1:
        for i, (heading, value, detail) in enumerate([
            ("CURRENT CROP", "Maize", "Rain-fed · Demo field"),
            ("FIELD CHECKS", "03", "Saved for review"),
            ("LOCAL OUTLOOK", "Mixed", "Illustrative forecast"),
            ("NEXT STEP", "Scout", "Walk the field"),
        ]):
            x = 265 + i * 278
            card(x, 177, 260, 100, heading)
            parts += [
                text(x + 18, 230, value, 23, ink, 700),
                text(x + 18, 257, detail, 10, muted),
            ]
        card(265, 298, 703, 366, "FIELD NOTES  /  LAST 6 WEEKS")
        parts += [
            text(287, 357, "Maize field · Central Region", 14, ink, 600),
            text(287, 380, "Example observations saved by the farmer", 10, muted),
            rect(288, 583, 656, 1, "#E9EEE7"),
        ]
        for i, height in enumerate([77, 116, 94, 145, 128, 174, 152, 203, 184, 228, 202, 244]):
            x = 308 + i * 51
            parts.append(rect(x, 578 - height / 2, 24, height / 2, "#8DAE7C" if i > 8 else "#D1DFCA", 5))
            parts.append(text(x + 12, 615, ["W1", "W2", "W3", "W4"][i % 4], 8, "#94A096", 400, 'text-anchor="middle"'))
        card(986, 298, 382, 168, "A USEFUL FIRST STEP")
        parts += [
            rect(1006, 344, 38, 38, "#EFF5E9", 12),
            text(1025, 369, "↗", 15, green, 700, 'text-anchor="middle"'),
            text(1058, 358, "Walk the field", 14, ink, 600),
            text(1058, 380, "Look for patterns across several plants.", 9, muted),
            rect(1007, 407, 340, 1, line),
            text(1007, 437, "AI suggestions are starting points, not diagnoses.", 9, "#788778"),
        ]
        card(986, 484, 382, 180, "QUICK ACTIONS")
        for i, (label, detail) in enumerate([
            ("Check a crop", "Add a photo and a few details"),
            ("Ask for guidance", "Read advice in your language"),
            ("Save a field note", "Keep a record to discuss"),
        ]):
            y = 528 + i * 42
            parts += [
                rect(1007, y - 14, 8, 8, ["#7FA06F", "#C39A53", "#829EAD"][i], 4),
                text(1028, y - 5, label, 11, ink, 600),
                text(1028, y + 12, detail, 9, muted),
            ]
    elif index == 2:
        card(265, 177, 508, 478, "CROP PHOTO  /  SAMPLE IMAGE")
        card(793, 177, 575, 478, "AI-ASSISTED FIELD CHECK  /  ILLUSTRATIVE")
        parts += [
            rect(284, 218, 470, 302, "#EAF0E4", 12),
            rect(305, 241, 428, 258, "#DCE8D2", 10),
        ]
        for i in range(5):
            x = 365 + i * 72
            parts += [
                f'<path d="M {x} 473 Q {x - 17} 377 {x + 1} 278" fill="none" stroke="#688A56" stroke-width="7" stroke-linecap="round"/>',
                f'<path d="M {x} 375 Q {x - 52} 326 {x - 38} 301 Q {x - 4} 309 {x} 375" fill="#91AD73"/>',
                f'<path d="M {x} 346 Q {x + 43} 301 {x + 62} 314 Q {x + 50} 348 {x} 346" fill="#A4BC82"/>',
            ]
        parts += [
            rect(305, 241, 428, 258, "none", 10, 'stroke="#FFFFFF" stroke-width="2" stroke-dasharray="8 8"'),
            text(305, 552, "Crop and region entered by farmer", 11, "#536A54"),
            text(305, 575, "Photo-based suggestions need local context and human review.", 9, muted),
            rect(305, 598, 166, 35, "#2C6447", 18),
            text(388, 620, "Review suggestion  →", 10, "#FFFFFF", 700, 'text-anchor="middle"'),
            rect(815, 225, 531, 55, "#F4F6EE", 9),
            rect(831, 240, 24, 24, "#E1EBD9", 8),
            text(843, 257, "i", 13, green, 700, 'text-anchor="middle"'),
            text(867, 248, "A starting point — not a confirmed diagnosis.", 11, ink, 600),
            text(867, 265, "Check the field and ask a local agriculture expert.", 9, muted),
            text(815, 321, "POSSIBLE OBSERVATION", 9, muted, 700, 'letter-spacing="1"'),
            text(815, 357, "Leaf condition to inspect", 23, ink, 700),
            text(815, 383, "The image may show a change in leaf colour.", 11, muted),
            rect(815, 410, 531, 1, line),
            text(815, 442, "BEFORE YOU ACT", 9, muted, 700, 'letter-spacing="1"'),
        ]
        for i, label in enumerate([
            "Compare several plants, not just one leaf.",
            "Note recent rain, planting date and field location.",
            "Share the photo with an extension officer for advice.",
        ]):
            y = 478 + i * 43
            parts += [
                rect(817, y - 13, 22, 22, "#EEF4E9", 11),
                text(828, y + 2, f"0{i+1}", 8, green, 700, 'text-anchor="middle"'),
                text(850, y + 2, label, 10, "#48584B"),
            ]
        parts.append(text(815, 625, "No pesticide or treatment recommendation is made.", 9, "#758578", 600))
    elif index == 3:
        card(265, 177, 715, 478, "LOCAL ADVICE  /  EXAMPLE CONTENT")
        card(1000, 177, 368, 478, "HOW GUIDANCE IS PREPARED")
        parts += [
            rect(286, 220, 674, 98, "#E9F1E4", 12),
            text(309, 250, "FIELD SCENARIO", 9, green, 700, 'letter-spacing="1"'),
            text(309, 279, "Maize · Early growth · Rain-fed", 17, ink, 600),
            text(309, 301, "Advice is tailored to the crop stage and farmer's location.", 10, muted),
            rect(286, 339, 324, 218, "#FFFFFF", 12, f'stroke="{line}" stroke-width="1"'),
            rect(626, 339, 334, 218, "#FFFFFF", 12, f'stroke="{line}" stroke-width="1"'),
            text(306, 372, "ENGLISH", 9, green, 700, 'letter-spacing="1"'),
            text(646, 372, "CHICHEWA", 9, green, 700, 'letter-spacing="1"'),
            text(306, 411, "Check the soil", 17, ink, 600),
            text(646, 411, "Yang'anani nthaka", 17, ink, 600),
            text(306, 441, "Look at soil moisture in a few", 11, muted),
            text(306, 461, "places across the field. Keep a", 11, muted),
            text(306, 481, "note of what you find.", 11, muted),
            text(646, 441, "Onani chinyezi cha nthaka", 11, muted),
            text(646, 461, "m'malo osiyanasiyana m'munda.", 11, muted),
            text(646, 481, "Lembani zimene mwaona.", 11, muted),
            text(306, 533, "EXAMPLE GUIDANCE  ·  VERIFY LOCALLY", 8, "#879386", 700, 'letter-spacing=".7"'),
            text(646, 533, "MALANGIZO ACHITSANZO", 8, "#879386", 700, 'letter-spacing=".7"'),
            rect(286, 575, 674, 57, "#F5F6F0", 10),
            text(306, 600, "Save advice for offline reference", 11, ink, 600),
            text(306, 618, "Content should be reviewed by local agriculture specialists.", 9, muted),
        ]
        for i, (heading, detail) in enumerate([
            ("01  Crop & growth stage", "Start with what is being grown."),
            ("02  Local context", "Consider season and district."),
            ("03  Clear next step", "Offer practical checks first."),
            ("04  Expert review", "Escalate when uncertain."),
        ]):
            y = 244 + i * 83
            parts += [
                rect(1021, y - 17, 326, 1, line),
                text(1021, y + 7, heading, 11, ink, 600),
                text(1021, y + 29, detail, 9, muted),
            ]
        parts += [
            rect(1021, 579, 326, 49, "#EFF4EA", 9),
            text(1037, 600, "English  /  Chichewa", 10, green, 700),
            text(1037, 617, "Language options for local access", 8, muted),
        ]
    else:
        card(265, 177, 703, 478, "FIELD JOURNAL  /  DEMO ENTRIES")
        parts += [
            text(288, 233, "Keep useful details together.", 19, ink, 700),
            text(288, 259, "A simple record helps farmers and experts discuss what changed.", 10, muted),
            rect(288, 286, 656, 1, line),
        ]
        for i, (day, heading, detail, tint) in enumerate([
            ("MON 12", "Field walk", "Checked five plants in the east plot.", "#EAF2E5"),
            ("FRI 09", "Rain observed", "Light rainfall after three dry days.", "#EEF2F4"),
            ("TUE 06", "Photo saved", "Leaf photo added for expert review.", "#F4EFE2"),
        ]):
            y = 337 + i * 92
            parts += [
                rect(290, y - 17, 69, 48, tint, 10),
                text(324, y + 11, day, 9, green, 700, 'text-anchor="middle"'),
                text(381, y - 1, heading, 13, ink, 600),
                text(381, y + 22, detail, 10, muted),
                rect(381, y + 42, 563, 1, line),
            ]
        rect(288, 610, 656, 30, "#F2F6EE", 8)
        text(304, 630, "Your notes stay yours — share only when you choose.", 9, green, 600)
        card(986, 177, 382, 478, "PREPARE FOR AN EXPERT")
        parts += [
            rect(1007, 224, 340, 117, "#EDF3E9", 12),
            text(1026, 255, "FIELD SUMMARY", 9, green, 700, 'letter-spacing="1"'),
            text(1026, 284, "Crop: maize  ·  Stage: early growth", 10, ink, 600),
            text(1026, 307, "3 notes saved  ·  1 photo to review", 9, muted),
            text(1007, 382, "QUESTIONS TO DISCUSS", 9, muted, 700, 'letter-spacing="1"'),
            rect(1007, 399, 340, 57, "#FFFFFF", 9, f'stroke="{line}" stroke-width="1"'),
            text(1024, 423, "What should I check next in this field?", 10, ink, 600),
            text(1024, 442, "Edit before sharing", 8, muted),
            rect(1007, 479, 340, 46, "#2C6447", 22),
            text(1177, 508, "Prepare a question  →", 10, "#FFFFFF", 700, 'text-anchor="middle"'),
            text(1007, 557, "Connect with a local extension officer.", 10, ink, 600),
            text(1007, 579, "AI can help organize notes; people guide decisions.", 9, muted),
            text(1007, 623, "FARMER-CONTROLLED  ·  HUMAN-IN-THE-LOOP", 8, green, 700, 'letter-spacing=".4"'),
        ]

    return svg_doc(parts)


def svg_doc(parts):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img">'
        '<title>Illustrative project interface artwork</title>'
        '<desc>Original vector artwork representing a project interface. This is not a product screenshot.</desc>'
        + "".join(parts)
        + "</svg>"
    )


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for index in range(1, 10):
        (OUTPUT / f"civicscore-{index:02}.svg").write_text(
            civic_art(index), encoding="utf-8"
        )
    for index in range(1, 7):
        (OUTPUT / f"mindsafe-{index:02}.svg").write_text(
            mindsafe_art(index), encoding="utf-8"
        )
    for index in range(1, 6):
        (OUTPUT / f"tibhukebus-{index:02}.svg").write_text(
            tibhu_art(index), encoding="utf-8"
        )
    for index in range(1, 5):
        (OUTPUT / f"school-management-{index:02}.svg").write_text(
            school_art(index), encoding="utf-8"
        )
    for index in range(1, 4):
        (OUTPUT / f"job-monitor-{index:02}.svg").write_text(
            job_monitor_art(index), encoding="utf-8"
        )
    for index in range(1, 6):
        (OUTPUT / f"dzikolens-{index:02}.svg").write_text(
            dzikolens_art(index), encoding="utf-8"
        )
    for index in range(1, 5):
        (OUTPUT / f"mlimisense-{index:02}.svg").write_text(
            mlimisense_art(index), encoding="utf-8"
        )
    print(f"Generated 36 vector project illustrations in {OUTPUT}")


if __name__ == "__main__":
    main()
