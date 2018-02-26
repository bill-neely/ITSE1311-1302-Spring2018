yahtzee = {
  'turnsRemaining' : 13,
  'throwsRemainingInTurn' : 3,
  'player' : {
    'name' : 'Bill',
    'avatar' : 'avatar.jpeg'
  },
  'dice' : [
    {
      'sideUp' : 0,
      'saved' : false
    },
    {
      'sideUp' : 0,
      'saved' : false
    },
    {
      'sideUp' : 0,
      'saved' : false
    },
    {
      'sideUp' : 0,
      'saved' : false
    },
    {
      'sideUp' : 0,
      'saved' : false
    }
  ],
  'scoreCard' : [
    {
      'title' : 'Ones',
      'top' : true,
      'displaySequence' : 1,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : 'notSureYet',
      'scoreMath' : 'sumOfOnes'
    },
    {
      'title' : 'Twos',
      'top' : true,
      'displaySequence' : 2,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : 'notSureYet',
      'scoreMath' : 'sumofTwos'
    },
    {
      'title' : 'Threes',
      'top' : true,
      'displaySequence' : 3,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : 'notSureYet',
      'scoreMath' : 'sumofThrees'
    },
    {
      'title' : 'Three of a Kind',
      'top' : false,
      'displaySequence' : 7,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : 'notSureYet',
      'scoreMath' : 'sumofDice'
    },
    {
      'title' : 'Four of a Kind',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : 'notSureYet',
      'scoreMath' : 'sumofDice'
    }
  ]
}
