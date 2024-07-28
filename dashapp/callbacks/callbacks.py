from callbacks.api import graduated_api, provinces_location, universities_data
from dash.dependencies import Input, Output
from dash import Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc
import plotly


def table_slection(app):
    @app.callback(
        Output("output-table", "children"), [Input("universities-dropdown", "value")]
    )
    def update_table(selected_universities):
        df = universities_data()
        # df = (universities_data()).drop(["pp3year", "level"], axis=1)

        if selected_universities:
            df = df[df["มหาวิทยาลัย"].isin(selected_universities)]

        df = df.rename(
            columns={
                "รอบ 1 Portfolio": "รอบ 1",
                "รอบ 2 Quota": "รอบ 2",
                "รอบ 3 Admission": "รอบ 3",
                "รอบ 4 Direct Admission": "รอบ 4",
            }
        )
        universities_df = df[
            [
                "มหาวิทยาลัย",
                "คณะ",
                "รอบ 1",
                "รอบ 2",
                "รอบ 3",
                "รอบ 4",
            ]
        ]
        universities_table = dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in universities_df.columns],
            data=df.to_dict("records"),
            style_header={
                "color": "black",
                "fontWeight": "bold",
                "backgroundColor": "rgb(200, 200, 200)",
            },
            style_cell={"padding-right": "10px", "fontSize": 18},
            style_data={"color": "black", "backgroundColor": "white"},
            style_table={"borderRadius": "10px", "overflow": "hidden"},
            style_data_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "rgb(220, 220, 220)",
                }
            ],
        )
        return universities_table


def summarization_students(app):
    @app.callback(
        [
            Output("first-card", "children"),
            Output("second-card", "children"),
            Output("third-card", "children"),
            Output("fourth-card", "children"),
        ],
        [Input("universities-dropdown", "value")],
    )
    def update_table(selected_universities):
        df = universities_data()

        if selected_universities:
            df = df[df["คณะ"].isin(selected_universities)]

        df = df.rename(
            columns={
                "รอบ 1 Portfolio": "รอบ 1",
                "รอบ 2 Quota": "รอบ 2",
                "รอบ 3 Admission": "รอบ 3",
                "รอบ 4 Direct Admission": "รอบ 4",
            }
        )

        first_total = df["รอบ 1"].sum()
        second_total = df["รอบ 2"].sum()
        third_total = df["รอบ 3"].sum()
        fourth_total = df["รอบ 4"].sum()
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..")
        # print(df["รอบ 1"].dtypes)
        # print(first_total)
        # print(second_total)

        first_card = [
            dbc.CardHeader("รอบที่1 Portfolio"),
            dbc.CardBody(
                [
                    html.H3(f"{first_total} คน", className="card-title"),
                ]
            ),
        ]

        second_card = [
            dbc.CardHeader("รอบที่2 Quota"),
            dbc.CardBody(
                [
                    html.H3(f"{second_total} คน", className="card-title"),
                ]
            ),
        ]

        third_card = [
            dbc.CardHeader("รอบที่3 Admission"),
            dbc.CardBody(
                [
                    html.H3(f"{third_total} คน", className="card-title"),
                ]
            ),
        ]

        fourth_card = [
            dbc.CardHeader("รอบที่4 Direct Admission"),
            dbc.CardBody(
                [
                    html.H3(f"{fourth_total} คน", className="card-title"),
                ]
            ),
        ]

        return (first_card, second_card, third_card, fourth_card)


def register_callbacks(app):
    table_slection(app)
    summarization_students(app)
