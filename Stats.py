import json

from scipy.stats import f_oneway

def __get_best_vals__(file):
    file = 'Data/' + file
    with open(file,'r') as f:
        d = json.load(f)
    vals = []
    for key in d.keys():
        vals.append(d[key][-1])
    return vals 


Normal_Select_Best_Vals = __get_best_vals__('NormalSelectFull.json')
Normal_Select_Wide_Best_Vals = __get_best_vals__('NormalSelectWide.json')
Normal_Select_Stats_Small_Best_Vals = __get_best_vals__('NormalSelectStats.json')
Normal_Select_Stats_Best_Vals = __get_best_vals__('NormalSelectStatsFull.json')

Replace_Low_Select_Best_Vals = __get_best_vals__('ReplaceLowSelectFull.json')
Replace_Low_Select_Wide_Best_Vals = __get_best_vals__('ReplaceLowSelectWide.json')
Replace_Low_Select_Stats_Small_Best_Vals = __get_best_vals__('ReplaceLowSelectStats.json')
Replace_Low_Select_Stats_Best_Vals = __get_best_vals__('ReplaceLowSelectStatsFull.json')

Select_Best_V_All_Best_Vals = __get_best_vals__('SelectBestVAllFull.json')
Select_Best_V_All_Wide_Best_Vals = __get_best_vals__('SelectBestVAllWide.json')
Select_Best_V_All_Stats_Small_Best_Vals = __get_best_vals__('SelectBestVAllStats.json')
Select_Best_V_All_Stats_Best_Vals = __get_best_vals__('SelectBestVAllStatsFull.json')

Select_Best_V_Groups_of_5_Best_Vals = __get_best_vals__('AllvGroupsof5SelectFull.json')
Select_Best_V_Groups_of_5_Wide_Best_Vals = __get_best_vals__('AllvGroupsof5SelectWide.json')
Select_Best_V_Groups_of_5_Stats_Small_Best_Vals = __get_best_vals__('AllvGroupsof5SelectStats.json')
Select_Best_V_Groups_of_5_Stats_Best_Vals = __get_best_vals__('AllvGroupsof5SelectStatsFull.json')

stat_lists = [
    Normal_Select_Stats_Best_Vals,
    Replace_Low_Select_Stats_Best_Vals,
    Select_Best_V_All_Stats_Best_Vals,
    Select_Best_V_Groups_of_5_Stats_Best_Vals,
]

Normal_V_Replace_Low = f_oneway(Normal_Select_Stats_Best_Vals,Replace_Low_Select_Stats_Best_Vals)
Normal_V_Select_Best_V_All = f_oneway(Normal_Select_Stats_Best_Vals,Select_Best_V_All_Stats_Best_Vals)
Normal_V_Select_Best_V_Groups_of_5 = f_oneway(Normal_Select_Stats_Best_Vals,Select_Best_V_Groups_of_5_Stats_Best_Vals)

print(Normal_V_Replace_Low)
print(Normal_V_Select_Best_V_All)
print(Normal_V_Select_Best_V_Groups_of_5)


# results = [[None]*4]*4

# for i in range(len(stat_lists)):
    # for j in range(len(stat_lists)):
        # results[i][j] = f_oneway(stat_lists[i],stat_lists[j])

# for i in range(len(results)):
    # for j in range(len(results[i])):
        # if results[i][j].pvalue < 0.10:
            # print(i,j, results[i][j])

lists = [Normal_Select_Best_Vals,
         Normal_Select_Wide_Best_Vals,
         Normal_Select_Stats_Best_Vals,
         Replace_Low_Select_Best_Vals,
         Replace_Low_Select_Wide_Best_Vals,
         Replace_Low_Select_Stats_Best_Vals,
         Select_Best_V_All_Best_Vals,
         Select_Best_V_All_Wide_Best_Vals,
         Select_Best_V_Groups_of_5_Best_Vals, 
         Select_Best_V_All_Stats_Best_Vals, 
         Select_Best_V_Groups_of_5_Wide_Best_Vals,
         Select_Best_V_Groups_of_5_Stats_Best_Vals]

#Normal v All 
Normal_V_Replace_Low = f_oneway(Normal_Select_Best_Vals,Replace_Low_Select_Best_Vals)
Normal_V_Select_Best_V_All = f_oneway(Normal_Select_Best_Vals,Select_Best_V_All_Best_Vals)
Normal_V_Select_Best_V_Groups_of_5 = f_oneway(Normal_Select_Best_Vals,Select_Best_V_Groups_of_5_Best_Vals)
# print(Normal_V_Replace_Low)
# print(Normal_V_Select_Best_V_All)
# print(Normal_V_Select_Best_V_Groups_of_5)



#Wide v FULL 
Normal_V_Normal_Wide = f_oneway(Normal_Select_Best_Vals,Normal_Select_Wide_Best_Vals)
Select_Best_V_All_V_Select_Best_V_All_Wide = f_oneway(Select_Best_V_All_Best_Vals,Select_Best_V_All_Wide_Best_Vals)
Select_Best_V_Groups_of_5_V_Select_Best_V_Groups_of_5_Wide = f_oneway(Select_Best_V_Groups_of_5_Best_Vals,Select_Best_V_Groups_of_5_Wide_Best_Vals)
# print(Normal_V_Normal_Wide)
# print(Select_Best_V_All_V_Select_Best_V_All_Wide)
# print(Select_Best_V_Groups_of_5_V_Select_Best_V_Groups_of_5_Wide)

#Wide v Wides 
Normal_Wide_V_Replace_Low_Wide = f_oneway(Normal_Select_Wide_Best_Vals,Replace_Low_Select_Wide_Best_Vals)
Normal_Wide_V_Select_Best_V_All_Wide = f_oneway(Normal_Select_Wide_Best_Vals,Select_Best_V_All_Wide_Best_Vals)
Normal_Wide_V_Select_Best_V_Groups_of_5_Wide = f_oneway(Normal_Select_Wide_Best_Vals,Select_Best_V_Groups_of_5_Wide_Best_Vals)
# print(Normal_Wide_V_Replace_Low_Wide)
# print(Normal_Wide_V_Select_Best_V_All_Wide)
# print(Normal_Wide_V_Select_Best_V_Groups_of_5_Wide)


#Normal_V_Wides
Normal_V_Replace_Low_Wide = f_oneway(Normal_Select_Best_Vals,Replace_Low_Select_Wide_Best_Vals)
Normal_V_Select_Best_V_All_Wide = f_oneway(Normal_Select_Best_Vals,Select_Best_V_All_Wide_Best_Vals)
Normal_V_Select_Best_V_Groups_of_5_Wide = f_oneway(Normal_Select_Best_Vals,Select_Best_V_Groups_of_5_Wide_Best_Vals)
# print(Normal_V_Replace_Low_Wide)
# print(Normal_V_Select_Best_V_All_Wide)
# print(Normal_V_Select_Best_V_Groups_of_5_Wide)