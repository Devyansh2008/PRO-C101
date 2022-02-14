import dropbox
class PROC101 :
    def __init__(self,accessToken) :
        self.a=accessToken
    
    def Upload(self,source,destination):
        dbx=dropbox.Dropbox(self.a)
        E=open(source,"rb")
        dbx.files_upload(E.read(),destination)


def Sus() :
    AT="sl.BCClwv1tpxNJqVeF7M6Cax_Egr8DqsYPMzf2uIbyLL7tHBaEnt4cWgElSw_E4lcJiioD7d41Ui8zMzOqJwsLjeLUMx8IG1o_OiqqWNZwxfMaFvNVK8We9OGzEppFKHZqFRIv00rFFTOS"
    Foil=PROC101(AT)
    s=input("What is the source file,\n")
    d=input("What is the apps name,\n")
    Foil.Upload(s,d)
    print("Project compelete")

Sus()