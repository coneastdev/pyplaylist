import json
import os

looping = False
data = {}

def loaddata():
  global data
  out_file = open("data.json", "r")
  data = json.load(out_file)
  out_file.close()

loaddata()

def updatedata():
  writefile = open('data.json', 'w')
  json.dump(data, writefile, indent=2)
  writefile.close()


# start menu
def startmenu(name, userpassword):
  global username
  username = name
  os.system('cls')
  print("welcome " + username)
  print()
  print("what would you like to do today?")
  print()
  print("1.serch")
  print("2.setings")
  print("3.playlist")
  print("4.add song")
  print("5.info/help")
  print()
  optnum = input("please input a number | > ")
  if optnum == "1":
    # serching
    os.system('cls')

    def serch(key, userinput):
      print()
      export = []
      for i in data["songs"]:
        if key == "length":
          if int(i[key]) < int(userinput + 1):
            print(i["name"] + " artist : " + i["artist"] + "  time : " +
                  i["length"] + " link : " + i["link"])
            export.append(i["name"] + " artist : " + i["artist"] +
                          "  time : " + i["length"] + " link : " + i["link"])
            print()
        elif i[key] == userinput:
          print(i["name"] + " artist : " + i["artist"] + "  time : " +
                i["length"] + " link : " + i["link"])
          export.append(i["name"] + " artist : " + i["artist"] + "  time : " +
                        i["length"] + " link : " + i["link"])
          print()
      print()
      usrinput = input(
        "press enter to go back to menu or type export to save to a txt file | > "
      )
      if usrinput == "export":
        with open('songlist.txt', 'w') as f:
          f.write(str(export))
      startmenu(username, userpassword)

    def serchopt():
      print("what would you like to serch for")
      print()
      print("1.name")
      print("2.genre")
      print("3.artist")
      print("4.length")
      print("5.show all A-z")
      print()
      option = input("please input a number | > ")
      if option == "1":
        print("please input name")
        serch("name", input())
      elif option == "2":
        print("please input genre")
        serch("genre", input())
      elif option == "3":
        print("please input artist")
        serch("artist", input())
      elif option == "4":
        print("please input length")
        serch("length", int(input()))
      elif option == "5":
        os.system('cls')
        atozlist = []

        def atozlistfunc(e):
          return e["name"]

        atozlist = data["songs"]
        atozlist.sort(key=atozlistfunc)
        for i in atozlist:
          print(i["name"] + " artist : " + i["artist"] + "  time : " +
                i["length"] + " link : " + i["link"] + "\n")
        print()
        usrinput = input(
          "press enter to go back to menu or type export to save to a txt file | > "
        )
        if usrinput == "export":
          with open('songlist.txt', 'w') as f:
            f.write(str(atozlist))
        startmenu(username, userpassword)
      else:
        os.system('cls')
        serchopt()

    serchopt()
  elif optnum == "2":
    # setings
    os.system('cls')

    def setseting(key):
      global username
      if key == "delhist":
        for i in data["users"]:
          if i["name"] == username:
            print(i["history"])
            print()
            print("deleate")
            i["history"] = ""
      elif key == "delacount":
        for i in data["users"]:
          if i["name"] == username:
            data["users"].remove(i)
            print("removeing. . .")
            updatedata()
            quit()
      else:
        for i in data["users"]:
          if i["name"] == username:
            print()
            print("please enter new " + key)
            i[key] = input()
            updatedata()
            if key == "pass":
              userpassword = i["pass"]
            elif key == "name":
              username = i["name"]
        startmenu(username, userpassword)

    def setingsopt():
      os.system('cls')
      print("what would you like to change?")
      print()
      print("1.password")
      print("2.fav artist")
      print("3.fav genre")
      print("4.gender")
      print("5.date of birth")
      print("6.delete all history")
      print("7. DELETE ACCOUNT")
      print()
      userinput = input("please input a number | > ")
      if userinput == "1":
        setseting("pass")
      elif userinput == "2":
        setseting("favart")
      elif userinput == "3":
        setseting("favgenre")
      elif userinput == "4":
        setseting("gender")
      elif userinput == "5":
        setseting("dob")
      elif userinput == "6":
        setseting("delhist")
      elif userinput == "7":
        setseting("delacount")
      else:
        setingsopt()

    def passopt():
      print("please input pass word")
      userinput = input()
      if userinput == userpassword:
        setingsopt()
      else:
        passopt()

    passopt()
  elif optnum == "3":
    # playlist
    os.system("cls")
    print("\n1.make playlist\n2.generate playlist\n3.view your playlists\n")
    userinput = int(input("please enter a number | > "))
    if userinput == 1:
      #create playlist
      os.system("cls")
      for user in data["users"]:
        if user["name"] == username:
          looping = True
          global dobole
          dobole = False
          while looping == True:
            playlistname = input("playlist name | > ")
            for e in user["playlists"]:
              if e["name"] == userinput:
                dobole = True
            if dobole == False:
              looping = False
          # songs
          def atozlistfuncplaylist(e):
            return e["name"]

          songs = []
          print("\n")
          atozlist = data["songs"]
          atozlist.sort(key=atozlistfuncplaylist)
          looping = True
          while looping == True:
            curentsongs = []
            for adf in songs:
              curentsongs.insert(len(songs), adf["name"])
            print("\n\ncurent songs = ", curentsongs,
                  "\n\n1.add song\n2.finish\n")
            userinput = input("please enter a number | > ")
            if userinput == "1":
              atozlist = data["songs"]
              atozlist.sort(key=atozlistfuncplaylist)
              for i in atozlist:
                print(i["name"] + " artist : " + i["artist"] + "  time : " +
                      i["length"] + " link : " + i["link"] + "\n")
              tmplooping = True
              failedtmp = True
              while tmplooping == True:
                userinput = input("\nplease enter  a song name | > ")
                for f in data["songs"]:
                  if str(f["name"]) == userinput:
                    songs.insert(len(songs), f)
                    failedtmp = False
                    tmplooping = False
                if failedtmp == True:
                  print("\nerror not in data base please retry\n")
            elif userinput == "2":
              if songs == []:
                print("you need at least 1 song")
              else:
                looping = False
          #print(user)
          user["playlists"].insert(len(user["playlists"]), {
            "name": playlistname,
            "songs": songs
          })
          updatedata()
          #startmenu(username, userpassword)
      startmenu(username, userpassword)
    elif userinput == 2:
      #generate playlist
      loopinggenerate = True
      requrements = {"amount": "0", "length": "0", "genres": {}, "artists": {}}
      while loopinggenerate == True:
        os.system("cls")
        print(
          "please select a requrement or generate you need 1 requrement to generate\ncurent requrements ",
          requrements,
          "\n\n1.amount\n2.length\n3.genres\n4.artists\n5.generate\n")
        userinput = input("please enter a number | > ")
        if userinput == "1":
          os.system("cls")
          print("curent count : ", requrements["amount"])
          requrements["amount"] = int(
            input("input number of songs type 0 for max | > "))
        elif userinput == "2":
          os.system("cls")
          print("curent length : ", requrements["length"])
          requrements["length"] = int(
            input("input max total length of all songs type 0 for max | > "))
        elif userinput == "3":
          os.system("cls")
          print("curent genres : ", requrements["genres"],
                "\n\n1.add genre\n2.remove genre\n")
          useropt = input("input a number leave blank to go back | > ")
          if useropt == "1":
            os.system("cls")
            print("curent genres : ", requrements["genres"])
            requrements["genres"][len(
              requrements["genres"])] = input("input genre | > ")
          elif useropt == "2":
            os.system("cls")
            print("curent genres : ", requrements["genres"])
            userinput = input(
              "input the number of the genre you want to remove | > ")
            del requrements["genres"][int(userinput)]
        elif userinput == "4":
          os.system("cls")
          print("curent artists : ", requrements["artists"],
                "\n\n1.add artist\n2.remove artist\n")
          useropt = input("input a number leave blank to go back | > ")
          if useropt == "1":
            os.system("cls")
            print("curent artists : ", requrements["artists"])
            requrements["artists"][len(
              requrements["artists"])] = input("input artist name | > ")
          elif useropt == "2":
            os.system("cls")
            print("curent artists : ", requrements["artists"])
            userinput = input(
              "input name of the artist you want to remove | > ")
            del requrements["artists"][int(userinput)]
        elif userinput == "5":
          if requrements == {
              "amount": "0",
              "length": "0",
              "genres": {},
              "artists": {}
          }:
            print("you requre at least 1 requrement press enter to retry")
            input()
          else:
            loopinggenerate = False
      #generate it
      playlistsongs = []
      playlistjson = []
      curentlength = 0
      curentamount = 0
      for s in data["songs"]:
        meetsrequrements = True
        if int(requrements["length"]) != 0:
          if (int(s["length"]) + curentlength) > int(requrements["length"]):
            print("length")
            meetsrequrements = False
        if int(requrements["amount"]) != 0:
          if (curentamount - 1) > int(requrements["amount"]):
            print("amount")
            meetsrequrements = False
        if requrements["genres"] != {}:
          isagenre = False
          for genres in requrements["genres"]:
            if s["genre"] == requrements["genres"][genres]:
              isagenre = True
          if isagenre == False:
            meetsrequrements = False
            print("genre")
        if requrements["artists"] != {}:
          isaartist = False
          for artists in requrements["artists"]:
            if s["artist"] == requrements["artists"][artists]:
              isaartist = True
          if isaartist == False:
            print("art")
            meetsrequrements = False
        if meetsrequrements == True:
          curentlength += int(s["length"])
          print("meets requrements")
          playlistjson.append({
            "name": s["name"],
            "artist": s["artist"],
            "length": s["length"],
            "genre": s["genre"],
            "link": s["link"]
          })
          playlistsongs.append(s["name"] + " " + s["artist"] + " " +
                               s["length"] + " " + s["genre"] + " " +
                               s["link"])
          playlistjson
          curentamount += 1
          input
      os.system("cls")
      for pls in playlistsongs:
        print(pls + "\n")
      for user in data["users"]:
        if user["name"] == username:
          user["playlists"].insert(len(user["playlists"]), {
            "name": input("enter playlist name | > "),
            "songs": playlistjson
          })
          updatedata()
      input("press enter")
      startmenu(username, userpassword)
    elif userinput == 3:
      # show playlists
      os.system("cls")
      for user in data["users"]:
        if user["name"] == username:
          for i in user["playlists"]:
            print("\n", i["name"])
          tmploop = True
          while tmploop == True:
            userinput = input("\ninput name or type 1 to cancel | > ")
            if userinput == "1":
              tmploop = False
              startmenu(username, userpassword)
            else:
              for n in user["playlists"]:
                if n["name"] == userinput:
                  tmploop = False
                  print(n)
              if tmploop == True:
                print("error not a name")
              input("\npress enter to go back")
              startmenu(username, userpassword)
  elif optnum == "4":
    # add song
    looping = True
    while looping == True:
      os.system("cls")
      print("please enter song name")
      sname = input()
      out_file = open("data.json", "r")
      istaken = False
      for i in json.load(out_file)["songs"]:
        if i["name"] == sname:
          istaken = True
      if istaken == True:
        print("name alredy taken")
        print()
        input("press enter to continue")
      elif istaken == False:
        looping = False
    out_file.close()
    print()
    print("what is the artists name")
    aname = input()
    print()
    print("what is the genre")
    gname = input()
    print()
    print("what is link?")
    slink = input()
    print("press enter to start caculating the length")
    input()
    os.system("cls")
    print("input hours")
    hlength = input()
    print()
    print("input minutes")
    mlength = input()
    print()
    print("input seconds")
    slength = input()
    length = str(
      (((int(hlength) * 60) * 60) + (int(mlength) * 60) + int(slength)))
    data["songs"].insert(
      len(data["songs"]), {
        "name": sname,
        "artist": aname,
        "genre": gname,
        "length": length,
        "link": slink,
      })
    updatedata()
    startmenu(name, userpassword)
  elif optnum == "5":
    os.system("cls")
    print("what can i help you with \n\n1.info\n2.help\n")
    userinput = input("please input a number | > ")
    if userinput == "1":
      os.system("cls")
      print(
        "what info would you like?\n\n1.licence\n2.creator\n3.other projects\n"
      )
      userinput = input("please input a number | > ")
      if userinput == "1":
        os.system("cls")
        licence = open("LICENCE", "r")
        print(" this project is under the mit licence\n", licence.read())
        licence.close()
        input("\npress enter")
        startmenu(name, userpassword)
      elif userinput == "2":
        os.system("cls")
        print(
          "the developer, me is coneastdev. My github account is https://github.com/coneastdev and my website is account is https://coneastdev.github.io"
        )
        input("\npress enter")
        startmenu(name, userpassword)
      elif userinput == "3":
        os.system("cls")
        print(
          "my other projects are on https://github.com/coneastdev")
        input("\npress enter")
        startmenu(name, userpassword)
    elif userinput == "2":
      os.system("cls")
      print(
        "what do you need help with?\n\n1.why dosent it play songs\n2.what does mit licence mean?"
      )
      userinput = input("please input a number | > ")
      if userinput == "3":
        os.system("cls")
        print(
          "mit licence refers to Massachusetts Institute of Technology licence it gives the user full permision to reuse assets and code for free with no warenty if something of yours is damged. The wikipedia page talks more in depth https://en.wikipedia.org/wiki/MIT_License"
        )
        input("\npress enter")
        startmenu(name, userpassword)
      elif userinput == "1":
        os.system("cls")
        print(
          "sorry but you want me to add a folder of music and load that via python, I dont want to do that so you need to click on the links provided"
        )
        input("\npress enter")
        startmenu(name, userpassword)
    else:
      os.system('cls')
      startmenu(name, userpassword)
  else:
    os.system('cls')
    startmenu(name, userpassword)

