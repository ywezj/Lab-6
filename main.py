class Lamp:

    def __init__(self, emission_power, energy_consumption, lifespan):
        self.emission_power = emission_power  
        self.energy_consumption = energy_consumption  
        self.lifespan = lifespan  

    def days_until_burnout(self, hours_per_day=8):
        return self.lifespan / hours_per_day

    def power_to_consumption_ratio(self):
        return self.emission_power / self.energy_consumption


class DaylightLamp(Lamp):

    def __init__(self, emission_power, energy_consumption, lifespan, spectrum_type):
        super().__init__(emission_power, energy_consumption, lifespan)
        self.spectrum_type = spectrum_type 


class Floodlight(Lamp):
    
    def __init__(self, emission_power, energy_consumption, lifespan, beam_angle):
        super().__init__(emission_power, energy_consumption, lifespan)
        self.beam_angle = beam_angle 


# Пример использования
if __name__ == '__main__':
    lamp = Lamp(60, 60, 2000)
    
    print(f"Лампа перегорит через {lamp.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для лампы: {lamp.power_to_consumption_ratio():.2f}\n")

    daylight_lamp = DaylightLamp(30, 10, 5000, "warm")
    print(f"Лампа дневного света перегорит через {daylight_lamp.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для лампы дневного света: {daylight_lamp.power_to_consumption_ratio():.2f}\n")

    floodlight = Floodlight(500, 550, 3000, 120)
    print(f"Прожектор перегорит через {floodlight.days_until_burnout()} дней.")
    print(f"Соотношение мощности к потреблению для прожектора: {floodlight.power_to_consumption_ratio():.2f}")
