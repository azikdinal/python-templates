class DataFilter:
    def __init__(self, dbContext):
        self.dbContext = dbContext

    def filter_data(self, author="", name="", guest="", place=""):
        # Выполняем фильтрацию данных в соответствии с критериями
        filtered_data = self.dbContext.filter_data(author, name, guest, place)
        return filtered_data
