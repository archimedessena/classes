def algorithm_development(problem_spec):
    correct = False
    while not correct or not fast_enough(running_time):
        algorithm = devise_algorithm(problem_spec)
        correct = analze_correctness(algorithm)
        running_time = analze_efficiency(algorithm)
    return algorithm


algo = algorithm_development(2)