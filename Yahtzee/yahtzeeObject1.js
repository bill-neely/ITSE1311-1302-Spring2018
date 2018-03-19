yahtzee = {
  'turnsRemaining' : 13,
  'throwsRemainingInTurn' : 3,
  'topSubTotal' : '',
  'topBonus' : '',
  'totalScore' : '',
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
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 1]
    },
    {
      'title' : 'Twos',
      'top' : true,
      'displaySequence' : 2,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 2]
    },
    {
      'title' : 'Threes',
      'top' : true,
      'displaySequence' : 3,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 3]
    },
    {
      'title' : 'Fours',
      'top' : true,
      'displaySequence' : 3,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 4]
    },
    {
      'title' : 'Fives',
      'top' : true,
      'displaySequence' : 3,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 5]
    },
    {
      'title' : 'Sixes',
      'top' : true,
      'displaySequence' : 3,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 6]
    },
    {
      'title' : 'Three of a Kind',
      'top' : false,
      'displaySequence' : 7,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['ofAKind', 3],
      'scoreMath' : ['sum', 0]
    },
    {
      'title' : 'Four of a Kind',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['ofAKind', 4],
      'scoreMath' : ['sum', 0]
    },
    {
      'title' : 'Full House',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['fullHouse', 2, 3],
      'scoreMath' : ['const', 25]
    },
    {
      'title' : 'Small Straight',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['inARow', 4],
      'scoreMath' : ['const', 30]
    },
    {
      'title' : 'Large Straight',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['inARow', 5],
      'scoreMath' : ['const', 40]
    },
    {
      'title' : 'Chance',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['none'],
      'scoreMath' : ['sum', 0]
    },
    {
      'title' : 'Yahtzee',
      'top' : false,
      'displaySequence' : 8,
      'scoreRecorded' : false,
      'score' : 0,
      'scoreCondition' : ['ofAKind', 5],
      'scoreMath' : ['const', 50]
    }
  ]
}
