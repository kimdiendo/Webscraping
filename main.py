from bs4 import  BeautifulSoup
#BeautifulSoup library là thư vien lấy dữ liệu từ các file html , xml
# with open("home.html" , 'rt') as home_html:
#          content = home_html.read()
# #sau câu lệnh trên , soup là một cây các đối tượng bao gồm BeautifulSoup , Tag , NavigateString , Comment
# soup = BeautifulSoup(content , 'html5lib')
# print(soup)
import requests
import time
import os
def Write_data_into_file(title , company , job_description , skills , date_posting):
    if os.path.exists('D:\Python project\Webscraping\jobdata.txt'):
         with open ("jobdata.txt" , "w") as data_holder:
              for i in range(len(title)):
                  data_holder.write("Title Job: {} \n Company: {} \n Job Description: {} \n Requirement Skills: {} \n Date Posting: {} \n \n".format(title[i]  , company[i] ,
                                                                                                                                                     job_description[i], skills[i] , date_posting[i]))
    else:
        print("Đường dẫn không tồn tại")

def Scraping_data_from_Web():
    req = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=java&txtLocation=")
    soup = BeautifulSoup(req.text, 'lxml')
    # content_html_tags = soup.find_all('h2') #find() tra ve the , dau vao la ten the , lay the dau tien
    # first_html_tag =  soup.find('h2') # find_all tra ve tat ca cac the cung ten
    # for content in content_html_tags:
    #       print(content.text)
    content_jobs = soup.find("ul", class_="new-joblist")
    list_title_all_jobs = content_jobs.find_all('h2')  # crawl title data
    list_company_all_jobs = content_jobs.find_all('h3', class_="joblist-comp-name")  # crawl company name
    list_date_updated = content_jobs.find_all('span', class_="sim-posted")  # list date posted
    list_skills = content_jobs.find_all('span' , class_='srp-skills')
    list_JD = content_jobs.find_all('ul' , class_='list-job-dtl clearfix')
    list_title_jobs = []
    list_company_jobs = []
    list_key_skills = []
    list_job_description =[]
    for title in list_title_all_jobs:
        list_title_jobs.append(title.text.strip())
    for comp in list_company_all_jobs:
        list_company_jobs.append(comp.text.strip())
    new_date_updated = []
    for date in list_date_updated:
        new_date_updated.append(date.text.strip())
    for skill in list_skills:
        list_key_skills.append(skill.text.strip())
    for job_description in list_JD:
        list_job_description.append(job_description.text.strip().splitlines()[1]) # lấy data từ thẻ li
    #print(list_title_jobs)
    # print(list_company_jobs)
    # print(new_date_updated)
    # print(list_job_description)
    # print(list_key_skills)
    Write_data_into_file(list_title_jobs , list_company_jobs ,list_job_description , list_key_skills , new_date_updated)
if __name__ == "__main__":
     Scraping_data_from_Web()



