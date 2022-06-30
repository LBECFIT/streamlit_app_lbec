import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta


fit_raw_data = pd.read_csv('fit_raw_data.csv',sep=',')
fit_raw_data['id_company+kitchen']=fit_raw_data['id_company']+'__'+fit_raw_data['kitchen']
fit_raw_data['stop_date'] = pd.to_datetime(fit_raw_data['stop_date']).dt.floor('d')

df_rf3 = pd.read_csv('df_rf3.csv',sep=',')
df_rf3['date_waste'] = pd.to_datetime(df_rf3['date_waste']).dt.floor('d')

df_covers = pd.read_csv('df_covers.csv',sep=',')
df_covers['covers'] = df_covers['covers'].astype(int)
df_covers['date_waste'] = pd.to_datetime(df_covers['date_waste']).dt.floor('d')
df_covers['id_company+kitchen']=df_covers['id_company']+'__'+df_covers['kitchen']








df_current_subs = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
df_current_subs = df_current_subs[df_current_subs['Current Type']=='subscribe']
df_current_subs = df_current_subs[df_current_subs['FIT Status']=='ongoing']

current_subs = list(df_current_subs['id_company+kitchen'])
nb_current_subs = len(current_subs)

#Get the current trial users  

df_current_trial = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
df_current_trial = df_current_trial[df_current_trial['Current Type']=='trial']
df_current_trial = df_current_trial[df_current_trial['FIT Status']=='ongoing']

current_trial = list(df_current_trial['id_company+kitchen'])
nb_current_trial = len(current_trial)

#Get users that stopped subscribing (pending)

df_stop_subs = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
df_stop_subs = df_stop_subs[df_stop_subs['Current Type']=='pending']
df_stop_subs = df_stop_subs[df_stop_subs['FIT Status']=='ongoing']

current_pending = list(df_stop_subs['id_company+kitchen'])
nb_current_pending = len(current_pending)

current_users =list(set(current_pending+current_subs+current_trial))
nb_current_users = len(current_users)


############################################################################

today = datetime.today()
yesterday = today-timedelta(days=1)
one_week_ago = today-timedelta(days=7)
two_weeks_ago = today-timedelta(days=14)


df_rf3['id_company+kitchen']=df_rf3['id_company']+'__'+df_rf3['kitchen']

df_this_week = df_rf3[(df_rf3['date_waste']<today.strftime("%Y-%m-%d"))&(df_rf3['date_waste']>=one_week_ago.strftime("%Y-%m-%d"))]
df_last_week = df_rf3[(df_rf3['date_waste']<one_week_ago.strftime("%Y-%m-%d"))&(df_rf3['date_waste']>=two_weeks_ago.strftime("%Y-%m-%d"))]

active_weight_this_week = list(df_this_week['id_company+kitchen'].unique())
active_weight_last_week = list(df_last_week['id_company+kitchen'].unique())




new_weight_from_this_week = list(set(active_weight_this_week)-set(active_weight_last_week))
weight_becoming_inactives = list(set(active_weight_last_week)-set(active_weight_this_week))

############################################################################


#get list of weight users that are currently subscribing
subs_weight_raw_data = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
subs_weight_raw_data = subs_weight_raw_data[subs_weight_raw_data['Current Type']=='subscribe']
subs_weight_raw_data = subs_weight_raw_data[subs_weight_raw_data['FIT Status']=='ongoing']
subs_weight_raw_data_list = list(subs_weight_raw_data['id_company+kitchen'].unique())
active_weight_subs_this_week = list(set(subs_weight_raw_data_list)&set(active_weight_this_week))
active_weight_subs_last_week = list(set(subs_weight_raw_data_list)&set(active_weight_last_week))


#get list of weight users that are currently pending
pending_weight_raw_data = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
pending_weight_raw_data = pending_weight_raw_data[pending_weight_raw_data['Current Type']=='pending']
pending_weight_raw_data = pending_weight_raw_data[pending_weight_raw_data['FIT Status']=='ongoing']
pending_weight_raw_data_list = list(pending_weight_raw_data['id_company+kitchen'].unique())
active_weight_pending_this_week = list(set(pending_weight_raw_data_list)&set(active_weight_this_week))
active_weight_pending_last_week = list(set(pending_weight_raw_data_list)&set(active_weight_last_week))

