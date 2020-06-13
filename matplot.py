# import matplotlib.pyplot as plt
# import numpy as np 
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.ylabel('some numbers')
# plt.xlabel('independend')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# names = np.random.randint(1,high=50,size=50)
# values =np.random.randint(1,high=50,size=50)
# # plt.figure(figsize=(9, 3))
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values,"r-")
# plt.suptitle('Categorical Plotting')
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# a=np.arange(1,100,10)
# plt.plot(a,a,marker=".",markersize=20,markerfacecolor="red")
# plt.show()


#Alpha and Zorder
# ALPHA
# import matplotlib.pyplot as plt

# plt.plot([34,56,66,2,3,5],alpha=0.75,linewidth=20)
# plt.plot([34,60,66,25,32,5],linewidth=20)
# plt.show()

# # ZORDER
# import matplotlib.pyplot as plt
# plt.plot([34,56,66,2,3,5],linewidth=20,zorder=3)
# plt.plot([34,60,66,25,32,5],linewidth=20,zorder=4)
# plt.show()

# grid function

# import matplotlib.pyplot as plt
# import numpy as np

# a=np.linspace(1,10,50)
# b=np.random.randint(1,100,size=50)
# plt.plot(a,b)
# plt.xlabel("numbers",{"size":20,"color":"red"},labelpad=5)
# plt.ylabel("values",{"size":20,"color":"red"})
# plt.minorticks_on()
# plt.grid(b=True,which="both",color="pink")
# plt.show()
# print("last line")

# LEGEND
# import matplotlib.pyplot as plt
# import numpy as np

# a=np.array([1,2,5,8,9,10])
# plt.plot(a,a**2,label="square")      #add label here
# plt.plot(a,a**3,label="cube")        #add label here
# plt.legend()                        #after adding label type plt.legend()
# plt.show()

#  2nd way of legend
# import matplotlib.pyplot as plt
# import numpy as np

# a=np.array([1,2,5,8,9,10])
# plot1,=plt.plot(a,a**2)   # using , to unpack this list      
# plot2,=plt.plot(a,a**3)    # using , to unpack this list
# plt.legend([plot1,plot2],["square","cube"])  
# plt.show(block=False)


# gas price data graph

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# plt.figure(figsize=(10,10))
# gas_data=pd.read_csv('gas_price.csv')
# plt.plot(gas_data.Year,gas_data.Japan,marker=".")
# plt.plot(gas_data.Year,gas_data.Canada ,marker=".")
# plt.plot(gas_data.Year,gas_data.Germany ,marker=".")
# # for country in gas_data:
# #     if country != 'Year':
# #         plt.plot(gas_data.Year,gas_data[country],marker=".",label=country)
        
# plt.title("Gas Prices Over Time In (USD)",color="#1ec0e8",size=20,fontweight="bold")
# plt.xlabel("Years",color="#1eb2e8",size=15)
# plt.ylabel("Gas Price",color="#1eb2e8",size=15)
# plt.legend(["japan","Canada","Germany"])
# plt.grid()
# plt.xticks(gas_data.Year[::3])
# plt.show()



# histogram 

# import matplotlib.pyplot as plt 
# import numpy as np
# import pandas as pd
# bins=[10,20,30,40,50,60,70,80,90,100]
# fifa=pd.read_csv('fifa_data.csv')
# plt.title("Distribution Of Player Skill")
# plt.xlabel("Player Skills")
# plt.ylabel("Number Of Player")
# plt.hist(fifa.Overall,bins=bins,rwidth=0.95)
# plt.show()


# Pie Chart
# import matplotlib.pyplot as plt 
# import numpy as np
# import pandas as pd
# fifa=pd.read_csv('fifa_data.csv')
# labels=["Left","Right"]
# explode=(0.1,0)

# left=fifa.loc[fifa['Preferred Foot']=="Left"].count()[0]
# right=fifa.loc[fifa['Preferred Foot']=="Right"].count()[0]
# plt.title("Foot Preference Of Fifa Players")
# plt.pie([left,right],labels=labels,shadow=True,autopct="%1.1f%%",explode=explode)
# plt.show()



import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

fifa=pd.read_csv('fifa_data.csv')
labels=["FC Barcelona","Real Madrid"]
barcelona=fifa.loc[(fifa.Club=="FC Barcelona")]["Overall"]
madrid=fifa.loc[(fifa.Club=="Real Madrid")]["Overall"]
plt.title("Soccer Team Comparison")
plt.ylabel("Over All Rating")
plt.boxplot([barcelona,madrid],labels=labels)
plt.show()
print(barcelona)
print(madrid)
