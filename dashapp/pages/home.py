import dash_bootstrap_components as dbc
from callbacks.api import graduated_api, universities_data
from components.navbar import Navbar
from components.footer import Footer
from dash import dcc, html

# เตรียมข้อมูล
df = universities_data()

# สร้าง dropdown options
dropdown_options = [
    {"label": str(universities), "value": universities}
    for universities in df["มหาวิทยาลัย"].drop_duplicates()
]

majors_dropdown_options = [
    {"label": str(major), "value": major} for major in df["คณะ"].unique()
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
                                "มหาวิทยาลัย",
                                style={"color": "white", "marginLeft": "20px"},
                            )
                        ]
                    ),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    dcc.Dropdown(
                                        id="universities-dropdown",
                                        options=dropdown_options,
                                        placeholder="มหาวิทยาลัย...",
                                        multi=True,
                                        style={
                                            "color": "black",
                                        },
                                    ),
                                    dcc.Dropdown(
                                        id="major-dropdown",
                                        options=majors_dropdown_options,
                                        placeholder="คณะ...",
                                        multi=True,
                                        style={"color": "black", "marginTop": "10px"},
                                    ),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#1A477F", "border-radius": "20px"},
            ),
        ),
        # Display Card
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Card(
                                                    id="first-card",
                                                    style={
                                                        "backgroundColor": "#F3B51B"
                                                    },
                                                    inverse=True,
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Card(
                                                    id="second-card",
                                                    style={
                                                        "backgroundColor": "#E66955"
                                                    },
                                                    inverse=True,
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Card(
                                                    id="third-card",
                                                    style={
                                                        "backgroundColor": "#52A1A9"
                                                    },
                                                    inverse=True,
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Card(
                                                    id="fourth-card",
                                                    style={
                                                        "backgroundColor": "#31719A"
                                                    },
                                                    inverse=True,
                                                )
                                            ),
                                        ],
                                        className="mb-4",
                                    ),
                                ],
                            ),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={
                    "backgroundColor": "#1A477F",
                    "border-radius": "20px",
                    "paddingBottom": 1,
                },
            ),
        ),
        # MAP
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "แผนที่", style={"color": "white", "marginLeft": "20px"}
                            )
                        ]
                    ),
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    # html.Div(id="output-map"),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#024070", "border-radius": "20px"},
            ),
        ),
        # Table
        dbc.Container(
            dbc.Container(
                [
                    html.Hr(),
                    dbc.Col(
                        [
                            html.H4(
                                "ตาราง", style={"color": "white", "marginLeft": "20px"}
                            )
                        ]
                    ),
                    html.Hr(),
                    dbc.Container(
                        [
                            dbc.Container(
                                [
                                    html.Div(id="output-table"),
                                ]
                            ),
                            html.Br(),
                        ],
                        style={"marginTop": 20, "Align": "center"},
                    ),
                ],
                style={"backgroundColor": "#1A477F", "border-radius": "20px"},
            ),
        ),
        Footer(),
    ]
)
