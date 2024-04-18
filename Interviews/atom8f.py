"""
Please email the solution in compilable format to contact@atom8.tech
 
Input to your program are 3 strings S1 S2 and S3 of lower case alphabets and no spaces or special characters. S1 and S2 are the same size. Here are the constraints on S1 and S2:
In string S1 and S2 the alphabets at the same index can be replaced with each other.
If alphabet p can be replaced with q then q can also be replaced with p
If alphabet p can be replaced with alphabet q , and the alphabet q can be replaced with alphabet r then alphabet p can also be replaced with r.
1 <  length of strings  S1,S2,S3 < 999999
length of string S1 = length of string S2
All the strings consist of lowercase English letters.
 
Ex : You are given two strings:
S1−pqr
S2−zrg
 
Here, the alphabet p can be replaced with alphabet z, alphabet q can be replaced with r, and alphabet r with g. The alphabet q can also be replaced with g according to the 3rd rule above.
 
Definition of lexicographical sorting https://en.wikipedia.org/wiki/Lexicographic_order#:~:text=In%20mathematics%2C%20the%20lexicographic%20or,of%20a%20totally%20ordered%20set.
 
Input format
First line: String S1
Second line: String S2
Third line: String S3
Output format
You can replace any alphabet of S3 with any of these alternatives based on the properties learned from S1 and S2. By doing so you can construct many such new strings. Out of all these strings your program should output the smallest string assuming they are sorted lexicographically.
 
Sample Input
dcba
edcb
decb
Output
aaaa

"""
def recheck(dp):
    flag=0
    for i in dp.keys():
        if dp[dp[i]] <dp[i]:
            dp[i]=dp[dp[i]]
            flag+=1
    if(flag==0):
        return
    else:
        recheck(dp)

# s1=input()
# s2=input()
# s3=input()

s1="dcba"
s2="edcb"
s3="decb"

s1="abcd"
s2="pqrs"
s3="srqp"

dp={}
for i in range(97,123):
    dp[chr(i)]=chr(i)
   
for i in range(len(s1)):
    if(s1[i]<s2[i]):
        dp[s2[i]]=s1[i]
    elif(s1[i]>s2[i]):
        dp[s1[i]]=s2[i]
    recheck(dp)
    print(dp)

res=""
for i in range(len(s3)):
    res+=dp[s3[i]]
print(res)