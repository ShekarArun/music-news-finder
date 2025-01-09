import os
from exa_py import Exa
from datetime import datetime

EXA_API_KEY = os.getenv("EXA_API_KEY")
if not EXA_API_KEY:
    raise ValueError("EXA_API_KEY is not set")

exa = Exa(api_key=EXA_API_KEY)

# Get search query from user
search_query = input("Enter your search query: ")

result = exa.search_and_contents(
    search_query,
    type="auto",
    category="news",
    use_autoprompt=True,
    num_results=5,
    text=True,
)

# Create timestamp and filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_dir = "out"
# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f"search_results_{timestamp}.txt")

# Write results to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Search Query: {search_query}\n")
    f.write(f"Timestamp: {timestamp}\n\n")
    f.write(str(result))

print(f"Results have been saved to {output_file}")
