class School:
  def __init__(self,name,level,numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = int(numberOfStudents)

  def get_name(self):
    return self.name
  def get_level(self):
    return self.level
  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self,newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."

# a = School("Tor Bridge", "High", 1400)
# print(a.get_name())
# print(a.get_level())
# a.set_numberOfStudents(200)
# print(a.get_numberOfStudents())
# print(a.__repr__())

class PrimarySchool(School):
  def __init__(self,name,numberOfStudents,pickupPolicy):
    super().__init__(name,"Primary",numberOfStudents)
    self.pickupPolicy = pickupPolicy
  def get_pickupPolicy(self):
    return self.pickupPolicy
  def __repr__(self):
    school_repr = super().__repr__()
    return f"{school_repr} The pickup policy is {self.pickupPolicy}."

b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
# print(b.get_pickupPolicy())
print(b)

class HighSchool(School):
  def __init__(self,name,numberOfStudents,sportsTeams):
    super().__init__(name,"High",numberOfStudents)
    self.sportsTeams = sportsTeams
  def get_sportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    school_repr = super().__repr__()
    return f"{school_repr} The sports teams are {self.sportsTeams}."

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
# print(c.get_sportsTeams())
print(c)
