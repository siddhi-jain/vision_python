import urllib.request

username=input("Enter the username : ")

link="http://localhost/users/"+username+".html"

response = urllib.request.urlopen(link)

source_code=str(response.read())

tmp=source_code.index('Problems Solved')

source_code=source_code[tmp:]

tmp=source_code.index('(')

ans=source_code[tmp+1:]

tmp=ans.index("</h5>")

ans=ans[:tmp-1]

ans=int(ans)

print("Number of problems solved by %s is %d"%(username,ans))
