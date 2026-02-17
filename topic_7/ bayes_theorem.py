def bayes_theorem(p_h, p_evidence_given_h, p_evidence_given_not_h):
    """
    Обчислює апостеріорну ймовірність гіпотези за теоремою Байєса.
    
    Параметри:
    p_h: P(H) - апріорна ймовірність гіпотези
    p_evidence_given_h: P(E|H) - ймовірність спостереження за умови що гіпотеза вірна
    p_evidence_given_not_h: P(E|not H) - ймовірність спостереження за умови що гіпотеза хибна
    
    Повертає:
    P(H|E) - апостеріорна ймовірність гіпотези після спостереження
    """
    # Апріорна ймовірність протилежної гіпотези
    p_not_h = 1 - p_h
    
    # Повна ймовірність спостереження (evidence)
    p_evidence = p_h * p_evidence_given_h + p_not_h * p_evidence_given_not_h
    
    # Апостеріорна ймовірність за теоремою Байєса
    p_h_given_evidence = (p_h * p_evidence_given_h) / p_evidence
    
    return p_h_given_evidence

# Приклад 1: Спам-фільтр
p_spam = 0.3           # 30% листів це спам
p_word_in_spam = 0.6   # 60% спам-листів містять слово "безкоштовно"
p_word_in_normal = 0.05 # 5% нормальних листів містять це слово

result_spam = bayes_theorem(p_spam, p_word_in_spam, p_word_in_normal)
print(f"Ймовірність спаму при слові 'безкоштовно': {result_spam:.1%}")


# Приклад 2: Медичний тест
p_disease = 0.01        # P(D) - базова частота хвороби 1%
sensitivity = 0.99      # P(T|D) - чутливість тесту 99%
false_positive = 0.05   # P(T|not D) - хибнопозитивний результат 5%

result = bayes_theorem(p_disease, sensitivity, false_positive)

print(f"Апріорна ймовірність хвороби: {p_disease:.1%}")
print(f"Апостеріорна ймовірність після позитивного тесту: {result:.1%}")

# Приклад 3: Урни з кулями
p_urn1 = 0.5              # P(H1) - вибрали першу урну
p_white_from_urn1 = 0.3   # P(A|H1) - біла куля з першої урни
p_white_from_urn2 = 0.6   # P(A|H2) - біла куля з другої урни

# Для першої урни (not H1 означає другу урну)
prob_urn1_given_white = bayes_theorem(p_urn1, p_white_from_urn1, p_white_from_urn2)

# Для другої урни
prob_urn2_given_white = bayes_theorem(0.5, p_white_from_urn2, p_white_from_urn1)

print(f"Ймовірність що біла куля з першої урни: {prob_urn1_given_white:.1%}")
print(f"Ймовірність що біла куля з другої урни: {prob_urn2_given_white:.1%}")
