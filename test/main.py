import config.config as conf
import src.list_generator as gen
import src.diagram as diagram

"""
Нужно:
    1. Создать лист заданной размерности с рандомными значениями в пределах от 0 до 1
    2. Посторить диаграмму по данному листу и сохранить в файл
"""
if __name__ == '__main__':
    list_ = gen.list_gen(conf.list_size)
    diagram.diagram(list_, conf.path_to_file)
