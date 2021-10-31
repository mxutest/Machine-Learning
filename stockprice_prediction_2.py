{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "stockprice_prediction_2.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNyqeWRwthb48zCHrEkO0Mo"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "LjmfvG8eQkuO"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import streamlit as st\n",
        "import chart_studio.plotly as plotly\n",
        "import plotly.figure_factory as ff\n",
        "from plotly import graph_objs as go\n",
        "from fbprophet import Prophet\n",
        "from fbprophet.plot import plot_plotly\n",
        "import yfinance as yf"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YzlB-jRzQnTJ"
      },
      "source": [
        "st.title('Stock Forecast App')\n",
        "dataset = ('AAPL','MSCT')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IGMlqTd4Uk7h"
      },
      "source": [
        "option = st.selectbox('Select dataset for prediction',dataset)\n",
        "year = st.slider('Year of prediction:',1,4)\n",
        "period = year * 365"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YQInG1ogUn4I"
      },
      "source": [
        "@st.cache\n",
        "def load_data():\n",
        "    data = yf.download(option, start=\"2010-01-01\")\n",
        "    data = data.reset_index()\n",
        "    return data"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "a9NE0QKMQp-a"
      },
      "source": [
        "data_load_state = st.text('Loading data...')\n",
        "data = load_data()\n",
        "data_load_state.text('Loading data... done!')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_rmHZ4wDU516"
      },
      "source": [
        "def plot_fig():\n",
        "\tfig = go.Figure()\n",
        "\tfig.add_trace(go.Scatter(x=data.Date, y=data['Open'], name=\"stock_open\",line_color='blue'))\n",
        "\tfig.add_trace(go.Scatter(x=data.Date, y=data['Close'], name=\"stock_close\",line_color='green'))\n",
        "\tfig.layout.update(title_text='Time Series data with Rangeslider',xaxis_rangeslider_visible=True)\n",
        "\tst.plotly_chart(fig)\n",
        "\treturn fig"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0nmtwS48U7qa"
      },
      "source": [
        "if st.checkbox('Show raw data'):\n",
        "    st.subheader('Raw data')\n",
        "    st.write(data)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sX8nsfj-Quu6"
      },
      "source": [
        "\t# plotting the figure of Actual Data\n",
        "plot_fig()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2DmSQeQAaDwq"
      },
      "source": [
        "# preparing the data for Facebook-Prophet.\n",
        "data_pred = data[['Date','Close']]\n",
        "data_pred=data_pred.rename(columns={\"Date\": \"ds\", \"Close\": \"y\"})"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "O-1tbengQxv4"
      },
      "source": [
        "# code for facebook prophet prediction\n",
        "m = Prophet()\n",
        "m.fit(data_pred)\n",
        "future = m.make_future_dataframe(periods=period)\n",
        "forecast = m.predict(future)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jyM4zDbjQ1eY",
        "outputId": "a75938b6-e79d-4b12-e67a-2d61483c4c46"
      },
      "source": [
        "#plot forecast\n",
        "fig1 = plot_plotly(m, forecast)\n",
        "if st.checkbox('Show forecast data'):\n",
        "    st.subheader('forecast data')\n",
        "    st.write(forecast)\n",
        "st.write('Forecasting closing of stock value for'+option+' for a period of: '+str(year)+'year')\n",
        "st.plotly_chart(fig1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fK_loeA2Q21w"
      },
      "source": [
        "#plot component wise forecast\n",
        "st.write(\"Component wise forecast\")\n",
        "fig2 = m.plot_components(forecast)\n",
        "st.write(fig2)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}