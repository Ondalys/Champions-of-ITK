export default {
  decisionTable: [
    {
      name: "start",
      decisions: [
        { description: "Walk towards the town", targetName: "walkToTown" },
        {
          description: "Walk towards the goblin",
          targetName: "walkToGoblin"
        }
      ]
    },
    {
      name: "death",
      decisions: [{ description: "Play again?", targetName: "start" }]
    },
    {
      name: "goblinEncounter",
      decisions: [
        { description: "Fight the goblin", targetName: "fightGoblin" },
        {
          description: "Talk to the goblin",
          targetName: "talkToGoblin"
        }
      ]
    }
  ],
  outcomeTable: [
    {
      name: "walkToTown",
      outcomes: [
        {
          targetName: "death",
          description: "A rock fell on you"
        }
      ]
    },
    {
      name: "walkToGoblin",
      outcomes: [
        {
          targetName: "death",
          description: "You rock fell on you and you"
        },
        {
          targetName: "goblinEncounter",
          description: "You arrive at the goblin"
        }
      ]
    },
    {
      name: "fightGoblin",
      outcomes: [
        {
          targetName: "death",
          description: "The goblin killed you"
        }
      ]
    },
    {
      name: "talkToGoblin",
      outcomes: [
        {
          targetName: "death",
          description: "The goblin killed you"
        }
      ]
    }
  ]
};
