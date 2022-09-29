#!pip install -U plotly#ejecutar si hay error, actualiza la libreria necesarioejecutarla solo una vez
import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
#import io 
import plotly.io as pio
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt
import json
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from datetime import datetime
import datetime
from pandas import Timestamp
from dotenv import load_dotenv
import os
import plotly.graph_objects as go
import time
import plost
load_dotenv()



sidebar = st.container()


with st.sidebar:
    choose = option_menu("", ["diccionario datos","Principales criptos","Volumen Transaccion", "Varianza", "Calculadora","Media movil"],
                         icons=['house', 'building', 'reception-4','phone', 'book','table'],
                         menu_icon="archive", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#5e5c5c"},
        "icon": {"color": "Black", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#121111"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    #logo = Image.open(r)
    logon= Image.open(r"cripto2.jpg")
    st.image(logon, width=400 )

if choose == "diccionario datos":
    def main():
        st.subheader('_____diccionario datos_____')
        st.subheader('markets')
        dic_datos = pd.read_excel(r"dic_datos3.xlsx")
        dic_datos.drop(columns=[' '], inplace=True)
        st.dataframe(dic_datos)

        #load_image()
    if __name__ == '__main__':
        main()


if choose == "Principales criptos":
    
    logo= Image.open(r"cripto.jpg")
    
    col1, col2 = st.columns( [0.7, 0.2])
    # with col1:               # To display the header text using css style
    #     st.markdown(""" <style> .font {
    #     font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    #     </style> """, unsafe_allow_html=True)
    #     st.markdown('<p class="font"></p>', unsafe_allow_html=True)    
    with col1:               # To display brand log
        st.subheader('Bitcoin')
        st.subheader("Bitcoin precio de hoy es el $19,321.75 USD con un volumen de comercio de 24 horas de $49,699,932,557 USD. Actualizamos nuestro precio de BTC a USD en tiempo real. Bitcoin subió 3.12% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #1, con una capitalización de mercado de $370,273,593,409 USD. Tiene un suministro circulante de 19,163,568 BTC monedas y un suministro máximo de 21,000,000 BTC monedas.")    
           
        if st.checkbox('Bitcoin'):

            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            all_markets = requests.get(endpoint_url).json()
            base_currency = 'BTC'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # 1 day = 60 * 60 * 24 seconds
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
                f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()
            # historical
            # Convert JSON to Pandas DataFrame
            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
                df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            df.drop(['startTime', 'time'], axis=1, inplace=True)
            st.dataframe(df)
            fig = go.Figure()
            fig.update_layout(
                title={
                    'text': f"{base_currency}/{quote_currency}",
                    'x':0.5,
                    'xanchor': 'center'
                },
                xaxis_title="Date",
                yaxis_title="Price",
                xaxis_rangeslider_visible=False
            )
            fig.add_trace(
                go.Candlestick(
                    x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close']
                )
            )
            fig.show()
            st.plotly_chart(fig)
            #st.dataframe(historical)
        
     #   st.image(logo, width=400 )
        if st.checkbox('Ethereum'):
            st.subheader('Ethereum')
            st.subheader("Ethereum precio de hoy es el $1,322.60 USD con un volumen de comercio de 24 horas de $16,755,934,683 USD. Actualizamos nuestro precio de ETH a USD en tiempo real. Ethereum subió 3.49% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #2, con una capitalización de mercado de $162,115,743,793 USD. Tiene un suministro circulante de 122,573,327 ETH monedas y el suministro máximo no está disponible.")    
           


            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            all_markets = requests.get(endpoint_url).json()
            base_currency = 'ETH'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # 1 day = 60 * 60 * 24 seconds
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
            f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()
            # historical
            # Convert JSON to Pandas DataFrame
            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
            df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            df.drop(['startTime', 'time'], axis=1, inplace=True)
            st.dataframe(df)
            fig = go.Figure()
            fig.update_layout(
            title={
                'text': f"{base_currency}/{quote_currency}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
            )
            fig.add_trace(
            go.Candlestick(
                x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
            )
            )
            fig.show()
            st.plotly_chart(fig)

        
        if st.checkbox('Tether USDT'):
            st.subheader('Tether')
            st.subheader("Tether precio de hoy es el $0.999954 USD con un volumen de comercio de 24 horas de $61,285,362,797 USD. Actualizamos nuestro precio de USDT a USD en tiempo real. Tether subió 0.00% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #3, con una capitalización de mercado de $67,953,085,917 USD. Tiene un suministro circulante de 67,956,206,763 USDT monedas y el suministro máximo no está disponible.")    
           


            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            all_markets = requests.get(endpoint_url).json()
            base_currency = 'USDT'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # 1 day = 60 * 60 * 24 seconds
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
            f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()
            # historical
            # Convert JSON to Pandas DataFrame
            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
            df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            df.drop(['startTime', 'time'], axis=1, inplace=True)
            st.dataframe(df)
            fig = go.Figure()
            fig.update_layout(
            title={
                'text': f"{base_currency}/{quote_currency}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
            )
            fig.add_trace(
            go.Candlestick(
                x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
            )
            )
            fig.show()
            st.plotly_chart(fig)

        
        if st.checkbox('BNB'):
            st.subheader('BNB')
            st.subheader("BNB precio de hoy es el $281.25 USD con un volumen de comercio de 24 horas de $844,504,016 USD. Actualizamos nuestro precio de BNB a USD en tiempo real. BNB subió 4.57% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #5, con una capitalización de mercado de $45,375,679,718 USD. Tiene un suministro circulante de 161,337,261 BNB monedas y un suministro máximo de 200,000,000 BNB monedas.")    
           


            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            all_markets = requests.get(endpoint_url).json()
            base_currency = 'BNB'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # 1 day = 60 * 60 * 24 seconds
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
            f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()
            # historical
            # Convert JSON to Pandas DataFrame
            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
            df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            df.drop(['startTime', 'time'], axis=1, inplace=True)
            st.dataframe(df)
            fig = go.Figure()
            fig.update_layout(
            title={
                'text': f"{base_currency}/{quote_currency}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
            )
            fig.add_trace(
            go.Candlestick(
                x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
            )
            )
            fig.show()
            st.plotly_chart(fig)

        
        if st.checkbox('DOGECOIN'):
            st.subheader('dogecoin')
            st.subheader("Dogecoin precio de hoy es el $0.059972 USD con un volumen de comercio de 24 horas de $226,260,650 USD. Actualizamos nuestro precio de DOGE a USD en tiempo real. Dogecoin bajó 0.43% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #10, con una capitalización de mercado de $7,956,584,358 USD. Tiene un suministro circulante de 132,670,764,300 DOGE monedas y el suministro máximo no está disponible.")    
           


            # endpoint_url = 'https://ftx.com/api/markets'
            # # Get all market data as JSON
            # all_markets = requests.get(endpoint_url).json()
            # base_currency = 'DOGE'
            # quote_currency = 'USD'
            # # Specify the base and quote currencies to get single market data
            # request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # # 1 day = 60 * 60 * 24 seconds
            # daily=str(60*60*24)
            # start_date = datetime.datetime(2021, 1, 1).timestamp()
            # # Get the historical market data as JSON
            # historical = requests.get(
            # f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            # ).json()
            # # historical
            # # Convert JSON to Pandas DataFrame
            # df = pd.DataFrame(historical['result'])
            # # Convert time to date
            # df['date'] = pd.to_datetime(
            # df['time']/1000, unit='s', origin='unix'
            # ) 
            # #Remove unnecessar columns
            # df.drop(['startTime', 'time'], axis=1, inplace=True)
            # st.dataframe(df)
            # fig = go.Figure()
            # fig.update_layout(
            # title={
            #     'text': f"{base_currency}/{quote_currency}",
            #     'x':0.5,
            #     'xanchor': 'center'
            # },
            # xaxis_title="Date",
            # yaxis_title="Price",
            # xaxis_rangeslider_visible=False
            # )
            # fig.add_trace(
            # go.Candlestick(
            #     x=df['date'],
            #     open=df['open'],
            #     high=df['high'],
            #     low=df['low'],
            #     close=df['close']
            # )
            # )
            # fig.show()
            # st.plotly_chart(fig)

            # endpoint_url = 'https://ftx.com/api/markets'
            # # Get all market data as JSON
            # doge_markets = requests.get(endpoint_url).json()
            # base_currency = 'DOGE'
            # quote_currency = 'USD'
            # # Specify the base and quote currencies to get single market data
            # request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # daily=str(60*60*24)
            # start_date = datetime(2021, 1, 1).timestamp()
            # # Get the historical market data as JSON
            # historical = requests.get(
            # f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            # ).json()

            # df = pd.DataFrame(historical['result'])
            # # Convert time to date
            # df['date'] = pd.to_datetime(
            # df['time']/1000, unit='s', origin='unix'
            # ) 
            # #Remove unnecessar columns
            # #df.drop(['startTime', 'time'], axis=1, inplace=True)
            # #st.dataframe(df)
            # df['time'] = pd.to_datetime(df['time'], unit='ms')
            # df.set_index('time', inplace=True)

            # #df['20 SMA'] = df.close.rolling(20).mean()
            # #df.tail()

            # import plotly.graph_objects as go
            # fig = go.Figure(data=[go.candlestick(x = df.index,
            #                                     open = df['open'],
            #                                     high = df['high'],
            #                                     low = df['low'],
            #                                     close = df['close'],
            #                                     ),
            #                     go.Scatter(x=df.index, y=df['20 SMA'], line=dict(color='purple', width=1))])


            # fig.show()
            # st.plotly_chart(fig)

            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            doge_markets = requests.get(endpoint_url).json()
            base_currency = 'DOGE'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
            f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()

            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
            df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            #df.drop(['startTime', 'time'], axis=1, inplace=True)
            #st.dataframe(df)
            df['time'] = pd.to_datetime(df['time'], unit='ms')
            df.set_index('time', inplace=True)
            df['20 SMA'] = df.close.rolling(20).mean()
            df.tail()

            import plotly.graph_objects as go
            fig = go.Figure(data=[go.Candlestick(x = df.index,
                                                open = df['open'],
                                                high = df['high'],
                                                low = df['low'],
                                                close = df['close'],
                                                ),
                                go.Scatter(x=df.index, y=df['20 SMA'], line=dict(color='purple', width=1))])


            fig.show()
            st.plotly_chart(fig)


            df['20 SMA'] = df.close.rolling(20).mean()
            df.tail()

            import plotly.graph_objects as go
            fig = go.Figure(data=[go.Candlestick(x = df.index,
                                                open = df['open'],
                                                high = df['high'],
                                                low = df['low'],
                                                close = df['close'],
                                                ),
                                go.Scatter(x=df.index, y=df['20 SMA'], line=dict(color='purple', width=1))])


            fig.show()
            st.plotly_chart(fig)




        if st.checkbox('POLYGON'):
            st.subheader('Polygon')
            st.subheader("Polygon precio de hoy es el $0.741258 USD con un volumen de comercio de 24 horas de $277,497,997 USD. Actualizamos nuestro precio de MATIC a USD en tiempo real. Polygon subió 0.68% en las últimas 24 horas. La clasificación actual de CoinMarketCap es #13, con una capitalización de mercado de $6,474,382,192 USD. Tiene un suministro circulante de 8,734,317,475 MATIC monedas y un suministro máximo de 10,000,000,000 MATIC monedas.")    
           


            endpoint_url = 'https://ftx.com/api/markets'
            # Get all market data as JSON
            all_markets = requests.get(endpoint_url).json()
            base_currency = 'MATIC'
            quote_currency = 'USD'
            # Specify the base and quote currencies to get single market data
            request_url = f'{endpoint_url}/{base_currency}/{quote_currency}'
            # 1 day = 60 * 60 * 24 seconds
            daily=str(60*60*24)
            start_date = datetime.datetime(2021, 1, 1).timestamp()
            # Get the historical market data as JSON
            historical = requests.get(
            f'{request_url}/candles?resolution={daily}&start_time={start_date}'
            ).json()
            # historical
            # Convert JSON to Pandas DataFrame
            df = pd.DataFrame(historical['result'])
            # Convert time to date
            df['date'] = pd.to_datetime(
            df['time']/1000, unit='s', origin='unix'
            ) 
            #Remove unnecessar columns
            df.drop(['startTime', 'time'], axis=1, inplace=True)
            st.dataframe(df)
            fig = go.Figure()
            fig.update_layout(
            title={
                'text': f"{base_currency}/{quote_currency}",
                'x':0.5,
                'xanchor': 'center'
            },
            xaxis_title="Date",
            yaxis_title="Price",
            xaxis_rangeslider_visible=False
            )
            fig.add_trace(
            go.Candlestick(
                x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close']
            )
            )
            fig.show()
            st.plotly_chart(fig)

    
if choose == "calculadora":
    # bitcoin_usd = input("¿Cuantos bitcoin_usd tienes ?")
    # st.number_input(bitcoin_usd)
    # bitcoin_usd = float(bitcoin_usd)
    # #Declaracion de valores
    # bitcoin_valor_usd =19219
    # # valor_euro = 4383
    # # valor_cake = 58800
    # # valor_btc = 136134100
    # bitcoin= bitcoin_usd / 19219
    # bitcoin = round(bitcoin, 2)
    # bitcoin = str(bitcoin)
    # print('tienes $' + bitcoin +'bitcoin')
    # st.text(print('tienes $' + bitcoin +'bitcoin'))

    


    # st.set_page_config(
    #     page_title="Financial Planning Calculator")

    st.title("cripto Calculator")

    # st.header("**Monthly Income**")
    # st.subheader("Salary")
    colAnnualSal = st.beta_columns(1)

    with colAnnualSal:
        bitcoin_usd = st.number_input("Cuantos bitcoin_usd tienes?($): ", min_value=0.0, format='%f')
    #with colTax:
        #tax_rate = st.number_input("Enter your tax rate(%): ", min_value=0.0, format='%f')

        bitcoin_usd = float(bitcoin_usd)
        # #Declaracion de valores
        bitcoin_valor_usd =19219
        bitcoin= bitcoin_usd / 19219
        bitcoin = round(bitcoin, 2)
        bitcoin = str(bitcoin)
        a=print('tienes $' + bitcoin +'bitcoin')
        st.text(a)

    st.header("**bitcoin a usd**")
    colExpenses1 = st.beta_columns(1)

    with colExpenses1:
        st.subheader("cantidad ")
        cant_bitcoin = st.number_input("Cuantos bitcoin tienes?($): ", min_value=0.0, format='%f')
        #monthly_rental = st.number_input("Enter your monthly rental($): ", min_value=0.0,format='%f' )
        
        st.subheader("bitcoin_usd")
        cant_bitcoin = float(cant_bitcoin)
        # #Declaracion de valores
        bitcoin_valor =19219
        bitcoin_usd= cant_bitcoin * 19219
        bitcoin_usd = round(bitcoin_usd, 2)
        bitcoin_usd = str(bitcoin_usd)
        b=print('tienes $' + bitcoin_usd +'bitcoin')
        st.text(b)
        # daily_food = st.number_input("Enter your daily food budget ($): ", min_value=0.0,format='%f' )
        # monthly_food = daily_food * 30
        
        # st.subheader("Monthly Unforeseen Expenses")
        # monthly_unforeseen = st.number_input("Enter your monthly unforeseen expenses ($): ", min_value=0.0,format='%f' ) 
       



    # profile = Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\muertes_estados_rankin3.jpg")
    # #"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\muertes_estados_rankin3.jpg"
    # st.image(profile, width=800)


# if choose == "hospitalizados covid":
#     logo1= Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\Estados con mayor ocupación hospitalaria por COVID.png")
#     col1, col2 = st.columns( [0.7, 0.2])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">Ocupación hospitalaria por COVID</p>', unsafe_allow_html=True)   
#         st.image(logo1, width=800 ) 
#     #with col2:               # To display brand log
#         #st.image(logo, width=135 )
    
#     st.write("Ocupación hospitalaria por COVID")    
    
#     profile = Image.open(r"ranking_estados.jpg")#imagen pacientes hospitalizados x estado
#     #"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\muertes_estados_rankin3.jpg"
#     st.image(profile, width=800)



# if choose == "Camas UCI":
    
#     col1, col2 = st.columns( [0.8, 0.2])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #d6cec6;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">Uso de Camas UCI por estado</p>', unsafe_allow_html=True) 


#     #with col2:               # To display the header text using css style
#         #st.image(logo, width=130 )
#     st.write('Total de uso de camas UCI(cuidados intensivos) utilizadas. Columnas analisadas(staffed_adult_icu_bed_occupancy) y (staffed_pediatric_icu_bed_occupancy)')
    
#     #st.subheader('Ranking de Ocupación camas UCI')

#     #porcentaje_uci = pd.DataFrame()
#     st.subheader('total camas UCI por estado, en el año 2020')
#     profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\Total_camas2.box.jpg')
#     st.image(profile, width=700 )

#     uci = pd.DataFrame()

#     uci['Fecha'] = data['date']
#     uci['Estado'] = data['state']
#     uci['Ocupación_de_camas_de_UCI_para_adultos_con_personal'] = data['staffed_adult_icu_bed_occupancy']
#     uci['Ocupación_de_camas_en_la_UCI_pediátrica_con_personal'] = data['staffed_pediatric_icu_bed_occupancy']
#     #"C:\Users\Manuel Revelo\Desktop\P!_2\prueba mapa\COVID-19_Reported_Patient_Impact_and_Hospital_Capacity_by_State_Timeseries.csv"
#         # Agrupacion por Estado
#     estados_2 = uci.groupby('Estado').sum([['Ocupación_de_camas_de_UCI_para_adultos_con_personal'],['Ocupación_de_camas_en_la_UCI_pediátrica_con_personal']])
#     estados_2['total_camas_uci'] = estados_2['Ocupación_de_camas_de_UCI_para_adultos_con_personal'] + estados_2['Ocupación_de_camas_en_la_UCI_pediátrica_con_personal']
#     st.write(estados_2.groupby("Estado").sum().sort_values(by="total_camas_uci", ascending=False).head(5))

#     estados_2.reset_index('Estado', inplace = True)

#     fig, ax = plt.subplots()
#     sns.lineplot(x='Estado', y='total_camas_uci', data=estados_2, ax=ax)
#     plt.gcf().set_size_inches(15, 8)
#     st.pyplot(fig)
          

    # #!pip install -U plotly
    # import streamlit as st
    # from streamlit_option_menu import option_menu
    # import streamlit.components.v1 as html
    # from  PIL import Image
    # import numpy as np
    # import pandas as pd
    # import plotly.express as px
    # import io 
    # import plotly.io as pio
    # from datetime import date
    # from pyexpat import features
    # import seaborn as sns
    # import matplotlib.pyplot as plt
    # import json
    # from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
    # import requests # library to handle requests
    # from pandas.io.json import json_normalize
    # import matplotlib.cm as cm
    # import matplotlib.colors as colors
    # import folium # map rendering library
    # import pandas as pd
    # import requests
    # import json
    # import plotly.express as px

    # df=pd.read_csv('usa_beds_uci_covid.csv')
    # #repo_url = 'https://github.com/PublicaMundi/MappingAPI/blob/master/data/geojson/us-states.json' #Archivo GeoJSON
    # #mx_regions_geo = requests.get(repo_url).json()
    # usa_states = json.load(open(r"states.geojson", "r"))

    # fig = px.choropleth(data_frame=df, 
    #                     geojson=usa_states,#mx_regions_geo, 
    #                     locations='state', # nombre de la columna del Dataframe
    #                     featureidkey="properties.STUSPS",#'id',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
    #                     color='inpatient_beds_used_covid', #El color depende de las cantidades
    #                     color_continuous_scale="greens",#burg", #greens
    #                     #scope="north america"
    #                 )
    # fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

    # fig.update_layout(
    #     title_text = 'ocupacion uci por covid',
    #     font=dict(
    #         #family="Courier New, monospace",
    #         family="Ubuntu",
    #         size=18,
    #         color="#7f7f7f"
    #     ),
    #     annotations = [dict(
    #         x=0.55,
    #         y=-0.1,
    #         xref='paper',
    #         yref='paper',
    #         text='Fuente: <a href="https://healthdata.gov/api/odata/v4/g62h-syeh">\
    #             https://healthdata.gov/ </a>',
    #         showarrow = False
    #     )]
    # )
    # fig.show()
       
# if choose == "Ocupación covid":
#     #logo= Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\prueba mapa\covid 3.jpg")
#     col1, col2 = st.columns( [0.8, 0.2])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #d6cec6;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">Estados con ocupación hospitalaria por COVID</p>', unsafe_allow_html=True) 


#     #with col2:               # To display the header text using css style
#      #   st.image(logo, width=430 )
#     st.write('Estados con mayor ocupación hospitalaria por COVID. Las columnas utilizadas son : (total_adult_patients_hospitalized_confirmed_covid)(staffed_icu_adult_patients_confirmed_covid)(total_pediatric_patients_hospitalized_confirmed_covid)')  
#     st.subheader('Ranking de estador con mayor ocupación hospilataria')

#     camas = pd.DataFrame()

#     camas['Fecha'] = data['date']
#     camas['Estado'] = data['state']
#     camas['Camas_UCI'] = data['total_adult_patients_hospitalized_confirmed_covid']
#     camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_UCI'] = data['staffed_icu_adult_patients_confirmed_covid']
#     camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_hospitalización_pediátrica'] = data['total_pediatric_patients_hospitalized_confirmed_covid']

#     # Pasando a INT  total_adult_patients_hospitalized_confirmed_covid
#     camas['Camas_UCI'] = camas['Camas_UCI'].astype(int)

#     # Pasando a INT  total_pediatric_patients_hospitalized_confirmed_covid
#     camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_UCI'] = camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_UCI'].astype(int)

#     # Pasando a INT  total_pediatric_patients_hospitalized_confirmed_covid
#     camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_hospitalización_pediátrica'] = camas['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_hospitalización_pediátrica'].astype(int)

#     # Camas por estados
#     camas_estado = camas.groupby('Estado').sum([['Camas_UCI'],['hospitalización_cama_covid_utilización'],['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_UCI']])

#     camas_estado['Mayor_Ocupacion'] = camas_estado['Camas_UCI'] + camas_estado['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_UCI'] + camas_estado['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_hospitalización_pediátrica'] +  camas_estado['Pacientes_informados_actualmente_hospitalizados_en_una_cama_de_hospitalización_pediátrica']

#     st.write(camas_estado.sort_values(by="Mayor_Ocupacion", ascending=False).head(5))

#     fig, ax = plt.subplots()
#     sns.lineplot(x='Estado', y='Mayor_Ocupacion', data=camas_estado, ax=ax)
#     plt.gcf().set_size_inches(15, 8)

    
#     st.pyplot(fig)

#     st.subheader('Ranking de Ocupación de camas hospitalaria por estado, en el primer semestre del año 2020')
#     profile = Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\Total_camas2.box.jpg")
#     #"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\Total_camas2.box.jpg"
#     #"C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\ranking_estados.jpg"
#     st.image(profile, width=700 )
   

# if choose == "muertes_covid":
#     #logo= Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\prueba mapa\covid 3.jpg")
#     col1, col2 = st.columns( [0.8, 0.2])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #d6cec6;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">Conclusiones</p>', unsafe_allow_html=True) 


#     #with col2:               # To display the header text using css style
#         st.image(logo, width=130 )
    
#     # st.subheader('Muertes por COVID')
#     # profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\deaths_covid.jpg')
#     # st.image(profile, width=700 )

#     # st.subheader('Falta de personal medico')
#     # profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\falta_de_personal.jpg')
#     # st.image(profile, width=700 )

#     st.subheader('Relación entre muertes y falta de personal medico')
#     profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\relacion_muertes_falta_de_personal.jpg')
#     st.image(profile, width=700 )


    # import streamlit as st
    # from streamlit_option_menu import option_menu
    # import streamlit.components.v1 as html
    # from  PIL import Image
    # import numpy as np
    # import pandas as pd
    # import plotly.express as px
    # import io 
    # import plotly.io as pio
    # from datetime import date
    # from pyexpat import features
    # import seaborn as sns
    # import matplotlib.pyplot as plt
    # import json
    # from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
    # import requests # library to handle requests
    # from pandas.io.json import json_normalize
    # import matplotlib.cm as cm
    # import matplotlib.colors as colors
    # import folium # map rendering library
    # import pandas as pd
    # import requests
    # import json
    # import plotly.express as px

    # df=pd.read_csv("muertes-personal.csv")
    # #repo_url = 'https://github.com/PublicaMundi/MappingAPI/blob/master/data/geojson/us-states.json' #Archivo GeoJSON
    # #mx_regions_geo = requests.get(repo_url).json()
    # usa_states = json.load(open(r"states.geojson", "r"))

    # fig = px.choropleth(data_frame=df, 
    #                     geojson=usa_states,#mx_regions_geo, 
    #                     locations='Estado', # nombre de la columna del Dataframe
    #                     featureidkey="properties.STUSPS",#'id',  # ruta al campo del archivo GeoJSON con el que se hará la relación (nombre de los estados)
    #                     color='deaths_covid', #El color depende de las cantidades
    #                     color_continuous_scale="greens",#burg", #greens
    #                     #scope="north america"
    #                 )
    # fig.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

    # fig.update_layout(
    #     title_text = 'muertes covid x estado',
    #     font=dict(
    #         #family="Courier New, monospace",
    #         family="Ubuntu",
    #         size=18,
    #         color="#7f7f7f"
    #     ),
    #     annotations = [dict(
    #         x=0.55,
    #         y=-0.1,
    #         xref='paper',
    #         yref='paper',
    #         text='Fuente: <a href="https://healthdata.gov/api/odata/v4/g62h-syeh">\
    #             https://healthdata.gov </a>',
    #         showarrow = False
    #     )]
    # )
    # fig.show()

    
    

# if choose == "Conclusiones": 
#     logo= Image.open(r"C:\Users\Manuel Revelo\Desktop\P!_2\prueba mapa\covid 3.jpg")

#     col1, col2 = st.columns( [0.8, 0.2])
#     with col1:               # To display the header text using css style
#         st.markdown(""" <style> .font {
#         font-size:35px ; font-family: 'Cooper Black'; color: #d6cec6;} 
#         </style> """, unsafe_allow_html=True)
#         st.markdown('<p class="font">Conclusiones</p>', unsafe_allow_html=True) 


#     with col2:               # To display the header text using css style
#         st.image(logo, width=130 )
#     st.write('Tomando conclusiones fue que el peor mes de la pandemia fue el 21-01 que fue el mes que mas hubo Muertes por covid. Y tambien fue donde hubo reporte de falta de personal Medico.') 
#     st.subheader('Muertes por COVID')
#     profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\deaths_covid.jpg')
#     st.image(profile, width=700 )

#     st.subheader('Falta de personal medico')
#     profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\falta_de_personal.jpg')
#     st.image(profile, width=700 )

#     st.subheader('Relación entre muertes y falta de personal medico')
#     profile = Image.open(r'C:\Users\Manuel Revelo\Desktop\P!_2\PI_agustin\relacion_muertes_falta_de_personal.jpg')
#     st.image(profile, width=700 )
    

#     st.write('Con respecto a los recursos hospilatarios, recomendaria una mayor inversión en temas de recursos, para futuros problemas como lo que paso con pandemia, recursos como camas, respiradores, etc.Se recomienda tambien contar con una mayor de personal capacitado, para tiempos de pandemía, que fueron bastantes escasos en comparación a como a sucedido la pandemia por COVID')   
    






    


