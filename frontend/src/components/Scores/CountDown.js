import React from "react";
class ReactTimer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      time: 5,
      timerInProgress: false,
      timerFinished: false,
      animDuration: 0,
    };
    this.handleClick = this.handleClick.bind(this);
    this.setTime = this.setTime.bind(this);
  }

  componentDidMount() {}

  componentWillUnmount() {
    this.stopTimer();
  }

  startTimer() {
    if (this.state.timerInProgress === false) {
      this.setState({
        timerInProgress: true,
        animDuration: this.state.time + "s",
      });

      this.timerID = setInterval(() => this.tick(), 1000);
    }
  }

  stopTimer() {
    clearInterval(this.timerID);
    this.timerID = null;
    this.setState({
      timerInProgress: false,
    });
  }

  tick() {
    if (this.state.time > 0) {
      this.setState({
        time: this.state.time - 1,
        timerFinished: false,
      });
    } else {
      this.setState({
        timerFinished: true,
      });
      this.stopTimer();
    }
  }

  setTime(e) {
    e.preventDefault();
    if (this.state.timerInProgress === false) {
      this.setState({
        time: e.target.value,
      });
    }
  }

  handleClick(e) {
    e.preventDefault();
    this.startTimer();
  }

  render() {
    return (
      <div>
        <form>
          <input type="number" min="1" max="10" onChange={this.setTime} />
          <button onClick={this.handleClick}>Start timer</button>
        </form>
        <div
          className={
            this.state.timerInProgress ? "timer countingDown" : "timer"
          }
        >
          <p>{this.state.time}</p>
          <svg>
            <circle
              r="18"
              cx="20"
              cy="20"
              style={{ animationDuration: this.state.animDuration }}
            ></circle>
          </svg>
        </div>
        <p className={this.state.timerFinished ? "winner" : "notWinner"}>
          Congratulations! You're a winner!
        </p>
      </div>
    );
  }
}
