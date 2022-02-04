### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    answer = input("Enter your answer")
    
    if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "mtls"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = "5"
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = "4"
    return(answer)
# Complete all the questions.

    if __name__ == "__main__":
    #use this space to debug and verify that the program works
        debug_question.A = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
        debug_question.B = "Are encoding and encryption the same? - Yes/No"
        debug_question.C = "Is it possible to decrypt a message without a key? - Yes/No"
        debug_question.D = "Is it possible to decode a message without a key? - Yes/No"
        debug_question.E = "Is a hashed message supposed to be un-hashed? - Yes/No"
        debug_question.F = "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
        debug_question.G = "Is MD5 a secured hashing algorithm? - Yes/No"
        debug_question.H = "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
        debug_question.I = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
        
        print(welcome_assignment_answers(debug_question.A))
        print(welcome_assignment_answers(debug_question.B))
        print(welcome_assignment_answers(debug_question.C))
        print(welcome_assignment_answers(debug_question.D))
        print(welcome_assignment_answers(debug_question.E))
        print(welcome_assignment_answers(debug_question.F))
        print(welcome_assignment_answers(debug_question.G))
        print(welcome_assignment_answers(debug_question.H))
        print(welcome_assignment_answers(debug_question.I))


###Questions:
###"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?"
###"Are encoding and encryption the same? - Yes/No"
###"Is it possible to decrypt a message without a key? - Yes/No"
###"Is it possible to decode a message without a key? - Yes/No"
###"Is a hashed message supposed to be un-hashed? - Yes/No"
###"What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
###"Is MD5 a secured hashing algorithm? - Yes/No"
###"What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
###"What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"