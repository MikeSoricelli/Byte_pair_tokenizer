import heapq

def tokenize(text, merges):
    tokens = list(text)
    mapping = {}


    #run byte pair encoding for until only 10,000 tokens remain
    for x in range(merges):

        max_token_count = 0
        max_token = tokens[0]

        #find candidate token with most occurances
        for i in range(len(tokens) - 1):
            candidate_token = tokens[i] + tokens[i+1]
            if candidate_token in mapping:
                mapping[candidate_token] += 1
                if mapping[candidate_token] > max_token_count:
                    max_token_count = mapping[candidate_token]
                    max_token = candidate_token
            else:
                mapping[candidate_token] = 1

        # replace all subcomponents of max token with max token

        for i, token in enumerate(tokens):
            if not(i >= (len(tokens) - 1)):
                if tokens[i] + tokens[i+1] == max_token:
                    tokens[i] = max_token
                    if i == (len(tokens) - 2):
                        tokens = tokens[:i + 1]
                    else:
                        tokens = tokens[:i+1] + tokens[i+2:]



    return tokens


