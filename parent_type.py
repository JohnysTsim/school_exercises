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

# Ζητάει από τον χρήστη να δώσει από το πληκτρολόγιο, το φίλο του - (1) Άνδρας, (2) Γυναίκα
gender=int(input("dwse to filo, 1 gia andras, 2 gia gynaika: "))

# Ζητάει από τον χρήστη να δώσει από το πληκτρολόγιο, τον αριθμό των παιδιών του
kids=int(input("dwse arithmo paidiwn: "))

# Αν/Εφόσον το φίλο που έδωσε ο χρήστης είναι ο αριθμός (1) δηλαδή Άνδρας
# θα μπει στην παρακάτω if και θα εκτελέσει τις εντολές 
# που βρίσκονται μέσα στην συγκεκριμένη if
if gender == 1:
    # Η εντολή μέσα σε αυτήν την if θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (από 1 έως και 2)
    if kids>=1 and kids<=2:
        print ("\nfysiologikos pateras\n")

    # Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (ίσος με 3)
    elif kids==3:
        print ("\ntriteknos pateras\n")

    # Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (από 4 και πάνω)
    elif kids>=4:
        print ("\npoliteknos pateras\n")


# Αν/Εφόσον το φίλο που έδωσε ο χρήστης είναι ο αριθμός (2) δηλαδή Γυναίκα
# θα μπει στην παρακάτω elif και θα εκτελέσει τις εντολές 
# που βρίσκονται μέσα στην συγκεκριμένη elif
elif gender == 2:
    # Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (από 1 έως και 2)
    if kids>=1 and kids<=2:
        print ("\nfysiologikh mhtera\n")
    
    # Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (ίσος με 3)
    elif kids==3:
        print ("\ntriteknh mhtera\n")

    # Η εντολή μέσα σε αυτήν την elif θα εκτελεστεί εφόσον ο αριθμός των παιδιών 
    # που έδωσε ο χρήστης είναι (από 4 και πάνω)
    elif kids>=4:
        print ("\npoliteknh mhtera\n")
