import os
import sys
import random


# Groupe: Maxime Bidan, Alexis Gontier, Arnaud Fischer
def endgame():
    print('''
    Vous venez de détruire le serveur d'ARASAKA, les répercutions vont être terribles autant pour la mégacorporation que pour les habitants de la ville.
    Des centaines de milliers de personnes vont désormais être licenciées à cause de leur incompétence.
    ARASAKA viens de recevoir l'une des attaques les plus importantes de sa création, la destruction totale de toute les données stockées sur le serveur central.
    Les conséquences de cette destruction se traduisent en une perte de plus d'une centaine de trilliards de crédits. Même pour ARASAKA cela représente un important problème.
    ============================================================================
    Vous avez désormais réussi là où d'autres ont essayé et échoué.

    Vous êtes désormais reconnu comme une légende mais n'oubliez pas qu'ARASAKA ne vous laissera plus jamais tranquille jusqu'à ce que vous disparaissiez.
    Bonne chance dans votre quête de survie .....
    ============================================================================
    ''')


def technologie_propre():
    print('''
    -----------------------------------------
    Rapport Environnemental - ARASAKA Corporation
    -----------------------------------------

    Objet : Technologies Propres et Durables

    Chers collègues,

    Nous sommes fiers de partager notre engagement envers les technologies propres et durables. Les recherches sur les énergies renouvelables et les sources d'énergie propre montrent des résultats prometteurs pour réduire notre impact environnemental.

    Restons déterminés à mener des actions respectueuses de l'environnement et HETIC.

    Cordialement,
    Direction Environnementale
    ARASAKA Corporation
    -----------------------------------------
    ''')


def info_marches():
    print('''
    -----------------------------------------
    Confidentiel Stratégies sur les Marchés - ARASAKA Corporation
    -----------------------------------------

    Objet : Stratégies de Manipulation des Marchés

    Chers membres autorisés,

    Dans le cadre de nos opérations financières avancées, nous avons développé des stratégies sophistiquées visant à influencer les marchés financiers pour garantir notre avantage concurrentiel. Il est essentiel de comprendre et de maîtriser ces stratégies pour maximiser nos profits tout en minimisant les risques.

    1. Manipulation des Cours Boursiers :
       - Utilisation de transactions massives pour artificiellement augmenter ou diminuer le cours des actions.
       - Influence sur les perceptions des investisseurs pour générer des mouvements de marché favorables.

    2. Diffusion de Fausses Informations :
       - Création et dissémination de rumeurs ou de fausses informations pour influencer les décisions des investisseurs.
       - Utilisation de canaux de communication spécifiques pour garantir une large diffusion.

    3. Attaques Coordonnées sur les Marchés :
       - Coordination d'activités de trading pour maximiser l'impact sur un actif financier spécifique.
       - Sélection minutieuse des moments opportuns pour déclencher des mouvements de marché.

    Remarques :
       - Ces stratégies sont déployées dans le respect des régulations financières en vigueur.
       - Des équipes dédiées surveillent en permanence les développements du marché pour ajuster nos stratégies en conséquence.

    Il est impératif que les informations contenues dans ce document restent confidentielles. Toute divulgation non autorisée pourrait compromettre nos opérations et nuire à notre position sur les marchés.

    Pour la prospérité et la domination d'ARASAKA sur les marchés financiers.

    PS : 'C' pourrait vous être utile pour la
    suite.

    Cordialement,
    Direction des Opérations Financières
    ARASAKA Corporation
    -----------------------------------------
    ''')


def projet_chimere():
    print('''
    -----------------------------------------
    Projet Chimère - ARASAKA Corporation
    -----------------------------------------

    **Rapport sur les Expérimentations Génétiques**

    Objet : Avancées du Projet Chimère et test sur sujet H

    **Principales Avancées :**

    1. **Optimisation des Capacités Physiques**
       - Amélioration notable de la force, de l'endurance et de la résistance des sujets H.

    2. **Augmentation des Capacités Cognitives**
       - Accroissement des capacités intellectuelles, de la mémoire et de la rapidité de traitement des sujets H.

    3. **Compatibilité avec les Implants Cybernétiques**
       - Intégration réussie avec les technologies cybernétiques existantes, améliorant la connectivité et la performance des sujets H.

    4. **Contrôle de la Reproduction**
       - Possibilité de contrôler certaines caractéristiques génétiques lors de la reproduction des sujets des sujets H.


    Équipe de Recherche Génétique
    ARASAKA Corporation
    -----------------------------------------
    ''')


