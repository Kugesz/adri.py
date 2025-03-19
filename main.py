from getting_files.getting_pdf import downloading_pdf
from processing import creating_message
from processing.converting import convert_pdf_to_excel
from processing.extracting_data import getting_data


def main():
    downloading_pdf()
    convert_pdf_to_excel()
    message_data = getting_data()
    if(len(message_data) == 0):
        return
    
    formated_messages = creating_message(message_data)
if __name__ == "__main__":
    main()

# CREATE TABLE all_date (
#	 type varchar(4),
#    lesson varchar(3),
#    class varchar(10),
#    inTheTimetabel varchar(10),
#    actualLesson varchar(10),
#    substituteTeacher varchar(20),
#    lessonDate varchar(10),
#    lessonNumber varchar(5),
#    fromWhere varchar(6),
#    toWhere varchar(6)
# )
