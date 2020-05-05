<template>
    <div>
        <v-expansion-panels>
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Creating A Character
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    Start by determining everything that is your character except the skills and game rules related things.
                    Continue by deciding your characters unique skill, it can be anything but make sure it does not overlap any of the other base skill too much, and remember that the limit to your ability is always decided by the other players in the group.
                    After you’ve made a unique skill for your character continue by rolling a d6 for every skill your character have and write the numbers down. After that choose one skill and add 10 points to it and then another skill and add 5 points to that. Now you have your stats!
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Playing:
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    The purpose of the game is to randomly roll on the database tables and then stuff happens, if a new table is needed create one and if a new entry is needed create one, the group or player that encounters empty entrys on a table makes up what that entry says and writes it down.
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Fighting:
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    The system is designed for inverse d20 mechanics, that means the lower youroll on a d20 the better.
                    When you fight an enemy both the enemy and you roll a d20, the lowest score gets to do damage and the other can try to evade. Remember the rolls because they can matter.
                    Base damage is always 1, any player or enemy that has Strength as a skill can roll a d20 and on success (lower than the skill value) does the difference between the roll and the skill value in extra damage.
                    The character or enemy that has Dexterity as a skill can use it to evade an attack by rolling a d20 and on success (lower than the skill value) the damage is evaded only if the difference between the success value and Dexterity is larger than the difference between the initial d20 values rolled.
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Death:
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    When a character ends up on 0 or lower life total that player makes a save roll. Roll a d20 based on the life skill and on success (lower than the skill value) if the difference on the success value and the life skill is larger than the difference in negative life points that characters life total becomes 1.
                    If a character fails on the save roll they DIE! Shed a tear or something then make a new character or call this game stupid and do something else.
                </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
                <v-expansion-panel-header>
                    Becoming better and other stuff:
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                    The basic rules are provided, every encounter can change that, every character can change permanently in any way depending on what the table says, remember this game works best as some kind of freeform fun.
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
</template>

<script>

export default {
    name: 'RulesDrawer'
}
</script>

<style scoped>
div {
    background-color: #9ecfff;
}
</style>
