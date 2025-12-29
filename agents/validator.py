def validator_agent(state):
    """
    Validator for demo purpose.
    Since LLM is mocked, we accept the first answer as valid
    to avoid infinite retries.
    """
    state["valid"] = True
    return state