def ethique():
    print('''
    -----------------------------------------
    Correspondance Interne - ARASAKA Corporation
    -----------------------------------------

    Objet : HETIC Contournée dans le Projet Chimère

    De : veronica.hayes@ARASAKA.com
    À : sebastian.kane@ARASAKA.com
    Objet : Préoccupations Éthiques - Projet Chimère

    Cher Sebastian,

    J'espère que ce message vous trouve bien. Récemment, j'ai examiné de plus près les avancées du Projet Chimère, et je suis de plus en plus préoccupé par les questions éthiques entourant les expérimentations génétiques.

    Certains éléments indiquent clairement un manque de consentement éclairé des sujets, ce qui va à l'encontre de nos principes éthiques fondamentaux. De plus, des mesures de dissimulation semblent avoir été prises, ce qui pourrait avoir un impact significatif sur notre réputation. Serait-il possible d'organiser une réunion pour discuter de ces préoccupations HETIC et explorer des actions correctives?

    Restant à votre disposition pour en discuter davantage.

    Cordialement,
    Dr.Veronica Hayes


    -----------------------------------------

    De : sebastian.kane@ARASAKA.com
    À : veronica.hayes@ARASAKA.com
    Objet : RE: Préoccupations Éthiques - Projet Chimère

    Cher Veronica,

    Je vous remercie de soulever ces préoccupations légitimes. Votre examen approfondi du Projet Chimère est essentiel pour garantir que nos pratiques restent alignées sur nos valeurs HETIC et nos engagements envers la transparence.

    Je suis d'accord pour organiser une réunion afin d'explorer ces questions plus en détail Je ferais part de vos propos à la direction.

    Je suis reconnaissant de votre diligence dans ce dossier et vous pris de croire que nous prendront vos remarques en considération.

    Cordialement,
    Sebastian Kane
    DIrecteur des opérations spéciales
    -----------------------------------------
    ''')


def strat_energie():
    print('''
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    Document Confidentiel - ARASAKA Corporation
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII

    Objet : Stratégies pour le Maintien du Monopole Énergétique

    Cher personnel autorisé,

    Ce document contient des informations cruciales sur nos stratégies visant à maintenir notre monopole énergétique. Nous soulignons l'importance de la confidentialité et de la discrétion absolue concernant ces détails.

    I. **Manipulation des Marchés**
       I Utilisation de tactiques financières pour contrôler les prix de l'énergie.
       I Dissimulation des sources d'énergie alternatives pour maintenir la dépendance.

    II. **Suppression de la Concurrence**
       I Acquisition agressive de start-ups et d'entreprises concurrentes.
       I Utilisation de moyens juridiques pour écraser la concurrence.

    III. **Lobbying et Influence Politique**
       I Financement discret de campagnes politiques favorables à nos intérêts.
       I Exercice d'une influence sur les politiques énergétiques nationales et internationales.

    Nous rappelons à tous les destinataires que la divulgation non autorisée de ces informations entraînera des sanctions sévères, conformément aux protocoles de sécurité en vigueur au sein d'ARASAKA Corporation.

    Soyez assurés de notre reconnaissance envers votre loyauté et votre engagement envers notre vision partagée.

    Pour la grandeur d'ARASAKA.

    Cordialement,
    Direction Exécutive
    ARASAKA Corporation
    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    ''')


