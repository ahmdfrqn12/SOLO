import KIA
from KIA import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
#-----------------------
cl = LineClient("email","paswod")
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = cl.getProfile()
lineSettings = cl.getSettings()
mid = cl.getProfile().mid
responsename = cl.getProfile().displayName

ka = LineClient("email","paswod")
ka.log("Auth Token : " + str(ka.authToken))
channel = LineChannel(ka)
cka.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = ka.getProfile()
lineSettings = ka.getSettings()
Amid = ka.getProfile().mid
responsename = ka.getProfile().displayName

kb = LineClient("email","paswod")
kb.log("Auth Token : " + str(kb.authToken))
channel = LineChannel(kb)
kb.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kb.getProfile()
lineSettings = kb.getSettings()
Bmid = kb.getProfile().mid
responsename = kb.getProfile().displayName

kc = LineClient("email","paswod")
kc.log("Auth Token : " + str(kc.authToken))
channel = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kc.getProfile()
lineSettings = kc.getSettings()
Cmid = kc.getProfile().mid
responsename = kc.getProfile().displayName

kd = LineClient("email","paswod")
kd.log("Auth Token : " + str(kd.authToken))
channel = LineChannel(kd)
kd.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kd.getProfile()
lineSettings = kd.getSettings()
Dmid = kd.getProfile().mid
responsename = kd.getProfile().displayName

ke = LineClient("email","paswod")
ke.log("Auth Token : " + str(ke.authToken))
channel = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = ke.getProfile()
lineSettings = ke.getSettings()
Emid = ke.getProfile().mid
responsename = ke.getProfile().displayName

kf = LineClient("email","paswod")
kf.log("Auth Token : " + str(kf.authToken))
channel = LineChannel(kf)
kf.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kf.getProfile()
lineSettings = cl.getSettings()
Fmid = kf.getProfile().mid
responsename = kf.getProfile().displayName

kg = LineClient("email","paswod")
kg.log("Auth Token : " + str(kg.authToken))
channel = LineChannel(kg)
kg.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kg.getProfile()
lineSettings = kg.getSettings()
Gmid = cl.getProfile().mid
responsename = kg.getProfile().displayName

kh = LineClient("email","paswod")
kh.log("Auth Token : " + str(kh.authToken))
channel = LineChannel(kh)
kh.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kh.getProfile()
lineSettings = kh.getSettings()
Hmid = kh.getProfile().mid
responsename = kh.getProfile().displayName

ki = LineClient("email","paswod")
ki.log("Auth Token : " + str(ki.authToken))
channel = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = ki.getProfile()
lineSettings = ki.getSettings()
Imid = ki.getProfile().mid
responsename = ki.getProfile().displayName

kj = LineClient("email","paswod")
kj.log("Auth Token : " + str(kj.authToken))
channel = LineChannel(kj)
kj.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kj.getProfile()
lineSettings = kj.getSettings()
Jmid = kj.getProfile().mid
responsename = kj.getProfile().displayName

kk = LineClient("email","paswod")
kk.log("Auth Token : " + str(kk.authToken))
channel = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kk.getProfile()
lineSettings = kk.getSettings()
Kmid = kk.getProfile().mid
responsename = kk.getProfile().displayName

kl = LineClient("email","paswod")
kl.log("Auth Token : " + str(kl.authToken))
channel = LineChannel(kl)
kl.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kl.getProfile()
lineSettings = kl.getSettings()
Lmid = kl.getProfile().mid
responsename = kl.getProfile().displayName

km = LineClient("email","paswod")
km.log("Auth Token : " + str(km.authToken))
channel = LineChannel(km)
km.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = km.getProfile()
lineSettings = km.getSettings()
Mmid = km.getProfile().mid
responsename = km.getProfile().displayName

kn = LineClient("email","paswod")
kn.log("Auth Token : " + str(kn.authToken))
channel = LineChannel(kn)
kn.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kn.getProfile()
lineSettings = kn.getSettings()
Nmid = kn.getProfile().mid
responsename = kn.getProfile().displayName

ko = LineClient("email","paswod")
ko.log("Auth Token : " + str(ko.authToken))
channel = LineChannel(ko)
ko.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = ko.getProfile()
lineSettings = ko.getSettings()
Omid = ko.getProfile().mid
responsename = ko.getProfile().displayName

kp = LineClient("email","paswod")
kp.log("Auth Token : " + str(kp.authToken))
channel = LineChannel(kp)
kp.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kp.getProfile()
lineSettings = kp.getSettings()
Pmid = kp.getProfile().mid
responsename = kp.getProfile().displayName

kq = LineClient("email","paswod")
kq.log("Auth Token : " + str(kq.authToken))
channel = LineChannel(kq)
kq.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kq.getProfile()
lineSettings = kq.getSettings()
Qmid = kq.getProfile().mid
responsename = kq.getProfile().displayName

kr = LineClient("email","paswod")
kr.log("Auth Token : " + str(kr.authToken))
channel = LineChannel(kr)
kr.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = kr.getProfile()
lineSettings = kr.getSettings()
Rmid = kr.getProfile().mid
responsename = kr.getProfile().displayName

ks = LineClient("email","paswod")
ks.log("Auth Token : " + str(ks.authToken))
channel = LineChannel(ks)
ks.log("Channel Access Token : " + str(channel.channelAccessToken))
lineProfile = ks.getProfile()
lineSettings = ks.getSettings()
Smid = ks.getProfile().mid
responsename = ks.getProfile().displayName

sw = LineClient("email","paswod")
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))
lineProfile = sw.getProfile()
lineSettings = sw.getSettings()
Zmid = sw.getProfile().mid
responsename = sw.getProfile().displayName

print("LOGIN SUCCES bot protect by : ahmdfrqn")

poll = LinePoll(cl)
call = cl
creator = ["ue8e0c10d65dd6b9427f861e3583071ea"]
owner = ["ue8e0c10d65dd6b9427f861e3583071ea"]
admin = ["ue8e0c10d65dd6b9427f861e3583071ea"]
staff = ["ue8e0c10d65dd6b9427f861e3583071ea"]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Imid = ki.getProfile().mid
Jmid = kj.getProfile().mid
Kmid = km.getProfile().mid
Lmid = kl.getProfile().mid
Mmid = km.getProfile().mid
Nmid = kn.getProfile().mid
Omid = ko.getProfile().mid
Pmid = kp.getProfile().mid
Qmid = kq.getProfile().mid
Rmid = kr.getProfile().mid
Smid = ks.getProfile().mid
Zmid = sw.getProfile().mid
KAC=[cl,ka,kb,kc,kd,ke,kf,kg,kh,ki,kj,kk,kl,km,kn,ko,kp,kq,kr,ks,sw]
ABC=[ka,kb,kc,kd,ke,kf,kg,kh,ki,kj,kk,kl,km,kn,ko,kp,kq,kr,ks,sw]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid,Zmid]
Dpk = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []

