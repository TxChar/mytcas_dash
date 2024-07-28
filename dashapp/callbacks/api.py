import httpx
import pandas
import plotly.graph_objects as go
import plotly.express as px


def universities_data():
    df = pandas.read_csv("dashapp/assets/universities_data.csv")

    df[
        ["รอบ 1 Portfolio", "รอบ 2 Quota", "รอบ 3 Admission", "รอบ 4 Direct Admission"]
    ] = df[
        ["รอบ 1 Portfolio", "รอบ 2 Quota", "รอบ 3 Admission", "รอบ 4 Direct Admission"]
    ].apply(
        pandas.to_numeric
    )
    return df


def graduated_api():
    client = httpx.Client()
    url = "https://gpa.obec.go.th/reportdata/pp3-4_2566_province.json"

    try:
        response = client.get(url)
        json_data = response.json()
        df = pandas.DataFrame(json_data)
    except:
        df = pandas.DataFrame(
            columns=[
                "pp3year",
                "level",
                "schools_province",
                "totalmale",
                "totalfemale",
                "totalstd",
            ]
        )

    df[["pp3year", "totalmale", "totalfemale", "totalstd"]] = df[
        ["pp3year", "totalmale", "totalfemale", "totalstd"]
    ].apply(pandas.to_numeric)

    return df


def provinces_location():
    df_graduated = (graduated_api()).drop(["pp3year", "level"], axis=1)
    df_locations = pandas.read_csv("dashapp/assets/ThailandProvincesLocation.csv")
    df_merge_locations = pandas.merge(df_graduated, df_locations, on="schools_province")
    return df_merge_locations