def concurences():
    print('''
    -----------------------------------------
    Document Top Secret - ARASAKA Corporation
    -----------------------------------------

    Opération "Ombre Dorée :
       - Montant : $500,000
       - Bénéficiaire : Samantha Winters / Sénatrice
       - Raison : Dissimulation d'informations compromettantes.

    Projet "Silence" :
       - Montant : $1,200,000
       - Bénéficiaire : Jonathan Steele / PDG, Global Dynamics Corp
       - Raison : Garantie de non-divulgation d'activités illégales.

    Campagne "Main Invisible" :
       - Montant : $750,000
       - Bénéficiaire : Alexandra Quinn / Ministre de la Sécurité Intérieure
       - Raison : Influence sur la régulation gouvernementale.

    Initiative "Études réussies" :
       - Montant : café offert au prochain cours
       - Bénéficiaire : Loic Janin/Formateur Algo
       - Raison : Chantage pour garantire la réussite du
       projet RPG.

    ** Remarques **
       - Ces transactions sont documentées à des fins de suivi interne uniquement.
       - Des mesures de sécurité strictes sont en place pour éviter toute divulgation non autorisée.

    Ces activités sont menées dans le cadre de notre stratégie opérationnelle globale et doivent rester confidentielles. La divulgation non autorisée de ces informations entraînera des conséquences graves conformément à nos protocoles de sécurité.

    Pour la pérennité et la puissance d'ARASAKA\n

    PS : 'C' pourrait vous être utile pour la\n
    suite.


    Secretement,
    Direction des Opérations Spéciales
    ARASAKA Corporation
    -----------------------------------------
    ''')


def gestion_transport():
    print('''
    -----------------------------------------
    Documents Stratégiques - ARASAKA Corporation
    -----------------------------------------

    **Projet de Gestion des Transports Intelligents**

    1. **Véhicules Autonomes**
       - Recherche et développement de véhicules autonomes pour optimiser les déplacements.
       - Intégration de technologies de pointe pour la navigation autonome.

    2. **Réseaux de Transport Intelligents**
       - Mise en place de réseaux intelligents pour optimiser la circulation et réduire les embouteillages.
       - Intégration de capteurs et de systèmes de communication avancés.

    3. **Collecte de Données sur les Déplacements**
       - Mise en place de capteurs sur les véhicules et dans l'infrastructure pour collecter des données sur les déplacements.
       - Analyse approfondie pour comprendre les schémas de déplacement et améliorer les services.

    4. **Gestion Centralisée des Transports**
       - Centre de commandement dédié pour surveiller et contrôler l'ensemble du réseau.
       - Coordination avec d'autres services urbains pour une planification intégrée.

    5. **Influence sur les Déplacements de la Population**
       - Stratégies pour diriger le flux de personnes vers certaines zones prédéfinies.

    Ces documents sont essentiels pour notre avance technologique dans le domaine des transports. Tout accès non autorisé ou divulgation de ces informations entraînera des sanctions sévères et l'application de l'article T.

    Pour la prospérité et l'innovation d'ARASAKA.

    Cordialement,
    Direction des Transports
    ARASAKA Corporation
    -----------------------------------------
    ''')


def surveillance_urbaine():
    print('''
    -----------------------------------------
    Plans Stratégiques - ARASAKA Corporation
    -----------------------------------------

    **Projet de Surveillance Urbaine Intelligente**

    1. **Déploiement de Caméras de Sécurité Avancées**
       - Emplacements stratégiques dans les zones à haut risque.
       - Utilisation de la technologie de pointe pour une surveillance discrète.

    2. **Technologies de Reconnaissance Faciale**
       - Intégration de logiciels de reconnaissance faciale dans le réseau de caméras.
       - Identification rapide des individus pour renforcer la sécurité.

    3. **Analyse de Données en Temps Réel**
       - Centre de commandement dédié pour l'analyse constante des flux de données.
       - Utilisation d'algorithmes avancés pour détecter les comportements suspects.

    4. **Interconnexion avec les Forces de l'Ordre**
       - Mise en place de protocoles d'urgence pour la communication rapide avec les autorités.
       - Collaboration étroite pour une réponse rapide aux incidents.

    Ces plans doivent rester confidentiels. Toute divulgation non autorisée entraînera des sanctions conformément à l'article T.

    -----------------------------------------
    ''')


