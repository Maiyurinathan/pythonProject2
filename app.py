import pandas as pd
import streamlit as st
import plotly.express as px


Dashboard=pd.read_csv('C:\\Users\\Maiyuri\\Desktop\\DASHBOARD.csv')

st.set_page_config(page_title='IPL Dashboard',layout="wide")
st.header('IPL Dashboard')
team1= Dashboard['team1'].unique().tolist()
st.sidebar.title("Teams")
option=st.sidebar.selectbox("Teams",(team1))
team_1 = Dashboard['team1'] == option
bar_chart = px.bar(Dashboard[team_1],x='year',y='loss',template='plotly_dark',color_discrete_sequence=['green'])
bar_chart.update_yaxes(showgrid=False)
line_chart = px.line(Dashboard[team_1],x='year',y='winner_times',template="plotly_dark",color_discrete_sequence=['blue'])
line_chart.update_yaxes(showgrid=False)
left_column, right_column=st.columns(2)
left_column.plotly_chart(bar_chart,use_container_width=True)
right_column.plotly_chart(line_chart,use_container_width=True)
tree = px.treemap(Dashboard[team_1], path=[px.Constant(option), 'year', 'win_bybowl'],values='year',color='win_bybowl',hover_data=['year'],color_discrete_sequence=['turquoise'],color_continuous_scale='PuBu')
bar_chart_1 = px.bar(Dashboard[team_1],x='run_times',y='year',orientation="h",color_discrete_sequence=['blue'])
bar_chart_1.update_yaxes(showgrid=False)
left_column, right_column=st.columns(2)
left_column.plotly_chart(bar_chart_1,use_container_width=True)
right_column.plotly_chart(tree,use_container_width=True)
pie_1=px.pie(Dashboard[team_1],'year','winner_times',hole=.3)
pie_2=px.pie(Dashboard[team_1],'year','loss')
left_column, right_column=st.columns(2)
left_column.plotly_chart(pie_1,use_container_width=True)
right_column.plotly_chart(pie_2,use_container_width=True)