print("welcome do you have an account y/n")
if input() == "y":
  # user login
  out_file = open("data.json", "r")
  looping = True
  out_file.close()
  while looping == True:
    out_file = open("data.json", "r")
    print("please log in")
    name = input("name : ")
    print()
    password = input("password : ")
    for i in json.load(out_file)["users"]:
      if i["name"] == name:
        if i["pass"] == password:
          name = i["name"]
          userpassword = i["pass"]
          looping = False
    if looping == True:
      print("incorect username and or password")
      print()
      input("press enter to continue")
      os.system('cls')
    out_file.close()
    out_file.close()
    print()
  startmenu(name, userpassword)
else:
  os.system('cls')
  print("would you like to make an account? y/n")
  if input() == "y":
    #user createing account
    looping = True
    out_file = open("data.json", "r")
    users = json.load(out_file)["users"]
    while looping == True:
      error = False
      print("please enter a user name")
      username = input()
      for i in users:
        if i["name"] == username:
          error = True
      if error == False:
        looping = False
      elif error == True:
        print()
        print("error user name alredy taken please retry")
    os.system('cls')
    print("please enter a password")
    password = input()
    out_file.close()
    os.system("cls")
    print("please input your gender male/female/other/no comment")
    looping = True
    gender = ""
    while looping == True:
      gender = input()
      if gender == "male":
        looping = False
      elif gender == "female":
        looping = False
      elif gender == "other":
        looping = False
      elif gender == "no comment":
        looping = False
      else:
        print("error please input one of the folowing male/female/other")
        input("press enter try agin")
        os.system("cls")
        print("please input your gender male/female/other")
    os.system("cls")
    print("please input fav artist")
    favart = input()
    print()
    print("please input fav genre")
    favgenre = input()
    os.system("cls")
    print("please enter YEAR of birth")
    dobyear = input()
    print()
    print("please enter MONTH of birth")
    dobmonth = input()
    print()
    print("please enter DAY of birth")
    dobday = input()
    data["users"].insert(
      len(data["users"]), {
        "name": username,
        "pass": password,
        "gender": gender,
        "favart": favart,
        "favgenre": favgenre,
        "dob": str(dobday + "/" + dobmonth + "/" + dobyear),
        "playlists": []
      })
    updatedata()
    startmenu(username, password)
  else:
    #user dosent have or want account
    quit()