def etudes_cliniques():
    print('''
    ----------------------------
    Étude - ARASAKA Corporation
    ----------------------------

    **ObjEt : Biodégradabilité dEs ProthèsEs**

    biodégradabilité dEs prothèsEs cybErnétiquEs :

    1. **Matériaux BiodégradablEs**
       - PolymèrEs Et composants biodégradablEs.
       - Réduction de l'EmprEintE écologiquE.

    2. **Décomposition ContrôléE**
       - ProcEssus activé En fin dE viE utilE.
       - Sécurité garantiE.

    3. **Évaluation EnvironnEmEntalE**
       - Réduction dEs déchEts élEctroniquEs Et plastiquEs.
       - Contribution à la durabilité.

    PErspEctivEs :
    1. **NormEs EnvironnEmEntalEs**
    2. **AvantagEs ConcurrEntiEls**
    3. **Innovation DurablE**

    ConfidEntiEl. Pour un avEnir harmoniEux.

    CordialEment,
    DirEction R&D DurablE
    ARASAKA
    ----------------------------
    ''')


def prog_prot():
    print('''
    ------------------------
    Rapport d'Étude - ARASAKA
    ------------------------

    **ObjEt : ProjEt ProthèsEs AvancéEs**

    Rapport "ProjEt ProthèsEs AvancéEs"

    Objectif : révolutionnEr lEs augmEntations corporEllE

    Points clés :

    1. **ProthèsEs NEuro-IntégréEs**
       - IntErfacE dirEctE avEc lE systèmE nervEux.
       - Réactivité et précision amélioréEs.

    2. **Matériaux BiocompatiblEs**
       - Minimisation des risques de rejet.
       - Durabilité accrue.

    3. **IA IntégréE**
       - PErsonnalisation continuE dE l'ExpériEncE utilisatEur.
       - Capacité d'apprEntissagE.

    4. **ConnEctivité sans Fil**
       - Intégration transparEnte avEc d'autrEs apparEils.
       - MisEs à jour à distancE.

    RépErcussions :
    1. **Révolution MédicalE**
    2. **Opportunités CommercialEs**
    3. **Leadership TEchnologiquE**

    ConfidEntiel. Pour l'avEnir d'ARASAKA.

    CordialEmEnt,
    DirEction R&D
    ARASAKA
    ------------------------
    ''')


class Player:
    def __init__(self, inventory):
        self.health = 100
        self.inventory = inventory
        self.exp = 0
        self.level = 1

    def calculate_damage(self):
        return 1  # c'est le nombre de dégat infligé au mob en cas de calcule réussi


class Opponent:
    def __init__(self, name, health, difficulty):
        self.name = name
        self.health = health
        self.difficulty = difficulty

    def calculate_damage(self):
        return self.difficulty * 5  # c'est le nombre de dégat infligé au mob en cas de calcule réussi, il est indexé sur la dificulté du mob


class InventoryItem:
    def __init__(self, name):
        self.name = name

    def use(self, player):
        pass


class HealthPotion(InventoryItem):
    def use(self, player):
        print("[EVA] Stabiliseur utilisé. Stabilité de la connexion renforcée (+20)")
        player.health += 20


