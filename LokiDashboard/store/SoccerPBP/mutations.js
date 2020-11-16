const soccerStats = {
  Goal: 0,
  GoalAttempt: 0,
  Assist: 0,
  Tackle: 0,
  Foul: 0,
  YellowCard: 0,
  RedCard: 0
};

export default {
  // Modify UPRM Set Scores.
  UPDATE_UPRM_SET(state, entry) {
    state.uprmSets.splice(entry.set - 1, 1, entry.score);
  },

  // Modify opponent Set Scores.
  UPDATE_OPP_SET(state, entry) {
    state.oppSets.splice(entry.set - 1, 1, entry.score);
  },

  // Update current set value.
  UPDATE_CURRENT_SET(state, set) {
    state.currentSet = set;
  },

  // Insert athlete entry into UPRM roster.
  ADD_UPRM_ROSTER(state, athlete) {
    state.uprmRoster.push(athlete);
  },

  // Update athlete entry from UPRM roster.
  UPDATE_UPRM_ROSTER(state, athlete) {
    for (let index in state.uprmRoster) {
      if (state.uprmRoster[index].key == athlete.key) {
        state.uprmRoster.splice(index, 1, athlete);
        break;
      }
    }
  },

  // Remove athlete entry from UPRM roster.
  REMOVE_UPRM_ROSTER(state, key) {
    for (let index in state.uprmRoster) {
      console.log(key);
      if (state.uprmRoster[index].key == key) {
        state.uprmRoster.splice(index, 1);
        break;
      }
    }
  },

  // Insert athlete entry into opponent roster.
  ADD_OPP_ROSTER(state, athlete) {
    state.oppRoster.push(athlete);
  },

  // Update athlete entry from opponent roster.
  UPDATE_OPP_ROSTER(state, athlete) {
    console.log(athlete);
    for (let index in state.oppRoster) {
      if (state.oppRoster[index].key === athlete.key) {
        state.oppRoster.splice(index, 1, athlete);
        break;
      }
    }
  },

  // Remove athlete entry from opponent roster.
  REMOVE_OPP_ROSTER(state, key) {
    for (let index in state.oppRoster) {
      if (state.oppRoster[index].key === key) {
        state.oppRoster.splice(index, 1);
        break;
      }
    }
  },

  // Update game over state.
  SET_GAME_OVER(state, isOver) {
    state.gameOver = isOver;
  },

  // Update opponent color.
  SET_OPP_COLOR(state, color) {
    state.oppColor = color;
  },

  // Insert game action into actions list.
  ADD_GAME_ACTION(state, action) {
    state.gameActions.unshift(action);
  },

  // Update value of existing action.
  UPDATE_GAME_ACTION(state, action) {
    for (let index in state.gameActions) {
      if (state.gameActions[index].key === action.key) {
        state.gameActions.splice(index, 1, action);
        break;
      }
    }
  },

  // Remove entry from existing game actions.
  REMOVE_GAME_ACTION(state, key) {
    for (let index in state.gameActions) {
      if (state.gameActions[index].key === key) {
        state.gameActions.splice(index, 1);
        break;
      }
    }
  },

  // Update UPRM team statistics based on the game actions list.
  UPDATE_UPRM_STATISTICS(state) {
    const result = { ...soccerStats };

    // For each game action, update result accordingly.
    state.gameActions.forEach(action => {
      if (action.team == "uprm") {
        result[action.action_type]++;
        if (action.action_type == "Goal") {
          result["GoalAttempt"]++;
        }
      }
    });

    state.uprmStatistics = result;
  },

  // Update opponent team statistics based on the game actions list.
  UPDATE_OPP_STATISTICS(state) {
    const result = { ...soccerStats };

    // For each game action, update result accordingly.
    state.gameActions.forEach(action => {
      if (action.team == "opponent") {
        result[action.action_type]++;
        if (action.action_type == "Goal") {
          result["GoalAttempt"]++;
        }
      }
    });

    state.oppStatistics = result;
  },

  // Update UPRM athlete statistics based on the game actions list.
  UPDATE_UPRM_ATHLETE_STATISTICS(state) {
    const result = {};
    state.uprmRoster.forEach(athlete => {
      result[athlete.key] = {
        name: `${athlete.first_name} ${
          athlete.middle_name ? athlete.middle_name + " " : ""
        }${athlete.last_names}`,
        number: athlete.number,
        ...soccerStats
      };
    });

    // For each game action, update athlete statistics accordingly.

    state.gameActions.forEach(action => {
      if (action.team == "uprm") {
        result[`athlete-${action.athlete_id}`][action.action_type]++;
        if (action.action_type == "Goal") {
          result[`athlete-${action.athlete_id}`]["GoalAttempt"]++;
        }
      }
    });

    state.uprmAthleteStatistics = Object.values(result);
  },

  // Update opponent athlete statistics based on the game actions list.
  UPDATE_OPP_ATHLETE_STATISTICS(state) {
    const result = {};
    state.oppRoster.forEach(athlete => {
      result[athlete.key] = {
        name: athlete.name,
        number: athlete.number,
        ...soccerStats
      };
    });

    // For each game action, update athlete statistics accordingly.
    state.gameActions.forEach(action => {
      if (action.team == "opponent") {
        result[`athlete-${action.athlete_id}`][action.action_type]++;
        if (action.action_type == "Goal") {
          result[`athlete-${action.athlete_id}`]["GoalAttempt"]++;
        }
      }
    });
    state.oppAthleteStatistics = Object.values(result);
  },

  // Set sport_name value.
  SET_SPORT_NAME(state, name) {
    state.sportName = name;
  },

  // Set hasPBP value.
  SET_HAS_PBP(state, value) {
    state.hasPBP = value;
  },

  // Set teamId value.
  SET_TEAM_ID(state, id) {
    state.teamId = id;
  },

  // Set validUPRMRoster value.
  SET_VALID_UPRM_ROSTER(state, roster) {
    state.validUPRMRoster = roster;
  },

  // Set sport branch value.
  SET_BRANCH(state, branch) {
    state.branch = branch;
  },

  // Set opponentName value.
  SET_OPPONENT_NAME(state, name) {
    state.opponentName = name;
  },

  // Clear function to be called before mounting component.
  CLEAR_STATE(state) {
    // Set every state attribute to its default value.
    state.currentSet = 0;
    state.uprmSets = [0, 0, 0, 0, 0];
    state.oppSets = [0, 0, 0, 0, 0];
    state.gameActions = [];
    state.uprmRoster = [];
    state.oppRoster = [];
    state.gameOver = false;
    state.oppColor = "";
    state.uprmStatistics = { ...soccerStats };
    state.oppStatistics = { ...soccerStats };
    state.uprmAthleteStatistics = [];
    state.oppAthleteStatistics = [];
    state.hasPBP = true;
    state.sportName = "";
    state.teamId = 0;
    state.validUPRMRoster = [];
    state.branch = "";
    state.opponentName = "";
  }
};
