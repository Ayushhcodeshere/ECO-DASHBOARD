def get_recommendations(current_usage, peak_ratio):
    """
    Returns a list of categorized energy-saving tips based on rule-based logic.
    """
    tips = []
    
    # Rule-based tips
    if current_usage > 10:
        tips.append({
            "category": "High Usage Alert",
            "text": "Your daily consumption is above 10 kWh. Consider turning off unused appliances.",
            "type": "warning",
            "impact": "High"
        })
        
    if peak_ratio > 0.4:
        tips.append({
            "category": "Peak Hours",
            "text": "Over 40% of your usage is during peak hours (12 PM - 4 PM). Shift laundry or heavy appliances to evening hours to save costs.",
            "type": "info",
            "impact": "Medium"
        })
        
    # AI-driven placeholders (simulated)
    tips.append({
        "category": "AI Smart Insight",
        "text": "Our AI model noticed your AC runs 2 hours longer on weekends. Consider setting a timer to save ~15% on cooling costs.",
        "type": "success",
        "impact": "High"
    })
    
    tips.append({
        "category": "AI Smart Insight",
        "text": "Your refrigerator's base load seems 10% higher than similar households. Check the temperature setting or door seals.",
        "type": "success",
        "impact": "Low"
    })
    
    return tips

def calculate_carbon_footprint(saved_kwh):
    """
    Estimates CO2 emissions saved based on kWh.
    Average conversion: 0.85 pounds of CO2 per kWh (depends on region, using a generic multiplier).
    Returns CO2 saved in kg (1 pound ≈ 0.45 kg, so ~0.385 kg per kWh).
    """
    co2_per_kwh_kg = 0.385
    return saved_kwh * co2_per_kwh_kg
