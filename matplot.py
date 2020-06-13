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
