var newGameObject = "";

function setup() {
  if (newGameObject == "") {
    newGameObject = JSON.stringify(yahtzee);
  }
  document.getElementById('newGame').style.display = 'none';
  document.getElementById('roll').style.display = 'inline-block';
  loadPlayerInfo();
  loadDice();
  loadScorecard();
}

function newGame() {
    yahtzee = JSON.parse(newGameObject);
    setup();
}

function loadPlayerInfo() {
  document.getElementById('playerName').innerHTML = yahtzee.player.name;
  document.getElementById('playerAvatar').src = yahtzee.player.avatar;
}

function loadDice() {
  dieImages = ['question-mark.jpg', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png'];
  yahtzee.dice.forEach(function (die, index) {
    img = document.getElementById('die' + index);
    img.src = dieImages[die.sideUp];
    if (die.saved) {
      img.className = "saved";
    } else {
      img.className = "";
    }
  });
  document.getElementById('throwsRemain').innerHTML = yahtzee.throwsRemainingInTurn;
  document.getElementById('throwsRemainLabel').innerHTML = yahtzee.throwsRemainingInTurn;
  document.getElementById('roll').disabled = (yahtzee.throwsRemainingInTurn <= 0);
}

function loadScorecard() {
  document.getElementById('scoreRows').innerHTML = "";
  yahtzee.scoreCard.forEach(function(scoreCardRow, index) {
    if (scoreCardRow.top) {
      buildScoreCardRow(scoreCardRow.title, scoreCardRow.score, (scoreCardRow.scoreRecorded ? "scored" : "unscored"), !scoreCardRow.scoreRecorded, index);
    }
  });
  buildScoreCardRow("Top Subtotal:", yahtzee.topSubTotal, "totals", false, 0);
  buildScoreCardRow("Top Bonus:", yahtzee.topBonus, "totals", false, 0);
  yahtzee.scoreCard.forEach(function(scoreCardRow, index) {
    if (!scoreCardRow.top) {
      buildScoreCardRow(scoreCardRow.title, scoreCardRow.score, (scoreCardRow.scoreRecorded ? "scored" : "unscored"), !scoreCardRow.scoreRecorded, index);
    }
  });
  buildScoreCardRow("Total Score:", yahtzee.totalScore, "totals", false, 0);
}

function buildScoreCardRow(title, score, columnClassName, clickable, scorecardIndex) {
  tr = document.createElement('tr');
  td1 = document.createElement('td');
  td1.innerHTML = title;
  tr.appendChild(td1);
  td2 = document.createElement('td');
  td2.innerHTML = score;
  td2.className = columnClassName;
  if (clickable) {
    td2.setAttribute('data-scorecardIndex', scorecardIndex);
    td2.onclick = saveScore;
  }
  tr.appendChild(td2);
  document.getElementById('scoreRows').appendChild(tr);
}

function saveScore() {
  if (yahtzee.throwsRemainingInTurn < 3) {
    index = this.getAttribute('data-scorecardIndex');
    yahtzee.scoreCard[index].scoreRecorded = true;
    loadScorecard();
    yahtzee.throwsRemainingInTurn = 3;
    yahtzee.turnsRemaining--;
    yahtzee.dice.forEach(function (die) {
      die.sideUp = 0;
      die.saved = false;
    });
    loadDice();
  }
  if (yahtzee.turnsRemaining === 0) {
    yahtzee.throwsRemainingInTurn = 0;
    document.getElementById('newGame').style.display = 'inline-block';
    document.getElementById('roll').style.display = 'none';
    calculateTotalScore();
    loadScorecard();
  }
}

function rollDice() {
  rerolled = false;
  if (yahtzee.throwsRemainingInTurn > 0) {
    yahtzee.dice.forEach(function (die) {
      if (!die.saved) {
        die.sideUp = Math.floor(Math.random() * 6) + 1;
        rerolled = true;
      }
    });
    if (rerolled)
      yahtzee.throwsRemainingInTurn--;
    loadDice();
    calculateScores();
  }
}

function saveDie(dieIndex) {
  if (yahtzee.throwsRemainingInTurn != 3) {
    yahtzee.dice[dieIndex].saved = !yahtzee.dice[dieIndex].saved;
    loadDice();
  }
}

function calculateScores() {
  yahtzee.scoreCard.forEach(function (scoreCardRow) {
    if (!scoreCardRow.scoreRecorded) {
      if (conditionIsMet(scoreCardRow.scoreCondition)) {
        if (scoreCardRow.scoreMath[0] == 'const') {
          scoreCardRow.score = scoreCardRow.scoreMath[1];
        }
        if (scoreCardRow.scoreMath[0] == 'sum') {
          scoreCardRow.score = sumOfDice(scoreCardRow.scoreMath[1]);
        }
      } else {
          scoreCardRow.score = 0;
      }
    }
  });
  loadScorecard();
}

function sumOfDice(valueToMatch) {
  total = 0;
  yahtzee.dice.forEach(function (die) {
    if (die.sideUp == valueToMatch || valueToMatch === 0) {
      total += die.sideUp;
    }
  })
  return total;
}

function conditionIsMet(condition) {
  if (condition[0] == 'none') {
    return true;
  }
  if (condition[0] == 'ofAKind') {
    return ofAKind(condition[1]);
  }
  if (condition[0] == 'fullHouse') {
    return fullHouse();
  }
  if (condition[0] == 'inARow') {
    return inARow(condition[1]);
  }
  return false;
}

function ofAKind(numberToMatch) {
  values = [0,0,0,0,0,0];
  yahtzee.dice.forEach(function(die) {
    values[die.sideUp-1]++;
  });
  for (i=0; i<values.length; i++)
    if (values[i] >= numberToMatch)
      return true;
  return false;
}

function fullHouse() {
  values = [0,0,0,0,0,0];
  yahtzee.dice.forEach(function(die) {
    values[die.sideUp-1]++;
  });
  return (values.includes(2) && values.includes(3));
}

function inARow(numberToMatch) {
  values = [0,0,0,0,0,0];
  yahtzee.dice.forEach(function(die) {
    values[die.sideUp-1]++;
  });
  consecutive = 0;
  currentStreak = 0;
  for (i=0; i<values.length; i++) {
    if (values[i] !== 0) {
      currentStreak++;
      if (consecutive < currentStreak)
        consecutive = currentStreak;
    } else {
      currentStreak = 0;
    }
  }
  return consecutive >= numberToMatch;
}

function calculateTotalScore() {
  topTotal = 0;
  bottomTotal = 0;
  yahtzee.scoreCard.forEach(function(scoreCardRow) {
    if (scoreCardRow.top)
      topTotal += scoreCardRow.score;
    else
      bottomTotal += scoreCardRow.score;
  });
  yahtzee.topSubTotal = topTotal;
  if (topTotal >= 63)
    yahtzee.topBonus = 35;
  else
    yahtzee.topBonus = 0;
  yahtzee.totalScore = topTotal + bottomTotal + yahtzee.topBonus;
}
