notes_module = {
    "salma": 16,
    "karim": 11,
    "zineb": 19,
    "hassan": 14,
}

students_num = 0
sum_notes = 0
milleur = 0
milleur_note = 0

for student in notes_module:
    students_num += 1
    sum_notes += notes_module

    if notes_module[student] > milleur_note:
        milleur_note = notes_module[student]
        milleur = student

moyenne = sum_notes / students_num

print(f"le nombre total des etudients est {students_num}")
print(f"le moyenne general des notes est {moyenne}")
print(f"le milleur etudient est {milleur} de note {milleur_note}")