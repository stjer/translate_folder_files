import os
from googletrans import Translator
translator = Translator()
import re


def list_files_recursive(folder_path):
    lista = []
    try:
        #print(f"폴더 '{folder_path}' 내 파일 목록:")
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                lista.append(file_path)
        return lista
    except FileNotFoundError:
        print(f"폴더 '{folder_path}'를 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일 목록을 가져오는 중 오류가 발생했습니다: {e}")

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        otmp = old_name.split('\\')[-1]
        ntmp = new_name.split('\\')[-1]
        print(f"파일 이름이 '{otmp}'에서 '{ntmp}'으로 변경되었습니다.")
    except FileNotFoundError:
        print(f"파일 '{old_name}'을 찾을 수 없습니다.")
    except Exception as e:
        print(f"파일 이름 변경 중 오류가 발생했습니다: {e}")
        

# 폴더 경로 입력 받기
folder_path = input("폴더 경로를 입력하세요: ")

# 폴더 내 파일 목록 출력
lista = list_files_recursive(folder_path)

for i in range(len(lista)):
    tmp = lista[i].split('\\')[-1].split('(')[0].split('.')[0]
    ct = re.sub(r'[a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣0-9 ]', '', tmp)
    if ct != '' :
        e = translator.translate(tmp, dest = 'en')
        e = e.text.replace('"',"'")
        rename_file(lista[i], lista[i].replace(tmp,e +' ('+tmp+')'))
