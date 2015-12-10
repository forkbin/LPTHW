# --coding: utf-8--


class Scene(object):

    def enter(self):
        print "Subclass this class and override it."
        exit(-1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map= scene_map

    def play(self):
        current_scene, current_scene_name = self.scene_map.open_scene()
        last_scene = self.scene_map.next_scene("mission_success")

        # current scene is not mission success yet
        while len(self.scene_map.missions) != 0:
            print self.scene_map.missions
            next_scene_name, current_scene_name = current_scene.enter()
            if next_scene_name == "death":
                self.scene_map.next_scene("death").enter()

            if next_scene_name != current_scene_name:
                self.scene_map.missions.remove(current_scene_name)

            if next_scene_name == "mission_success" and current_scene_name =="mission_success":
                break;
            if next_scene_name == "mission_success" and len(self.scene_map.missions):
                next_scene_name = self.scene_map.missions.pop()

            current_scene = self.scene_map.next_scene(next_scene_name)

        # mission success
        last_scene.enter()


class ReservoirDam(Scene):

    def enter(self):
        print "Your team came to the reservoir dam, and infiltrate into it."
        print "While you go to the control room, you are detected by the guards."
        print "To accomplish the first mission, you have to kill this 24-person guards."
        print "What would you do next? Shoot or kill them by saber?"

        action = raw_input("> ")

        if action == "shoot":
            print "More reinforcement is coming, you are surround."
            return "death", "reservoir_dam"
        elif action == "kill them by saber":
            print "You have killed the whole guard team."
            print "You should destory the control center and withdrawal as soon as possible."
            return "strategic_arsenal", "reservoir_dam"
        else:
            print "I do not understand what you mean."
            return "reservoir_dam", "reservoir_dam"


class StrategicArsenal(Scene):

    def enter(self):
        print "This mission is pretty difficult. And There are two infantry divisions around it. "
        print "After disscuss with your teamates, you propose two battle-plan."
        print "First, infiltrate into the divisions and eliminate their commander."
        print "Second, trun to the Air Force Command Center, and control their fighter aircraft to bomb the strategic arsenal."
        print "What plan do you choose? First or Second?"

        action = raw_input("> ")

        if action == "First":
            print "All of you are exposured by the armies, and you are killed in 15 minutes."
            print "Your mom would be proud...if she were smarter."
            return "death", "reservoir_dam"
        elif action == "Second":
            print "The idea is great! Good luck to you."
            return "air_force_command_center", "air_force_command_center"
        else:
            print "I do not understand what you mean."
            return "strategic_arsenal", "reservoir_dam"



class AirForceCommandCenter(Scene):

    def enter(self):
        print "You infiltrate in and control the Air Force command center successfully, and what's the target do you want to attack?"
        target = raw_input("> ")
        if target == "strategic arsenal":
            return "mission_success", "mission_success"
        else:
            return "strategic_arsenal", "strategic_arsenal"


class MissionSuccess(Scene):

    def enter(self):
        print "Congratulations! You have completed your mission successfully."
        print "Motherland is proud of you! And people will never forget you!"
        print "Please stay silence and wait for the next command."
        exit(0)


class Death(Scene):

    def enter(self):
        print "Mission failed! You and your teamates died."
        exit(1)


class Map(object):
    scenes = {
        "reservoir_dam": ReservoirDam(),
        "strategic_arsenal": StrategicArsenal(),
        "air_force_command_center": AirForceCommandCenter(),
        "mission_success": MissionSuccess(),
        "death": Death(),
    }

    missions = [
        "reservoir_dam",
        "strategic_arsenal",
        "air_force_command_center",
    ]

    def __init__(self, start_scene):
        self.start_scene = start_scene

    # return corresponding scene object with scene name
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    # start this game from start scene
    def open_scene(self):
        return self.next_scene(self.start_scene), self.start_scene


myMap = Map("reservoir_dam")
myGame = Engine(myMap)
myGame.play()
