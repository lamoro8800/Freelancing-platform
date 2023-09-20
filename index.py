import os
client_id=1;freelancer_id=1;post_id=1;
print("welcome in our programme!\nenter 1 to register\nenter 2 to login\nenter 0 to exit.")
register_or_login=int(input(""))
while register_or_login!=0:
    if register_or_login==1:
        print("***********************    register    *****************************")
        print("enter 1 for client account\nenter 2 for freelancer account\nenter 0 to exit.")
        freelancer_or_client=int(input(""))
        if freelancer_or_client==1:#client register
            print ("*********************** client account *****************************")
            name=input("please, enter username : ")
            password=input("enter password : ")
            email=input("enter your e-mail : ")
            file_name=name+".txt"
            if os.path.exists(file_name):
                print("error! this username is existed before.")
            else:
                f=open(file_name,"w")#this file is for client
                f.write(name+"\n"+password+"\n"+email+"\n")
                f.close
                f=open("fclients_list.txt","a+")#this file is for client_id
                f.write(f"{name}\n")
                f.close
                f=open("fclients_list.txt","r+")
                client_id=len(f.readlines())
                f.close
                print(f"\nyour ID is {client_id}\n")
                enter=input("press enter to continue")
                register_or_login=2
        elif freelancer_or_client==2:#freelancer register
            print ("*********************** freelancer account *****************************")       
            name=input("please, enter username : ")
            password=input("enter password : ")
            email=input("enter your e-mail : ")
            phone_number=input("enter your phone number : ")
            national_id=input("enter your national id : ")
            file_name=name+".txt"
            if os.path.exists(file_name)==True:
                print("error! this username is existed before.")
            else:
                f=open(file_name,"w")#this file is for freelancer
                f.write(name+"\n"+password+"\n"+email+"\n")
                f.close
                f=open("freelancers_list.txt","a+")#this file is for freelancer list and freelancer id
                f.write(f"{name:20s}{email}\n")#rjust() or :20s or {:>20} to make output align
                f.close
                f=open("freelancers_list.txt","r+")#this file is for freelancer_id
                freelancer_id=len(f.readlines())
                print(f"\nyour ID is {freelancer_id}\n")
                enter=input("press enter to continue")
                register_or_login=2
        elif freelancer_or_client==0:
            register_or_login=0
        else:
            print("\nerror! please try again.")
            register_or_login=1
    elif register_or_login==2:
        print("***********************     login      *****************************")
        print("enter 1 for client account\nenter 2 for freelancer account\nenter 0 to exit.")
        freelancer_or_client=int(input(""))
        if freelancer_or_client==1:#client login
            print("*********************** client account *****************************")
            name=input("please, enter username : ")
            password=input("enter password : ")
            file_name=name+".txt"
            if os.path.exists(file_name)==False:
                print("\nerror! this username not existed.")
            else:
                f=open(file_name,"r")
                if f.readline()==name+"\n" and f.readline()==password+"\n":
                    print ("***********************  welcome back  *****************************")
                    if freelancer_or_client==1:#now we are in application as a client 
                        while True:#client loop
                            print("enter 1 to see registered freelancers List\nenter 2 to add a new job post\nenter 3 to see list proposals that sent by freelancers\nenter 4 to delete a job post\nenter 0 to exit.")
                            op_client=int(input(""))
                            if op_client==1:#first option for client "freelancers list"
                                print("")
                                freelancers_list=open("freelancers_list.txt","r")
                                print(freelancers_list.read())
                                freelancers_list.close()
                                enter=input("press enter to continue")
                            elif op_client==2:#second option for client "adding a new job post"
                                id = input("please enter your ID : ")
                                if not os.path.exists("Jobs list"):
                                    os.mkdir("Jobs list")
                                if not os.path.exists(f"E:\\python\\freelancer IS\\Jobs list\\{id}"):
                                    os.mkdir(f"E:\\python\\freelancer IS\\Jobs list\\{id}")
                                title=input("enter job title : ")
                                job_description=input("enter job description : ")
                                list_of_required_skills=input("enter list of required skills : ")
                                post_title=title+".txt"
                                f=open(f"E:\\python\\freelancer IS\\Jobs list\\{id}\\{post_title}","w+")
                                f.write(title+"\n"+job_description+"\n"+list_of_required_skills+"\n")
                                f.close
                                print("\nPost created successfully\n")
                                enter=input("Press enter to the previous menu\n")
                            elif op_client==3:#third option for client "list proposals"
                                print("********************************************************")
                                id = input("Please enter your ID : ")
                                client_jobs = os.listdir(f"E:\\python\\freelancer IS\\Jobs list\\{id}")
                                print("Your posts list: ")
                                for client_job in client_jobs:
                                    print(client_job)
                                    print("****************************************")
                                job_name = input("Enter the name of the job to see proposals without '.txt': ") + ".txt"
                                job_folders = os.listdir("Jobs list")
                                for job_folder in job_folders:
                                    if os.path.exists(f"E:\\python\\freelancer IS\\Jobs list\\{id}\\{job_name}"):
                                        f = open(f"E:\\python\\freelancer IS\\proposals list\\{job_name}", "r")
                                        print(f.read())
                                        print("***************************************")
                                        break
                                ID_to_acc_or_rej = input("enter freelancer's ID you want to accept or reject: ")
                                h = open(ID_to_acc_or_rej + job_name, "w")
                                acc_or_rej = int(input("press 1 to accept or 2 to reject: "))
                                if acc_or_rej == 1:
                                    h.write("you are accepted in the job")
                                    print("proposal accepted successfully")
                                elif acc_or_rej == 2:
                                    print("proposal rejected successfully")
                                    h.write("you are rejected in the job")
                                enter = input("Press enter to the previous menu\n")
                            elif op_client==4:#fourth option for client "delete a job"
                                id = input("Please enter your ID : ")
                                client_jobs = os.listdir(f"E:\\python\\freelancer IS\\Jobs list\\{id}")
                                print("Your posts list: ")
                                for client_job in client_jobs:
                                    print(client_job)
                                job_name = input("Enter the name of the job you want to delete without '.txt': ") + ".txt"
                                os.remove(f"E:\\python\\freelancer IS\\Jobs list\\{id}\\{job_name}")
                                print("\nPost deleted successfully\n")
                            elif op_client==0:#to exit
                                register_or_login=0
                                break
                            else:
                                print("\nerror! please try again.")
                else:
                    print("error! username or password are not correct, please try again")
        elif freelancer_or_client==2:#freelancer login
            print ("*********************** freelancer account *****************************")
            name=input("please, enter username : ")
            password=input("enter password : ")
            file_name=name+".txt"
            
            if os.path.exists(file_name)==False:
                print("\nerror! this username not existed.")
            else:
                f=open(file_name,"r")
                if f.readline()==name+"\n" and f.readline()==password+"\n":
                    print ("***********************   welcome back   *****************************")
                    if freelancer_or_client==2:#now we are in application as a freelancer
                        while True:
                            print("enter 1 to see job posts list\nenter 2 to Search in job posts\nenter 3 to Send a proposal\nenter 4 to see proposals status\nenter 0 to exit.")
                            op_freelancer=int(input(""))
                            if op_freelancer==1:#the first option is seeing the job posts list
                                if os.path.exists("Jobs list"):
                                    job_folders = os.listdir("Jobs list")
                                    for job_folder in job_folders:
                                        job_files = os.listdir(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}")
                                        for job_file in job_files:
                                            f = open(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}\\{job_file}", "r")
                                            print(f.read())
                                            print("***************************************************************************")
                                    enter=input("Press enter to the previous menu\n")
                                else:
                                    print("there are no posts now!")
                                    
                            elif op_freelancer==2:#the second option is searching by title of post
                                while True:
                                    j = 0
                                    search_name = input("enter job name : ")
                                    search_name = search_name + ".txt"
                                    job_folders = os.listdir("Jobs list")
                                    for job_folder in job_folders:
                                        if os.path.exists(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}\\{search_name}"):
                                            search = open(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}\\{search_name}", "r")
                                            print(search.read())
                                            search.close
                                            j = 1
                                            break
                                    if j == 1:
                                        break
                                    enter = input("Press enter to the previous menu\n")
                            elif op_freelancer==3:#the third option
                                print("***************************************************************************")
                                if os.path.exists("Jobs list"):
                                    job_folders = os.listdir("Jobs list")
                                    for job_folder in job_folders:
                                        job_files = os.listdir(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}")
                                        for job_file in job_files:
                                            f = open(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}\\{job_file}", "r")
                                            print(f.read())
                                            print("***************************************************************************")
                                search_name = input("enter job name you want to propose : ")
                                search_name = search_name + ".txt"
                                job_folders = os.listdir("Jobs list")
                                for job_folder in job_folders:
                                    if os.path.exists(f"E:\\python\\freelancer IS\\Jobs list\\{job_folder}\\{search_name}"):
                                        f = open(f"E:\\python\\freelancer IS\\proposals list\\{search_name}", "a+")
                                        freelancerID = input("enter your ID: ")
                                        skills = input("what are you perfect in? ")
                                        f.write("freelancer ID: "+freelancerID+"\n"+"job title: "+search_name+"\n"+"freelancer skill: "+skills+"\n")
                                enter = input("Press enter to the previous menu\n")
                            elif op_freelancer == 4:#fourth option to see proposals status
                                print("***************************************************************************")
                                freelancerID = input("please enter your ID: ")
                                job_name = input("please enter name of job you proposed to: ")
                                title = freelancerID + job_name + ".txt"
                                if os.path.exists(title):
                                    f = open(title, "r")
                                    print(f.read())
                                    print("***************************************************************************")
                                    enter = input("Press enter to the previous menu\n")
                                else:
                                    print("you didn't get any respond yet")
                                    enter = input("Press enter to the previous menu\n")
                            elif op_freelancer==0:#to exit
                                register_or_login=0
                                break
                            else:
                                print("\nerror! please try again.")
                else:
                    print("error! username or password are not correct, please try again")
        elif freelancer_or_client==0:
            register_or_login=0
        else:
            print("\nerror! please try again.")
            register_or_login=2
    else :
        print("error! please, try again\nenter 1 to register\nenter 2 to login\nenter 0 to exit.")
        register_or_login=int(input(""))