from Exams.project import Category
from Exams.project import Document
from Exams.project import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for x in self.categories:
            if x.id == category.id and x.name == category.name:
                return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for x in self.topics:
            if x.__dict__ == topic.__dict__:
                return

        self.topics.append(topic)

    def add_document(self, document: Document):
        for x in self.documents:
            if x.__dict__ == document.__dict__:
                return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__get_obj_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__get_obj_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__get_obj_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__get_obj_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_obj_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_obj_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__get_obj_by_id(self.documents, document_id)
        return document

    def __repr__(self):
        result = '\n'.join([str(x) for x in self.documents])
        return result

    def __get_obj_by_id(self, objects, object_id):
        for object in objects:
            if object.id == object_id:
                return object
