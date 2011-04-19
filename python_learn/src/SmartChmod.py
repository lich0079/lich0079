
# coding:utf-8
import os
import stat
path="/Users/lich0079/BOOKS"



for root, dirs, files in os.walk(path):
    for file in files:
        if(not file[0] == "."):
            fp=os.path.join(root, file)   #生成完整路径
            print fp
            # 在原来的权限基础上加上 g+r o+r
            os.chmod(fp, stat.S_IMODE(os.stat(fp)[stat.ST_MODE]) | stat.S_IRGRP | stat.S_IROTH )
    for dir in dirs:
        if(not dir[0] == "."):  # 这句话没有起作用  因为walk自己还是会遍历到.dir下面去
            dp = os.path.join(root, dir)
            print dp
            os.chmod(dp, stat.S_IMODE(os.stat(dp)[stat.ST_MODE])  | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
               # visit(os.path.join(root, dir))   walk方法自己会去递归遍历子目录 不要加这句
