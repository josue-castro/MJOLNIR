// TODO -> Add default team statistics JSON.
const soccerStats = {
  Goal: 0,
  GoalAttempt: 0,
  Assist: 0,
  Tackle: 0,
  Foul: 0,
  YellowCard: 0,
  RedCard: 0
};
export default () => ({
  currentSet: 0, // Current Volleyball game set (1, 2, 3, 4, 5).
  uprmSets: [0, 0, 0, 0, 0], // UPRM set scores.
  oppSets: [0, 0, 0, 0, 0], // Opponent set scores.
  gameActions: [], // List of game actions (notifications and plays...)
  uprmRoster: [], // List of UPRM athletes for this match.
  oppRoster: [], // List of opponent athletes for this match.
  gameOver: false, // Denotes if the game is over.
  oppColor: "", // Keeps track of the opponent team color (for UI purposes).
  uprmStatistics: { ...soccerStats }, // Keep collective UPRM statistics for this match.
  oppStatistics: { ...soccerStats }, // Keep collective opponent statistics for this match.
  uprmAthleteStatistics: [], // For each UPRM athlete, keeps their individual stats for this match.
  oppAthleteStatistics: [], // For each opponent athlete, keeps their individual stats for this match.
  hasPBP: true,
  sportName: "",
  teamId: 0,
  validUPRMRoster: [], // Lists all UPRM athletes for the corresponding event.
  branch: "", // Sport branch (masculino, femenino, exhibición).
  opponentName: "" // Name to be displayed in
});
