# IMPORT RANDOM - MODULE D'ALEATOIRE
import random

# PRINT QUESTION AND CHECK REPONSE AND PRINT RESULTAT
def questions_check():

    point = 0

    for i in range(5):

        print(questionsPOSE[i])
        print('-------------------')

        reponseUser = input(str('>>> Réponse: '))
        reponse = str(listReponse[i])

        if reponseUser == reponse:
            point = point + 1

        else:
            pass

    print("Votre résultat est : ", point, "/ 5")
    
# SELECTIONNER LES 5 QUESTIONS DANS UNE LISTE ET METTRE LES REPONSES DES QUESTIONS DANS UNE LISTE
def select_questions():

    global questionsPOSE
    global listReponse

    readQCM = open('assets/qcm_noms.txt', 'r')
    lalignesuivante = readQCM.readlines()

    questionsPOSE = []
    listReponse = []

    while len(questionsPOSE) < 5:

        ChoixRandomQuestion = random.choice(lalignesuivante)
        # ----------------------
        searchChar = ChoixRandomQuestion.find('~') - 1 # or .split('~')
        searchReponse = ChoixRandomQuestion.find('~') + 1
        # ----------------------
        QuestionChoose = ChoixRandomQuestion[0:searchChar]
        ReponseQuestion = ChoixRandomQuestion[searchReponse:searchReponse + 1]
        # ----------------------

        if QuestionChoose in questionsPOSE:
            pass

        else:
            questionsPOSE.append(QuestionChoose)
            listReponse.append(ReponseQuestion)

    # Close .txt
    readQCM.close()

    # Appelle de la fonction "questions_check()"
    questions_check()

# LANCEMENT DU PROGRAMME - APPELLE DE LA FONCTION "select_questions()"
if __name__ == "__main__":
    select_questions()