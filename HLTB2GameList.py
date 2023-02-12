from GameListModel import GameListDB
from howlongtobeatpy import HowLongToBeat

class HLTB2GameList:
    def __init__(self,path) -> None:
        self.gameListModel = GameListDB(path)
        self.hltb=HowLongToBeat()

    def run(self):
            for var in self.gameListModel.getMissingTimes():
                print("Searching " + var[1])
                self.searchGame(var[0],var[1])

    def searchGame(self, id, name):
        # list = ({})
        list = self.hltb.search(name)
        match len(list):
            case 0: print(name+" doesn't found"); self.customName(id); return;
            case 1: print("Adding "+list[0].game_name); self.updateEntry(id,list[0]); return; 
        
        selection = self.reviewList(list)
        self.updateEntry(id,list[selection])
        return;


    def reviewList(self, list):
        for count,game in enumerate(list):
            print("["+str(count)+"]: "+game.game_name +" ("+str(game.release_world)+") By "+ game.profile_dev)

        return self.inputChoosing(0,len(list))

    def customName(self,id):
        ## TODO Make a y/n answer
        print("Do You Wish search for another name? 0 = No, 1 = Yes ")
        if self.inputChoosing(0,2):
            name = input("Write a Alternative Name: ")
            self.searchGame(id,name)

    ## TODO Extract this function from the main script
    def inputChoosing(self, min: int, length: int):
        while True:
            selection = int(input("Choose an option (Default: 0): ") or "0")
            if selection >= min and selection < length:
                break;
            print("Pardon, Could You repeat?")
        
        return selection

    def updateEntry(self,id: int,game):
            self.gameListModel.updateEntry(int(id),game.main_story,game.main_extra)

    def __del__(self):
        del self.gameListModel
        del self.hltb

