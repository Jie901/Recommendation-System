import numpy as np
'''
def read_t():
    f = open('train.txt',encoding='UTF-8')
    line = f.readline()
    count=0
    while count<19835:
        count=count+1
        #print(count)
        user_id=line.split('|')[0]
        user_item_num=int(line.split('|')[1])
        temp=random.randrange(0,user_item_num-1,1)
        for i in range(0,user_item_num):
            line=f.readline()
            if temp==i:
                test_user_item_score.append([int(user_id),int(line.split('  ')[0]),int(line.split('  ')[1].split('  ')[0])])
            else:
                user_item_score.append([int(user_id),int(line.split('  ')[0]),int(line.split('  ')[1].split('  ')[0])])
            if user_item_num<500:
                if int(line.split('  ')[0]) in item_id:
                    temp_list=list_find(y_pred[item_id.index(int(line.split('  ')[0]))],y_pred)
                    temp_index=random.randint(0,len(temp_list)-1)
                    temp=temp_list[temp_index]
                    user_item_score.append([int(user_id),item_id[temp],int(line.split('  ')[1].split('  ')[0])])
                    user_item_num=user_item_num+1
        user_item_num=user_item_num-1
        user_item_nums.append(user_item_num)
        line = f.readline()
    f.close()
    return user_item_nums,user_item_score,test_user_item_score
'''

#'''
score_matrix = np.array([[1,2,],[3,4,]])


average_matrix = np.mean(score_matrix)#打分矩阵的平均值
average_column = np.mean(score_matrix,axis=0)#计算每一列的平均值
average_row = np.mean(score_matrix,axis=1)#计算每一行的平均值

item_id = 624960
user_id = 19834

i,j =eval(input())#用户i，针对电影j的评分(用户和电影均从0开始编号)
#输入格式为item_id,user_id(先行后列，item为行，user为列)
final_score = average_matrix + (average_column[i]-average_matrix) + (average_row[j]-average_matrix)
print(final_score)
#'''