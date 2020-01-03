import random
# rules
# 1) if a cell < 2 neighbors than die
# 2) if a cell > 3 neighbors than die
# 3) if a cell has 2 or 3 neighbors it lives on
# 4) if a cell has 3 neighbors than it reproduces at that cell
# glider gun 38X11 board
screenx = 600
screeny = 400
numrows = 20
numcols = 20
marginx = 40
marginy = 40
temprows = str(numrows)
tempcols = str(numcols)
tempscreenx = str(screenx)
tempscreeny = str(screeny)
tempmarginx = str(marginx)
tempmarginy = str(marginy)
generation = 0
status = 0
options = 0
focus = 0
focusstatus = 0
cursorpos = 0
lifex = (screenx-(marginx*2))/numrows
lifey = (screeny-(marginy*2))/numcols
boxlist = []
rowlist = []


def setup():
    global boxlist
    size(600,400)  # might have to adjust based on the number of cells
    frameRate(3)  # can adjusted recomment values 1-10
    background(0, 0, 0)
    setupboard()
    setpercent(20)  #percent of the board that will be randomly selected to be alive
    #testrule() # test function to verify function leave commented out
 
def draw():
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist,status,options
    background(0, 0, 0)
    if(status==0):
        rungeneration()
    drawlife()
    if(options==1):
        drawoptions()
        drawtextarea()
        drawoptionstext()
    drawbuttons()
    drawtext()
    #status=1
    
def initsetting():
    global temprows,tempcols,tempscreenx,tempscreeny,tempmarginx,tempmarginy,generation,status
    global options,focus,focusstatus,lifex,lifey,boxlist,rowlist,numrows,numcols,screenx,screeny,marginx,marginy
    temprows = str(numrows)
    tempcols = str(numcols)
    tempscreenx = str(screenx)
    tempscreeny = str(screeny)
    tempmarginx = str(marginx)
    tempmarginy = str(marginy)
    generation = 0
    #status = 0
    options = 0
    focus = 0
    focusstatus = 0
    cursorpos = 0
    lifex = (screenx-(marginx*2))/numrows
    lifey = (screeny-(marginy*2))/numcols
    boxlist = []
    rowlist = []
    
def boardclick(x,y):
    global numcols,numrows,marginx,marginy,boxlist,lifex,lifey
    for l in range(numcols):
        for k in range(numrows):
            if(x>marginx+(k*lifex) and x<marginx+(k*lifex)+lifex and y>marginy+(l*lifey) and y<marginy+(l*lifey)+lifey):
                if(boxlist[l][k]==1):
                    boxlist[l][k] = 0
                else:
                    boxlist[l][k] = 1
                    
def saveboard(selection):
    global boxlist
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        file1 = selection.getAbsolutePath()
        #print("User selected " + file1)
        list2 = []
        for list1 in boxlist:
            str1 = ""
            for i in list1:
                str1 = str1+str(i)+","
            str1 = str1[:-1]
            list2.append(str1)
        saveStrings(file1, list2)
    
def drawlife():
    for l in range(numcols):
        for k in range(numrows):
            if(boxlist[l][k] == 1):
                fill(200,20,20)
            else:
                fill(255,255,255)
            rect(marginx+(k*lifex),marginy+(l*lifey),lifex,lifey)

def drawoptions():
    global screenx, screeny, numrows, numcols, marginx, marginy, focus
    fill(20,200,20)
    rect(screenx/4,marginy+20,screenx/2,screeny/2) 

