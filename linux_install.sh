
# color variables
BLACK='\033[0;30m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGREY='\033[0;37m'
RESET='\033[0m'


# set default installation to current DIR
custom_path=$PWD

while [ 0 == 0 ]
do
    # ask if they agree path
    echo -e "would you like to add ${MAGENTA}manager${RESET} program at ${GREEN}$custom_path${RESET}? (y/n)"
    read answer

    #if there answer is empty 
    if [ "$answer" == "" ]
    then
        continue
    fi

    # if user answers something
    if [ ${answer:0:1} == 'y' ] || [ ${answer:0:1} == 'Y' ]
    then
        # user agrees to path
        echo -e "todo!"
    else
        # if he don't agree ask his custom path
        echo -e "enter custom path : (${RED}!!${RESET} to exit installation!)"
        read custom_path
        if [ $custom_path == "!!" ]
        then
            echo -e "${RED}cancelled installation!"
            break
        else
            echo -e "todo"
        fi
    fi
done