# gradereport.py
#
# Extracts data from a text file containing student records and
# produces a grade report.

# Use constants for the filenames.
INPUT_FILE = "coursegrades.txt"
OUTPUT_FILE = "gradereport.txt"

# Open the two files.
studentFile = open(INPUT_FILE, "r")
reportFile = open(OUTPUT_FILE, "w")

# Extract the course name.
courseName = studentFile.readline()

# Print the report header.
reportFile.write("STUDENT REPORT\n")
reportFile.write(courseName)
reportFile.write("-" * 40 + "\n")

# Initialize the two running totals.
gradeTotal = 0
numStudents = 0

# Process each record in the grade file.
studentId = studentFile.readline()
while studentId != "":

     # Extract the other two parts of the record.
    studentName = studentFile.readline()
    studentGrade = float(studentFile.readline())

    # Add this grade to the running total.
    gradeTotal += studentGrade
    numStudents += 1

    # Print the output for this student.
    output = "%4s  %-20s  %6.2f\n" % \
             (studentId.rstrip(),
              studentName.rstrip(),
              studentGrade)
    reportFile.write(output)

    # Extract the next record.
    studentId = studentFile.readline()

  # Compute the average grade.
avgGrade = gradeTotal / float(numStudents)

# Print the footer.
reportFile.write("-" * 40 + "\n")
reportFile.write("%-26s  %6.2f\n" % ("Average Grade", avgGrade))

# Close the two files.
studentFile.close()
reportFile.close()
