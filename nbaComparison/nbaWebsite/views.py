import time

from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
import pandas as pd
from nba_api.stats import endpoints
from nba_api.stats.static import players
import numpy as np
import requests
from .forms import QueryForm
from .models import Query

def result(request):
    comparisons = Query.objects.all()
    for query in comparisons:
        playerOneYear = query.yearOptionOne
        playerTwoYear = query.yearOptionTwo
        playerOneID = find_id(query.playerNameOne)
        playerTwoID = find_id(query.playerNameTwo)
        playerOneStats = get_season_totals(playerOneID)
        playerTwoStats = get_season_totals(playerTwoID)
        filteredPlayerOne = filterPlayers(playerOneStats,playerOneYear)
        filteredPlayerTwo = filterPlayers(playerTwoStats,playerTwoYear)

        #player1 stats
        gp1 = filteredPlayerOne.iloc[0,0]
        fgp1 = filteredPlayerOne.iloc[0,1]
        fg3p1 =filteredPlayerOne.iloc[0,2]
        ftp1 = filteredPlayerOne.iloc[0,3]
        reb1 = filteredPlayerOne.iloc[0, 4]
        ast1 = filteredPlayerOne.iloc[0, 5]
        pts1 = filteredPlayerOne.iloc[0, 6]

        #player2 stats
        gp2 = filteredPlayerTwo.iloc[0, 0]
        fgp2 = filteredPlayerTwo.iloc[0, 1]
        fg3p2 = filteredPlayerTwo.iloc[0, 2]
        ftp2 = filteredPlayerTwo.iloc[0, 3]
        reb2 = filteredPlayerTwo.iloc[0, 4]
        ast2 = filteredPlayerTwo.iloc[0, 5]
        pts2 = filteredPlayerTwo.iloc[0, 6]


    print(playerOneID)
    print(playerTwoID)
    print(filteredPlayerOne)
    print(filteredPlayerTwo)

    return render(request, 'nbaWebsite/result.html',{'comparisons':comparisons, 'playerOneID':playerOneID, 'playerTwoID':playerTwoID, 'playerOneStats':playerOneStats,'playerTwoStats':playerTwoStats, 'filteredPlayerOne':filteredPlayerOne,'filteredPlayerTwo':filteredPlayerTwo, 'gp1':gp1, 'gp2':gp2, 'fgp1':fgp1,'fgp2':fgp2,'fg3p1':fg3p1,'fg3p2':fg3p2,'ftp1':ftp1,'ftp2':ftp2,'reb1':reb2,'ast1':ast1,'ast2':ast2,'pts1':pts1,'pts2':pts2})



def query(request):
    form=QueryForm()
    if request.method=="POST":
        form=QueryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'nbaWebsite/query.html')


    context={'form':form}
    return render(request, 'nbaWebsite/query.html',context)


def home(request):
    return render(request,'nbaWebsite/home.html')

def main(request):
    playerOneID = find_id(Query.object.playerNameOne)
    print(playerOneID)

def find_id(user_input):
    lower_user_input = str(user_input).lower()
    player_data_frame = pd.DataFrame(players.get_players())
    player_data_frame["lower_full_name"] = player_data_frame["full_name"].str.lower()
    filtered_frame = player_data_frame[player_data_frame.lower_full_name == lower_user_input]
    user_player_id = filtered_frame.iloc[0, 0]
    time.sleep(10)
    return user_player_id

def get_season_totals(user_player_id):
    data = endpoints.PlayerCareerStats(player_id=user_player_id).get_data_frames()

    career_totals_all_star_season = data[0]
    time.sleep(10)
    return career_totals_all_star_season

def filterPlayers(playerStats, playerYear):
    filtered_frame_player = playerStats[playerStats.SEASON_ID == playerYear]
    filtered_frame_player = filtered_frame_player[["GP","FG_PCT","FG3_PCT","FT_PCT","REB","AST","PTS"]]
    return filtered_frame_player