responsename1 = ka.getProfile().displayName
responsename2 = kb.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kd.getProfile().displayName
responsename5 = ke.getProfile().displayName
responsename6 = kf.getProfile().displayName
responsename7 = kg.getProfile().displayName
responsename8 = kh.getProfile().displayName
responsename9 = ki.getProfile().displayName
responsename10 = kj.getProfile().displayName
responsename11 = kk.getProfile().displayName
responsename12 = kl.getProfile().displayName
responsename13 = km.getProfile().displayName
responsename14 = kn.getProfile().displayName
responsename15 = ko.getProfile().displayName
responsename16 = kp.getProfile().displayName
responsename17 = kq.getProfile().displayName
responsename18 = kr.getProfile().displayName
responsename19 = ks.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":True,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": {},
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "pinvite":True,
    "pcancel":True,
    "pkick":True,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoBlock':False,
    'autoAdd':False,
    'qr':True,
    'antijs':True,
    'autoRead':False,
    'autoLeave':True,
    'autoLeave1':True,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "protectantijsOn":True,
    "ghostOn":False,
    "mention":"Lagi Stalking yaaa...! gabung sini ðŸ˜Š",
    "Respontag":"Apaan tag2 kalo penting VC aja langsung",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like ",
    "message":"[ Auto block ]\nThanks for add me ðŸ˜­",
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "DAFTAR JONESã€Œ{}ã€\n\n  [ Silahkan pilih ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâ•šâ•â•[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâ•šâ•â•[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Hallo  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâ•šâ•â•[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\nâ•šâ•â•[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"â— Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nâ— Group : "+str(len(gid))+"\nâ— Teman : "+str(len(teman))+"\nâ— Expired : In "+hari+"\nâ— Version : MAX v10\nâ— Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nâ— Runtime : \n â€¢ "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
    
def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "â–¬â–¬â–¬â–¬*****â–¬â–¬â–¬â–¬\n" + \
                  "â•”â•[ PROTECT BY TEAM A.D.M ]\n"+\
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Help\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Help bot\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Help group\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Invitebot\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Respon\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "join\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "bye\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ghost join\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ghost bye\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Bye me\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Leaveã€ŒNamagrupã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ginfo\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Open\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Close\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Url\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Gruplist\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Openã€Œnomerã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Closeã€Œnomerã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Infogrupã€Œnomerã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Infomemã€Œnomerã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Leaveallã€Œnomerã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Remove chat\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Lurkingã€Œon/offã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Lurkers\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Siderã€Œon/offã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Updatefoto\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Updategrup\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Updatebot\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Broadcast:ã€ŒTextã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Setkeyã€ŒNew Keyã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Mykey\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Resetkey\n" + \
                  "â• â•â•[ á´á´‡á´…Éªá´€ ]\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Kode wilayah\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Listmp3\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Listvideo\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Listimage\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Liststicker\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Addimgã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Dellimgã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Addmp3ã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Dellmp3ã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Addvideoã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Dellvideoã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Addstickerã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Dellstickerã€ŒTeksã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Spamtag:ã€Œjumlahnyaã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Spamtagã€Œ@ã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Spamcall:ã€Œjumlahnyaã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Spamcall\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Ytmp3:ã€ŒJudul Laguã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Ytmp4:ã€ŒJudul Videoã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Musikã€ŒNama Penyanyiã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-fsã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-lineã€ŒID Lineã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-apkã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-gifã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-xxxã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-animeã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-mimpiã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-audioã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-mp3ã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-videoã€ŒQueryã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-bintangã€ŒZodiakã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-zodiakã€ŒZodiakã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-sholatã€ŒNama Kotaã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-cuacaã€ŒNama Kotaã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-lokasiã€ŒNama Kotaã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-lirikã€ŒJudul Laguã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-instagramã€ŒUser Nameã€\n" + \
                  "â•‘ðŸ”°â˜ˆ " + key + "Get-dateã€Œtgl-bln-thnã€\n" + \
                  "â• â•â•[ protect ]\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Notagã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Allproã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Protecturlã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Protectjoinã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Protectkickã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Protectinviteã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Protectcancelã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Antijsã€Œon/offã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Ghostã€Œon/offã€\n" + \
                  "â• â•â•[ Set kicker ]\n" + \
                  "â•‘ðŸ˜ˆâ˜ˆ " + key + "Kickã€Œon/offã€\n" + \
                  "â•‘ðŸ˜ˆâ˜ˆ " + key + "Gkã€Œ@ã€\n" + \
                  "â•‘ðŸ˜ˆâ˜ˆ " + key + "Bkã€Œ@ã€\n" + \
                  "â•‘ðŸ˜ˆâ˜ˆ " + key + "Sadis *à¸„à¸³à¸ªà¸±à¹ˆà¸‡à¸šà¸´à¸™à¸à¸¥à¸¸à¹ˆà¸¡\n" + \
                  "â• â•â•[ Set user ]\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Inviteã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Stickerã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Unsendã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Respontimeã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Timelineã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Contactã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Autojoinã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Autoaddã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Welcomeã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Autoleaveã€Œon/offã€\n" + \
                  "â•‘ðŸ””â˜ˆ " + key + "Jointicketã€Œon/offã€\n" + \
                  "â• â•â•[ Set Admin ]\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Selfã€Œon/offã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Bot:on\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Bot:expell\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Staff:on\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Staff:expell\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Admin:on\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Admin:expell\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Botaddã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Botdellã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Staffaddã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Staffdellã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Adminaddã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Admindellã€Œ@ã€\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Refresh\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Listbot\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Listadmin\n" + \
                  "â•‘ðŸ’€â˜ˆ " + key + "Listprotect\n" + \
                  "â•šâ•[ PROTECT BY TEAM A.D.M ]\n" + \
                  "â–¬â–¬â–¬â–¬*****â–¬â–¬â–¬â–¬\n" + \
                  "\nKetikã€Œ Refresh ã€jika sudah habis anu...\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "â–¬â–¬â–¬â–¬*****â–¬â–¬â–¬â–¬\n" + \
                  "â•”â•[ Help blacklist ]\n"+\
                  "â•‘ðŸ›¡â˜ˆ " + key + "Blc\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Ban:on\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Unban:on\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Banã€Œ@ã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Unbanã€Œ@ã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Talkbanã€Œ@ã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Untalkbanã€Œ@ã€\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Talkban:on\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Untalkban:on\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Banlist\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Talkbanlist\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Clearban\n" + \
                  "â•‘ðŸ›¡â˜ˆ " + key + "Refresh\n" + \
                  "â• â•â•[ Help bot ]\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist1\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist2\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist3\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist4\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist5\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist6\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist7\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist8\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist9\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist10\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist11\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist12\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist13\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist14\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist15\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist16\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist17\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist18\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Assist19\n" + \
                  "â• â•â•[ Help update ]\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Updatefoto\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot1up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot2up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot3up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot4up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot5up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot6up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot7up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot8up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot9up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot10up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot11up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot12up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot13up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot14up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot15up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot16up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot17up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot18up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot19up\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Ghostup\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Myname:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot1name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot2name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot3name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot4name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot5name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot6name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot7name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot8name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot9name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot10name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot11name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot12name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot13name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot14name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot15name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot16name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot17name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot18name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Bot19name:ã€ŒNameã€\n" + \
                  "â•‘ðŸ•µâ˜ˆ " + key + "Ghostname:ã€ŒNameã€\n" + \
                  "â• â•â•[ Cek Seting ]\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek sider\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek spam\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek pesan \n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek respon \n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek leave\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Cek welcome\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set sider:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set spam:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set pesan:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set respon:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set leave:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Set welcome:ã€ŒTextã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Myname:ã€ŒNamaã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Gift:ã€ŒMid korbanã€ã€ŒJumlahã€\n" + \
                  "â•‘ðŸ¤–â˜ˆ " + key + "Spam:ã€ŒMid korbanã€ã€ŒJumlahã€\n" + \
                  "â•šâ•[ PROTECT BY TEAM A.D.M ]\n" + \
                  "â–¬â–¬â–¬â–¬à®œÛ©ÛžÛ©à®œâ–¬â–¬â–¬â–¬\n" + \
                  "\nKetikã€Œ Refresh ã€jika sudah habis anu....\n"
    return helpMessage1

