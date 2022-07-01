import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import date, datetime, timedelta
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import plotly.express as px
from streamlit_option_menu import option_menu


from waste_graph_functions import *
from list_weekly_kpis import *


header = st.container()
waste_dataset = st.container()
covers_dataset = st.container()
heatmap_dataset = st.container()
model_training = st.container()

inactive_dataset = st.container()
table_new_drop_dataset = st.container()
kpi_dataset = st.container()
fig_bar_dataset = st.container()
fig_pie_dataset = st.container()
line_chart_input_dataset = st.container()

box_plot_dataset = st.container()

individual_heatmap_dataset = st.container()


impact_report_metrics_dataset = st.container()





with st.sidebar:
	selected = option_menu(
		menu_title = 'Menu',
		options = ["Activity Tracker","Weekly KPIs","Outstanding data","Missing data","Impact Report"],
	)


################################################################
################################################################
################################################################

	if selected == 'Weekly KPIs':
		

		with inactive_dataset:

			st.title('Hello AK')

			headerColor = 'royalblue'
			rowEvenColor = 'paleturquoise'
			rowOddColor = 'white'


			fig_table = go.Figure(data=[go.Table(
			    header=dict(values=['id_company','kitchen','status'],
					fill_color='paleturquoise',
					align='left'),
			    cells=dict(values=[fit_inactive_this_month['id_company'], fit_inactive_this_month['kitchen'], fit_inactive_this_month['Current Type']],
				       fill_color='lavender',
				       align='left'))
			])

			fig_table.update_layout(title_text='Inactive users from last month')

			st.plotly_chart(fig_table,use_container_width=True)


	################################################################

		with table_new_drop_dataset:

			fig_table_2 = make_subplots(
			    rows=1, cols=2,
			    shared_xaxes=True,
			    horizontal_spacing=0.1,
			    specs=[[{"type": "table"},{"type": "table"}]],
			    subplot_titles=['Newcomers', 'Droppers']

			)

			fig_table_2.add_trace(
			    go.Table(
			        header=dict(
			            values=['<b> User</b>','<b> Regarding</b>'],
			            line_color='darkslategray',
			            fill_color='darkgrey',
			            align=['left','center'],
			            font=dict(color='white', size=11)),
			        cells=dict(
			            values=[
			            [' ']+new_companies_from_this_week+new_weight_from_this_week+new_cover_users_from_this_week,
			            [' ']+['both' for i in range(len(new_companies_from_this_week))]+['weight' for i in range(len(new_weight_from_this_week))]+['covers' for i in range(len(new_cover_users_from_this_week))]],
			            line_color='darkslategray',
			    # 2-D list of colors for alternating rows
			            fill_color = [['white']+['lightblue' for i in range(len(new_companies_from_this_week))]+['#7EDBB4' for i in range(len(new_weight_from_this_week)) ]+['#88C87E' for i in range(len(new_cover_users_from_this_week))]*2],
			            align = ['left', 'center'],
			            font = dict(color = 'darkslategray', size = 12)
			        )
			    ),
			    row = 1,col = 1
			)

			fig_table_2.add_trace(
			    go.Table(
			        header=dict(
			            values=['<b> User</b>','<b> Regarding</b>'],
			            line_color='darkslategray',
			            fill_color='darkgrey',
			            align=['center','center'],
			            font=dict(color='white', size=11)
			        ),
			        cells=dict(
			            values=[[' ']+companies_becoming_inactives+weight_becoming_inactives+covers_users_becoming_inactives,
			                [' ']+['both' for i in range(len(companies_becoming_inactives))]+['weight' for i in range(len(weight_becoming_inactives))]+['covers' for i in range(len(covers_users_becoming_inactives))]
			            ],
			            line_color='darkslategray',
			    # 2-D list of colors for alternating rows
			            fill_color = [['white']+['#EB7C7C' for i in range(len(companies_becoming_inactives))]+['#F1C300' for i in range(len(weight_becoming_inactives)) ]+['#E69214' for i in range(len(covers_users_becoming_inactives))]*2],
			            align = ['left', 'center'],
			            font = dict(color = 'darkslategray', size = 12)
			        )
			    ),
			    row = 1,col = 2
			)

			fig_table_2.update_layout(title_text='Name of droppers and newcomers')
			st.plotly_chart(fig_table_2,use_container_width=True)
	############################################################

		with kpi_dataset:


			fig_kpi = make_subplots(
			    rows=1, cols=2,
			    shared_xaxes=True,
			    horizontal_spacing=0.1,
			    specs=[[{"type": "table"},{"type": "bar"}]],
			    subplot_titles=['', 'Turnover']

			)

			fig_kpi.add_trace(
			    go.Table(
			        header=dict(
			            values=['<b> Period</b>','<b>Active Users (ALL)</b>','<b>Active Users (COVERS)</b>','<b>Active Users (WEIGHT)</b>'],
			            line_color='darkslategray',
			            fill_color=headerColor,
			            align=['center','center'],
			            font=dict(color='white', size=11)
			        ),
			        cells=dict(
			            values=[
			            ['Last week', '2 weeks ago', 'New users','Dropping users'],
			            [len(active_companies_this_week),len(active_companies_last_week),len(new_companies_from_this_week),len(companies_becoming_inactives)],
			            [len(active_covers_this_week),len(active_covers_last_week),len(new_cover_users_from_this_week),len(covers_users_becoming_inactives)],
			            [len(active_weight_this_week),len(active_weight_last_week),len(new_weight_from_this_week),len(weight_becoming_inactives)]],
			            line_color='darkslategray',
			    # 2-D list of colors for alternating rows
			            fill_color = [[rowOddColor,rowOddColor,rowOddColor,]*4],
			            align = ['left', 'center'],
			            font = dict(color = 'darkslategray', size = 12)
			        )
			    ),
			    row = 1,col = 1

			)

			fig_kpi.add_trace(
			    go.Bar(
			        x=['All','Weight','Covers'],
			        y=[len(new_companies_from_this_week),len(new_weight_from_this_week),len(new_cover_users_from_this_week)],
			        customdata = [new_companies_from_this_week,new_weight_from_this_week,new_cover_users_from_this_week],
			        name='New users',
			        marker_color='lightblue',
			        text=[len(new_companies_from_this_week),len(new_weight_from_this_week),len(new_cover_users_from_this_week)],
			        textposition='auto',
			        hovertemplate = "users: %{customdata}",
			    ),
			    row=1,col=2
			)

			fig_kpi.add_trace(
			    go.Bar(
			        x=['All','Weight','Covers'],
			        y=[len(companies_becoming_inactives),len(weight_becoming_inactives),len(covers_users_becoming_inactives)],
			        customdata = [companies_becoming_inactives,weight_becoming_inactives,covers_users_becoming_inactives],
			        name='Dropping Users',
			        marker_color='crimson',
			        base=[-len(companies_becoming_inactives),-len(weight_becoming_inactives),-len(covers_users_becoming_inactives)],
			        text=[-len(companies_becoming_inactives),-len(weight_becoming_inactives),-len(covers_users_becoming_inactives)],
			        textposition='auto',
			        hovertemplate = "users: %{customdata}",
			    ),
			    row=1,col=2
			)

			fig_kpi.update_layout(title_text='Active Users Indicators')

			st.plotly_chart(fig_kpi,use_container_width=True)

		
	######################################################

		with fig_bar_dataset:

			fig_bar=go.Figure(data=[go.Bar(
			        x=['Current Subscribers','Current Trial','Current Pending'],
			        y=[len(active_subs_this_week),len(active_trial_this_week),len(active_pending_this_week)],
			        name='Active',
			        marker_color='green',
			        text=[len(active_subs_this_week),len(active_trial_this_week),len(active_pending_this_week)],
			        textposition='auto'
			    )]

			)

			fig_bar.add_trace(
			    go.Bar(
			        x=['Current Subscribers','Current Trial','Current Pending'],
			        y=[nb_current_subs-len(active_subs_this_week),nb_current_trial-len(active_trial_this_week),nb_current_pending-len(active_pending_this_week)],
			        name='Inactive',
			        marker_color='orange',
			        text=[nb_current_subs-len(active_subs_this_week),nb_current_trial-len(active_trial_this_week),nb_current_pending-len(active_pending_this_week)],
			        textposition='auto'
			    )
			)
			fig_bar.update_layout(barmode='stack')

			st.plotly_chart(fig_bar,use_container_width=True)

	######################################################

		with fig_pie_dataset:

			labels = ['Subscribers','Trial users','Pending users']
			values = [len(active_subs_this_week), len(active_trial_this_week), len(active_pending_this_week)]

			fig_pie=go.Figure(data=[go.Pie(
			        labels=labels,
			        values=values,
			        textinfo='label+percent',
			        name = "Last week users' status",
			        textfont_size=15
			    )]
			)

			st.plotly_chart(fig_pie,use_container_width=True)

	######################################################


		with line_chart_input_dataset:

			today = datetime.today()

			df_weight_2022 = df_rf3[(df_rf3['date_waste']<today.strftime("%Y-%m-%d"))&(df_rf3['date_waste']>='2022-01-10')]
			df_covers_2022 = df_covers[(df_covers['date_waste']<today.strftime("%Y-%m-%d"))&(df_covers['date_waste']>='2022-01-10')]
			df_covers_2022['data_entry'] = 1
			df_weight_2022['data_entry'] = 1
			df_graph_weight_2022 = df_weight_2022.groupby(['date_waste'])['data_entry'].sum().reset_index()
			df_graph_covers_2022 = df_covers_2022.groupby(['date_waste'])['data_entry'].sum().reset_index()

			df_weight_2022['name'] = 'a'
			df_covers_2022['name'] = 'a'

			df_weight_2022['date_waste'] = pd.to_datetime(df_weight_2022['date_waste'], format="%Y-%m-%d")
			df_covers_2022['date_waste'] = pd.to_datetime(df_covers_2022['date_waste'], format="%Y-%m-%d")



			df_weight_2022= df_weight_2022.groupby(['name', df_weight_2022['date_waste'].dt.strftime('%W')])['data_entry'].sum().reset_index()
			df_covers_2022= df_covers_2022.groupby(['name', df_covers_2022['date_waste'].dt.strftime('%W')])['data_entry'].sum().reset_index()

			df_all = pd.merge(df_graph_weight_2022,df_graph_covers_2022, how='outer', on='date_waste') 
			df_all= df_all.fillna(0)
			df_all['all_entries'] = df_all['data_entry_x']+df_all['data_entry_y']
			df_all = df_all.groupby(['date_waste'])['all_entries'].sum().reset_index()



			weight_list = list(df_weight_2022['data_entry'])
			var_weight = [' ']
			for i in range(len(weight_list)-1):
			    var_weight.append("{0:+.0f}".format(round(((weight_list[i+1]-weight_list[i])/weight_list[i])*100))+'%')


			covers_list = list(df_covers_2022['data_entry'])
			var_covers = [' ']
			for i in range(len(covers_list)-1):
			    var_covers.append("{0:+.0f}".format(round(((covers_list[i+1]-covers_list[i])/covers_list[i])*100))+'%')

			all_entries_list = [x + y for x, y in zip(weight_list, covers_list)]
			var_all_entries = [' ']
			for i in range(len(all_entries_list)-1):
			    var_all_entries.append("{0:+.0f}".format(round(((all_entries_list[i+1]-all_entries_list[i])/all_entries_list[i])*100))+'%')




			fig_line_chart = make_subplots(
			    rows=4, cols=1,
			    shared_xaxes=True,
			    vertical_spacing=0.04,
			    subplot_titles =['data entries per week',
			                     'covers entries overtime',
			                     'weight entries overtime',
			                     'all entries overtime'],
			    specs=[[{"type": "table"}],
			           [{"type": "scatter"}],
			           [{"type": "scatter"}],
			           [{"type": "scatter"}]]
			)



			fig_line_chart.add_trace(
			    go.Scatter(
			        x=df_all["date_waste"],
			        y=df_all['all_entries'],
			        mode="lines",
			        name="all data entries"
			    ),
			    row=4, col=1
			)


			fig_line_chart.add_trace(
			    go.Scatter(
			        x=df_graph_weight_2022["date_waste"],
			        y=df_graph_weight_2022["data_entry"],
			        mode="lines",
			        name="weight entries"
			    ),
			    row=3, col=1
			)

			fig_line_chart.add_trace(
			    go.Scatter(
			        x=df_graph_covers_2022["date_waste"],
			        y=df_graph_covers_2022["data_entry"],
			        mode="lines",
			        name="covers entries"
			    ),
			    row=2, col=1
			)

			fig_line_chart.add_trace(
			    go.Table(
			        header=dict(
			            values=["<b>week</b>", "<b>weight entries</b>", "<b>weight variation</b>",
			                    "<b>covers entries</b>", "<b>covers variation</b>", "<b>all entries</b>","<b>overall variation</b>"],
			            font=dict(size=12),
			            align="left"

			        ),
			        cells=dict(
			            values=[list(df_weight_2022['date_waste'][::-1]),
			                    list(df_weight_2022['data_entry'][::-1]),
			                    var_weight[::-1],
			                    list(df_covers_2022['data_entry'][::-1]),
			                    var_covers[::-1],
			                    all_entries_list[::-1],
			                    var_all_entries[::-1]],
			            fill_color = [['turquoise','lightblue','white']],
			            align = "left")
			    ),
			    row=1, col=1
			)
			fig_line_chart.update_layout(
			    height=800,
			    showlegend=False,
			    title_text="number of data entries",
			            )


			

			st.plotly_chart(fig_line_chart,use_container_width=True)
			
