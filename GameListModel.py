import sqlite3
import os

class GameListDB:
    def __init__(self,path) -> None:
        con = sqlite3.connect(path);
        self.cur = con.cursor();

    def getMissingTimes(self):
        res = self.cur.execute(
            "SELECT id, name "+
            "FROM Backlog " +
            "where min_time is null or max_time is null ");
        return res.fetchall();
    
    def updateEntry(self,id: int,min_hours,max_hours):
            
        self.cur.executescript("UPDATE Backlog "+
        "SET "+
            "min_time = " +str(min_hours)+","+
            "max_time = " +str(max_hours)+
        " WHERE id="+str(id));

    def __del__(self):
        self.cur.close()