def helpgroup():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "â–¬â–¬â–¬â–¬****â–¬â–¬â–¬â–¬\n" + \
                  "â•”â•[ Help Group ]\n"+\
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Me\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Midã€Œ@ã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Infoã€Œ@ã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Gkã€Œ@ã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Bkã€Œ@ã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "SADIS\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Absen\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Status\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "About\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Restart\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Runtime\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Creator\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Sp\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Spb\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Sprespon\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Invitebot\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Respon\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "join\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "bye\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ghost join\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ghost bye\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Bye me\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Leaveã€ŒNamagrupã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Ginfo\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Open\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Close\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Url\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Gruplist\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Remove chat\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Lurkingã€Œon/offã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Lurkers\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Siderã€Œon/offã€\n" + \
                  "â•‘ðŸ‘¿â˜ˆ " + key + "Broadcast:ã€ŒTextã€\n" + \
                  "â•š[ PROTECT BY TEAM A.D.M ]\n" + \
                  "â–¬â–¬â–¬â–¬*****â–¬â–¬â–¬â–¬\n" + \
                  "\nKetikã€Œ Refresh ã€jika sudah habis anu....\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
            
        if op.type == 11:
            if wait["qr"] == True:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ka.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ka.reissueGroupTicket(op.param1)
                                X = ka.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ka.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                ka.updateGroup(X)
                    except:
                        try:
                    	    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kb.reissueGroupTicket(op.param1)
                                    X = kb.getGroup(op.param1)
                            		X.preventedJoinByTicket = True
                            		Ticket = kb.reissueGroupTicket(op.param1)
                            		sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            		sw.kickoutFromGroup(op.param1,[op.param2])
                            		sw.leaveGroup(op.param1)
                            		kb.updateGroup(X)
                        except:
                            try:
                            	if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                    	X = kc.getGroup(op.param1)
                            			X.preventedJoinByTicket = True
                            			Ticket = kc.reissueGroupTicket(op.param1)
                            			sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            			sw.kickoutFromGroup(op.param1,[op.param2])
                            			sw.leaveGroup(op.param1)
                            			kc.updateGroup(X)
                        	except:
                            	try:
                            	    if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    		kd.reissueGroupTicket(op.param1)
                           			 	X = kd.getGroup(op.param1)
                            				X.preventedJoinByTicket = True
                            				Ticket = kd.reissueGroupTicket(op.param1)
                            				sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            				sw.kickoutFromGroup(op.param1,[op.param2])
                            				sw.leaveGroup(op.param1)
                            				kd.updateGroup(X)
                                except:
                                    try:
                                    	if cl.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        	random.choice(ABC).reissueGroupTicket(op.param1)
                                    		X = kc.getGroup(op.param1)
                            				X.preventedJoinByTicket = True
                            				Ticket = random.choice(ABC).reissueGroupTicket(op.param1)
                            				sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            				sw.kickoutFromGroup(op.param1,[op.param2])
                            				sw.leaveGroup(op.param1)
                            				cl.updateGroup(X)
                        		except:
                            		pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"à¸à¸¥à¸¸à¹ˆà¸¡à¸à¸²à¸ à¸à¸²à¸ à¸à¸¹à¹„à¸¡à¹ˆà¸­à¸¢à¸¹à¹ˆà¸«à¸£à¸­à¸ " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        #cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        #cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        #kb.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        #ka.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        #kb.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        #kb.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        #kc.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        #kc.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        #kd.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        #kd.sendMessage(op.param1,"Haii " + str(ginfo.name))
		    if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        #ke.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        #ke.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        #kf.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        #kf.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        #kg.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        #kg.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        #kh.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        #kh.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kj.acceptGroupInvitation(op.param1)
                        ginfo = kj.getGroup(op.param1)
                        #kj.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kj.acceptGroupInvitation(op.param1)
                        ginfo = kj.getGroup(op.param1)
                        #kj.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Kmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Lmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kl.acceptGroupInvitation(op.param1)
                        ginfo = kl.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kl.acceptGroupInvitation(op.param1)
                        ginfo = kl.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Mmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Nmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kn.acceptGroupInvitation(op.param1)
                        ginfo = kn.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Omid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ko.acceptGroupInvitation(op.param1)
                        ginfo = ko.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Pmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kp.acceptGroupInvitation(op.param1)
                        ginfo = kp.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kp.acceptGroupInvitation(op.param1)
                        ginfo = kp.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Qmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kq.acceptGroupInvitation(op.param1)
                        ginfo = kq.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kq.acceptGroupInvitation(op.param1)
                        ginfo = kq.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Rmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kr.acceptGroupInvitation(op.param1)
                        ginfo = kr.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        kr.acceptGroupInvitation(op.param1)
                        ginfo = kr.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))
			if Smid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        ks.acceptGroupInvitation(op.param1)
                        ginfo = ks.getGroup(op.param1)
                        #ki.sendMessage(op.param1,"Haii " + str(ginfo.name))

		if op.type == 13:
            if wait["pinvite"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

		if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

		if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

		if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

		if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

		if op.type == 5:
            print ("[ 5 ] PROTECT BY TEAM A.D.M")
            if wait["autoBlock"] == True:
                cl.sendText(op.param1, wait["message"])
                cl.sendContact(op.param1, "ue8e0c10d65dd6b9427f861e3583071ea")
                cl.blockContact(op.param1)

		if op.type == 19:
            if wait["pkick"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

		if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass

		if op.type == 19:
            try:
                if wait["antijs"] == True:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.prevenJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        random.choice(KAC).acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.prevenJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                       pass

				if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"Pro Tect Js")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

		if op.type == 32:
            if wait["pcancel"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                           pass
                           
                return

		if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ka.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    ka.updateGroup(G)
                                    Ticket = ka.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ka.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ka.updateGroup(G)
                                    Ticket = ka.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kb.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kb.updateGroup(G)
                                    Ticket = kb.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

			if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kd.updateGroup(G)
                                Ticket = kd.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)
                                Ticket = kd.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
		
			if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = ke.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                ke.updateGroup(G)
                                Ticket = ke.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ke.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)
                                Ticket = ke.reissueGroupTicket(op.param1)
                            except:
                                pass
				return

			if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kf.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kf.updateGroup(G)
                                Ticket = kf.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kf.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)
                                Ticket = kf.reissueGroupTicket(op.param1)
                            except:
                                pass
				return

			if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kg.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kg.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kg.updateGroup(G)
                                Ticket = kg.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kg.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)
                                Ticket = kg.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kh.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kh.updateGroup(G)
                                Ticket = kh.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kh.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)
                                Ticket = kh.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ki.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)
                                Ticket = ki.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kj.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kj.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kj.updateGroup(G)
                                Ticket = kj.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kj.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kj.updateGroup(G)
                                Ticket = kj.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Jmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)
                                Ticket = kk.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Kmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kl.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kl.updateGroup(G)
                                Ticket = kl.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kl.updateGroup(G)
                                Ticket = kl.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Lmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = km.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                km.updateGroup(G)
                                Ticket = km.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = km.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)
                                Ticket = km.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Mmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kn.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kn.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kn.updateGroup(G)
                                Ticket = kn.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kn.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kn.updateGroup(G)
                                Ticket = kn.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Nmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            ko.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = ko.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                ko.updateGroup(G)
                                Ticket = ko.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)
                                Ticket = ko.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
            if Omid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kp.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kp.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kp.updateGroup(G)
                                Ticket = kp.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kp.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kp.updateGroup(G)
                                Ticket = kp.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Pmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kq.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kq.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kq.updateGroup(G)
                                Ticket = kq.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kq.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kq.updateGroup(G)
                                Ticket = kq.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Qmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kr.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kr.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kr.updateGroup(G)
                                Ticket = kr.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kr.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kr.updateGroup(G)
                                Ticket = kr.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Rmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            ks.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = ks.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                ks.updateGroup(G)
                                Ticket = ks.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = ks.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                ks.updateGroup(G)
                                Ticket = ks.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if Smid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2]
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                 		       G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                kd.updateGroup(G)
                                Ticket = kd.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                km.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kn.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kp.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kq.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                G = kd.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)
                                Ticket = kd.reissueGroupTicket(op.param1)
                            except:
                                pass
				return
				
			if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,admin)
                        random.choice(ABC).inviteIntoGroup(op.param1,admin)
                    except:
                        pass

                return
                
            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(ABC).findAndAddContactsByMid(op.param1,staff)
                        random.choice(ABC).inviteIntoGroup(op.param1,staff)
                    except:
                        pass

                return
                
        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        #image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"136","STKPKGID":"1","STKVER":"100"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"ã€ŒCek ID Stickerã€\nâ§STKID : " + msg.contentMetadata["STKID"] + "\nâ§STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nâ§STKVER : " + msg.contentMetadata["STKVER"]+ "\n\nã€ŒLink Stickerã€" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"â§Nama : " + msg.contentMetadata["displayName"] + "\nâ§MID : " + msg.contentMetadata["mid"] + "\nâ§Status Msg : " + contact.statusMessage + "\nâ§Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nã€ŒLink Stickerã€" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"â§Nama : " + msg.contentMetadata["displayName"] + "\nâ§MID : " + msg.contentMetadata["mid"] + "\nâ§Status Msg : " + contact.statusMessage + "\nâ§Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#Menambahkan bot
				if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot TEAM A.D.M")