######################################################
######################################################
######################################################

	if selected == 'Outstanding data':

		with box_plot_dataset:

			df_rf3 = pd.read_csv('df_rf3.csv',sep=',')
			liste_company = list(df_rf3['id_company'].unique())

			cols_name = st.columns((1, 1))

			company = cols_name[0].selectbox('Choose a company',(liste_company))

			df_filtered_company = df_rf3[df_rf3['id_company']==company]
			liste_kitchen = list(df_filtered_company['kitchen'].unique())


			kitchen = cols_name[1].selectbox(
				'Choose a kitchen',
				(liste_kitchen)

			)



			cols_date = st.columns((1, 1))



			start_date = cols_date[0].date_input(
				"Select start date",
				date(2022, 5, 6)
			)

			end_date = cols_date[1].date_input(
				"Select end date",
				date(2022, 5, 6))

			df_box_plot = df_filtered_company[(df_filtered_company['date_waste']<=end_date.strftime("%Y-%m-%d"))&(df_filtered_company['date_waste']>=start_date.strftime("%Y-%m-%d"))&(df_filtered_company['kitchen']==kitchen)]

			fig_box_plot = px.box(df_box_plot, y="weight",color = 'shift' , points = 'all', title = '{} distribution'.format(company),hover_data = ['date_waste'])
			st.plotly_chart(fig_box_plot,use_container_width=True)
			
