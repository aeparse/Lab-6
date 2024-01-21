#Вариант 7

class Lamp:
    def __init__(self, radiation_power, energy_consumption, operation_life):
        self.radiation_power = radiation_power
        self.energy_consumption = energy_consumption
        self.operation_life = operation_life

    def time_before_burnout(self):
        burnout_in_hours = self.operation_life * 365 * 24  # предположим, что срок службы указан в годах
        working_hours_per_day = 8  # часов
        return burnout_in_hours / working_hours_per_day


class Daylight_lamp(Lamp):
    def __init__(self, radiation_power, energy_consumption, operation_life, color_temperature):
        super().__init__(radiation_power, energy_consumption, operation_life)
        self.color_temperature = color_temperature


class Searchlight(Lamp):
    def __init__(self, radiation_power, energy_consumption, operation_life, lighting_angle):
        super().__init__(radiation_power, energy_consumption, operation_life)
        self.lighting_angle = lighting_angle

    def power_to_consumption_ratio(self):
        return self.radiation_power / self.energy_consumption