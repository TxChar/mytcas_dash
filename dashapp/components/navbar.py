import dash_bootstrap_components as dbc
from dash import callback, html, Input, Output, dash_table, dcc


def Navbar():
    return html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink("หน้าหลัก", href="/"),
                            outline=True,
                            color="light",
                            className="ms-2",
                            n_clicks=0,
                        )
                    ),
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink(
                                "เกี่ยวกับ",
                                href="/about",
                            ),
                            outline=True,
                            color="light",
                            className="ms-2",
                            n_clicks=0,
                        )
                    ),
                ],
                brand="MyTCAS Dashboard",
                brand_style={"fontSize": 32},
                brand_href="/",
                color="#B33939",
                dark=True,
            ),
        ]
    )