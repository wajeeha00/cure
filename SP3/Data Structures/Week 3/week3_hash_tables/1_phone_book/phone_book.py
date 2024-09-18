class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def process_queries(queries):
    phone_book = {}
    results = []

    for query in queries:
        if query.type == "add":
            phone_book[query.number] = query.name
        elif query.type == "del":
            if query.number in phone_book:
                del phone_book[query.number]
        elif query.type == "find":
            if query.number in phone_book:
                results.append(phone_book[query.number])
            else:
                results.append("not found")

    return results

def read_queries():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    queries = [Query(line.split()) for line in data[1:n+1]]
    return queries

def write_responses(result):
    import sys
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
