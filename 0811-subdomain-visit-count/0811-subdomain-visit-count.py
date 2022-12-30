class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        track, ans = defaultdict(int), []
        
        for site in cpdomains:
            cur = site.split()
            cur[1] = cur[1].split(".")
            char = ""
            for i in range (len(cur[1]) - 1, -1, -1):
                if char:
                    char = cur[1][i] + "." + char
                else:
                    char =  cur[1][i] + char
                track[char] += int(cur[0])
        
        for item in track.items():
            ans.append(str(item[1]) + " " + item[0])
        return ans    