#get list of weight users that are currently on trial
trial_weight_raw_data = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
trial_weight_raw_data = trial_weight_raw_data[trial_weight_raw_data['Current Type']=='trial']
trial_weight_raw_data = trial_weight_raw_data[trial_weight_raw_data['FIT Status']=='ongoing']
trial_weight_raw_data_list = list(trial_weight_raw_data['id_company+kitchen'].unique())
active_weight_trial_this_week = list(set(trial_weight_raw_data_list)&set(active_weight_this_week))
active_weight_trial_last_week = list(set(trial_weight_raw_data_list)&set(active_weight_last_week))

############################################################################


active_companies_that_are_subs = list(set(active_weight_this_week)-set(current_pending)-set(current_trial))
active_companies_that_stopped_sub = list(set(active_weight_this_week)-set(current_subs)-set(current_trial))
active_companies_that_are_trial = list(set(active_weight_this_week)-set(current_subs)-set(current_pending))

############################################################################


covers_this_week = df_covers[(df_covers['date_waste']<today.strftime("%Y-%m-%d"))&(df_covers['date_waste']>=one_week_ago.strftime("%Y-%m-%d"))]
covers_last_week = df_covers[(df_covers['date_waste']<one_week_ago.strftime("%Y-%m-%d"))&(df_covers['date_waste']>=two_weeks_ago.strftime("%Y-%m-%d"))]


active_covers_this_week = list(covers_this_week['id_company+kitchen'].unique())
active_covers_last_week = list(covers_last_week['id_company+kitchen'].unique())

new_cover_users_from_this_week = list(set(active_covers_this_week)-set(active_covers_last_week))
covers_users_becoming_inactives = list(set(active_covers_last_week)-set(active_covers_this_week))

############################################################################


def get_current_type(current_type,list_this_week,list_last_week):
    df_current_type = fit_raw_data.loc[(fit_raw_data['Origin']!='Sample')&(fit_raw_data['Origin'] != 'Online workshop')]
    df_current_type = df_current_type[df_current_type['Current Type']==current_type]
    df_current_type = df_current_type[df_current_type['FIT Status']=='ongoing']
    current_type_list = list(df_current_type['id_company+kitchen'].unique())
    current_type_this_week = list(set(current_type_list)&set(list_this_week))
    current_type_last_week = list(set(current_type_list)&set(list_last_week))
    return(current_type_list,current_type_this_week,current_type_last_week)

#get list of cover users that are currently pending
pending_covers_raw_data_list,active_covers_pending_this_week,active_covers_pending_last_week = get_current_type('pending',active_covers_this_week,active_covers_last_week)

#get list of cover users that are currently trial
trial_covers_raw_data_list,active_covers_trial_this_week,active_covers_trial_last_week = get_current_type('trial',active_covers_this_week,active_covers_last_week)

#get list of cover users that are currently subs
subs_covers_raw_data_list,active_covers_subs_this_week,active_covers_subs_last_week = get_current_type('subscribe',active_covers_this_week,active_covers_last_week)

############################################################################

active_companies_this_week = list(set(active_covers_this_week+active_weight_this_week))
active_companies_last_week = list(set(active_covers_last_week+active_weight_last_week))

new_companies_from_this_week = list(set(active_companies_this_week)-set(active_companies_last_week))
companies_becoming_inactives = list(set(covers_users_becoming_inactives)&set(weight_becoming_inactives))

############################################################################

active_trial_this_week = set(active_covers_trial_this_week).union(set(active_weight_trial_this_week))
active_pending_this_week = set(active_covers_pending_this_week).union(set(active_weight_pending_this_week))
active_subs_this_week = set(active_covers_subs_this_week).union(set(active_weight_subs_this_week))

############################################################################

four_weeks_ago = today-timedelta(days=28)

df_weight_this_month = df_rf3[(df_rf3['date_waste']<today.strftime("%Y-%m-%d"))&(df_rf3['date_waste']>=four_weeks_ago.strftime("%Y-%m-%d"))]
df_covers_this_month = df_covers[(df_covers['date_waste']<today.strftime("%Y-%m-%d"))&(df_covers['date_waste']>=four_weeks_ago.strftime("%Y-%m-%d"))]


active_weight_this_month = list(df_weight_this_month['id_company+kitchen'].unique())
active_covers_this_month = list(df_covers_this_month['id_company+kitchen'].unique())

active_users_this_month = list(set(active_weight_this_month+active_covers_this_month))
inactive_users_last_month = list(set(current_users)-set(active_users_this_month))

fit_inactive_this_month = fit_raw_data[fit_raw_data['id_company+kitchen'].isin(inactive_users_last_month)]



############################################################################

