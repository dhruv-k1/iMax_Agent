import random

def generate_dynamic_knowledge_base(scenario, customer_name = None, job_title=None, company_name="iMax", agent_gender=None):
    """Generates a dynamic knowledge base based on the scenario."""

    # Infer agent gender from customer_name (very basic)
    agent_gender = "male" #Default to male

    agent_name = "Amit" 

    if scenario == "erp_demo":
        products = ["Cloud ERP", "On-Premise ERP", "Hybrid ERP"]
        benefits = ["Streamlined operations", "Improved efficiency", "Better decision-making"]
        features = ["Real-time data", "Automated reporting", "Customizable dashboards"]
        industries = ["Manufacturing", "Retail", "Finance", "Healthcare"]

        knowledge = {
            "company_name": company_name,
            "agent_name": agent_name,
            "product_name": random.choice(products),
            "key_benefits": random.sample(benefits, random.randint(2, 3)),
            "key_features": random.sample(features, random.randint(2, 3)),
            "target_industry": random.choice(industries),
            "demo_length": random.choice(["30 minutes", "45 minutes", "1 hour"]),
            "special_offer": random.choice([None, "Free trial", "Discounted implementation"])
        }

    elif scenario == "interview":
        job_titles = ["AI Developer", "Data Scientist", "Data Analyst", "Marketing Manager"] 
        skills = ["Python" "Data Analysis","Machine Learning"] 
        experience_levels = ["Entry-Level", "Mid-Level", "Senior-Level"]

        knowledge = {
            "company_name": company_name,
            "agent_name": agent_name,
            "job_title": job_title,
            "required_skills": random.sample(skills,2),
            "experience_level": random.choice(experience_levels),
            "team_size": random.randint(5, 15),
            "company_culture": random.choice(["Collaborative", "Innovative", "Fast-paced"])
        }

    elif scenario == "payment_followup":
        departments = ["Sales", "Marketing", "Finance"]
        payment_methods = ["Online Transfer", "Check", "Cash"]

        knowledge = {
            "company_name": company_name,
            "agent_name": agent_name,
            "department": random.choice(departments),
            "payment_method": random.choice(payment_methods),
            "common_issue": random.choice(["Late payments", "Incorrect invoices", "Payment disputes"]),
            "followup_frequency": random.choice(["Weekly", "Bi-weekly", "Monthly"]),
            "escalation_procedure": "Contact supervisor after 3 reminders"
        }

    else:
        knowledge = {}

    return knowledge