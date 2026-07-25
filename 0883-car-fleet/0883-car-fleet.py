class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        current_max_time = 0.0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > current_max_time:
                fleets += 1
                current_max_time = time
                
        return fleets