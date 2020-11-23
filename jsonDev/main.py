courses = []
allcourses = []
with open("正则匹配结果.txt", "r") as f:
    for i in range(99):
        Course = f.readline().replace("\n","")
        time = f.readline().replace("\n","")
        preCourse = f.readline().replace("\n","")
        # print("Course:",Course)
        # print("time:",time)
        # print("preCourse:",preCourse)
        tmpCourses = preCourse.split(",")
        tmpCourses.append(Course)
        # print(tmpCourses)
        for tmpCourse in tmpCourses:
            if tmpCourse not in allcourses:
                allcourses.append(tmpCourse)
    # print(allcourses)

for Course in allcourses:
    tmp=dict()
    tmp["name"]=Course
    tmp["time"]="32"
    tmp["pre"]=[]
    courses.append(tmp)
# print(courses)

with open("正则匹配结果.txt", "r") as f:
    for i in range(99):
        Course = f.readline().replace("\n","")
        time = f.readline().replace("\n","")
        preCourse = f.readline().replace("\n","").split(",")

        for tmpCourse in courses:
            if(tmpCourse["name"] == Course):
                tmpCourse["time"]=time
                for preCourse in preCourse:
                    tmpCourse["pre"].append(preCourse)
                break
print(courses)