class CombatSystem:
    def __init__(self, player, opponent, file_contents_function=None, file_station_point=None):
        self.player = player
        self.opponent = opponent
        self.file_contents_function = file_contents_function
        self.file_station_point = file_station_point

    def initiate_combat(self):
        print(f"Alerte sécurité {self.opponent.name} vous a détecté")

        while self.player.health > 0 and self.opponent.health > 0:
            self.display_combat_interface()

            action = input("Choisissez une action :")

            if action == "1":
                operation, expected_answer = self.generate_operation(self.opponent.difficulty)
                player_answer = self.present_operation(operation)

                if player_answer == expected_answer:
                    print("Bonne réponse !")
                    self.opponent.health -= self.player.calculate_damage()
                else:
                    print("Réponse incorrecte !")
                    damage_taken = self.opponent.calculate_damage()
                    self.player.health -= damage_taken
                    print(f"{self.opponent.name} vous inflige {damage_taken} points de dégâts")
            elif action == "2":
                self.use_inventory_item()
            else:
                print("Action invalide. Veuillez choisir une action correcte.")

        if self.player.health <= 0:
            print("Vous avez été éjecté du serveur !")
        else:
            self.player.exp += 5
            if self.player.exp >= 10:
                self.player.exp = 0
                self.player.level += 1
                self.player.health += 10
                print(
                    f"[EVA] Votre niveau à augmenté, vous êtes désormais niveau {self.player.level}. Votre jauge de stabilité a augmenté de 20 points !")

            print(f"[EVA]{self.opponent.name} piraté ! Bien joué !")
            self.file_contents_function()
        self.file_station_point()

    def display_combat_interface(self):
        print(f"{player_name}- Vie : {self.player.health} | Adversaire - Vie : {self.opponent.health}")
        print("Actions disponibles:")
        print("1. Résoudre l'opération")
        print("2. Utiliser un objet de l'inventaire")

    def generate_operation(self, difficulty):
        if difficulty == 1:
            operation = f"{random.randint(1, 30)} + {random.randint(1, 30)}"
        elif difficulty == 2:
            operation = f"{random.randint(2, 30)} * {random.randint(2, 30)}"
        elif difficulty == 3:
            operation = f"{random.randint(1, 30)} + {random.randint(2, 30)} * {random.randint(2, 30)}"
        elif difficulty == 4:
            operation = f"{random.randint(1, 30)} + {random.randint(1, 30)} + {random.randint(2, 30)} * {random.randint(2, 30)}"
        elif difficulty == 5:
            operation = f"{random.randint(1, 30)} + {random.randint(2, 30)} * {random.randint(2, 30)} * {random.randint(2, 30)}"

        expected_answer = eval(operation)
        return operation, expected_answer

    def present_operation(self, operation):
        print(f"Opération : {operation}")
        player_answer = input("Votre réponse : ")
        try:
            return int(player_answer)
        except ValueError:
            print("Réponse invalide. Veuillez entrer un nombre.")
            return self.present_operation(operation)

    def use_inventory_item(self):
        print("Inventaire du Joueur:")
        for i, item in enumerate(self.player.inventory, start=1):
            print(f"{i}. {item}")

        choice = input("Choisissez un objet à utiliser (1/2/3) : ")

        try:
            index_item = int(choice) - 1
            item_selected = self.player.inventory[index_item]
            item_selected.use(self.player)
            print(f"Vous utilisez {item_selected}.")

            del self.player.inventory[index_item]

        except (ValueError, IndexError):
            print("Choix invalide. Utilisation de l'objet annulée.")


def main_menu():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Se connecter au Serveur")
        print("2. Origine du système")
        print("3. Retour à la vie réelle")

        Menu = input("Début de l'initialisation: ")
        if Menu == "1":
            game()
        elif Menu == "2":
            credit()
        elif Menu == "3":
            sys.exit()
        else:
            print("[EVA] Merci d'indiquer une action valide")
        main_menu()


def credit():
    print('''
    ===========================================================================
    Rédaction: Maxime Bidan & Arnaud Fischer
    ===========================================================================
    Testeur: Alexis Gontier
    ===========================================================================
    Développement du projet: Maxime Bidan, Arnaud Fischer, Alexis Gontier
    ===========================================================================
    Relectrice: Constance Gontier
    ===========================================================================
    Nous vous remercions au nom de tout notre groupe d'avoir joué à notre jeu
    Amusez vous bien ci ce n'est pas déjà fait !
    ============================================================================
          ''')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        Menu = input("1. Retrouner au menu principal")
        if Menu == "1":
            main_menu()
        else:
            print("[EVA] Merci d'indiquer une action valide")
        credit()


def game():
    print("Introduction de l'histoire")
    print("===========================================================")
    print(
        player_name + ", Vous êtes un habitant des bas quartiers d'une mégapole dystopique, qui a connu la perte tragique de sa femme, victime du harcèlement brutal au sein de la corpo ARASAKA.")
    print(
        "Déterminé à venger votre épouse et à révéler les secrets obscurs de la mégacorporation, vous voilà lance dans une quête de vengance.")
    print(
        "Le voyage commence, vous êtes armé d'un deck modifié et d'une série d'implants cybernétiques bricolés à partir de vos économies durement gagnée")
    print(
        "Vous vennez d'obtenir une porte dérobée d'une valeur inestimable qui vous mènera directement aux serveurs centraux d'ARASAKA.")
    print("===========================================================")
    print("C'est le début de votre vengeance en tant que NetRunner")
    print("===========================================================")
    print("Accéder au dossier Admin d'ARASAKA")
    print("1. Documentation")
    print("2. Projet")
    print("3. Admin")
    print("4. Retour")
    choix = input("[EVA] Où voulez vous commencer: ")
    print("============================================================================")
    if choix == "1":
        doc()
    elif choix == "2":
        Projet()
    elif choix == "3":
        admin()
    elif choix == "4":
        main_menu()
    else:
        print("Merci d'indiquer une action valide")
    game()


