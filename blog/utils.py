from datetime import datetime, time


def get_uploaded_file_name(instance, filename):
    return "image/{y}/{m}/{d}/{time}_{filename}".format(
        y=datetime.now().year,
        m='0' + str(datetime.now().month) if len(str(datetime.now().month)) == 1 else str(datetime.now().month),
        d='0' + str(datetime.now().day) if (len(str(datetime.now().day)) == 1) else str(datetime.now().day),
        # ternary for swag :p
        time=str(time()).replace('.', '_'),
        filename=filename
    )
