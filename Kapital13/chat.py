from re import *  # Import module re để sử dụng các hàm và phương thức liên quan đến regular expression.

class Chat:

    def __alle(self, e):
        re1 = compile('alle \w\w+en', I)  # Biểu thức chính quy tìm kiếm mẫu "alle + hai ký tự chữ cái hoặc nhiều + en" (không phân biệt chữ hoa/thường)
        re2 = compile('alle', I)  # Biểu thức chính quy tìm kiếm từ "alle" (không phân biệt chữ hoa/thường)
        re3 = compile('[.!,;]+')  # Biểu thức chính quy tìm kiếm một hoặc nhiều dấu chấm, dấu chấm than, dấu phẩy hoặc dấu chấm phẩy.
        m1 = re1.search(e)  # Tìm kiếm một khớp của biểu thức chính quy re1 trong chuỗi e.
        m2 = re2.search(e)  # Tìm kiếm một khớp của biểu thức chính quy re2 trong chuỗi e.
        if m1:
            passendesStueck1 = m1.string[m1.start():m1.end()]  # Lấy phần khớp được tìm thấy từ m1 trong chuỗi gốc e.
            verb = passendesStueck1.split()[1]  # Tách từ thứ hai trong phần khớp thành động từ.
            stamm = verb[:-2]  # Lấy phần gốc của động từ bằng cách loại bỏ hai ký tự cuối cùng.
            passendesStueck2 = m2.string[m2.start():]  # Lấy phần khớp từ m2 đến hết chuỗi gốc e.
            satz = re3.split(passendesStueck2)[0]  # Tách câu từ phần khớp passendesStueck2 bằng các dấu chấm, dấu chấm than, dấu phẩy hoặc dấu chấm phẩy.
            restsatz = passendesStueck2.split(' ', 2)[2]  # Tách phần còn lại của câu sau passendesStueck2.
            restsatz = restsatz.replace('mich', 'Sie')  # Thay thế từ 'mich' bằng 'Sie' trong phần còn lại của câu.
            restsatz = restsatz.replace('mein', 'Ihr')  # Thay thế từ 'mein' bằng 'Ihr' trong phần còn lại của câu.
            antwort = 'Wer {}t {}?'.format(stamm, restsatz)  # Tạo câu trả lời bằng cách kết hợp động từ gốc và phần còn lại của câu.

            antwort += ' Denken Sie an bestimmte Personen?'  # Thêm vào câu trả lời một phần cuối chung.
            return antwort  # Trả về câu trả lời nếu có tìm thấy khớp của biểu thức chính quy re1 trong chuỗi e.

    def __familie(self, e):
        re = compile('bruder|schwester|mutter|vater', I)  # Biểu thức chính quy tìm kiếm các từ 'bruder', 'schwester', 'mutter', 'vater' (không phân biệt chữ hoa/thường)
        if re.search(e):
            antwort = 'Erzählen Sie mir mehr über Ihre Familie.'  # Gán câu trả lời khi tìm thấy từ khớp trong chuỗi e.
            return antwort  # Trả về câu trả lời nếu có tìm thấy từ khớp của biểu thức chính quy trong chuỗi e.

    def __negativ(self, e):
        re = compile('nein|nicht|kein', I)  # Biểu thức chính quy tìm kiếm các từ 'nein', 'nicht', 'kein' (không phân biệt chữ hoa/thường)
        if re.search(e):
            antwort = 'Denken Sie nicht ein bisschen negativ?'  # Gán câu trả lời khi tìm thấy từ khớp trong chuỗi e.
            return antwort  # Trả về câu trả lời nếu có tìm thấy từ khớp của biểu thức chính quy trong chuỗi e.

    def chat(self):
        print('Hallo, ich bin Mini-Eliza.')
        e = input('Sie: ')
        while e:
            if self.__alle(e): print(self.__alle(e))
            elif self.__familie(e): print(self.__familie(e))
            elif self.__negativ(e): print(self.__negativ(e))
            else: print('Aha ...')
            e = input('Sie: ')
        print('Auf Wiedersehen!')


chat = Chat()
chat.chat()