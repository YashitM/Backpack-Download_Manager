import requests as re
import webbrowser
import wget


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
	#compiled_urls=[lecture_link,homework_link,tutorial_link,lab_link,solution_link,other_link,exam_link,project_link]
	print ("Downloading has started. This might take a while...")
	print ()
	print ("Downloading Lectures...")
	file_name = wget.download(lecture_link)
	print ("Lectures have been downloaded")
	print()
	print ("Downloading Homeworks...")
	file_name = wget.download(homework_link)
	print ("Homeworks have been downloaded")
	print()
	print ("Downloading Tutorials...")
	file_name = wget.download(tutorial_link)
	print ("Tutorials have been downloaded")
	print()
	print ("Downloading Labs...")
	file_name = wget.download(lab_link)
	print ("Labs have been downloaded")
	print()
	print ("Downloading Solutions...")
	file_name = wget.download(solution_link)
	print ("Solutions have been downloaded")
	print()
	print ("Downloading Exams...")
	file_name = wget.download(exam_link)
	print ("Exams have been downloaded")
	print()
	print ("Downloading Projects...")
	file_name = wget.download(project_link)
	print ("Projects have been downloaded")
	print()
	print ("Downloading Others...")
	file_name = wget.download(other_link)
	print ()
	print ("All downloads have been completed!")

def main():
	no=input("Enter the course number: ").lower().replace(" ","")
	semester_name=input("Enter your semester: ").lower().replace(" ","")
	get_all_links(no,semester_name)

main()


