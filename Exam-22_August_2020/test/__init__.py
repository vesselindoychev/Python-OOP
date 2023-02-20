from Exam_10_April_2021.project import System
#
# software = Software('Software', 'Ordinary', 16, 24)
# light_software = LightSoftware('LightSoftware', 16, 24)
# express_software = ExpressSoftware('ExpressSoftware', 16, 24)
# print(software)
# print(light_software)
# print(express_software)
#
# hardware = Hardware('Hardware', 'Type', 17, 25)
# hardware.install(software)
# print(hardware.software_components)
#
# hh = HeavyHardware('HeavyHardware', 200, 200)
# ph = PowerHardware('PowerHardware', 200, 200)
# print(hh)
# print(ph)
#
# system = System()
# system.register_power_hardware('Powerhardware', 200, 100)
# print(system.register_express_software('Powerhardware', 'ExpressSoftware', 1000, 1000))

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
