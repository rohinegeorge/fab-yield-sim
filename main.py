import random
import math

class SemiconductorFabSimulation:
    def __init__(self, num_wafers=2500, defect_rate_base=0.015):
        self.num_wafers = num_wafers
        self.defect_rate_base = defect_rate_base
        self.stages = ["Photolithography", "Etching", "Chemical Vapor Deposition", "Ion Implantation", "CMP"]

    def simulate_wafer_pass(self):
        passed_count = 0
        total_yield_sum = 0.0

        for wafer_id in range(1, self.num_wafers + 1):
            defects = 0
            for stage in self.stages:
                if random.random() < self.defect_rate_base:
                    defects += random.randint(1, 4)
            
            die_yield_pct = max(0.0, math.exp(-defects * 0.15) * 100)
            total_yield_sum += die_yield_pct
            
            if die_yield_pct >= 85.0:
                passed_count += 1
                
        avg_yield = total_yield_sum / self.num_wafers
        pass_rate = (passed_count / self.num_wafers) * 100

        print("=== SILICON FAB OPERATIONS REPORT ===")
        print(f"Total Wafers Processed: {self.num_wafers}")
        print(f"Pass Rate (Quality >= 85%): {pass_rate:.2f}%")
        print(f"Average Batch Yield: {avg_yield:.2f}%")

if __name__ == "__main__":
    fab = SemiconductorFabSimulation()
    fab.simulate_wafer_pass()
