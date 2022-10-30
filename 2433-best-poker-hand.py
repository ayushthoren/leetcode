class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
      def flush(ranks,suits): return len(set(suits))==1
      def threeOfAKind(ranks,suits): return len([i for i in set(ranks) if ranks.count(i)>=3])>=1
      def pair(ranks,suits): return len([i for i in set(ranks) if ranks.count(i)==2])>=1
      def highCard(ranks,suits): return True
      if flush(ranks,suits): return "Flush"
      if threeOfAKind(ranks,suits): return "Three of a Kind"
      if pair(ranks,suits): return "Pair"
      if highCard(ranks,suits): return "High Card"