######################################################
######################################################
######################################################


if selected == 'Missing data':

	with individual_heatmap_dataset:

		df_rf3 = pd.read_csv('df_rf3.csv',sep=',')
		df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.floor('d')
		df_covers = pd.read_csv('df_covers.csv',sep=',')
		df_covers['date_waste'] = pd.to_datetime(df_covers['date_waste']).dt.floor('d')


		liste_company = list(df_rf3['id_company'].unique())
		cols_name = st.columns((1, 1))

		company = cols_name[0].selectbox('Choose a company',(liste_company))

		liste_kitchen = list(df_rf3[df_rf3['id_company']==company]['kitchen'].unique())

		kitchen = cols_name[1].selectbox(
			'Choose a kitchen',
			(liste_kitchen)

		)



		cols_date = st.columns((1, 1))



		startdate = cols_date[0].date_input(
			"Select start date",
			date(2022, 5, 6)
		)

		end_date = cols_date[1].date_input(
			"Select end date",
			date(2022, 5, 6))
		
		st.markdown('<p style="font-family:Courier; color:Black; font-size: 13px;">To keep the table readable, we advise you not to take a date range wider than 3 weeks.</p>',unsafe_allow_html=True)


		st.markdown('<p style="font-family:Courier; color:Black; font-size: 15px;">Legend:</p>',unsafe_allow_html=True)


		col_info_1, col_info_2, col_info_3,col_info_4 = st.columns(4)

		with col_info_1:
		    st.markdown(f'<p style="background-color:#F1F1F1;color:#030303;font-size:15px;border-radius:2%;<div style="text-align: center">- : no missing input</p>', unsafe_allow_html=True)

		with col_info_2:
		    st.markdown(f'<p style="background-color:#F2893C;color:#FFFCF8;font-size:15px;border-radius:2%;">C : cover input missing</p>', unsafe_allow_html=True)

		with col_info_3:
		    st.markdown(f'<p style="background-color:#EE4D34;color:#030303;font-size:15px;border-radius:2%;"> W : weight input missing </p>', unsafe_allow_html=True)


		with col_info_4:
		    st.markdown(f'<p style="background-color:#A8A8A8;color:#FFFCF8;font-size:15px;border-radius:2%;"> X : both inputs missing</p>', unsafe_allow_html=True)

		if (end_date-startdate).days > 21:
			st.markdown('<p style="font-family:Courier; color:Red; font-size: 15px;">Careful, your date range is too wide, you should lower it, otherwise the table will not be easily readable.</p>',unsafe_allow_html=True)


		df_covers = df_covers[df_covers['id_company'].str.startswith(company, na = False)].reset_index()
		df_covers = df_covers[df_covers['kitchen'].str.startswith(kitchen, na = False)].reset_index()
		df_rf3 = df_rf3[df_rf3['id_company'].str.startswith(company, na = False)].reset_index()
		df_rf3 = df_rf3[df_rf3['kitchen'].str.startswith(kitchen, na = False)].reset_index()

		df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.date
		df_covers['date_waste'] = pd.to_datetime(df_covers['date_waste']).dt.date

		###############################

		df_merged_left = pd.merge(df_rf3, df_covers, how='left', 
	    	left_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    	right_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    	suffixes=("__rf3", "__covers"),
	    	copy=True
		)
		df_merged_left.drop(columns=['id_waste'], inplace=True)
		df_merged_left.drop(columns=['date_added__rf3'], inplace=True)
		df_merged_left.drop(columns=['Unnamed: 0__rf3'], inplace=True)
		df_merged_left.drop(columns=['Unnamed: 0__covers'], inplace=True)
		#df_merged_left.drop(columns=['id_user__covers'], inplace=True)
		#df_merged_left.drop(columns=['id_user__rf3'], inplace=True)

		df_merged_left.drop(columns=['index__covers'], inplace=True)
		df_merged_left.drop(columns=['index__rf3'], inplace=True)

		df_merged_left.drop(columns=['date_added__covers'], inplace=True)
		#df_merged_left.drop(columns=['id_covers'], inplace=True)

		###############################

		df_merged_right = pd.merge(df_rf3, df_covers, how='right', 
	    	left_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    	right_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    	suffixes=("__rf3", "__covers"),
	    	copy=True
		)
		df_merged_right.drop(columns=['id_waste'], inplace=True)
		df_merged_right.drop(columns=['date_added__rf3'], inplace=True)
		df_merged_right.drop(columns=['Unnamed: 0__rf3'], inplace=True)
		df_merged_right.drop(columns=['Unnamed: 0__covers'], inplace=True)
		#df_merged_right.drop(columns=['id_user__covers'], inplace=True)
		#df_merged_right.drop(columns=['id_user__rf3'], inplace=True)
		df_merged_right.drop(columns=['index__covers'], inplace=True)
		df_merged_right.drop(columns=['index__rf3'], inplace=True)
		df_merged_right.drop(columns=['date_added__covers'], inplace=True)
		#df_merged_right.drop(columns=['id_covers'], inplace=True)
		
		print(df_merged_left)

		###############################

		df_missing_covers = df_merged_left[df_merged_left['covers'].isna()]
		df_missing_weight = df_merged_right[df_merged_right['weight'].isna()]

		df_missings = pd.concat([df_missing_covers,df_missing_weight])
		df_missings = df_missings.drop_duplicates()

		df_missings.loc[df_missings['weight'].isnull(),'heatmap'] = 0.25
		df_missings.loc[df_missings['covers'].isnull(),'heatmap'] = 1
		df_missings.loc[(df_missings['weight'].notnull())&(df_missings['covers'].notnull()), 'heatmap'] = 0.0

		df_missings.loc[df_missings['weight'].isnull(),'heatmap_text'] = 'W'
		df_missings.loc[df_missings['covers'].isnull(),'heatmap_text'] = 'C'
		df_missings.loc[(df_missings['weight'].notnull())&(df_missings['covers'].notnull()), 'heatmap_text'] = 'OK'

		###############################

		df_all_merged = pd.concat([df_merged_left,df_merged_right])
		df_all_merged.loc[df_all_merged['weight'].isnull(),'heatmap'] = 0.25
		df_all_merged.loc[df_all_merged['covers'].isnull(),'heatmap'] = 1
		df_all_merged.loc[(df_all_merged['weight'].notnull())&(df_all_merged['covers'].notnull()), 'heatmap'] = 0.0

		df_all_merged.loc[df_all_merged['weight'].isnull(),'heatmap_text'] = 'W'
		df_all_merged.loc[df_all_merged['covers'].isnull(),'heatmap_text'] = 'C'
		df_all_merged.loc[(df_all_merged['weight'].notnull())&(df_all_merged['covers'].notnull()), 'heatmap_text'] = 'OK'

		###############################

		x = ['Breakfast','Lunch','Dinner']


		y = [startdate.strftime("%b-%-d")]
		for i in range((end_date-startdate).days):
		    date = startdate+timedelta(days=i+1)
		    y.append(date.strftime("%b-%-d"))

		z = np.zeros((len(y),len(x)))
		z_text = [['-' for i in range(len(x))] for j in range(len(y))]

		###############################

		df_all_merged['date_waste'] = pd.to_datetime(df_all_merged['date_waste']).dt.floor('d')
		df_all_merged_filtered = df_all_merged[(df_all_merged['date_waste']>=startdate.strftime("%Y-%m-%d"))]
		df_all_merged_filtered = df_all_merged_filtered[(df_all_merged_filtered['date_waste']<=end_date.strftime("%Y-%m-%d"))]
		df_all_merged_filtered['date_waste'] = df_all_merged_filtered['date_waste'].dt.strftime("%b-%-d")

		df_missings['date_waste'] = pd.to_datetime(df_missings['date_waste']).dt.floor('d')
		df_missings_filtered = df_missings[df_missings['date_waste']>=startdate.strftime("%Y-%m-%d")]
		df_missings_filtered = df_missings_filtered[df_missings_filtered['date_waste']<=end_date.strftime("%Y-%m-%d")]
		df_missings_filtered['date_waste'] = df_missings_filtered['date_waste'].dt.strftime("%b-%-d")

		###############################

		for j in range(len(x)) :
		    df_all_merged_shift = df_all_merged_filtered[df_all_merged_filtered['shift']==x[j]]
		    dates_table = list(df_all_merged_shift['date_waste'].unique())
		    missing_dates = list(set(y) - set(dates_table))
		    for elt in range(len(missing_dates)) :
		        #print(z_text)
		        position_shift = x.index(x[j])
		        position_date = y.index(missing_dates[elt])
		        z[position_date,position_shift]=0.5
		        z_text[position_date][position_shift]='X'

		###############################


		liste_shift = list(df_missings_filtered['shift'])
		liste_date = list(df_missings_filtered['date_waste'])

		liste_heatmap = list(df_missings_filtered['heatmap'])
		liste_heatmap_text = list(df_missings_filtered['heatmap_text'])

		liste_shift = list(df_missings_filtered['shift'])
		liste_date = list(df_missings_filtered['date_waste'])

		liste_heatmap = list(df_missings_filtered['heatmap'])
		liste_heatmap_text = list(df_missings_filtered['heatmap_text'])


		for elt in range(len(liste_shift)) : 
		    position_shift = x.index(liste_shift[elt])
		    position_date = y.index(liste_date[elt])
		    z[position_date,position_shift]=liste_heatmap[elt]
		    z_text[position_date][position_shift]=liste_heatmap_text[elt]

		z = z.tolist()
		import plotly.figure_factory as ff



		color_schemes = [
		    ['#F1F1F1','#F1F1F1','#F1F1F1'],
		    ['#F14D29','#F14D29','#F14D29'],
		    ['#A8A8A8','#A8A8A8','#A8A8A8'],
		    ['#FF8A00','#FF8A00','#FF8A00']]

		colorscale = generateDiscreteColourScale(color_schemes)


		fig_individual_heatmap = ff.create_annotated_heatmap(z,x=x,y=y, colorscale=colorscale,annotation_text=z_text)

		st.plotly_chart(fig_individual_heatmap,use_container_width=True)
		
