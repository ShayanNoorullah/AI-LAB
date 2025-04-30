from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpdDisease = TabularCPD(variable='Disease', variable_card=2, values=[[0.6], [0.4]])

cpdFever = TabularCPD(variable='Fever', variable_card=2, 
    values=[[0.9, 0.3], [0.1, 0.7]],
    evidence=['Disease'], evidence_card=[2])

cpdCough = TabularCPD(variable='Cough', variable_card=2, 
    values=[[0.8, 0.4], [0.2, 0.6]],
    evidence=['Disease'], evidence_card=[2])

cpdFatigue = TabularCPD(variable='Fatigue', variable_card=2, 
    values=[[0.7, 0.2], [0.3, 0.8]],
    evidence=['Disease'], evidence_card=[2])

cpdChills = TabularCPD(variable='Chills', variable_card=2, 
    values=[[0.85, 0.3], [0.15, 0.7]],
    evidence=['Disease'], evidence_card=[2])

model.add_cpds(cpdDisease, cpdFever, cpdCough, cpdFatigue, cpdChills)

inference = VariableElimination(model)

prob1 = inference.query(variables=['Disease'], evidence={'Fever': 1, 'Cough': 1})
print(prob1)

prob2 = inference.query(variables=['Disease'], evidence={'Fever': 1, 'Cough': 1, 'Chills': 1})
print(prob2)

prob3 = inference.query(variables=['Fatigue'], evidence={'Disease': 1})
print(prob3)