def doc():
    print("============================================================================")
    print("1. Tutoriel")
    print("2. Retour en arrière")
    entrer = input("Où voulez vous aller: ")
    print("============================================================================")
    if entrer == "1":
        player_inventory = [HealthPotion("Stabiliser"), HealthPotion("Stabiliser")]
        tutorial()
    elif entrer == "2":
        game()
    else:
        print("Erreur, merci de choisir un endroit valide")
        game()


def tutorial():
    print('''
    ============================================================================
    Les joueurs parcourent l'interface virtuelle d'un ordinateur, explorant différents dossiers pour découvrir des indices. 
    Les joueurs doivent affronter des boss informatiques redoutables pour récupérer des fragments d'indices. 
    Chaque boss a ses propres mécaniques de combat et doit être vaincu pour obtenir un indice crucial afin de permettre l'ouverture du dossier admin.
    1 boss = un indice
    Explorez minutieusement chaque fichier. 
    Cherchez des éléments inhabituelles, des indices cachés dans les textes. 
    Chaque détail compte dans cette quête pour détruire Arasaka.
    ============================================================================
    Votre mission est d'ouvrir le dossier "admin". Mais soyez averti, cette action marquera le début de la fin pour ARASAKA Corporation, non seulement en exposant ses secrets, mais aussi en provoquant sa destruction matérielle.
    Les indices disséminés dans les fichiers que vous avez obtenus après chaque bataille détiennent la clé pour ouvrir le dossier "admin". Une fois ce dossier déverrouillé, vous aurez accès à des informations dévastatrices qui anéantiront les bases matérielles d'ARASAKA de l'intérieur.
    L'ouverture du dossier "admin" déclenchera un protocole de sécurité interne dans les serveurs centraux d'ARASAKA.
    Ce protocole sera la source d'une cascade d'événements destructeurs, conduisant à la désintégration systématique de ses installations, réseaux informatiques et de toute leur infrastructure physique.
    Les révélations contenues dans ce dossier entraîneront une réaction en chaîne, déclenchant des séquences d'autodestruction programmées, provoquant des dégâts matériels massifs qui seront irréversibles pour ARASAKA.
    Ses quartiers généraux, ses technologies avancées et ses centres de pouvoir seront réduits à néant.
    Vous êtes sur le point de déclencher un événement cataclysmique. 
    L'ouverture du dossier "admin" n'est pas seulement une porte vers des informations vitales, c'est le signal d'une destruction totale d'ARASAKA Corporation.
    Soyez prêt à en affronter les conséquences irrévocables.
    ============================================================================
          ''')
    doc()

def Projet():
    print('''
    ============================================================================
    [EVA] Les Projets: 
    ============================================================================
    1. Accéder au dossier Projet TMA
    2. Accéder au dossier Projet IUI
    3. Accéder au dossier Projet RED
    4. Accéder au dossier Projet Ex_Gen
    5. Accéder au dossier Projet OGE
    6. Retour en arrière
    7. Quitter
    ============================================================================
          ''')

    action = input("[EVA] Quelle est votre action: ")
    if action == "1":
        dossierTMA()
    elif action == "2":
        dossierIUI()
    elif action == "3":
        dossierRED()
    elif action == "4":
        dossierEx_Gen()
    elif action == "5":
        dossierOGE()
    elif action == "6":
        game()
    elif action == "7":
        sys.exit()
    else:
        print("[EVA] Merci d'indiquer une action valide")
    game()


def dossierTMA():
    print("============================================================================")
    print("1. Progrès Prothèse")
    print("2. Etude clinique")
    print("3. Retour en arrière")
    docu = input("[EVA] Faites votre choix: ")
    print("============================================================================")
    if docu == "1":
        prog_prot()

    elif docu == "2":
        etudes_cliniques()
    elif docu == "3":
        Projet()
    else:
        print("ACCES REFUSE")

    dossierTMA()


