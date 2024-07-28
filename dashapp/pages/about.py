import dash_bootstrap_components as dbc
from callbacks.api import graduated_api
from components.navbar import Navbar
from components.footer import Footer
from dash import dcc, html

# เตรียมข้อมูล
df = graduated_api()

# สร้าง dropdown options
dropdown_options = [
    {"label": str(schools_province), "value": schools_province}
    for schools_province in df["schools_province"]
]

card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

# กำหนดเลย์เอาท์ของแอป
layout = html.Div(
    children=[
        Navbar(),
        # Dropdown Provinces
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "เกี่ยวกับผู้จัดทำ",
                                style={"color": "white", "marginLeft": "18px"},
                            )
                        ]
                    ),
                    dbc.Container(
                        [
                            dbc.Container(
                                dbc.Row(
                                    [
                                        dbc.Row(
                                            html.Div(
                                                "จตุรวิชญ์ ค่อฉุ้น",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                        dbc.Row(
                                            html.Div(
                                                "นักศึกษาปริญญาตรี วิศวกรรมปัญญาประดิษฐ์",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                        dbc.Row(
                                            html.Div(
                                                "มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตหาดใหญ่",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                    ],
                                    className="mb-4",
                                ),
                            ),
                            html.Br(),
                            dbc.Container(
                                dbc.Row(
                                    [
                                        dbc.Row(
                                            html.A(
                                                "GITHUB - TxChar",
                                                href="https://github.com/TxChar",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        ),
                                        dbc.Row(
                                            html.A(
                                                "GITLAB - TxCharnom",
                                                href="https://gitlab.com/TxCharnom",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        ),
                                        dbc.Row(
                                            html.A(
                                                "LINKED-IN - Jaturawich Khochun",
                                                href="https://www.linkedin.com/in/jaturawich-khochun-923662317/",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        ),
                                    ],
                                    className="mb-4",
                                ),
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                    dbc.Container(
                        [
                            dbc.Container(
                                dbc.Row(
                                    [
                                        dbc.Row(
                                            html.Div(
                                                "พชรวุธ ธนาวุฒิ",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                        dbc.Row(
                                            html.Div(
                                                "นักศึกษาปริญญาตรี วิศวกรรมปัญญาประดิษฐ์",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                        dbc.Row(
                                            html.Div(
                                                "มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตหาดใหญ่",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                    "text-align": "center",
                                                },
                                            ),
                                        ),
                                    ],
                                    className="mb-4",
                                ),
                            ),
                            html.Br(),
                            dbc.Container(
                                dbc.Row(
                                    [
                                        dbc.Row(
                                            html.A(
                                                "GITHUB - babebp",
                                                href="https://github.com/babebp",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        ),
                                        dbc.Row(
                                            html.A(
                                                "MEDIUM - babebp",
                                                href="https://medium.com/@babebp",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        ),
                                        dbc.Row(
                                            html.A(
                                                "LINKEDIN - Pacharawut Thanawut",
                                                href="https://www.linkedin.com/in/babebp/",
                                                style={
                                                    "color": "white",
                                                    "fontSize": "18px",
                                                },
                                                target="_blank",
                                            ),
                                        )
                                    ],
                                    className="mb-4",
                                ),
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#B33939", "border-radius": "18px"},
            ),
        ),
    ]
)
