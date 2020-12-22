import sys
from random import randint

#functions
def game_list(user_list, variable):


    while variable.lower() != "x":
    
        if variable.lower() == "" :
            variable = input("Type here::> ")
            
        elif len(user_list) == 3 :
            variable = input("Type x please::> ")
    
        else:
            user_list.append(variable)
            if len(user_list) != 3:
                variable = input("Type here::> ")
                
def spin_the_wheel(user_list):
    print('')
    print("Now it is time to Spin the Wheel of Destiny")
    a = input("(press enter to spin)")
    print('')
    print("Spinning......... ")
    for count in range(0,10):
        for count in range(10):
            print('.', end='')
        print('')
    #display results
    print('')
    wheel_spin = randint(1,len(user_list))
    list_index = wheel_spin-1
    print("You got.....\n\t", user_list[list_index])
    return user_list[list_index]

def my_inputs(user_list, v1, v2, v3):
    print('')
    print("Now I Will Add Three Of My Own. Muwahahaha!")
    user_list.insert(1, v1)
    user_list.insert(3, v2)
    user_list.insert(5, v3)
    a = input("(press enter)")
    print('')
    
def end_game():
    print("")
    a = input("press enter")
    print("\n\n")
    print('\t\t'+"="*60)
    print("\t\t No Actual lives were negatively affected by this game.")
    print('\t\t'+"="*60)
    print("\n\n\n\n\n")
    print("\t*****************************************************************")
    print("\t*                                                               *")
    print("\t*\tBrought to you by the Childrenhood Industries.\t\t*")
    print("\t*\tCreated and programed by H. Rene Baltar.\t\t*")
    print("\t*                                                                ")
    print("\t*****************************************************************")
def reset_list(user_list):
    
    for item in user_list:
        user_list.remove(item)
        print('')
        
    


