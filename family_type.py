# coding: utf-8

# το 'coding: utf-8' χρησιμεύει για να μπορούμε να γράφουμε Ελληνικά στο πρόγραμμα μας 

"""
όταν λέμε μέσα στην if/elif/else εννοούμε τις εντολές που βρίσκονται κάτω από
από την if/elif/else και έχουν λίγο κενό στην αρχή, μόλις φτάσουμε στην επόμενη
εντολή που δεν έχει κενό στην αρχή, σημαίνει οτι έχουμε πλεόν βγεί από
την if/elif/else και προχωρήσαμε στην επόμενη εντολή. το (if) το χρησιμοποιούμε για
την πρώτη περίπτωση/συνθήκη συνήθως και την (elif -> else if) την χρησιμοποιούμε
για τις ενδυάμεσες περιπτώσεις/συνθήκες και όταν δεν έχουν μείνει πλέον άλλες περιπτώσεις/συνθήκες
να καλύψουμε, αλλά θέλουμε να είμαστε όσο το δυνατό πιο σίγουροι οτι τις καλύψαμε όλες,
χρησιμοποιούμε την (else) η οποία θα τρέξει σε περίπτωση που δεν ισχύει καμία από τις παραπάνω
περιπτώσεις/συνθήκες.
"""

"""
1) Το 'int' το χρησιμοποιούμε όταν αυτό που θα δώσει ο χρήστης από το πληκτρολόγιο είναι ακέραιος ή θέλουμε να είμαστε σίγουροι οτι θα είναι ακέραιος
2) Το 'float' το χρησιμοποιούμε όταν αυτό που θα δώσει ο χρήστης από το πληκτρολόγιο είναι πραγματικός ή θέλουμε να είμαστε σίγουροι οτι θα είναι πραγματικός
3) Το 'string' το χρησιμοποιούμε όταν αυτό που θα δώσει ο χρήστης από το πληκτρολόγιο είναι κείμενο ή θέλουμε να είμαστε σίγουροι οτι θα είναι κείμενο
"""


# !!! Τα παραπάνω είναι σχόλια δεν χρησιμεύουν σε κάτι, Πέρα από το να βοηθάνε τον προγραμματιστή που γράφει το πρόγραμμα. Τα σχόλια πρέπει να ξεκινάνε με αυτό το σύμβολο '#' για σχόλιο μίας γραμμής 
# !!! ή αυτό """ και ξανά αυτό """ για να κλείσει το σχόλιο αν θέλουμε να γράψουμε """σχόλιο πολλών γραμμών""" και γράφουμε ανάμεσα
# !!! Πέρα από το να βοηθάνε τον προγραμματιστή που γράφει το πρόγραμμα
# ------------------------------------------------------------------------------------------------------------------------------------------------------------



# Ζητάει από τον χρήστη να δώσει των αριθμό των Αγοριών της οικογένειας
agoria_number = int(input("dwse arithmo agoriwn ths oikogeneias: "))

# Ζητάει από τον χρήστη να δώσει των αριθμό των Κοριτσιών της οικογένειας
koritsia_number = int(input("dwse arithmo koritsiwn ths oikogeneias: "))

# Υπολογίζει των Συνολικό αριθμό των παιδιών της οικογένειας (Αγόρια + Κορίτσια)
sunolika_paidia = agoria_number + koritsia_number

# Υπολογίζει των μέσω όρο των παιδιών της οικογένειας ((Αγορία + Κορίτσια) / 2)
mo_paidiwn = ((agoria_number + koritsia_number) / 2)

# Εμφανίζει τον Μέσο Όρο των παιδιών της Οικογένειας
print(mo_paidiwn)

# Η εντολή μέσα σε αυτήν την if θα εκτελεστεί εφόσον ο συνολικός αριθμός των παιδιών
# της οικογένειας είναι ίσος με 3
if sunolika_paidia == 3:
    print("Triteknh Oikogeneia")

# Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο συνολικός αριθμός των παιδιών
# της οικογένειας είναι μεγαλύτερος ή ίσος με 4
elif sunolika_paidia >= 4:
    print("Polyteknh Oikogeneia")

# Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο συνολικός αριθμός των παιδιών
# της οικογένειας είναι μικρότερος από 3
elif sunolika_paidia < 3:
    print("Fysiologikh Oikogeneia")


# Η εντολή μέσα σε αυτήν την if θα εκτελεστεί εφόσον ο αριθμός των Κοριτσιών της οικογένειας
# είναι μεγαλύτερος από τον μέσο όρο
if koritsia_number > mo_paidiwn:
    print("Koritso Oikogeneia")

# Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των Αγοριών της οικογένειας
# είναι μεγαλύτερος από τον μέσο όρο
elif agoria_number > mo_paidiwn:
    print("Agoro Oikogeneia")