##############################################################
##############################################################
##############################################################

if selected == 'Impact Report':
	df_kitchen = pd.read_csv('df_kitchen.csv',sep=',')
	df_companies = pd.read_csv('df_companies.csv',sep=',')
	df_rf3 = pd.read_csv('df_rf3.csv',sep=',')
	df_covers = pd.read_csv('df_covers.csv',sep = ',')
	fit_raw_data = pd.read_csv('fit_raw_data.csv',sep=',')

	liste_company = list(df_rf3['id_company'].unique())


	col_impact_1, col_impact_2 = st.columns(2)

	with col_impact_1:

		focus_company =st.selectbox('Choose a company',(liste_company))


	df_filtered_company = df_rf3[df_rf3['id_company']==focus_company]
	liste_kitchen = list(df_filtered_company['kitchen'].unique())


	with col_impact_2:

		focus_kitchen = st.selectbox('Choose a kitchen',(liste_kitchen))

	col_dates_1, col_dates_2 = st.columns(2)


	with col_dates_2:
		end_date = st.date_input("Select end date for data collection",date(2022, 6, 6))

	with col_dates_1:
		starting_date = st.date_input("Select start date for data collection",date(2022, 6, 6))



	################################### GETTING THE BASELINE START AND END DATES

	df_baseline = fit_raw_data[fit_raw_data["id_company"].str.startswith(focus_company, na = False)].reset_index()
	df_baseline = fit_raw_data[fit_raw_data["kitchen"].str.startswith(focus_kitchen, na = False)].reset_index()

	df_baseline['baseline_start'] = pd.to_datetime(df_baseline['baseline_start'], format='%Y-%m-%d').dt.floor('d')
	df_baseline['baseline_end'] = pd.to_datetime(df_baseline['baseline_end'], format='%Y-%m-%d').dt.floor('d')

	baseline_start = df_baseline.loc[0]['baseline_start']
	baseline_end = df_baseline.loc[0]['baseline_end']

	list_baseline = [(baseline_end - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(((baseline_end-baseline_start).days)+1)]
	list_baseline.reverse()

	dates_to_remove = st.multiselect(
     'What day(s) do you want to take out of the baseline ?',
     list_baseline,
     [])

	list_baseline = [x for x in list_baseline if x not in dates_to_remove]

	################################### FILTERING FIT RAW DATA
	

	df_companies_hbrand = df_companies[df_companies["id_company"].str.startswith(focus_company, na = False)].reset_index(drop=True)
	df_kitchen_hbrand = df_kitchen[df_kitchen["id_company"].str.startswith(focus_company, na = False)].reset_index(drop=True)

	df_kitchen_hbrand = df_kitchen_hbrand[df_kitchen_hbrand["kitchen"].str.startswith(focus_kitchen, na = False)].reset_index(drop=True)

	user_data_hbrand = pd.merge(df_companies_hbrand,df_kitchen_hbrand,how = 'right',
	                    left_on=['id_company'],
	                    right_on=['id_company'],
	                    suffixes=("__companies", "__kitchen"),
	                    copy=True)

	fit_raw_data =user_data_hbrand.copy()

	fit_raw_data['id_company+kitchen']=fit_raw_data['id_company']+'__'+fit_raw_data['kitchen']
	user_data_hbrand['id_company+kitchen']=user_data_hbrand['id_company']+'__'+user_data_hbrand['kitchen']
	################################### FILTERING RF3
	df_rf3 = df_rf3[df_rf3["id_company"].str.startswith(focus_company, na = False)]
	df_rf3 = df_rf3[df_rf3["kitchen"].str.startswith(focus_kitchen, na = False)]
	df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.floor('d')
	df_rf3['id_company+kitchen']=df_rf3['id_company']+'__'+df_rf3['kitchen']
	df_rf3 = df_rf3[(df_rf3['date_waste']>=starting_date.strftime('%Y-%m-%d'))&(df_rf3['date_waste']<=end_date.strftime('%Y-%m-%d'))]
	################################### FILTERING COVERS
	df_covers = df_covers[df_covers["id_company"].str.startswith(focus_company, na = False)]
	df_covers = df_covers[df_covers["kitchen"].str.startswith(focus_kitchen, na = False)]
	df_covers['covers'] = df_covers['covers'].astype(int)
	df_covers['date_waste'] = pd.to_datetime(df_covers['date_waste']).dt.floor('d')
	df_covers['id_company+kitchen']=df_covers['id_company']+'__'+df_covers['kitchen']
	df_covers = df_covers[(df_covers['date_waste']>=starting_date.strftime('%Y-%m-%d'))&(df_covers['date_waste']<=end_date.strftime('%Y-%m-%d'))]
	################################### MERGING COVERS AND FOOD WASTE
	df_rf3['weight'] = df_rf3['weight'].astype(float)
	df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste'], format='%Y-%m-%d').dt.floor('d')
	df_covers['date_waste'] = pd.to_datetime(df_covers['date_waste'], format='%Y-%m-%d').dt.floor('d')
	df_covers = df_covers.groupby(['id_company','shift','date_waste','kitchen'])['covers'].sum().reset_index()
	df = pd.merge(df_rf3, df_covers,how = 'left',
	    left_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    right_on=['id_company', 'date_waste', 'kitchen', 'shift'],
	    suffixes=("__rf3", "__covers"),
	    copy=True
	)
	################################### DISPLAY FW RECORDED + TOTAL COVERS + TOTAL INPUTS
	df_tar = df[(df['date_waste']>=baseline_start.strftime("%Y-%m-%d"))&(df['date_waste']<=end_date.strftime("%Y-%m-%d"))]
	df_tar = df_tar.groupby(['id_company','kitchen','date_waste','shift','covers'])['weight'].sum().reset_index()
	col_metrics_fw_rec, col_tot_covers, col_nb_inputs = st.columns(3)
	col_metrics_fw_rec.metric("Food waste recorded (Kg)", round(df_tar.weight.sum()))
	col_tot_covers.metric("Total covers served", round(df_tar.covers.sum()))
	col_nb_inputs.metric("Number of food waste entries", df.shape[0])
	################################### DISPLAY BASELINE, AFTER BASELINE AND VARIATION
	company = focus_company+'__'+focus_kitchen
	df_baseline['id_company+kitchen'] = company
	waste_byday = df.copy()
	base = df_baseline.copy()
	base = base[(base['id_company+kitchen'] == company)].reset_index()
	#list_baseline = ['2022-01-27','2022-01-28','2022-02-03','2022-02-04','2022-02-05','2022-02-06','2022-02-07','2022-02-08','2022-02-09']
	waste_byday['date_waste'] = pd.to_datetime(waste_byday['date_waste'], format='%Y-%m-%d').dt.floor('d')
	waste_byday = waste_byday[waste_byday['date_waste'].isin(list_baseline)]
	waste_byday = waste_byday[(waste_byday['id_company+kitchen'] == company)]
	waste_byday['weight'] = waste_byday['weight'].astype(float)
	waste_byday = waste_byday.dropna()
	waste_byday = waste_byday.groupby(['id_company+kitchen','date_waste','covers','shift'])['weight'].sum().reset_index()
	waste_byday = waste_byday.groupby(['date_waste','shift'])['weight','covers'].sum().reset_index()
	waste_byday_bf = waste_byday[(waste_byday['shift'] == 'Breakfast')]
	waste_byday_lunch = waste_byday[(waste_byday['shift'] == 'Lunch')]
	waste_byday_din = waste_byday[(waste_byday['shift'] == 'Dinner')]
	covers_sum = waste_byday['covers'].sum()
	waste_sum = waste_byday['weight'].sum()
	print(covers_sum,waste_sum)
	#waste_sum_baseline_count +=waste_sum
	#covers_sum_baseline_count +=covers_sum
	if covers_sum == 0 or waste_sum ==0 : 
	    per_cover_avg = 0 
	else : 
	    per_cover_avg = round((waste_sum*1000)/covers_sum)
	covers_sum_bf = waste_byday_bf['covers'].sum()
	waste_sum_bf = waste_byday_bf['weight'].sum()
	#print(covers_sum_bf,waste_sum_bf)
	if waste_sum_bf == 0 or covers_sum_bf ==0 : 
	    per_cover_avg_bf = 0 
	else : 
	    per_cover_avg_bf = round((waste_sum_bf*1000)/covers_sum_bf)
	covers_sum_lunch = waste_byday_lunch['covers'].sum()
	waste_sum_lunch = waste_byday_lunch['weight'].sum()
	#print(covers_sum_lunch,waste_sum_lunch)
	if waste_sum_lunch == 0 or covers_sum_lunch ==0 : 
	    per_cover_avg_lunch = 0 
	else : 
	    per_cover_avg_lunch = round((waste_sum_lunch*1000)/covers_sum_lunch)
	covers_sum_din = waste_byday_din['covers'].sum()
	waste_sum_din = waste_byday_din['weight'].sum()
	if waste_sum_din == 0 or covers_sum_din ==0 : 
	    per_cover_avg_din = 0 
	else : 
	    per_cover_avg_din = round((waste_sum_din*1000)/covers_sum_din)
	print(waste_sum,covers_sum,per_cover_avg,per_cover_avg_bf,per_cover_avg_lunch,per_cover_avg_din,'breakfast '+'{}'.format(company)+ '= ' + '{}'.format(per_cover_avg_bf),
	'lunch '+'{}'.format(company)+ '= ' + '{}'.format(per_cover_avg_lunch),
	'dinner '+'{}'.format(company)+ '= ' + '{}'.format(per_cover_avg_din),
	'overall '+'{}'.format(company)+ '= ' + '{}'.format(per_cover_avg))
	def waste_test_p(company) : 
	    waste_byday = df.copy()
	    base = df_baseline.copy()
	    base = base[(base['id_company+kitchen'] == company)].reset_index()
	    baseline_end = base.loc[0]['baseline_end']
	    baseline_end = baseline_end.strftime("%Y-%m-%d")
	    baseline_end = datetime.strptime(baseline_end,'%Y-%m-%d')
	    waste_byday['date_waste'] = pd.to_datetime(waste_byday['date_waste'], format='%Y-%m-%d').dt.floor('d')
	    waste_byday = waste_byday[(waste_byday['date_waste'] > baseline_end )&(waste_byday['id_company+kitchen'] == company)&(waste_byday['date_waste'] <= end_date.strftime('%Y-%m-%d'))]
	    waste_byday['weight'] = waste_byday['weight'].astype(float)
	    waste_byday = waste_byday.dropna()
	    waste_byday = waste_byday.groupby(['id_company+kitchen','date_waste','covers','shift','kitchen'])['weight'].sum().reset_index()
	    waste_byday = waste_byday.groupby(['date_waste'])['weight','covers'].sum().reset_index()
	    covers_sum = waste_byday['covers'].sum()
	    waste_sum = waste_byday['weight'].sum()
	    print(company,"covers_sum: {}".format(covers_sum),"waste_sum: {}".format(waste_sum))
	    per_cover_avg = (waste_sum*1000)/covers_sum
	    per_cover_avg = round(per_cover_avg)
	    
	    return(per_cover_avg,covers_sum,waste_sum)
    
	per_cover_after_baseline = waste_test_p(company)[0]
	variation = round(((per_cover_after_baseline - per_cover_avg)/per_cover_avg)*100)
	col_per_cover_avg, col_per_cover_after_baseline = st.columns(2)
	col_per_cover_avg.metric("Baseline", str(per_cover_avg)+" g/cover")
	col_per_cover_after_baseline.metric("After baseline",str(per_cover_after_baseline)+" g/cover",str(variation)+"%",delta_color="inverse")
	################################### DF NEW
	baseline_df = pd.DataFrame(
	{"id_company+kitchen" : [company],
	"fw/cover baseline" : [per_cover_avg],
	"fw/cover baseline bf" : [per_cover_avg_bf],
	"fw/cover baseline lunch" : [per_cover_avg_lunch],
	"fw/cover baseline dinner" : [per_cover_avg_din]})
	df_new = pd.merge(df, baseline_df,how = 'left',
	    left_on=['id_company+kitchen'],
	    right_on=['id_company+kitchen'],
	    suffixes=("__df", "__baseline"),
	    copy=True
	)
	################################### PREPARE TABLE SAINGS PER MONTH
	kg_saved = df_new.copy()
	base = df_baseline.copy()
	base = base[(base['id_company+kitchen'] == company)].reset_index()
	baseline_end = base.loc[0]['baseline_end']
	coef = base.loc[0]['cost_kilo']
	baseline_end = baseline_end.strftime("%Y-%m-%d")
	baseline_end = datetime.strptime(baseline_end,'%Y-%m-%d')
	print(baseline_end)
	kg_saved = kg_saved[(kg_saved['date_waste'] > baseline_end)]
	################# ENTER BELOW THE END DATE 
	kg_saved = kg_saved[(kg_saved['date_waste'] <= end_date.strftime("%Y-%m-%d"))]
	kg_saved['date_waste'] = pd.to_datetime(kg_saved['date_waste']).dt.floor('d')
	kg_saved['weight'] = kg_saved['weight'].astype(float)
	kg_saved = kg_saved[kg_saved['id_company+kitchen'] == company]
	#Breakfast
	kg_saved_bf = kg_saved[(kg_saved['shift']=='Breakfast')]
	kg_saved_bf = kg_saved_bf.groupby(['id_company+kitchen','date_waste','covers','fw/cover baseline bf'])['weight'].sum().reset_index()
	kg_saved_bf = kg_saved_bf.groupby(['id_company+kitchen','date_waste','fw/cover baseline bf'])['weight','covers'].sum().reset_index()
	kg_saved_bf['fw/cover'] = (kg_saved_bf['weight']*1000)/kg_saved_bf['covers']
	kg_saved_bf['kg_saved'] = ((kg_saved_bf['fw/cover baseline bf'] - kg_saved_bf['fw/cover'])*kg_saved_bf['covers'])/1000
	#Lunch
	kg_saved_lunch = kg_saved[(kg_saved['shift']=='Lunch')]
	kg_saved_lunch = kg_saved_lunch.groupby(['id_company+kitchen','date_waste','covers','fw/cover baseline lunch'])['weight'].sum().reset_index()
	kg_saved_lunch = kg_saved_lunch.groupby(['id_company+kitchen','date_waste','fw/cover baseline lunch'])['weight','covers'].sum().reset_index()
	kg_saved_lunch['fw/cover'] = (kg_saved_lunch['weight']*1000)/kg_saved_lunch['covers']
	kg_saved_lunch['kg_saved'] = ((kg_saved_lunch['fw/cover baseline lunch'] - kg_saved_lunch['fw/cover'])*kg_saved_lunch['covers'])/1000
	#Dinner
	kg_saved_din = kg_saved[(kg_saved['shift']=='Dinner')]
	kg_saved_din = kg_saved_din.groupby(['id_company+kitchen','date_waste','covers','fw/cover baseline dinner'])['weight'].sum().reset_index()
	kg_saved_din = kg_saved_din.groupby(['id_company+kitchen','date_waste','fw/cover baseline dinner'])['weight','covers'].sum().reset_index()
	kg_saved_din['fw/cover'] = (kg_saved_din['weight']*1000)/kg_saved_din['covers']
	kg_saved_din['kg_saved'] = ((kg_saved_din['fw/cover baseline dinner'] - kg_saved_din['fw/cover'])*kg_saved_din['covers'])/1000
	kg_saved_bf['month'] = pd.DatetimeIndex(kg_saved_bf['date_waste']).month
	kg_saved_lunch['month'] = pd.DatetimeIndex(kg_saved_lunch['date_waste']).month
	kg_saved_din['month'] = pd.DatetimeIndex(kg_saved_din['date_waste']).month
	kg_saved_bf["month"].replace({ 1 : "January",
	                            2: "February",
	                            3: "March",
	                            4: "April",
	                            5: "May",
	                            6: "June",
	                            7: "July",
	                            8: "August",
	                            9: "September",
	                            10: "October",
	                            11: "November",
	                            12 : "December"}, inplace=True)
	kg_saved_lunch["month"].replace({ 1 : "January",
	                            2: "February",
	                            3: "March",
	                            4: "April",
	                            5: "May",
	                            6: "June",
	                            7: "July",
	                            8: "August",
	                            9: "September",
	                            10: "October",
	                            11: "November",
	                            12 : "December"}, inplace=True)
	kg_saved_din["month"].replace({ 1 : "January",
	                            2: "February",
	                            3: "March",
	                            4: "April",
	                            5: "May",
	                            6: "June",
	                            7: "July",
	                            8: "August",
	                            9: "September",
	                            10: "October",
	                            11: "November",
	                            12 : "December"}, inplace=True)
	try : 
	    kg_saved_bf = kg_saved_bf.groupby(['month'])['kg_saved'].sum().reset_index()
	    kg_saved_bf=kg_saved_bf.rename(columns={'kg_saved':'Breakfast'})
	except :
	    kg_saved_bf = pd.DataFrame(columns=['month','Breakfast'])
	try:
	    kg_saved_lunch = kg_saved_lunch.groupby(['month'])['kg_saved'].sum().reset_index()
	    kg_saved_lunch=kg_saved_lunch.rename(columns={'kg_saved':'Lunch'})
	except :
	    kg_saved_lunch = pd.DataFrame(columns=['month','Lunch'])
	try:
	    kg_saved_din = kg_saved_din.groupby(['month'])['kg_saved'].sum().reset_index()
	    kg_saved_din=kg_saved_din.rename(columns={'kg_saved':'Dinner'})
	except:
	    kg_saved_din = pd.DataFrame(columns=['month','Dinner'])
	from functools import reduce
	data_frame = [kg_saved_bf,kg_saved_lunch,kg_saved_din]
	df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['month'],
	                                        how='outer'), data_frame)
	df_merged = df_merged.fillna(0)
	df_merged['total_saved'] = (df_merged['Breakfast']+df_merged['Lunch']+df_merged['Dinner']).round()
	df_merged['Breakfast'] = df_merged['Breakfast'].round()
	df_merged['Lunch'] = df_merged['Lunch'].round()
	df_merged['Dinner'] = df_merged['Dinner'].round()
	df_merged['total_saved'] = df_merged['total_saved'].round()
	################################### DISPLAY SAVINGS
	total_food_saved = round(df_merged['total_saved'].sum())
	total_CO2_saved = round(df_merged['total_saved'].sum()*2.5)
	total_USD_saved = round(df_merged['total_saved'].sum()*coef)
	col_total_food_saved, col_total_CO2_saved, col_total_USD_saved = st.columns(3)
	col_total_food_saved.metric("Total food saved", str(total_food_saved)+" Kg")
	col_total_CO2_saved.metric("Total CO2 not emitted",str(total_CO2_saved)+" CO2 eq.")
	col_total_USD_saved.metric("Total USD saved",str(total_USD_saved)+" USD")
	################################### DISPLAY TABLE KG SAVED PER MONTH
	fig_impact_table = go.Figure(data=[go.Table(
	    header=dict(values=list(df_merged.columns),
	                fill_color='pink',
	                align='left'),
	    cells=dict(values=[df_merged.month, df_merged.Breakfast, df_merged.Lunch, df_merged.Dinner,df_merged.total_saved],
	               fill_color='lightgrey',
	               align='left'))
	])
	fig_impact_table.update_layout(title_text="food saved by month and per shift (Kg)")
	st.plotly_chart(fig_impact_table,use_container_width=True)
	################################### DISPLAY BAR GRAPH PER DAY OF THE WEEK
	waste_byday = df_new.copy()
	waste_byday['date_waste'] = pd.to_datetime(waste_byday['date_waste'], format='%Y-%m-%d').dt.floor('d')
	lundi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 0]
	lundi['week_day'] = 'Monday'
	mardi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 1]
	mardi['week_day'] = 'Tuesday'
	mercredi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 2]
	mercredi['week_day'] = 'Wednesday'
	jeudi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 3]
	jeudi['week_day'] = 'Thursday'
	vendredi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 4]
	vendredi['week_day'] = 'Friday'
	samedi = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 5]
	samedi['week_day'] = 'Saturday'
	dimanche = waste_byday.loc[waste_byday['date_waste'].dt.weekday == 6]
	dimanche['week_day'] = 'Sunday'
	waste_byday = pd.concat([lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche])
	waste_byday = waste_byday.groupby(['id_company','week_day','date_waste','covers'])['weight'].sum().reset_index()
	waste_byday = waste_byday.groupby(['id_company','week_day'])['weight','covers'].sum().reset_index()
	waste_byday['weight'] = waste_byday['weight']/waste_byday['covers']
	waste_byday['weight'] = waste_byday['weight']*1000
	waste_byday['weight'] = waste_byday['weight'].round()
	waste_byday_fig = px.bar(waste_byday, x='week_day', y='weight', title='Waste/cover per day of the week - {}'.format(company),
	                labels={'weight': 'weight/cover (g/cover)',
	                        'week_day': 'Day',
	                        'id_company': 'Company'},
	                category_orders={"week_day": ["Monday", "Tuesday", "Wednesday", "Thursday","Friday",'Saturday','Sunday']},
	                text = 'weight')
	waste_byday_fig.update_traces(marker_color='thistle')
	st.plotly_chart(waste_byday_fig,use_container_width=True)