#Menambahkan staff
				if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#Menambahkan admin
				if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#Menambahkan blacklist
				if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#talkban
				if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#updatepicture
				if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")
                            
                if msg.contentType == 1:
                    if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ka.updateProfilePicture(path)
                            ka.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["ARfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["ARfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = kj.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            kj.updateProfilePicture(path)
                            kj.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Kmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Kmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Lmid in Setmain["ARfoto"]:
                            path = kl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Lmid]
                            kl.updateProfilePicture(path)
                            kl.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Mmid in Setmain["ARfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Mmid]
                            km.updateProfilePicture(path)
                            km.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Nmid in Setmain["ARfoto"]:
                            path = kn.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Nmid]
                            kn.updateProfilePicture(path)
                            kn.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Omid in Setmain["ARfoto"]:
                            path = ko.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Omid]
                            ko.updateProfilePicture(path)
                            ko.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Pmid in Setmain["ARfoto"]:
                            path = kp.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Pmid]
                            kp.updateProfilePicture(path)
                            kp.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Qmid in Setmain["ARfoto"]:
                            path = kq.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Qmid]
                            kq.updateProfilePicture(path)
                            kq.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Rmid in Setmain["ARfoto"]:
                            path = kr.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Rmid]
                            kr.updateProfilePicture(path)
                            kr.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Smid in Setmain["ARfoto"]:
                            path = ks.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Smid]
                            ks.updateProfilePicture(path)
                            ks.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")
                            
               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kd.downloadObjectMsg(msg_id)
                     path5 = ke.downloadObjectMsg(msg_id)
                     path6 = kf.downloadObjectMsg(msg_id)
                     path7 = kg.downloadObjectMsg(msg_id)
                     path8 = kh.downloadObjectMsg(msg_id)
                     path9 = ki.downloadObjectMsg(msg_id)
                     path10 = kj.downloadObjectMsg(msg_id)
                     path11 = kk.downloadObjectMsg(msg_id)
                     path12 = kl.downloadObjectMsg(msg_id)
                     path13 = km.downloadObjectMsg(msg_id)
                     path14 = kn.downloadObjectMsg(msg_id)
                     path15 = ko.downloadObjectMsg(msg_id)
                     path16 = kp.downloadObjectMsg(msg_id)
                     path17 = kq.downloadObjectMsg(msg_id)
                     path18 = kr.downloadObjectMsg(msg_id)
                     path19 = ks.downloadObjectMsg(msg_id)
                     path20 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path1)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path2)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kh.updateProfilePicture(path3)
                     kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ki.updateProfilePicture(path4)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kj.updateProfilePicture(path5)
                     kj.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path5)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 kl.updateProfilePicture(path1)
                     kl.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 km.updateProfilePicture(path5)
                     km.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 kn.updateProfilePicture(path5)
                     kn.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 ko.updateProfilePicture(path5)
                     ko.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 kp.updateProfilePicture(path5)
                     kp.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 kq.updateProfilePicture(path5)
                     kq.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
				 	kr.updateProfilePicture(path5)
                     kr.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 ks.updateProfilePicture(path5)
                     ks.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
					 sw.updateProfilePicture(path5)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ka.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        kd.sendChatChecked(msg.to, msg_id)
                        ke.sendChatChecked(msg.to, msg_id)
                        kf.sendChatChecked(msg.to, msg_id)
                        kg.sendChatChecked(msg.to, msg_id)
                        kh.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kj.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kl.sendChatChecked(msg.to, msg_id)
                        km.sendChatChecked(msg.to, msg_id)
                        kn.sendChatChecked(msg.to, msg_id)
                        ko.sendChatChecked(msg.to, msg_id)
                        kp.sendChatChecked(msg.to, msg_id)
                        kq.sendChatChecked(msg.to, msg_id)
                        kr.sendChatChecked(msg.to, msg_id)
                        ks.sendChatChecked(msg.to, msg_id)
                        sw.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))

                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")

                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")

                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "help group":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = helpgroup()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "PROTECT BY TEAM A.D.M"
                                if wait["sticker"] == True: md+="ðŸ˜ˆ Stickerã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Stickerã€Œ âœ– ã€\n"
                                if wait["contact"] == True: md+="ðŸ˜ˆ Contactã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Contactã€Œ âœ– ã€\n"
                                if wait["talkban"] == True: md+="ðŸ˜ˆ Talkbanã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Talkbanã€Œ âœ– ã€\n"
                                if wait["Mentionkick"] == True: md+="ðŸ˜ˆ Notagã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Notagã€Œ âœ– ã€\n"
                                if wait["detectMention"] == True: md+="ðŸ˜ˆ Responã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Responã€Œ âœ– ã€\n"
                                if wait["autoJoin"] == True: md+="ðŸ˜ˆ Autojoinã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Autojoinã€Œ âœ– ã€\n"
                                if wait["autoAdd"] == True: md+="ðŸ˜ˆ Autoaddã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Autoaddã€Œ âœ– ã€\n"
                                if msg.to in welcome: md+="ðŸ˜ˆ Welcomeã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Welcomeã€Œ âœ– ã€\n"
                                if wait["autoLeave"] == True: md+="ðŸ˜ˆ Autoleaveã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Autoleaveã€Œ âœ– ã€\n"
                                if msg.to in protectqr: md+="ðŸ˜ˆ Protecturlã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Protecturlã€Œ âœ– ã€\n"
                                if msg.to in protectjoin: md+="ðŸ˜ˆ Protectjoinã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Protectjoinã€Œ âœ– ã€\n"
                                if msg.to in protectkick: md+="ðŸ˜ˆ Protectkickã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Protectkickã€Œ âœ– ã€\n"
                                if msg.to in protectinvite: md+="ðŸ˜ˆ Protectinviteã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Protectinviteã€Œ âœ– ã€\n"
                                if msg.to in protectcancel: md+="ðŸ˜ˆ Protectcancelã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Protectcancelã€Œ âœ– ã€\n"
                                if msg.to in protectantijs: md+="ðŸ˜ˆ Antijsã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Antijsã€Œ âœ– ã€\n"  
                                if msg.to in ghost: md+="ðŸ˜ˆ Ghostã€Œ âœ” ã€\n"
                                else: md+="ðŸ˜ˆ Ghostã€Œ âœ– ã€\n"                                   
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'à¸œà¸ª':
                            #if msg._from in admin:
                                cl.sendText(msg.to,"ã€Œ MY CREATOR ã€\nAhmad + Drew + Mj") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "ã€Œ Type Selfbot ã€\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
 
                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "â§Nama : "+str(mi.displayName)+"\nâ§Mid : " +key1+"\nâ§Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "absen":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Kmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Lmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Mmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Nmid}
                               cl.sendMessage1(msg)
        					   msg.contentType = 13
                               msg.contentMetadata = {'mid': Omid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Pmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Qmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Rmid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Smid}
                               cl.sendMessage1(msg)
							   msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ka.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kl.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kn.removeAllMessages(op.param2)
                                   ko.removeAllMessages(op.param2)
                                   kp.removeAllMessages(op.param2)
                                   kq.removeAllMessages(op.param2)
                                   kr.removeAllMessages(op.param2)
                                   ks.removeAllMessages(op.param2)
                                   ka.sendText(msg.to,"Chat dibersihkan...")
                                   kb.sendText(msg.to,"Chat dibersihkan...")
                                   kc.sendText(msg.to,"Chat dibersihkan...")
                                   kd.sendText(msg.to,"Chat dibersihkan...")
                                   ke.sendText(msg.to,"Chat dibersihkan...")
                                   kf.sendText(msg.to,"Chat dibersihkan...")
                                   kg.sendText(msg.to,"Chat dibersihkan...")
                                   kh.sendText(msg.to,"Chat dibersihkan...")
                                   ki.sendText(msg.to,"Chat dibersihkan...")
                                   kj.sendText(msg.to,"Chat dibersihkan...")
                                   kk.sendText(msg.to,"Chat dibersihkan...")
                                   kl.sendText(msg.to,"Chat dibersihkan...")
                                   km.sendText(msg.to,"Chat dibersihkan...")
                                   kn.sendText(msg.to,"Chat dibersihkan...")
                                   ko.sendText(msg.to,"Chat dibersihkan...")
                                   kp.sendText(msg.to,"Chat dibersihkan...")
                                   kq.sendText(msg.to,"Chat dibersihkan...")
                                   kr.sendText(msg.to,"Chat dibersihkan...")
                                   ks.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ PROTECT BY TEAM A.D.M ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒMykeyã€\nSetkey bot muã€Œ " + str(Setmain["keyCommand"]) + " ã€")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "ã€ŒSetkeyã€\nSetkey diganti jadiã€Œ{}ã€".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "ã€ŒSetkeyã€\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "â§Bot Fams Grup Info\n\nâ§Nama Group : {}".format(G.name)+ "\nâ§ID Group : {}".format(G.id)+ "\nâ§Pembuat : {}".format(G.creator.displayName)+ "\nâ§Waktu Dibuat : {}".format(str(timeCreated))+ "\nâ§Jumlah Member : {}".format(str(len(G.members)))+ "\nâ§Jumlah Pending : {}".format(gPending)+ "\nâ§Group Qr : {}".format(gQr)+ "\nâ§Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " Fams Grup Info\n"
                                ret_ += "\nâ§Nama Group : {}".format(G.name)
                                ret_ += "\nâ§ID Group : {}".format(G.id)
                                ret_ += "\nâ§Pembuat : {}".format(gCreator)
                                ret_ += "\nâ§Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nâ§Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nâ§Jumlah Pending : {}".format(gPending)
                                ret_ += "\nâ§Group Qr : {}".format(gQr)
                                ret_ += "\nâ§Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "â§"+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"â§Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nã€ŒTotal %i Membersã€" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ka.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    ki.leaveGroup(i)
                                    kj.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kl.leaveGroup(i)
                                    km.leaveGroup(i)
                                    kn.leaveGroup(i)
                                    ko.leaveGroup(i)
                                    kp.leaveGroup(i)
                                    kq.leaveGroup(i)
                                    kr.leaveGroup(i)
                                    ks.leaveGroup(i)
                                    cl.leaveGroup(i)
                      
                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â•  " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"â•”â•â•[ FRIEND LIST ]\nâ•‘\n"+ma+"â•‘\nâ•šâ•â•[ Totalã€Œ"+str(len(gid))+"ã€Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â•  " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"â•”â•â•[ GROUP LIST ]\nâ•‘\n"+ma+"â•‘\nâ•šâ•â•[ Totalã€Œ"+str(len(gid))+"ã€Groups ]")

                          elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â•  " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"â•”â•â•[ GROUP LIST ]\nâ•‘\n"+ma+"â•‘\nâ•šâ•â•[ Totalã€Œ"+str(len(gid))+"ã€Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â•  " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"â•”â•â•[ GROUP LIST ]\nâ•‘\n"+ma+"â•‘\nâ•šâ•â•[ Totalã€Œ"+str(len(gid))+"ã€Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "â•  " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"â•”â•â•[ GROUP LIST ]\nâ•‘\n"+ma+"â•‘\nâ•šâ•â•[ Totalã€Œ"+str(len(gid))+"ã€Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#update bot
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ka.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kb.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                kd.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                ke.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                kf.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                kg.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Hmid] = True
                                kh.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Imid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Jmid] = True
                                kj.sendText(msg.to,"Kirim fotonya.....")

                         elif cmd == "bot11up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Kmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot12up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Lmid] = True
                                kl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot13up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Mmid] = True
                                km.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot14up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Nmid] = True
                                kn.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot15up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Omid] = True
                                ko.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot16up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Pmid] = True
                                kp.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot17up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Qmid] = True
                                kq.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot18up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Rmid] = True
                                kr.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot19up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Smid] = True
                                ks.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "ghostup":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kj.getProfile()
                                profile.displayName = string
                                kj.updateProfile(profile)
                                kj.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot12name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kl.getProfile()
                                profile.displayName = string
                                kl.updateProfile(profile)
                                kl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot13name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                km.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot14name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kn.getProfile()
                                profile.displayName = string
                                kn.updateProfile(profile)
                                kn.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot15name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ko.getProfile()
                                profile.displayName = string
                                ko.updateProfile(profile)
                                ko.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot16name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kp.getProfile()
                                profile.displayName = string
                                kp.updateProfile(profile)
                                kp.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot17name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kq.getProfile()
                                profile.displayName = string
                                kq.updateProfile(profile)
                                kq.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot18name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kr.getProfile()
                                profile.displayName = string
                                kr.updateProfile(profile)
                                kr.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot19name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ks.getProfile()
                                profile.displayName = string
                                ks.updateProfile(profile)
                                ks.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("ghostname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#botupdate
                        elif cmd == "tag" or text.lower() == 'ðŸ˜†':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7,nm8,nm9,nm10,nm11,nm12,nm13,nm14,nm15, jml = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (150, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-1):
                                       nm8 += [nama[q]]                                       
                                   mentionMembers(msg.to, nm9)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-1):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, len(nama)-1):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, len(nama)-1):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                               if jml > 220 and jml < 239:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, len(nama)-1):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                               if jml > 240 and jml < 259:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, len(nama)-1):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                               if jml > 260 and jml < 279:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 279):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, len(nama)-1):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                               if jml > 280 and jml < 299:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 159):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 179):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 199):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, 219):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)
                                   for t in range (220, 239):
                                       nm12 += [nama[t]]
                                   mentionMembers(msg.to, nm12)
                                   for u in range (240, 259):
                                       nm13 += [nama[u]]
                                   mentionMembers(msg.to, nm13)
                                   for v in range (260, 279):
                                       nm14 += [nama[v]]
                                   mentionMembers(msg.to, nm14)
                                   for w in range (280, 299):
                                       nm15 += [nama[w]]
                                   mentionMembers(msg.to, nm15)
                                   for x in range (300, len(nama)-1):
                                       nm16 += [nama[x]]
                                   mentionMembers(msg.to, nm16)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"PROTECT BY TEAM A.D.M\n\n"+ma+"\nTotalã€Œ%sã€ Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"PROTECT BY TEAM A.D.M\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotalã€Œ%sã€ Anggota" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    md += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    me += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mf += str(a) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"PROTECT BY TEAM A.D.M\n\nã€ŒðŸ˜ˆã€ PROTECT URL :\n"+ma+"\nã€ŒðŸ˜ˆã€ PROTECT KICK :\n"+mb+"\nã€ŒðŸ˜ˆã€ PROTECT JOIN :\n"+md+"\nã€ŒðŸ˜ˆã€ PROTECT CANCEL:\n"+mc+"\nã€ŒðŸ˜ˆã€ PROTECT INVITE:\n"+me+"\nã€ŒðŸ˜ˆã€ PROTECT ANTIJS :\n"+mf+"\nTotalã€Œ%sã€Grup diamankan" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite)+len(protectantijs))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ka.sendMessage(msg.to,responsename1)
                                kb.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kd.sendMessage(msg.to,responsename4)
                                ke.sendMessage(msg.to,responsename5)
                                kf.sendMessage(msg.to,responsename6)
                                kg.sendMessage(msg.to,responsename7)
                                kh.sendMessage(msg.to,responsename8)
                                ki.sendMessage(msg.to,responsename9)
                                kj.sendMessage(msg.to,responsename10)
                                kk.sendMessage(msg.to,responsename11)
                                kl.sendMessage(msg.to,responsename12)
                                km.sendMessage(msg.to,responsename13)
                                kn.sendMessage(msg.to,responsename14)
                                ko.sendMessage(msg.to,responsename15)
                                kp.sendMessage(msg.to,responsename16)
                                kq.sendMessage(msg.to,responsename17)
                                kr.sendMessage(msg.to,responsename18)
                                ks.sendMessage(msg.to,responsename19)

                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Kmid,Lmid,Mmid,Nmid,Omid,Pmid,Qmid,Rmid,Smid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                    kj.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kl.acceptGroupInvitation(msg.to)
                                    km.acceptGroupInvitation(msg.to)
                                    kn.acceptGroupInvitation(msg.to)
                                    ko.acceptGroupInvitation(msg.to)
                                    kp.acceptGroupInvitation(msg.to)
                                    kq.acceptGroupInvitation(msg.to)
                                    kr.acceptGroupInvitation(msg.to)
                                    ks.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Grup ã€Œ"+str(ginfo.name)+"ã€ Aman Dari JS")
                                except:
                                    pass

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                cl.inviteIntoGroup(msg.to, [Zmid])

                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                #ka.sendText(msg.to, "Bye bye fams "+str(G.name))
                                ka.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kj.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kl.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kn.leaveGroup(msg.to)
                                ko.leaveGroup(msg.to)
                                kp.leaveGroup(msg.to)
                                kq.leaveGroup(msg.to)
                                kr.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                cl.cancelGroupInvitation(msg.to,[Zmid])

                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ka.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ka.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kh.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kj.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kl.leaveGroup(i)
                                        km.leaveGroup(i)
                                        kn.leaveGroup(i)
                                        ko.leaveGroup(i)
                                        kp.leaveGroup(i)
                                        kq.leaveGroup(i)
                                        kr.leaveGroup(i)
                                        ks.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "assist4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "assist5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "assist6":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kf.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kf.updateGroup(G)

                        elif cmd == "assist7":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kg.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kg.updateGroup(G)

                        elif cmd == "assist8":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kh.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kh.updateGroup(G)

                        elif cmd == "assist9":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist10":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kj.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kj.updateGroup(G)

                        elif cmd == "assist11":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist12":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kl.updateGroup(G)

                        elif cmd == "assist13":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = km.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                km.updateGroup(G)

                        elif cmd == "assist14":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kn.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kn.updateGroup(G)

                        elif cmd == "assist15":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ko.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ko.updateGroup(G)

                        elif cmd == "assist16":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kp.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kp.updateGroup(G)

                        elif cmd == "assist17":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kq.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kq.updateGroup(G)

                        elif cmd == "assist18":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kr.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kr.updateGroup(G)

                        elif cmd == "assist19":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ks.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ks.updateGroup(G)

                        elif cmd == "ghost join":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "ghost bye":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                cl.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ka.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kb.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kc.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kd.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ke.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kf.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kg.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kh.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ki.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kj.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kk.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kl.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                km.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kn.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ko.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kp.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kq.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                kr.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                ks.sendMessage(msg.to, "Speed\n%.10f detik" % (get_profile_time/3))
                                
                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Wait.....")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} secon".format(str(elapsed_time)))
                   
                        elif cmd == "speedbot" or cmd == "spb":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               ka.sendMessage(msg.to, "Pusiiing...")
                               elapsed_time = time.time() - start
                               ka.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kd.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kf.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kg.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kh.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kj.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               km.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kn.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ko.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kp.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kq.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               kr.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               elapsed_time = time.time() - start
                               ks.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudah tidak aktif")

