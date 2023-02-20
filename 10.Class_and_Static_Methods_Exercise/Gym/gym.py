from Exams.project import Customer
from Exams.project import Equipment
from Exams.project import ExercisePlan
from Exams.project import Subscription
from Exams.project import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        c = self.__get_object_by_attributes(self.customers, customer)
        if c is None:
            return
        self.customers.append(c)

    def add_trainer(self, trainer: Trainer):
        t = self.__get_object_by_attributes(self.trainers, trainer)
        if t is None:
            return
        self.trainers.append(t)

    def add_equipment(self, equipment: Equipment):
        e = self.__get_object_by_attributes(self.equipment, equipment)
        if e is None:
            return
        self.equipment.append(e)

    def add_plan(self, plan: ExercisePlan):
        p = self.__get_object_by_attributes(self.plans, plan)
        if p is None:
            return
        self.plans.append(p)

    def add_subscription(self, subscription: Subscription):
        s = self.__get_object_by_attributes(self.subscriptions, subscription)
        if s is None:
            return
        self.subscriptions.append(s)

    def subscription_info(self, subscription_id):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        customer = self.__get_object_by_id(self.customers, subscription.customer_id)
        trainer = self.__get_object_by_id(self.trainers, subscription.trainer_id)
        plan = self.__get_object_by_id(self.plans, subscription.exercise_id)
        equipment = self.__get_object_by_id(self.equipment, plan.equipment_id)

        result = str(subscription) + '\n'
        result += str(customer) + '\n'
        result += str(trainer) + '\n'
        result += str(equipment) + '\n'
        result += str(plan) + '\n'

        return result

    @staticmethod
    def __get_object_by_attributes(object_list, object_type):

        for obj in object_list:
            if obj.__dict__ == object_type.__dict__:
                return
        return object_type

    @staticmethod
    def __get_object_by_id(object_list, object_id):
        for obj in object_list:
            if obj.id == object_id:
                return obj



