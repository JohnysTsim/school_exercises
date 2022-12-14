# coding: utf-8

""" Δυαδική αναζήτηση αριθμού """


# Εισαγωγή - Κάλεσμα της Κλάσης random
import random

# Μεταβλητή με τιμή False
found=False

# Μεταβλητή με τιμή 1, η οποία θα κρατάει το αρχικό όριο, από το πεδίο που θα κάνει το
# πρόγραμμα αναζήτηση
start=1

# Μεταβλητή στην οποία αποθηκεύεται ο αριθμός που πληκτρολογεί ο χρήστης 
# int(input("give a number: ")) <- αυτή η γραμμή κώδικα δεν τρέχει είναι, διότι είναι σχόλιο

# παράγει έναν ακέραιο τυχαίο αριθμό από το 1 μέχρι το 100
mySecretNumber = random.randint(1, 100)

# Μεταβλητή με τιμή 100, η οποία θα κρατάει το τελικό όριο, από το πεδίο που θα κάνει το
# πρόγραμμα αναζήτηση
end=100

# Μεταβλητή με τιμή 0, η οποία θα κρατάει το ποσό των προσπαθειών που θα κάνει το πρόγραμμα
# να βρεί τον αριθμό που έδωσε ο χρήστης ή ο υπολογιστής
tries=0

# εμφανίζει την πρώτη φόρα το αρχικό και το τελικό όριο
print(f"start={start}, end={end}")


# όσο ακόμα το found είναι ίσο με false
while not found:

    # υπολόγισε το middle, λίγο πιο κάτω λέει πως υπολογίζεται το middle και η ακριβώς επόμενη γραμμή λέει την πράξη
    middle = (start + end) // 2

    # εφόσον ο αριθμός που έδωσε ο χρήστης είναι μεγαλύτερος από το middle, όρισε την τιμή του start σε -> middle + 1
    # και αύξησε τις προσπάθεις κατά 1
    if (mySecretNumber > middle):
        start = middle + 1
        tries+=1

    # εφόσον ο αριθμός που έδωσε ο χρήστης είναι μικρότερος από το middle, όρισε την τιμή του end σε -> middle - 1
    # και αύξησε τις προσπάθεις κατά 1
    if (mySecretNumber < middle):
        end = middle - 1
        tries+=1
    
    # εμφανίζει κάθε φορά(εκτός από την πρώτη φορά) το αρχικό όριο, το τελικό όριο και το middle που υπολογίζεται από το ((προηγούμενο αρχικό όριο + προηγούμενο τελικό όριο) / 2)
    print(f"start={start}, end={end}, middle={middle}")
    
    
    # εφόσον το middle είναι ίσο με τον αριθμό που έδωσε ο χρήστης ή ο υπολογιστής 'mySecretNumber' τοτε άλλαξε την τιμή του found από false σε true
    if (middle == mySecretNumber):
        found = True

# εμφανίζει τον αριθμό που έδωσε ο χρήστης ή ο υπολογιστής στην αρχή και τις προσπάθεις που πήρε στο πρόγραμμα για να καταφέρει να το βρεί
print(f"O arithmos pou edwsa einai: {mySecretNumber}, Kai vrethike me {tries} Prospatheies")