#hiburan
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "ã€ŒJadwal Sholatã€"
                                         ret_ += "\nâ§Lokasi : " + data[0]
                                         ret_ += "\nâ§" + data[1]
                                         ret_ += "\nâ§" + data[2]
                                         ret_ += "\nâ§" + data[3]
                                         ret_ += "\nâ§" + data[4]
                                         ret_ += "\nâ§" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "ã€ŒStatus Cuacaã€"
                                    ret_ += "\nâ§Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\nâ§Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\nâ§Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\nâ§Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\nâ§Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "ã€ŒInfo Lokasiã€"
                                    ret_ += "\nâ§Location : " + data[0]
                                    ret_ += "\nâ§Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "â•”â•â•[ Lyric ]"
                                          ret_ += "\nâ•  Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\nâ•  Durasi : {}".format(str(song[1]))
                                          ret_ += "\nâ•  Link : {}".format(str(song[3]))
                                          ret_ += "\nâ•šâ•â•[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "â•”â•â•[ Music ]"
                                          ret_ += "\nâ•  Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\nâ•  Durasi : {}".format(str(song[1]))
                                          ret_ += "\nâ•  Link : {}".format(str(song[3]))
                                          ret_ += "\nâ•šâ•â•[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik tidak ditemukan")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"ã€ŒGoogle Imageã€\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nâ§Author : ' + str(vid.author)
                                    durasi = '\nâ§Duration : ' + str(vid.duration)
                                    suka = '\nâ§Likes : ' + str(vid.likes)
                                    rating = '\nâ§Rating : ' + str(vid.rating)
                                    deskripsi = '\nâ§Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nâ§Author : ' + str(vid.author)
                                    durasi = '\nâ§Duration : ' + str(vid.duration)
                                    suka = '\nâ§Likes : ' + str(vid.likes)
                                    rating = '\nâ§Rating : ' + str(vid.rating)
                                    deskripsi = '\nâ§Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "â§Link : " + "https://www.instagram.com/" + instagram
                                text = "â§Name : "+namaIG+"\nâ§Username : "+usernameIG+"\nâ§Biography : "+bioIG+"\nâ§Follower : "+followerIG+"\nâ§Following : "+followIG+"\nâ§Post : "+mediaIG+"\nâ§Verified : "+verifIG+"\nâ§Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"â§I N F O R M A S I â§\n\n"+"â§Date Of Birth : "+lahir+"\nâ§Age : "+usia+"\nâ§Ultah : "+ultah+"\nâ§Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")
                                    
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ka.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kd.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kf.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kg.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kh.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kj.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      km.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kn.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ko.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kp.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kq.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kr.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ks.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      sw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ka.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kb.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kd.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ke.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kf.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kg.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kh.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kj.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kl.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      km.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kn.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ko.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kp.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kq.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kr.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ks.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                  
#Protection
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)           

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "ã€ŒDiaktifkanã€\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "ã€ŒDinonaktifkanã€\n" + msgs)                                    

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:                             
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                #if wait["allprotect"] == True:
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectantijs:
                                      msgs = ""
                                  else:
                                      protectantijs.append(msg.to)
                                  if msg.to in ghost:
                                      msgs = ""
                                  else:
                                      ghost.append(msg.to)                                      
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "ã€Œ Status Protection ã€\n" + msgs)
                              elif spl == 'off':
                                 #if wait["allprotect"] == False:
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "ã€Œ Status Protection ã€\n" + msgs)
                                    
