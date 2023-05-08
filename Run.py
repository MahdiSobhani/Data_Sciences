

import matplotlib.pyplot as plt  

Records_Me = {4736:0, 4719:0, 7267:45, 7625:0, 6709:0, 6793:0, 8645:0, 9580:60, 7777:0, 9200:0, 12370:75, 6101:40, 8700:60, 5400:0, 6700:0, 5800:0, 6451:0, 4800:0, 5900:0, 6450:35, 9700:60,
8900:65, 5160:33, 6100:40, 9120:60, 7951:50, 6150:40, 5501:37, 5200:35, 8030:55, 10200:76, 9030:62, 7702:50, 7950:54, 7701:53, 4150:28, 7600:55, 7500:56, 4300:31, 5510:37, 5600:38, 
5500:40, 7704:56, 7440:50, 7703:47,   }

Rec,x=0,0
Avrages=[]
Total_distance,Total_Time=0,0

mxtime= max(Records_Me.values())

for k,v in (Records_Me.items()):
    Total_distance += k
    Total_Time +=v
    x +=1
    if v !=0:
        if (k//v) > Rec:
            Avrages.append(x)
            Avrages.append(('%.2f'%(k/v)))      
  
            
    if x < 10:                                          # For Showing Records In Terminal (Open Your Terminal Maximize)
        if k <10000:
            if v ==0:
                v = k
                print('',x,')',k,' Mtr           (No Time !!!)')
            else:    
                print('',x,')',k,' Mtr in',v,'Min',(k//v) * '.')
        elif k > 10000:
            print('',x,')',k,'Mtr in',v,'Min',(k//v) * '.')
    elif x >= 10:
        if k <10000:
            if v ==0:
                v = k
                print(x,')',k,' Mtr           (No Time !!!)')
            else:    
                print(x,')',k,' Mtr in',v,'Min',(k//v) * '.')
        elif k >= 10000:
            print(x,')',k,'Mtr in',v,'Min',(k//v) * '.')


print('\n')
w,y=0,1                                                 
AA,xplot,yplot=[],[],[]
x=0
for i in Avrages:
    x +=2
    if x <= len(Avrages):
        AA.append((float(Avrages[y]),int(Avrages[w])))
        xplot.append(float(Avrages[y]))
        yplot.append(Avrages[w])
        w +=2
        y +=2

AA.sort(reverse=True)                               
                             
print(f"""(From Autumn 1398)    
Total_distance          : {Total_distance} M  {'%.0f'%(Total_distance / 1000)} Km""")
print('Total_Time              :',(Total_Time),'Min',' (',('%.2f'%(Total_Time/60)),'H)')

mxrun = max(Records_Me.keys())                                               # Max run and time in One Run
print('Max Distance in One Run :',mxrun,'in',Records_Me.get(mxrun),'Min')
for k,v in Records_Me.items():
    if v == mxtime:
        print('Max Time in One Run     :',v,'Min With',k) 

print('\t')
print("       <<Records>>")

x=1
xx=0
for i in AA:                                                     # Show Records
    if x <= 9:
       print('',x,')','%.2f'%i[0] ,' ==>  No.',i[1])
    else:
        if i[0] <100:
            print(x,')','%.2f'%i[0],'  ==>  No.',i[1])
        else:
            print(x,')','%.2f'%i[0],' ==>  No.',i[1])
    xx = x
    x +=1

print('\n')

plt.style.use('seaborn-v0_8')                                                   # Plot
plt.plot(yplot, xplot,label=f'{xx} Entries',color='c',marker='o',ms=6 ,mfc='m')

plt.title('Records of Running',loc='left')
plt.legend()
plt.xlabel('No.')
plt.ylabel('Points')

plt.show()