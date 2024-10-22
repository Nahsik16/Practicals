
def pagerank(links, damp=0.85, iteration=100):
    N = len(links)
    ranks = {page: 1 / N for page in links}  # Initial ranks for all pages
    
    for i in range(iteration):
        new_rank = {}
        for page in links:
            rank_sum = sum(
                ranks[ref_page] / len(links[ref_page])
                for ref_page in links
                if page in links[ref_page]
            )
            # Correct formula
            new_rank[page] = (1 - damp) / N + damp * rank_sum
        
        ranks = new_rank  # Update ranks after each iteration

    return ranks

links = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}

ranks = pagerank(links)
print("PageRank Scores:")
for page, rank in ranks.items():
    print(f"Page {page}: {rank:.4f}")

# def pagerank(links, damp=0.85, iteration=100):

#     N = len(links)
#     ranks = {page: 1 / N for page in links}
#     for i in range(iteration):
#         new_rank = {}
#         for page in links:
#             rank_sum = sum(
#                 ranks[ref_page] / len(links[ref_page])
#                 for ref_page in links
#                 if page in links[ref_page]
#             )
#             # Alternate Rank_sum
#             # for ref_page in links:
#             #     if page in links[ref_page]:
#             #         rank_sum += ranks[ref_page] / len(links[ref_page])
#             new_rank[page] = (1 - damp) / (N + damp * rank_sum)
#         ranks = new_rank
#     return ranks

# links = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": ["C"]}

# ranks = pagerank(links)
# print("PageRank Scores:")
# for page, rank in ranks.items():
#     print(f"Page {page}: {rank:.4f}")