#kickout
                        elif ("Gk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Bk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                 
#kickall
                        elif "kickall" in msg.text:
                          if msg._from in admin:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace("kickall","")
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              gs = cl.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 cl.sendText(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if not target in admin and Bots:
                                      try:
                                          klist=[cl]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          break

                        elif text.lower() == 'sadis':
                            if msg._from in admin:
                                if msg.toType == 2:
                                    gs = cl.getGroup(msg.to)
                                gs.preventedJoinByTicket = False
                                cl.updateGroup(gs)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kn.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kp.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kq.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                time.sleep(0.1)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendText(msg.to,"SADIS KICK OUT BYE")
                                else:
                                    for target in targets:
                                      if target not in Bots:
                                        try:
                                            klist=[ka,kb,kc,kd,ke,kf,kg,kh,ki,kj,kl,km,kn,ko,kp,kq,kr,ks]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            print (msg.to,[g.mid])
                                        except:
                                           pass

#adminadd
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Dpk:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#coman on/off
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendText(msg.to,"ã€Œ Status Autoleave ã€\nAutoleave telah diaktifkan")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendText(msg.to,"ã€Œ Status Autoleave ã€\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Autojoin Tiket dinonaktifkan")

#command blacklist
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Blacklist User\n\n"+ma+"\nTotalã€Œ%sã€Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"Famz__Botz Talkban User\n\n"+ma+"\nTotalã€Œ%sã€Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "ã€Œ%iã€User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)

#command set
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "ã€ŒPesan Msgã€\nPesan Msg diganti jadi :\n\nã€Œ{}ã€".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "ã€ŒWelcome Msgã€\nWelcome Msg diganti jadi :\n\nã€Œ{}ã€".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "ã€ŒRespon Msgã€\nRespon Msg diganti jadi :\n\nã€Œ{}ã€".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "ã€ŒSpam Msgã€\nSpam Msg diganti jadi :\n\nã€Œ{}ã€".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "ã€ŒSider Msgã€\nSider Msg diganti jadi :\n\nã€Œ{}ã€".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒPesan Msgã€\nPesan Msg mu :\n\nã€Œ " + str(wait["message"]) + " ã€")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒWelcome Msgã€\nWelcome Msg mu :\n\nã€Œ " + str(wait["welcome"]) + " ã€")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒRespon Msgã€\nRespon Msg mu :\n\nã€Œ " + str(wait["Respontag"]) + " ã€")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒSpam Msgã€\nSpam Msg mu :\n\nã€Œ " + str(Setmain["ARmessage1"]) + " ã€")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "ã€ŒSider Msgã€\nSider Msg mu :\n\nã€Œ " + str(wait["mention"]) + " ã€")

