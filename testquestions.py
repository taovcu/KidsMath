testcases = {
                'alltestdone':
                    [{'questiontext':'', 'expectedAns':'', 'ansList':['','','','']}],
                'AddObjectTestCases':
                    [
                    {'questiontext': 'Bob has 3 pears, Joy has 4 pears, how many pears do they have in total?', 'expectedAns': '7', 'ansList': ['1', '2', '4', '7'], 'pictures':[['BobSmall'], ['pear']*3, ['JoySmall'], ['pear']*4]},
                    {'questiontext': 'Bob has 6 apples, Joy has 7 apples, how many apples do they have in total?', 'expectedAns':'13', 'ansList':['11', '13', '15', '21'], 'pictures':[['BobSmall'], ['red-apple']*6, ['JoySmall'], ['red-apple']*7]}
                    ],
                'AddTestCases':
                    [{'questiontext':'Add numbers \n 4 + 5 = ?', 'expectedAns':'9', 'ansList':['6', '9', '12', '13']},
                     {'questiontext':'Add numbers \n 5 + 8 = ?', 'expectedAns':'13', 'ansList':['6', '9', '12', '13']}
                    ],
                'Number2NameCases':
                    [{'questiontext':'Translate Digit to English words \n\n 7', 'expectedAns':'Seven', 'ansList':['Five', 'Seven', 'Nine', 'Eleven']},
                     {'questiontext':'Translate Digit to English words \n\n 11', 'expectedAns':'Eleven', 'ansList':['Five', 'Seven', 'Nine', 'Eleven']}
                    ],
                'Name2NumberCases':
                    [{'questiontext':'Translate English words to digit \n\n Eight', 'expectedAns':'8', 'ansList':['3', '5', '8', '11']}],
                'countNumby10sCases':
                    [{'questiontext':'Count number by tens in sequence \n\n Count from 10 to 100 by tens', 'expectedAns':'10 20 30 40 50 60 70 80 90 100', 'ansList':['10 20 30 40 50 60 70 80 90 100', '10 20 30 40 60 70  80  90 100', '10 20 30  50  60 70 80 90 100', '20  30  40 50 60 70 80 90 100']}],
                'countNumfromXCases':
                    [{'questiontext':'Count number from 6 to 13', 'expectedAns':'6 7 8 9 10 11 12 13', 'ansList':['6 7  9 10 11 12 13', '6  7  8 9 10 11 13', '7  8 9 10  11 12 13', '6 7 8 9 10 11 12 13']}],
                'writeNumCases':
                    [{'questiontext':'Write number 8 in English word', 'expectedAns':'Eight', 'ansList':['Seven', 'Eight', 'Nine', 'Ten']}],
                'countObjectCases':
                    [{'questiontext':'How many pears do you see?', 'expectedAns':'6', 'ansList':['5', '6', '7', '8'], 'pictures':[['pear']*6]}],
                'compareObjectCases':
                    [{'questiontext':'Who has more pears, Joy or Bob?', 'expectedAns':'Joy', 'ansList':['Joy', 'Bob', '', ''], 'pictures':[['JoySmall'], ['pear']*8, ['BobSmall'], ['pear']*6]}],
                'compareNumCases':
                    [{'questiontext':'Choose the greatest number', 'expectedAns':'12', 'ansList':['6', '9', '12', '10']}],
                'subtractTestCases':
                    [
                        {'questiontext':'Subtract numbers \n\n 10 - 5 = ?', 'expectedAns':'5', 'ansList':['6', '5', '12', '13']},
                        {'questiontext':'Subtract numbers \n\n 15 - 5 = ?', 'expectedAns':'10', 'ansList':['6', '5', '10', '13']},
                        {'questiontext':'Subtract numbers \n\n 15 - 7 = ?', 'expectedAns':'8', 'ansList':['8', '5', '10', '13']}
                    ],
                'compareTestCases':
                    [{'questiontext':'Compare number of objects\n\n Who has more cookies, Joy or Bob ?', 'expectedAns':'Bob', 'ansList':['Joy', 'Bob'], 'pictures':[['JoySmall'], ['cookie']*4, ['BobSmall'], ['cookie']*6]}],
                'guessTestCases':
                    [{'questiontext':'Guess a number less than 100?', 'expectedAns':'24', 'ansList':['', '', '', '']}],
                'SubObjectTestCases':
                    [{'questiontext':'Joy has 10 pears, Bob eats 4, how many pears are left?', 'expectedAns':'6', 'ansList':['6', '9', '14', '7'], 'pictures':[['JoySmall'], ['pear']*10, ['BobSmall'], ['pear']*4]}],
                'DecomposeNumTestCases':
                    [{'questiontext':'Decompose numbers \n\n 9 = ?', 'expectedAns':'4 + 5', 'ansList':['1 + 7', '2 + 6', '4 + 5', '2 + 8']}],
                'AddupNumTestCases':
                    [{'questiontext':'Add numbers \n\n Joy has 4 pears, how many pears Joy need buy to have 9?', 'expectedAns':'5', 'ansList':['6', '9', '5', '13'], 'pictures':[['JoySmall'], ['pear']*4, ['JoySmall'], ['pear']*9]}],
                'composeObjBaseTenTestCases':
                    [{'questiontext':'Compose object based on ten \n\n Joy has 10 pears, Bob gives Joy 4 more, how many pears does Joy have now?', 'expectedAns':'14', 'ansList':['6', '9', '12', '14'], 'pictures':[['JoySmall'], ['pear']*10, ['BobSmall'], ['pear']*4]}],
                'decomposeObjBaseTenTestCases':
                    [{'questiontext':'Decompose object based on ten \n\n Joy has 16 pears, Bob takes away 10, how many pears does Joy have now', 'expectedAns':'6', 'ansList':['6', '9', '12', '13'], 'pictures':[['JoySmall'], ['pear']*16, ['BobSmall'], ['pear']*10]}],
                'composeNumBaseTenTestCases':
                    [{'questiontext':'10 + 5 = ?', 'expectedAns':'15', 'ansList':['15', '9', '12', '13']}],
                'decomposeNumBaseTenTestCases':
                    [{'questiontext':'Add numbers \n 17 - 10 = ?', 'expectedAns':'7', 'ansList':['6', '9', '7', '13']}],
                'CompareWeightTestCases':
                    [{'questiontext':'Bob is 20 pounds, Joy is 40 pounds, who is heavier?', 'expectedAns':'Joy', 'ansList':['Joy', 'Bob']}],
                'ClassifyCountTestCases':
                    [{'questiontext':'How many grapess do you see?', 'expectedAns':'6', 'ansList':['6', '7', '8', '9'], 'pictures':[['pear', 'grapes', 'grapes', 'red-apple'], ['pear']+['grapes']*4, ['watermelon']*5]}],
                'IdentifyShapeTestCases':
                    [{'questiontext':'What is the shape?', 'expectedAns':'Cone', 'ansList':['Cone', 'Rectangle', 'Triangle', 'Square']}]
            }
