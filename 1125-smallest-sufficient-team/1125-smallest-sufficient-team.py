class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}    
        min_people = {0: []}                
        for person_index, person_skills in enumerate(people):
            person_bitmask = 0
            for skill in person_skills:
                if skill in skill_to_index:
                    skill_index = skill_to_index[skill]
                    person_bitmask |= 1 << skill_index
            for team_bitmask, team in list(min_people.items()):
                new_bitmask = team_bitmask | person_bitmask
                if new_bitmask not in min_people or len(min_people[new_bitmask]) > len(team) + 1:
                    min_people[new_bitmask] = team + [person_index]
        return min_people[(1 << len(req_skills)) - 1]
            
            
        