import os,shutil,time,random,MySQLdb,hashlib
from mutagen.mp3 import MP3
from mutagen.mp3 import MPEGInfo

'os.chdir(/var/www/upload/)'
'''MYSQL CONN'''
conn=MySQLdb.connect(host="localhost",user="root",passwd="881010",db="mysql")
cursor=conn.cursor()
filepath='/var/www/upload/'
desFilepath='/var/www/audio/'
for root,dirs,files in os.walk(filepath):
 for filename in files:
   currentFileName="".join(str(time.time()).split('.'))+hashlib.sha1(filename).hexdigest()+"."+str(filename.split('.')[1])
   filesize=os.stat(filepath+filename).st_size
   audio=MP3(filepath+filename)
   audioLength=int(audio.info.length)
   msg=filename 
   sql = """INSERT INTO podlb_postings (author_id,title,posted,filelocal,audio_file,audio_type,audio_size,status, 
         countweb,countfla,countpod,countall,audio_length,message_input,message_html,
         comment_on,comment_size,category1_id,category2_id,category3_id,category4_id,tags,sticky)
         VALUES
         (
         '1',
         '"""+str(filename.split('.')[0])+"""',
         '"""+time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(time.time()))+"""',
         '1',
         '"""+currentFileName+"""',
         '1',
         '"""+str(filesize)+"""',
         '3','0','0','0','0','"""+str(audioLength)+"""','NoInfo','NoInfo','0','0','1','0','0','0','autoupload','0'
         );"""
   n=cursor.execute(sql)
   shutil.move(filepath+filename,desFilepath+currentFileName)

