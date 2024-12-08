# filename: write_summary.py

summary = """
In the year's grand symphony of business performance, Anthropic played a symphony that hit all the right notes. Their product suite introduced the virtuoso "Claude 3.5" with its impressive 200K token context window, and then echoed it through the 'Enterprise Plan' featuring a mammoth 500K context window and top-tier security. The curtains lifted on the 'Prompt Caching' feature, promising cost benefits and a performance boost for the audience. The company also showcased their technological brilliance by announcing the 'Computer Use' Feature for automating complex tasks, and tuning up 'Haiku' and 'Sonnet' for better performances. The audience responded in kind, with vague, but positive signs of growth in both revenue and user base. Anthropic's service also hit a crescendo, gaining high applause on improved performance and reliability stats. All an encore to an already exceptional year.
"""

with open('Anthropic_summary.txt', 'w') as f:
    f.write(summary)

print("Company summary saved to 'Anthropic_summary.txt'")