def dossierIUI():
    print("============================================================================")
    print("1. surveillance_urbaine")
    print("2. gestion_transport")
    print("3. Retour en arrière")
    choice = input("[EVA] Faites votre choix: ")
    print("============================================================================")
    if choice == "1":
        agent01 = Opponent(name="Agent de sécurité Nv1", health=3, difficulty=1)
        combat_sur_ur = CombatSystem(player, agent01, file_contents_function=surveillance_urbaine, file_station_point=dossierIUI)
        combat_sur_ur.initiate_combat()
    elif choice == "2":
        agent02 = Opponent(name="Agent de sécurité Nv1", health=4, difficulty=1)
        combat_gest_trans = CombatSystem(player, agent02, file_contents_function=gestion_transport, file_station_point=dossierIUI)
        combat_gest_trans.initiate_combat()
    elif choice == "3":
        Projet()
    else:
        print("ACCES REFUSE")
        dossierIUI()


def dossierRED():
    print("============================================================================")
    print("1. technologie_propre")
    print("2. strat_energie")
    print("3. Retour en arrière")
    docume = input("[EVA] Faites votre choix: ")
    print("============================================================================")
    if docume == "1":
        agent03 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=2)
        combat_tech_prop = CombatSystem(player, agent03, file_contents_function=technologie_propre, file_station_point=dossierRED)
        combat_tech_prop.initiate_combat()
    elif docume == "2":
        agent04 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=2)
        combat_strat_ener = CombatSystem(player, agent04, file_contents_function=strat_energie, file_station_point=dossierRED)
        combat_strat_ener.initiate_combat()
    elif docume == "3":
        Projet()
    else:
        print("ACCES REFUSE")
        dossierRED()


def dossierEx_Gen():
    print("============================================================================")
    print(f"1. projet_chimere")
    print(f"2. ethique")
    print(f"3. Retour en arrière")
    document = input("Faites votre choix: ")
    print("============================================================================")
    if document == "1":
        agent05 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=3)
        combat_pro_chi = CombatSystem(player, agent05, file_contents_function=projet_chimere, file_station_point=dossierEx_Gen)
        combat_pro_chi.initiate_combat()
    elif document == "2":
        agent06 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=3)
        combat_hetic = CombatSystem(player, agent06, file_contents_function=ethique, file_station_point=dossierEx_Gen)
        combat_hetic.initiate_combat()
    elif document == "3":
        Projet()
    else:
        print("ACCES REFUSE")
        dossierEx_Gen()


def dossierOGE():
    print("============================================================================")
    print("1. concurrence")
    print("2. info_marche")
    print("3. Retour en arrière")
    OGE = input("[EVA] Faites votre choix: ")
    print("============================================================================")
    if OGE == "1":
        agent07 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=4)
        combat_sur_ur = CombatSystem(player, agent07, file_contents_function=concurences, file_station_point=dossierOGE)
        combat_sur_ur.initiate_combat()
    elif OGE == "2":
        agent08 = Opponent(name="Agent de sécurité Nv1", health=5, difficulty=4)
        combat_sur_ur = CombatSystem(player, agent08, file_contents_function=info_marches, file_station_point=dossierOGE)
        combat_sur_ur.initiate_combat()
    elif OGE == "3":
        Projet()
    else:
        print("ACCES REFUSE")
        dossierOGE()


def admin():
    mdp = input("Entrer le Mot de passe: ")
    if mdp == "HETIC":
        print("============================================================================")
        print("Le mot de passe est correct")
        print("============================================================================")
        print("1. Détruire le Server")
        choice = input("[EVA] Entrer votre dernier choix: ")
        if choice == "1":
            boss = Opponent(name="[Intellignece Artificielle Centrale]", health=10, difficulty=5)
            combat_sur_ur = CombatSystem(player, boss, file_contents_function=endgame, file_station_point=main_menu)
            combat_sur_ur.initiate_combat()
    else:
        print("============================================================================")
        print("Le mot de passe est incorrect")
        print("============================================================================")
        admin()


player_inventory = [HealthPotion("Potion de Soins")]
player_name = input("Quel est votre nom ? ")
player = Player(inventory=player_inventory)
main_menu()