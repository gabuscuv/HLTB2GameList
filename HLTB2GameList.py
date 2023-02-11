from GameListModel import GameListDB
from howlongtobeatpy import HowLongToBeat

class HLTB2GameList:
    def __init__(self,path) -> None:
        self.gameListModel = GameListDB(path)
        self.hltb=HowLongToBeat()

    def run(self):
 #           list = ({})
            for var in self.gameListModel.getMissingTimes():
                print("Searching "+var[1])
                list = self.hltb.search(var[1])
                match len(list):
                    case 0: print(var[1]+" doesn't found"); continue;
                    case 1: print("Adding "+list[0].game_name); self.updateEntry(var[0],list[0]); continue; 
                
                selection = self.reviewList(list)
                self.updateEntry(var[0],list[selection])
                continue;

    def reviewList(self,list):
        for count,game in enumerate(list):
            print("["+str(count)+"]: "+game.game_name +" ("+str(game.release_world)+") By "+ game.profile_dev)
        
        while True:
            selection = int(input("Choose an option (Default: 0): ") or "0")
            if selection >= 0 and selection < len(list):
                break;
            print("Pardon, Could You repeat?")
        
        return selection

    def updateEntry(self,id: int,game):
            self.gameListModel.updateEntry(int(id),game.main_story,game.main_extra)

    def __del__(self):
        del self.gameListModel
        del self.hltb

