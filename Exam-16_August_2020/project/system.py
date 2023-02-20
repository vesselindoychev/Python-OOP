from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        ph = PowerHardware(name, capacity, memory)
        System._hardware.append(ph)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hh = HeavyHardware(name, capacity, memory)
        System._hardware.append(hh)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardwares = [h for h in System._hardware if h.name == hardware_name]

        if not hardwares:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware = hardwares[0]
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardwares = [h for h in System._hardware if h.name == hardware_name]

        if not hardwares:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware = hardwares[0]
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardwares = [hn for hn in System._hardware if hn.name == hardware_name]
        softwares = [sn for sn in System._software if sn.name == software_name]

        if not hardwares and not softwares:
            return "Some of the components do not exist"
        hardware = hardwares[0]
        software = softwares[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = f'System Analysis' + '\n'
        result += f'Hardware Components: {len(System._hardware)}' + '\n'
        result += f'Software Components: {len(System._software)}' + '\n'
        result += f'Total Operational Memory: {sum([h.used_memory for h in System._hardware])} / {sum([h.memory for h in System._hardware])}' + '\n'
        result += f'Total Capacity Taken: {sum([h.used_capacity for h in System._hardware])} / {sum([h.capacity for h in System._hardware])}'

        return result

    @staticmethod
    def system_split():
        result = ''
        for h in System._hardware:
            result += f'Hardware Component - {h.name}' + '\n'
            express_soft_comps = [s for s in h.software_components if s.__class__.__name__ == "ExpressSoftware"]
            result += f'Express Software Components: {len(express_soft_comps)}' + '\n'
            light_soft_comps = [s for s in h.software_components if s.__class__.__name__ == "LightSoftware"]
            result += f'Light Software Components: {len(light_soft_comps)}' + '\n'
            result += f'Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.memory}' + '\n'
            result += f'Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.capacity}' + '\n'
            result += f'Type: {h.hardware_type}' + '\n'
            software_names_comps = [s.name for s in h.software_components]
            result += f'Software Components: {", ".join(software_names_comps) if software_names_comps else None}' + '\n'

        return result
