Hello

This is a set of data formatting tools I built (with heavy, heavy help from chat GPT) to reformat the Andrew Tate leaked Discord .json files into human readable chatlogs.

Simply extract the .json files from a channel into a folder and drop these files into that folder. Run ./wrapper.sh and it will do the following:

1. jq . all the files to pretty format them and make them more parseable.
2. Combine the json data structures into one big structure so the later steps can function properly
3. Convert all of the epoch time stamps to human readable time stamps
4. Reformat the .json files to be simple chat logs formatted to Timestamp - Author: Message format.
5. Sort all of the messages in each file chronologically 
6. Reference users.key and replace all of the UIDs with the human readable username in each message.

The UID replace takes AGES, sorry I'm not a software engineer.

Have fun
Quack the Planet
Fuck Andrew Tate
