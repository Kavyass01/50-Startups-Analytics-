import plotly.express as px
import plotly.graph_objects as go


def profit_distribution(df):

    fig = px.histogram(
        df,
        x="Profit",
        nbins=20,
        title="Profit Distribution",
        template="plotly_white"
    )

    return fig


def rd_vs_profit(df):

    fig = px.scatter(
        df,
        x="R&D Spend",
        y="Profit",
        color="State",
        size="Marketing Spend",
        hover_data=["Administration"],
        title="R&D Spend vs Profit",
        template="plotly_white"
    )

    return fig


def state_profit_chart(df):

    state_profit = (
        df.groupby("State")["Profit"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        state_profit,
        x="State",
        y="Profit",
        color="State",
        title="Average Profit by State",
        template="plotly_white"
    )

    return fig


def correlation_heatmap(df):

    corr = (
        df.select_dtypes(
            include=["int64", "float64"]
        )
        .corr()
    )

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Matrix"
    )

    return fig


def boxplot_profit(df):

    fig = px.box(
        df,
        x="State",
        y="Profit",
        color="State",
        title="Profit Distribution by State"
    )

    return fig


def feature_importance_chart(features, importance):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=importance,
            y=features,
            orientation="h"
        )
    )

    fig.update_layout(
        title="Feature Importance",
        yaxis_title="Features",
        xaxis_title="Importance"
    )

    return fig
