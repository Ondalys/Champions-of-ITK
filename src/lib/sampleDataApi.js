import sampleData from "./sampleData.js";

const { decisionTable, outcomeTable } = sampleData;

const getRandomInt = max => Math.floor(Math.random() * Math.floor(max));

/* This function returns the starting decsions */
const initialize = () =>
  decisionTable.find(entry => entry.name === "start").decisions;

/* From a decsion get a random outcome as well as a set of new decisions */
const getNext = decision => {
  const { outcomes } = outcomeTable.find(
    entry => entry.name === decision.targetName
  );

  const outcome = outcomes[getRandomInt(outcomes.length)];
  const { decisions } = decisionTable.find(
    entry => entry.name === outcome.targetName
  );
  return { outcome: outcome.description, decisions };
};

export { initialize, getNext };
