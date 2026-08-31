"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced."""
    if temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    eff = (generated_power/theoretical_max_power)*100
    if eff >= 80:
        return 'green'
    if 80 > eff >= 60:
        return 'orange'
    if 60 > eff >= 30:
        return 'red'
    return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    product = temperature * neutrons_produced_per_second
    if product < threshold * 0.9:
        return 'LOW'
    if threshold - threshold * 0.1 <= product <= threshold + threshold * 0.1:
        return 'NORMAL'
    return 'DANGER'