def MASH():
    ##Main Program
    a=input("Start Engine")
    #title Screen
    print("\n"*10)
    print("\t\tChildrenhood Entertainment Production\t\t")
    print("\t\t\tpresents...\t\t")
    print("\n" *5)
    print("Loading......... ")
    for count in range(0,10):
        for count in range(40):
            print('.', end='')
        print("")
    print("\n" * 3)

    print("\t\t*****   *****     ***     *********** |***   ***|")
    print("\t\t*  **   **  *    * * *    |  |****  | |  *   *  |")
    print("\t\t*  **   **  *   * * * *   |  |******| |  *   *  |")
    print("\t\t*  **   **  *  * *   * *  *         | |  *****  |")
    print("\t\t*  * * * *  * * ******* * ********  | |         |")
    print("\t\t*  *  *  *  * * ******* * |  |   *  | |  *****  |")
    print("\t\t*  *     *  * * *     * * |  |****  | |  *   *  |")
    print("\t\t*  *     *  * * *     * * |         | |  *   *  |")
    print("\t\t****     **** ***     *** *********** |***   ***|")

    a = input("\n\n\t\t\t\tpress enter to start")
        

    #welcome the user
    print("=======================================================================")
    print("Welcome to MASH! This Classic Game Will Test Your Luck And Tell Your")
    print("Future. The task is simple. Just enter 3 variables for each list that")
    print("is asked of you. Keep in mind if you want a more challenging game, you")
    print("can enter less than 3 and press x to quit to decrease your chance of")
    print("having a brighter future. Have fun and I wish you the best of Luck!")
    print("=======================================================================")
    a = input("\n(press enter to start)")
    print('')
    #create a list of shelters based on the game MASH

    mash_list = ["Mansion", "Apartment", "Shack", "House","Apartment", "Shack", "House",
                 "Shack","Apartment", "Shack"]

    ## Set up the appropriate functions for Places of interests
    #create a list for locations in which the user can choose 3 or less

    place_list = []
    print("=======================================================================")
    print("\tType in a city or location of your choice in which you either")
    print("\twish to stay for your dream home. (type x to quit)")
    print("=======================================================================")
    place = input("Type here::> ")
    game_list(place_list, place)



    #modify the list to insert 2 or 3 mad locations
    my_inputs(place_list,"Antarctica","Deep Ugly Jungle","Middle of Nowhere")

    #display list
    print("Here is your list of Places::\n")
    for location in place_list:
        print('\t',location)
    print('')
    a = input("(press enter)")


    #Time to spinn the will

    xplace = spin_the_wheel(place_list)
    supreme_place = xplace
    print('')
    a = input("(press enter)")

    ## set up functions for Vehicle of interest
    # create a list for cars/vehicles
    car_list = []
    print("=======================================================================")
    print("\tType in a car or vehicle of your choice in which you either")
    print("\twish to navigate for the rest of your life. (type x to quit)")
    print("=======================================================================")
    car = input("Type here::> ")
    game_list(car_list, car)



    #modify the list to insert 2 or 3 mad locations
    my_inputs(car_list,"Tricycle","Carboard Box with wheels","Barefoot")

    #display list
    print("Here is your list of vehicles::\n")
    for vehicle in car_list:
        print('\t',vehicle)
    print('')
    a = input("(press enter)")


    #Time to spinn the will
    xcar = spin_the_wheel(car_list)
    supreme_car = xcar
    print('')
    a = input("(press enter)")

    ## set up functions for Job/career of interest
    # create a list for jobs
    job_list = []
    print("=======================================================================")
    print("\tType in a career of your choice in which you either")
    print("\twish to do for the rest of your life. (type x to quit)")
    print("=======================================================================")
    job = input("Type here::> ")
    game_list(job_list, job)



    #modify the list to insert 2 or 3 mad locations
    my_inputs(job_list,"Garbage person","Hobo","Janitor")

    #display list
    print("Here is your list of vehicles::\n")
    for career in job_list:
        print('\t',career)
    print('')
    a = input("(press enter)")


    #Time to spinn the will

    xjob = spin_the_wheel(job_list)
    supreme_job = xjob
    print('')
    a = input("(press enter)")

    ## set up functions for status of interest
    # create a list for status
    stat_list = []

    print("\tType in a status (rich, married, smart, pretty, etc.) of your") 
    print("\tchoice in which you wish to be throughtout your future. (type x to quit)")
    stat = input("Type here::> ")
    game_list(stat_list, stat)




    #modify the list to insert 2 or 3 mad locations
    my_inputs(stat_list,"Sad","Forever Alone",'"Happily" Divorced')

    #display list
    print("Here is your list of vehicles::\n")
    for adj in stat_list:
        print('\t',adj)
    print('')
    a = input("(press enter)")


    #Time to spinn the will

    xstat = spin_the_wheel(stat_list)
    supreme_stat = xstat
    print('')
    a = input("(press enter)")

    ###Begin MASH!
    print("\n" * 5)
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Now it is time to spin for the win and test your ultimate luck for MASH!')
    print('')


    finale = spin_the_wheel(mash_list)
    print('')

    ##diplay final results
    while supreme_job != "Hobo":
        if finale == "Mansion":
            print("\t------------------------------------------------------------------------")
            print("\tWOW! Congratulations you hit the jackpot and Won yourself a Mansion!!!!!!")
            print("\tIt doesn't really matter that you are a", supreme_job)
            print("\tliving in", supreme_place)
            print("\twith a", supreme_stat,"lifestyle.")
            print("\You Live in an AWSOME Mansions and all your dreams will come true!")
            print("\t------------------------------------------------------------------------")
            
        elif finale == "House":
            print("\t---------------------------------------------------------------------------------------")
            print("\tNot bad. You did not hit the jackpot but you did hit a better than average house")
            print("\tWhether you are in a mid life crisis or not, you can still enjoy being a", supreme_job)
            print("\tliving in", supreme_place)
            print("\twith a", supreme_stat,"lifestyle.")
            print("\tYour life will most likey be at least average... good luck!")
            print("\t------------------------------------------------------------------------")
            
        elif finale == "Apartment":
            print("\t------------------------------------------------------------------------")
            print("\tyawwwwwwwwwwwnnnnnnnnnnnnn")
            print("\tbut at least you can be a", supreme_job)
            print("\tliving in", supreme_place)
            print("\twith a", supreme_stat ,"Lifestyle.")
            print("\tYour life will most likely be very dull with a small chance of success")
            print("\t------------------------------------------------------------------------")
            
        else:
            print("\t------------------------------------------------------------------------")
            print("\tOh dear..... luck was not on your side and you will make terrible decisions")
            print("\tit is going to be hard to even be a", supreme_job)
            print("\tliving in", supreme_place)
            print("\twith A", supreme_stat ,"Lifestyle.")
            print("\tIt is probably pointless me telling you this anyways since your dreams will")
            print("\tprobably not come true. hahahaha")
            print("\t-------------------------------------------------------------------------")
        end_game()
        print("\n" * 5)
        print("Would you like to try agian?")
        c = input("(Type yes or no)")
        if c.lower() == "yes":
            reset_list(place_list)
            reset_list(car_list)
            reset_list(job_list)
            reset_list(stat_list)
            MASH()
        else:
            print("\n\n Bye Bye :)" )
            sys.exit()
        
    print("But.... Since you spin for Hobo, You lose everthing!")
    print("Muwahahahahah!!!! Congradulations, YOU LOSE!!!!!!!")
    end_game()
    print("\n" * 5)
    print("Would you like to try agian?")
    c = input("(Type yes or no)")
    if c.lower() == "yes":
        MASH()
    else:
        print("\n\n Bye Bye :)" )
        sys.exit()
MASH()

    
          
    