#jointicket
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ka.findGroupByTicket(ticket_id)
                                     ka.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ka.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kb.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     kd.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     ke.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     kf.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     kg.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group8 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     kh.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group10 = kj.findGroupByTicket(ticket_id)
                                     kj.acceptGroupInvitationByTicket(group10.id,ticket_id)
                                     kj.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group11 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group12 = kl.findGroupByTicket(ticket_id)
                                     kl.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group13 = km.findGroupByTicket(ticket_id)
                                     km.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     km.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group14 = km.findGroupByTicket(ticket_id)
                                     kn.acceptGroupInvitationByTicket(group4.id,ticket_id)
                                     kn.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group15 = ko.findGroupByTicket(ticket_id)
                                     ko.acceptGroupInvitationByTicket(group5.id,ticket_id)
                                     ko.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group16 = kp.findGroupByTicket(ticket_id)
                                     kp.acceptGroupInvitationByTicket(group6.id,ticket_id)
                                     kp.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group17 = kq.findGroupByTicket(ticket_id)
                                     kq.acceptGroupInvitationByTicket(group7.id,ticket_id)
                                     kq.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group18 = kr.findGroupByTicket(ticket_id)
                                     kr.acceptGroupInvitationByTicket(group8.id,ticket_id)
                                     kr.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group19 = ks.findGroupByTicket(ticket_id)
                                     ks.acceptGroupInvitationByTicket(group9.id,ticket_id)
                                     ks.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass                 
