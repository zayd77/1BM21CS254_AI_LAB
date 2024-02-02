def evaluate_expression(p, q, r):
    # Evaluate the given expression (p v q) ^ (~r v p)
    expression_result = (p or q) and (not r or p)
    return expression_result

def generate_truth_table():
    # Print the header of the truth table
    print(" p | q | r | Expression (KB) | Query (p^r)")
    print("---|---|---|-----------------|------------")

    # Evaluate and print each row of the truth table
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                expression_result = evaluate_expression(p, q, r)
                query_result = p and r

                print(f" {p} | {q} | {r} | {expression_result}               | {query_result}")

def query_entails_knowledge():
    # Check if query entails the knowledge
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                expression_result = evaluate_expression(p, q, r)
                query_result = p and r

                # If the expression is true and the query is false, query does not entail the knowledge
                if expression_result and not query_result:
                    return False

    # If the loop completes without returning, query entails the knowledge
    return True

def main():
    # Generate and print the truth table
    generate_truth_table()

    # Check if query entails the knowledge and print the result
    if query_entails_knowledge():
        print("\nQuery entails the knowledge.")
    else:
        print("\nQuery does not entail the knowledge.")

if __name__ == "__main__":
    main()
