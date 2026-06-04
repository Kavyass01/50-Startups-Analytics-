import pandas as pd


def generate_business_insights(df):

    insights = {}

    insights["total_startups"] = len(df)

    insights["average_profit"] = round(
        df["Profit"].mean(),
        2
    )

    insights["maximum_profit"] = round(
        df["Profit"].max(),
        2
    )

    insights["minimum_profit"] = round(
        df["Profit"].min(),
        2
    )

    insights["best_state"] = (
        df.groupby("State")["Profit"]
        .mean()
        .idxmax()
    )

    insights["best_state_profit"] = round(
        df.groupby("State")["Profit"]
        .mean()
        .max(),
        2
    )

    insights["highest_rd_spend"] = round(
        df["R&D Spend"].max(),
        2
    )

    return insights


def investment_recommendation(df):

    corr = df.corr(numeric_only=True)

    rd_corr = corr.loc["R&D Spend", "Profit"]
    marketing_corr = corr.loc["Marketing Spend", "Profit"]
    admin_corr = corr.loc["Administration", "Profit"]

    recommendation = []

    if rd_corr > 0.8:
        recommendation.append(
            "R&D Spend strongly influences profit growth."
        )

    if marketing_corr > 0.5:
        recommendation.append(
            "Marketing investment positively affects profit."
        )

    if admin_corr < 0.3:
        recommendation.append(
            "Administration cost has limited impact on profit."
        )

    return recommendation


def detect_outliers(df):

    q1 = df["Profit"].quantile(0.25)

    q3 = df["Profit"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr

    upper = q3 + 1.5 * iqr

    outliers = df[
        (df["Profit"] < lower)
        | (df["Profit"] > upper)
    ]

    return outliers


def top_profitable_startups(df, n=5):

    return (
        df.sort_values(
            by="Profit",
            ascending=False
        )
        .head(n)
    )


def startup_risk_score(df):

    avg_profit = df["Profit"].mean()

    risk_score = []

    for profit in df["Profit"]:

        if profit >= avg_profit:
            risk_score.append("Low Risk")

        elif profit >= avg_profit * 0.75:
            risk_score.append("Medium Risk")

        else:
            risk_score.append("High Risk")

    df["Risk Score"] = risk_score

    return df
