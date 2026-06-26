import numpy as np

def stdmean(grades):
    return np.mean(grades,axis=1) 

def sbjmean(grades):
    return np.mean(grades,axis=0)  

def highstd(grades,min=85):
    stdmean =np.mean(grades,axis=1) 
    mask=stdmean>min
    return np.where(mask)[0] + 1,stdmean[mask]

def bonus(grades,b):
    return grades+b     

def normgrades(grades):
    return (grades-grades.min())/(grades.max()-grades.min()).astype(float)

def flatgrades(grades):
    return grades.flatten()





def display(grades,bs=5):
    studmean=stdmean(grades)
    sbjtmean=sbjmean(grades)
    stdnum,avrg= highstd(grades)
    bouncedgrades= bonus(grades,bs)
    normlgrade=normgrades(grades)
    flatgrade=flatgrades(grades)

    print("The shape:\n",np.shape(grades))
    print("The Mean of each student:\n",studmean)
    print("The Mean of each subject:\n",sbjtmean)
    print("The Students whose average grade is greater than 85:\n",stdnum)
    print("And The averages:\n",avrg)
    print("The Grades after bonus:\n",bouncedgrades)
    print("The normalized grades:\n",normlgrade)
    print("The flattened grades:\n",flatgrade)






grades = np.array([[85, 78, 92, 88],
                [70, 76, 80, 65],
                [90, 88, 94, 91],
                [60, 65, 58, 62],
                [100, 95, 98, 97]])


display(grades)
