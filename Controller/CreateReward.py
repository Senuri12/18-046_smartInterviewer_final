# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:54:23 2018

@author: ASUS
"""
import importlib
import numpy as np
from xml.etree import ElementTree as ET
from Controller import ConnectionToNeo4j,vari



def rewardForQuestion(languageName, subName, nodeId, difficultyLevel, QuestionAsked):

    print("ANURUDDHA RESULTS")
    # print(languageName)
    print(nodeId)
    print(difficultyLevel)

    importlib.reload(vari)
    userid = vari.userId

    # print(vari.Ftesting1(aa))
    # print(vari.Vtesting1(bb))
    # print(vari.Atesting1(cc))

    # facial = vari.Ftesting1(aa) #have to remove
    # voice = vari.Vtesting1(bb) #have to remove
    # answer = vari.Atesting1(cc) #have to remove
    facial = 15
    voice = 15
    answer = 40

    total = (facial + voice + answer)

    print("Total = ", total)
    total = int(total)

    if (0 < total <= 20):
        state = 1
        print("State = ", state)

    elif (21 < total <= 40):
        state = 2
        print("State = ", state)

    elif (41 < total <= 60):
        state = 3
        print("State = ", state)

    elif (61 < total <= 80):
        state = 4
        print("State = ", state)

    else:
        state = 5
        print("State = ", state)

    # -----------------------------------------------------------------------------------
    # Get the latest updated q-table from ontology - only for shown

    print("--------Output 1-------------------------------------------")
    print("Latest updated q-table regarding asked knowledge area \n", ConnectionToNeo4j.createQtable1(languageName, subName))
    print(type(ConnectionToNeo4j.createQtable1(languageName, subName)))


    # data = R
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

    # Get the String array matrix from ontology - split
    I = np.array(ConnectionToNeo4j.createQtable1(languageName, subName)).tolist()
    Z = I.split(" ")
    # QuestionAsked = "new"
    # print("Z-spit krapu 1 \n", Z)
    # print(type(Z)) --> Gives List

    # to remove the []
    number = " ".join(Z)
    # print("this remove[] \n", number)
    # print(type(number)) --> Gives String

    if QuestionAsked == "existing":
        R= ConnectionToNeo4j.createQtable1(languageName, subName)

    else:
        R = np.matrix([[0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0],
                       [0.0, 0.0, 0.0, 0.0, 0.0]])




    print("------Rewarding process is starting----------------------------------------")
    # Q matrix
    Q = np.matrix(np.zeros([5, 5]))

    if state == 5:
        R[0, 4] = total
    elif state == 4:
        R[1, 3] = total
    elif state == 3:
        R[2, 2] = total
    elif state == 2:
        R[3, 1] = total
    else:
        R[4, 0] = total

    # Gamma (learning parameter).
    gamma = 0.8

    # Initial state
    if state == 5:
        initial_state = 4
    else:
        initial_state = state

    # initial_state = state
    # This function returns all available actions in the state given as an argument
    def available_actions(state):
        current_state_row = R[state,]
        av_act = np.where(current_state_row >= 0)[1]
        return av_act

    # Get available actions in the current state
    available_act = available_actions(initial_state)

    # This function chooses at random which action to be performed within the range
    def sample_next_action(available_actions_range):
        next_action = int(np.random.choice(available_act, 1))
        return next_action

    # Sample next action to be performed
    action = sample_next_action(available_act)

    # This function updates the Q matrix
    def update(current_state, action, gamma):
        max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

        if max_index.shape[0] > 1:
            max_index = int(np.random.choice(max_index, size=1))
        else:
            max_index = int(max_index)
        max_value = Q[action, max_index]

        # Q learning formula - Reward Function
        Q[current_state, action] = R[current_state, action] + gamma * max_value

    # Update Q matrix
    update(initial_state, action, gamma)

    # -------------------------------------------------------------------------------
    # Create the reward value

    # iterarte the process
    for i in range(100):
        current_state = np.random.randint(0, int(Q.shape[0]))
        available_act = available_actions(current_state)
        action = sample_next_action(available_act)
        update(current_state, action, gamma)

    print("New q table \n", Q)

    # ----------------------------------------------------------------------------------------------------------------
    # Save the Q-metrix in text file

    print(" Maximum reward value:")
    print(np.max(Q))
    T = Q * 100 / np.max(Q)
    print("\n Convert q-table to precentage scale")
    print(T)
    # np.savetxt('Database/text.txt', T, fmt='%f')

    print("--------Output 2-------------------------------------------")
    print("Find the Difficulty level index, containing the max reward")

    newOne = np.unravel_index(np.argmax(T, axis=None), T.shape)
    # print(type(newOne)) --> Gives Tuple
    print(newOne)

    [m,n] = newOne
    print(n)
    # print(type(n)) --> Gives numpy.int32
    convertStr = str(n)
    # print(type(convertStr)) --> Gives String

    if convertStr == "0" or convertStr == "1":
        rewardState = "hard"

    elif convertStr == "2":
        rewardState = "medium"

    else:
        rewardState = "easy"


    print(rewardState)


    # -------------------------------------------------------
    # send to ontology
    print("\n Then the updated q-table is sent to the ontology")

    qTableCreated = str(T)

    ConnectionToNeo4j.sendQtable(languageName, subName, qTableCreated)
    # -------------------------------------------------------------------------------


    # --update the ontology---------------------------
    print("--------Output 3-------------------------------------------")
    print("Get the existing difficulty list \n")

    print(ConnectionToNeo4j.getDifficultyList(userid, languageName, difficultyLevel))

    getDiffList = str(ConnectionToNeo4j.getDifficultyList(userid, languageName, difficultyLevel))
    print(getDiffList)
    # print(type(getDiffList))



    getDiffList2 = getDiffList.split(',')
    getDiffList2.remove(str(nodeId))
    getDiffList3 = list(map(int, getDiffList2))
    print("then removed node and int it \n", getDiffList3)
    # print(type(getDiffList3)) --> Gives list
    str_getDiffList3 = ','.join(str(e) for e in getDiffList3)
    print("Convert to String to save \n", str_getDiffList3)
    # print(type(str_getDiffList3)) --> Gives string


    # update the existing category with new value
    ConnectionToNeo4j.sendExistingDifficultyList(userid, languageName, difficultyLevel, str_getDiffList3)

    print("\n --------Output 4-------------------------------------------")
    print("Get the new difficulty list to update \n")

    # get the new category list

    getNewList = ConnectionToNeo4j.getNewRewardList(userid, languageName, rewardState)
    print(ConnectionToNeo4j.getNewRewardList(userid, languageName, rewardState))
    # print(type(getNewList)) --> Gives string
    # print(type(nodeId)) --> Gives Integer

    str_nodeId = str(nodeId)
    # print(type(str_nodeId)) --> Gives String

    getnewList = getNewList.split(',')
    getnewList.append(str_nodeId)
    print("append new nod = ", getnewList)

    str_getDiffList4 = ','.join(str(e) for e in getnewList)
    print("converted to string =", str_getDiffList4)

    print("Appended new list \n", str_getDiffList4)

    # send to the new list to the new category

    ConnectionToNeo4j.sendNewDifficultyList(userid, languageName, rewardState, str_getDiffList4)




# rewardForQuestion("python","hierarchical inheritance",17,"easy","new")