def drawbuttons():
    #buttons - stop/start, settings, loadfile, reset
    global screenx, screeny, numrows, numcols, marginx, marginy, options
    fill(20,200,20)
    rect(marginx,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*2/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*3/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*4/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*5/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    if(options==1):
        fill(0,0,0)
        rect(screenx/2+(screenx/10),(screeny/2)+30,screenx/10,20)
        
def keyPressed():
    global focus, cursorpos
    #9 - tab, 8 - backspace, 127 - delete, 32 - space 
    #37 <-, 39 ->, 38 - up arrow, 40 - down arrow, 36 - home, 35 - end
    if(keyCode==37):
        cursorpos -= 1
    if(keyCode==39):
        cursorpos += 1
    if(keyCode==127):
        #del key
        deltext()
    if(keyCode>47 and keyCode<58):
        changetext(keyCode)
    if(keyCode==8):
        bstext()
    if (keyCode==9):
        focus+=1
        initcursorpos()
    if(focus>6):
        focus=1
        
def initcursorpos():
    global cursorpos, temprows, temprows, tempscreenx, tempscreeny, tempmarginx, tempmarginy
    if(focus==1):
        cursorpos = len(temprows)
    elif(focus==2):
        cursorpos = len(tempcols)
    elif(focus==3):
        cursorpos = len(tempscreenx)
    elif(focus==4):
        cursorpos = len(tempscreeny)
    elif(focus==5):
        cursorpos = len(tempmarginx)
    elif(focus==6):
        cursorpos = len(tempmarginy)
    else:
        #print "something happen"
        cv=0

def deltext():
    global temprows, tempcols, tempscreenx, tempscreeny, tempmarginx, tempmarginy, focus, cursorpos
    if(focus==1):
        temprows = temprows[:cursorpos]+temprows[cursorpos+1:]
    elif(focus==2):
        tempcols = tempcols[:cursorpos]+tempcols[cursorpos+1:]
    elif(focus==3):
        tempscreenx = tempscreenx[:cursorpos]+tempscreenx[cursorpos+1:]
    elif(focus==4):
        tempscreeny = tempscreeny[:cursorpos]+tempscreeny[cursorpos+1:]
    elif(focus==5):
        tempmarginx = tempmarginx[:cursorpos]+tempmarginx[cursorpos+1:]
    elif(focus==6):
        tempmarginy = tempmarginy[:cursorpos]+tempmarginy[cursorpos+1:]
    else:
        #print "something happen"
        cv=0          
            
def changetext(n):
    global temprows, tempcols, tempscreenx, tempscreeny, tempmarginx, tempmarginy, focus
    strn = str(n - 48)
    if(focus==1):
        temprows = temprows + strn
    elif(focus==2):
        tempcols = tempcols + strn
    elif(focus==3):
        tempscreenx = tempscreenx + strn
    elif(focus==4):
        tempscreeny = tempscreeny + strn
    elif(focus==5):
        tempmarginx = tempmarginx + strn
    elif(focus==6):
        tempmarginy = tempmarginy + strn
    else:
        #print "something happen"
        cv=0
        
def bstext():
    global focus, screenx, screeny, numrows, numcols, marginx, marginy
    global temprows, tempcols, tempscreenx, tempscreeny, tempmarginx, tempmarginy
    if(focus==1):
        temprows = temprows[:-1]
    elif(focus==2):
        tempcols = tempcols[:-1]
    elif(focus==3):
        tempscreenx = tempscreenx[:-1]
    elif(focus==4):
        tempscreeny = tempscreeny[:-1]
    elif(focus==5):
        tempmarginx = tempmarginx[:-1]
    elif(focus==6):
        tempmarginy = tempmarginy[:-1]
    else:
        #print "something happen"
        cv=0

def drawoptionstext():
    global screenx, screeny, numrows, numcols, marginx, marginy, options, focusstatus, focus
    global temprows, tempcols, tempscreenx, tempscreeny, tempmarginx, tempmarginy, cursorpos
    #textfields - numrows,numcols,screenx,screeny,marginx,marginy,percent,framerate
    fill(0,0,0)
    if(focusstatus==1):
        focusstatus = 0
        if(focus==1):
            if(cursorpos>len(temprows)-1):
                temprows1 = temprows+"|"
                curpospos = len(temprows)-1
            elif(cursorpos<1):
                temprows1 = "|"+temprows
                cursorpos = 0
            else:
                temprows1 = temprows[:cursorpos]+"|"+temprows[cursorpos:]
            tempcols1 = tempcols
            tempscreenx1 = tempscreenx
            tempscreeny1 = tempscreeny
            tempmarginx1 = tempmarginx
            tempmarginy1 = tempmarginy
        elif(focus==2):
            if(cursorpos>len(tempcols)-1):
                tempcols1 = tempcols+"|"
                curpospos = len(tempcols)-1
            elif(cursorpos<1):
                tempcols1 = "|"+tempcols
                cursorpos = 0
            else:
                tempcols1 = tempcols[:cursorpos]+"|"+tempcols[cursorpos:]
            temprows1 = temprows
            tempscreenx1 = tempscreenx
            tempscreeny1 = tempscreeny
            tempmarginx1 = tempmarginx
            tempmarginy1 = tempmarginy
        elif(focus==3):
            if(cursorpos>len(tempscreenx)-1):
                tempscreenx1 = tempscreenx+"|"
                curpospos = len(tempscreenx)-1
            elif(cursorpos<1):
                tempscreenx1 = "|"+tempscreenx
                cursorpos = 0
            else:
                tempscreenx1 = tempscreenx[:cursorpos]+"|"+tempscreenx[cursorpos:]
            tempcols1 = tempcols
            temprows1 = temprows
            tempscreeny1 = tempscreeny
            tempmarginx1 = tempmarginx
            tempmarginy1 = tempmarginy
        elif(focus==4):
            if(cursorpos>len(tempscreeny)-1):
                tempscreeny1 = tempscreeny+"|"
                curpospos = len(tempscreeny)-1
            elif(cursorpos<1):
                tempscreeny = "|"+tempscreeny
                cursorpos = 0
            else:
                tempscreeny1 = tempscreeny[:cursorpos]+"|"+tempscreeny[cursorpos:]
            tempcols1 = tempcols
            tempscreenx1 = tempscreenx
            temprows1 = temprows
            tempmarginx1 = tempmarginx
            tempmarginy1 = tempmarginy
        elif(focus==5):
            if(cursorpos>len(tempmarginx)-1):
                tempmarginx1 = tempmarginx+"|"
                curpospos = len(tempmarginx)-1
            elif(cursorpos<1):
                tempmarginx1 = "|"+tempmarginx
                cursorpos = 0
            else:
                tempmarginx1 = tempmarginx[:cursorpos]+"|"+tempmarginx[cursorpos:]
            tempcols1 = tempcols
            tempscreenx1 = tempscreenx
            tempscreeny1 = tempscreeny
            temprows1 = temprows
            tempmarginy1 = tempmarginy
        elif(focus==6):
            if(cursorpos>len(tempmarginy)-1):
                tempmarginy1 = tempmarginy+"|"
                curpospos = len(tempmarginy)-1
            elif(cursorpos<1):
                tempmarginy1 = "|"+tempmarginy
                cursorpos = 0
            else:
                tempmarginy1 = tempmarginy[:cursorpos]+"|"+tempmarginy[cursorpos:]
            tempcols1 = tempcols
            tempscreenx1 = tempscreenx
            tempscreeny1 = tempscreeny
            tempmarginx1 = tempmarginx
            temprows1 = temprows
        else:
            #print "something wrong"
            temprows1 = temprows
            tempcols1 = tempcols
            tempscreenx1 = tempscreenx
            tempscreeny1 = tempscreeny
            tempmarginx1 = tempmarginx
            tempmarginy1 = tempmarginy
    else:
        focusstatus = 1
        temprows1 = temprows
        tempcols1 = tempcols
        tempscreenx1 = tempscreenx
        tempscreeny1 = tempscreeny
        tempmarginx1 = tempmarginx
        tempmarginy1 = tempmarginy
    text(temprows1, screenx/2+15, marginy*2)
    text(tempcols1, screenx/2+15, marginy*2+20)
    text(tempscreenx1, screenx/2+15, marginy*2+40)
    text(tempscreeny1, screenx/2+15, marginy*2+60)
    text(tempmarginx1, screenx/2+15, marginy*2+80)
    text(tempmarginy1, screenx/2+15, marginy*2+100)
   
def drawtextarea():
    global screenx, screeny, numrows, numcols, marginx, marginy, options
    fill(200,200,200)
    rect(screenx*2/4,marginy*2-13,50,17)
    rect(screenx*2/4,marginy*2-13+20,50,17)
    rect(screenx*2/4,marginy*2-13+40,50,17)
    rect(screenx*2/4,marginy*2-13+60,50,17)
    rect(screenx*2/4,marginy*2-13+80,50,17)
    rect(screenx*2/4,marginy*2-13+100,50,17)
       
def mousePressed():
    global numrows, numcols, marginx, marginy, screenx, screeny, boxlist, generation, status, options
    global temprows, tempcols, tempscreenx, tempscreeny, tempmarginx, tempmarginy, focus
    x=mouseX
    y=mouseY
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13) and (y<marginy*2-13+17)):
        #numrows
        focus = 1
        initcursorpos()
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13+20) and (y<marginy*2-13+17+20)):
        #numcols
        focus = 2
        initcursorpos()
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13+40) and (y<marginy*2-13+17+40)):
        #screenx
        focus = 3
        initcursorpos()
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13+60) and (y<marginy*2-13+17+60)):
        #screeny
        focus = 4
        initcursorpos()
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13+80) and (y<marginy*2-13+17+80)):
        #marginx
        focus = 5
        initcursorpos()
    if(options==1 and (x>screenx/2) and (x<screenx/2+50) and (y>marginy*2-13+100) and (y<marginy*2-13+17+100)):
        #marginy
        focus = 6
        initcursorpos()
    if(options==1 and x>screenx/2+(screenx/10) and x<screenx/2+(screenx/10)*2 and y>(screeny/2)+30 and y<(screeny/2)+30+20):
        status = 1
        numrows = int(temprows)
        numcols = int(tempcols)
        screenx = int(tempscreenx)
        screeny = int(tempscreeny)
        marginx = int(tempmarginx)
        marginy = int(tempmarginy)
        initsetting()
        setupboard()
        setpercent(20)
        status = 0
    if(x>screenx-marginx-screenx*5/10 and x<screenx-marginx-screenx*5/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        #clear
        generation = 0
        status = 1
        boxlist=[]
        setupboard()
    if(x>screenx-marginx-screenx*4/10 and x<screenx-marginx-screenx*4/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        #save
        selectOutput("Select a file to write to:", "saveboard")
    if(x>screenx-marginx-screenx*3/10 and x<screenx-marginx-screenx*3/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        options = 1
        focus = 1
        initcursorpos()
    if(x>screenx-marginx-screenx*2/10 and x<screenx-marginx-screenx*2/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        selectInput("Select a file to process:", "fileSelected")
    if(x>marginx and x<marginx+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        generation = 0
        status = 0
        boxlist=[]
        setupboard()
        setpercent(20)
    if(x>screenx-marginx-screenx/10 and x<screenx-marginx and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        if(status==0):
            status = 1
        else:
            status = 0
    boardclick(x,y)

def fileSelected(selection):
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        file1 = selection.getAbsolutePath()
        #print("User selected " + file1)
        ext = file1[len(file1)-3:]
        lines = loadStrings(file1)
        if(ext=="LIF"):
            henzeltransform(lines)
        else:
            reset(lines)
            
def stripcomments(lines):
    list1=[]
    for line1 in lines:
        if(line1[0]!="#" or line1[:2]=="#P"):
            list1.append(line1)
    return list1

def getsections(lines):
    list1=[]
    list2=[]
    c=0
    for line1 in lines:
        c+=1
        if(line1[:2]=="#P"):
            list2.append(list1)
            list1=[]
            list1.append(line1)
        else:
            list1.append(line1)
    list2.append(list1)
    del list2[0]
    return list2

def longeststring(list1):
    n = 0
    for line2 in list1:
        len1 = len(line2)
        if (len1>n):
            n=len1
    return n

def getcoor(list1):
    list2=[]
    for section in list1:
        listpos = getcoor1(section[0])
        list2.append(listpos)
    return list2

def getcoor1(pos):
    pos = pos[2:]
    listpos = pos.split()
    return listpos

def getsize(list1):
    n1=1000
    n2=-1000
    m1=1000
    m2=-1000
    for line1 in list1:
        n=int(line1[0])
        m=int(line1[1])
        if(n<n1):
            n1=n
        if(n>n2):
            n2=n
        if(m<m1):
            m1=m
        if(m>m2):
            m2=m
    list2=[n2-n1,m2-m1,n1,n2,m1,m2]
    return list2

def longestrow(list1):
    n=0
    for lines in list1:
        r = longeststring(lines)
        if(r>n):
            n=r
    return n

def longestcol(list1):
    m=0
    for lines in list1:
        r = len(lines)
        if(r>m):
            m=r
    return m

def converthenzel(list1,poslist):
    for lines in list1:
        listpos = getcoor1(lines[0])
        x1 = int(listpos[0]) + (-1 * int(poslist[2]))
        y1 = int(listpos[1]) + (-1 * int(poslist[4]))
        del lines[0]
        list3 = converthenzel1(lines)
        converthenzel2(list3,x1,y1)
        
def converthenzel1(list1):
    list3=[]
    for line3 in list1:
        list2=[]
        for k in range(len(line3)):
            if(line3[k]=="."):
                list2.append(0)
            else:
                list2.append(1)
        list3.append(list2)
    return list3
        
def converthenzel2(list1,n,m):
    global boxlist
    for l in range(len(list1)):
        for k in range(len(list1[l])):
            boxlist[l+m][k+n] = list1[l][k]
            
def henzeltransform(lines):
    global generation, numrows, numcols, boxlist, status
    status = 1
    list1=stripcomments(lines)
    list2 = getsections(list1)
    list3 = getcoor(list2)
    list4 = getsize(list3)
    n=longestrow(list2)
    n=n+int(list4[0])
    m=longestcol(list2)
    m=m+int(list4[1])
    numrows = n
    numcols = m
    initsetting()
    setupboard()
    converthenzel(list2,list4)
    #print "boxlist - "+str(boxlist)
    status = 0
                
def reset(lines):
    global generation, numrows, numcols, boxlist, status
    status = 1
    numcols = len(lines)
    numrows = len(lines[0].split(","))
    initsetting()
    for line1 in lines:
        list1 = line1.split(",")
        list1 = [int(i) for i in list1]
        boxlist.append(list1)
    status = 0
                                                                                                                                                
def rungeneration():
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist,rowlist,generation
    generation+=1
    list1 = []
    list2 = rowlist
    for l in range(numcols):
        list2 = []
        for k in range(numrows):
            value = checklife(k,l)
            if(value<2 or value>3):
                 list2.append(0)
            elif(value==2 and boxlist[l][k]==1):
                 list2.append(1)
            elif(value==2 and boxlist[l][k]==0):
                 list2.append(0)
            elif(value==3):
                 list2.append(1)
            else:
                 list2.append(0)
        list1.append(list2)
    boxlist = list1

def drawtext():
    global generation, marginx, marginy, options
    textSize(12);
    fill(200,200,200)
    text("Game of Life",100, marginy/1.5)
    text("Generation "+str(generation), 450, marginy/1.5) 
    text("Restart",marginx+10,screeny-(marginy*3/4)+15)
    if(status==0):
        text("Stop",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    else:
        text("Start",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    if(options==1):
        #rect(screenx/2+(screenx/10),(screeny/2)+30,screenx/10,20)
        text("Close",screenx/2+(screenx/10)+15,(screeny/2)+30+15)
        text("Number of Rows", screenx/4+20, marginy*2)
        text("Number of Columns", screenx/4+20, marginy*2+20)
        text("Display Width", screenx/4+20, marginy*2+40)
        text("Display Height", screenx/4+20, marginy*2+60)
        text("Border Width", screenx/4+20, marginy*2+80)
        text("Boarder Height", screenx/4+20, marginy*2+100)
    text("Load",screenx-marginx-screenx*2/10+15,screeny-(marginy*3/4)+15)
    text("Option",screenx-marginx-screenx*3/10+10,screeny-(marginy*3/4)+15)
    text("Save",screenx-marginx-screenx*4/10+15,screeny-(marginy*3/4)+15)
    text("Clear",screenx-marginx-screenx*5/10+15,screeny-(marginy*3/4)+15)
                                    
def checklife(x,y):
    global boxlist, numrows, numcols
    value = 0
    x1 = x - 1
    y1 = y - 1
    x2 = x1 + 1
    x3 = x1 + 2
    y2 = y1 + 1
    y3 = y1 + 2
    if(x1<0):
        x1 = 99
    if(x3>numrows-1):
        x3 = 99
    if(y1<0):
        y1 = 99
    if(y3>numcols-1):
        y3 = 99
    if(y1!=99 and x1!=99 and boxlist[y1][x1]==1):
        value+=1
    if(y1!=99 and boxlist[y1][x2]==1):
        value+=1
    if(y1!=99 and x3!=99 and boxlist[y1][x3]==1):
        value+=1
    if(x1!=99 and boxlist[y2][x1]==1):
        value+=1
    if(x3!=99 and boxlist[y2][x3]==1):
        value+=1
    if(y3!=99 and x1!=99 and boxlist[y3][x1]==1):
        value+=1
    if(y3!=99 and boxlist[y3][x2]==1):
        value+=1
    if(y3!=99 and x3!=99 and boxlist[y3][x3]==1):
        value+=1
    return value

def setupboard():
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist,rowlist
    list2 = rowlist
    for l in range(numcols):
        list2 = []
        for k in range(numrows):
            list2.append(0)
        boxlist.append(list2)

def randomlife(n):
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist
    for k in range(n):
        randx = random.randint(0,numrows-1)
        randy = random.randint(0,numcols-1)
        boxlist[randy][randx] = 1
    
def setpercent(n):
    global numrows, numcols
    t=numrows*numcols*n/100
    randomlife(t)
    
def testrule():
    #test rules on a 3 X 3 board
    global boxlist
    boxlist[0][1] = 1
    boxlist[0][0] = 1
    boxlist[0][2] = 1
    
