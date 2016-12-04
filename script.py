import requests as re
import webbrowser
import urllib.request
import os
import glob
import zipfile as zf
from time import sleep

def get_course_link(no,semester_name):
	if("monsoon" in semester_name):
		semester_name=semester_name.replace("monsoon","m")
	elif("summer" in semester_name):
		semester_name=semester_name.replace("summer","s")
	elif("winter" in semester_name):
		semester_name=semester_name.replace("winter","w")
	link="https://www.usebackpack.com/iiitd/"+semester_name+"/"+no+"/resources"
	"""
	FOR TESTING, UNCOMMENT THIS
	link="https://www.usebackpack.com/iiitd/m2016/ece113/resources
	"""
	return link

def get_course_id(no,semester_name):
	url=get_course_link(no,semester_name)
	var=re.get(url)	
	website_content=var.content
	website_content=str(website_content)
	start_position_of_coure_id=website_content.find("background-image: url(/courses/photo/")+37
	end_position_of_coure_id=website_content.find("/",start_position_of_coure_id)
	course_id=website_content[start_position_of_coure_id:end_position_of_coure_id]
	return course_id

def get_all_links(no,semester_name):
	course_id=get_course_id(no,semester_name)
	full_link=get_course_link(no,semester_name)
	#LIST OF ALL POSSIBLE DOWNLOAD SUB-LINKS
	lecture_base_link="/resources/Lecture/"+course_id+"/generate"
	homework_base_link="/resources/Homework/"+course_id+"/generate"
	tutorial_base_link="/resources/Tutorial/"+course_id+"/generate"
	lab_base_link="/resources/Lab/"+course_id+"/generate"
	solution_base_link="/resources/Solution/"+course_id+"/generate"
	other_base_link="/resources/Other/"+course_id+"/generate"
	exam_base_link="/resources/Exam/"+course_id+"/generate"
	project_base_link="/resources/Project/"+course_id+"/generate"
	#FINAL LINKS
	lecture_link=full_link[:27]+lecture_base_link
	homework_link=full_link[:27]+homework_base_link
	tutorial_link=full_link[:27]+tutorial_base_link
	lab_link=full_link[:27]+lab_base_link
	solution_link=full_link[:27]+solution_base_link
	other_link=full_link[:27]+other_base_link
	exam_link=full_link[:27]+exam_base_link
	project_link=full_link[:27]+project_base_link
	print ("Downloading has started. This might take a while...")
	urllib.request.urlretrieve(lab_link,no+"_Labs.zip")
	urllib.request.urlretrieve(lecture_link,no+"_Lectures.zip")
	urllib.request.urlretrieve(homework_link,no+"_Homeworks.zip")
	urllib.request.urlretrieve(other_link,no+"_Others.zip")
	urllib.request.urlretrieve(exam_link,no+"_Exams.zip")
	urllib.request.urlretrieve(solution_link,no+"_Solutions.zip")
	urllib.request.urlretrieve(project_link,no+"_Projects.zip")
	urllib.request.urlretrieve(tutorial_link,no+"_Tutorials.zip")
	print ("All downloads have been completed!")
	print ()
	print ("Files are being extracted..")
	all_zip_files=glob.glob('*.zip')
	for i in all_zip_files:
		directory=os.path.splitext(i)[0]
		os.mkdir(directory)
		data=zf.ZipFile(i,"r")
		data.extractall(directory)
		data.close()
		os.remove(i)
	print ("All files have been extracted!")

def main():
	no=input("Enter the course number: ").lower().replace(" ","")
	semester_name=input("Enter your semester: ").lower().replace(" ","")
	get_all_links(no,semester_name)

main()


