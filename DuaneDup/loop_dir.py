import os
import shutil
from datetime import datetime


class DeDup():
    def __init__(self, **kw):
        super(DeDup, self).__init__(**kw)
        self.dir_ = os.getcwd()
        self.all_files = []
        date_time = ""
        
        dt_now = datetime.now()
        date_time = dt_now.strftime("_%Y_%m_%d_%H_%M_%S")
        print("[CURRENT_DATE_TIME]:[",date_time,"]")
        self.stash = "de_dup"+date_time
        print("[NEW_FOLDER_MADE]:[",str(self.stash),"]")


    def get_all_files(self, path):
        try:
            files = os.listdir(path)
            for item in files:
                if os.path.isdir(os.path.join(path,item)):
                    self.get_all_files(os.path.join(path,item))
                else:
                    if item.endswith('.txt'):
                        print(">> ", str(os.path.join(path,item)))
                        try:
                            self.all_files.append(os.path.join(path,item))
                            print("[COLLECTED]:: ", str(item))
                        except Exception as e:
                            print('[ERROR]:[SELF.ALL_FILES.APPEND]:[', str(e), "]")
        except Exception as e:
            print("[ERROR]::[GET_ALL_FILES]::[", str(e),"]")


    def copy_files(self):
        try:
            self.get_all_files(self.dir_)
        except Exception as e:
            print(f"[ERROR]::[GET_ALL_FILES]::[CP_FILES]::[{str(e)}]")
        try:
            for file_ in self.all_files:
                try:
                    print("[COPYING]: \n >> ", str(file_))
                    shutil.copy2(file_, self.stash)
                    print("[TO]: >>", str(self.stash))
                except Exception as e:
                    print("[DUPLICATE_FOUND]:?:", str(e))
                    pass
        except Exception as e:
            print("[ERROR]::[COPY_FILES]::[", str(e),"]")



    def mk_folder(self):
        if not os.path.exists(self.stash):
            print("[MAKING_NEW_FOLDER]", str(self.stash))
            # Create a new directory called "de_dupped" if it does not exist
            os.mkdir(self.stash)
            print("[FOLDER_MADE]\n")




    def clean_up(self):
        pass



    def main(self):
        opt = ""
        while "Q" not in opt.upper():
            try:
                opt = input( "[DE_DUP]\n\
                        by:[DUANE]\n\n\
                        OPTIONS: \n\
                        >>  [SCAN]  '-s'  \n\
                        >>  [COPY]  '-cp' \n\
                        >>  [CLEAN] '-cl' \n\n\
                        ->>     ")
                if opt.upper() == "-s" or "SCAN" in opt.upper():
                    self.get_all_files(self.dir_)

                elif opt.upper() == "-cp" or "COPY" in opt.upper():
                    try:
                        self.mk_folder()
                    except Exception as e:
                        print("[ERROR]::[", str(e),"]")
                    try:
                        self.copy_files()
                    except Exception as e:
                        print("[ERROR]::[", str(e),"]")

            except Exception as e:
                print('[ERROR]::[', str(e),"]")



if __name__=="__main__":
    D = DeDup()
    D.main()