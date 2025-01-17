from callbacks.api import universities_data
from dash.dependencies import Input, Output
from dash import Input, Output, dash_table, dcc, html
import dash_bootstrap_components as dbc
import plotly


def map_selection(app):
    @app.callback(
        Output("output-map", "children"),
        [Input("universities-dropdown", "value"), Input("major-dropdown", "value")],
    )
    def update_map(selected_universities, selected_majors):
        df = universities_data()

        if selected_universities:
            df = df[df["มหาวิทยาลัย"].isin(selected_universities)]

        if selected_majors:
            df = df[df["คณะ"].isin(selected_majors)]

        # Get total number
        df["total"] = (
            df["รอบ 1 Portfolio"]
            + df["รอบ 2 Quota"]
            + df["รอบ 3 Admission"]
            + df["รอบ 4 Direct Admission"]
        )
        df2 = df.groupby(["มหาวิทยาลัย"]).sum()["total"].to_frame().reset_index()
        df = df.merge(df2, how="inner", on="มหาวิทยาลัย")

        # Rename columns
        df = df.rename(columns={"total_y": "จำนวนนักศึกษาที่รับ"})

        fig = plotly.express.scatter_mapbox(
            df,
            lat="ละติจูด",
            lon="ลองจิจูด",
            hover_name="มหาวิทยาลัย",
            # hover_data=["รอบ 1 Portfolio", "รอบ 2 Quota", "รอบ 3 Admission", "รอบ 4 Direct Admission"],
            center=dict(lat=13.736717, lon=100.523186),
            color="จำนวนนักศึกษาที่รับ",
            size="จำนวนนักศึกษาที่รับ",
            color_continuous_scale=plotly.express.colors.sequential.Rainbow,
            size_max=30,
            zoom=5,
            height=750,
        )
        fig.update_layout(
            margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_style="open-street-map"
        )

        fig = dcc.Graph(figure=fig)
        return fig


def table_slection(app):
    @app.callback(
        Output("output-table", "children"),
        [Input("universities-dropdown", "value"), Input("major-dropdown", "value")],
    )
    def update_table(selected_universities, selected_majors):
        df = universities_data()
        # df = (universities_data()).drop(["pp3year", "level"], axis=1)

        if selected_universities:
            df = df[df["มหาวิทยาลัย"].isin(selected_universities)]

        if selected_majors:
            df = df[df["คณะ"].isin(selected_majors)]

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
            page_current=0,  # Page number
            page_size=15,  # Number of rows per page
            page_action="native",  # Enable pagination
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
        [Input("universities-dropdown", "value"), Input("major-dropdown", "value")],
    )
    def update_table(selected_universities, selected_majors):
        df = universities_data()

        if selected_universities:
            df = df[df["มหาวิทยาลัย"].isin(selected_universities)]

        if selected_majors:
            df = df[df["คณะ"].isin(selected_majors)]

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
    map_selection(app)
