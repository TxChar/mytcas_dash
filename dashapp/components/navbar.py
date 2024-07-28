import dash_bootstrap_components as dbc
from dash import callback, html, Input, Output, dash_table, dcc


def Navbar():
    return html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink("หน้าหลัก"),
                            outline=True,
                            color="light",
                            className="ms-2",
                            n_clicks=0,
                            href="/",
                        )
                    ),
                    dbc.NavItem(
                        dbc.Button(
                            dbc.NavLink("เกี่ยวกับ"),
                            outline=True,
                            color="light",
                            className="ms-2",
                            n_clicks=0,
                            href="/about",
                        )
                    ),
                ],
                brand="MyTCAS Dashboard",
                brand_style={"fontSize": 32},
                brand_href="/",
                color="#1A477F",
                dark=True,
            ),
        ]
    )
