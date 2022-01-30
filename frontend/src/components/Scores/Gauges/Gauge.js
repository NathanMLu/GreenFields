import React from "react";
import "./Gauge.css";
const r = 100;
const meter_dimension = r * 2 + 100;
const cf = 2 * Math.PI * r;
const semi_cf = cf / 2;
const semi_cf_1by3 = semi_cf / 3;
const semi_cf_2by3 = semi_cf_1by3 * 2;

const semi_cf_1by6 = semi_cf / 6;
const semi_cf_2by6 = (2 * semi_cf) / 6;
const semi_cf_5by6 = 5 * semi_cf_1by6;
const semi_cf_4by6 = 4 * semi_cf_1by6;

class RefulGauge extends React.Component {
  render() {
    const { percent } = this.props;

    const meter_value = semi_cf - (percent * semi_cf) / 100;

    return (
      <div
        id="wrapper"
        style={{ width: meter_dimension, height: meter_dimension }}
      >
        <svg id="meter">
          <circle
            id="outline_curves"
            class="circle outline"
            cx="50%"
            cy="50%"
            r={r}
            strokeDasharray={semi_cf / 4 + "," + cf}
          />

          <circle
            id="low"
            class="circle range"
            cx="50%"
            cy="50%"
            stroke="#d83043"
            r={r}
            strokeDasharray={semi_cf + "," + cf}
          />

          <circle
            id="avg"
            class="circle range"
            cx="50%"
            cy="50%"
            r={r}
            stroke="#f4a430"
            strokeDasharray={semi_cf_5by6 + "," + cf}
          />

          <circle
            id="high"
            class="circle range"
            cx="50%"
            cy="50%"
            r={r}
            stroke="#0da654"
            strokeDasharray={semi_cf_4by6 + "," + cf}
          />
          <circle
            id="avg2"
            class="circle range"
            cx="50%"
            cy="50%"
            r={r}
            stroke="#f4a430"
            strokeDasharray={semi_cf_2by6 + "," + cf}
          />
          <circle
            id="low-2"
            class="circle range"
            cx="50%"
            cy="50%"
            r={r}
            stroke="#d83043"
            strokeDasharray={semi_cf_1by6 + "," + cf}
          />

          <circle
            id="mask"
            class="circle"
            cx="50%"
            cy="50%"
            r={r}
            strokeDasharray={meter_value + "," + cf}
          />
          <circle
            id="outline_ends"
            class="circle outline"
            cx="50%"
            cy="50%"
            r={r}
            strokeDasharray={2 + "," + (semi_cf - 2)}
          />
        </svg>
        <div id="percentage">{percent}</div>
      </div>
    );
  }
}

export class Gauge extends React.Component {
  render() {
    const percent = this.props.score / this.props.maxScore;
    return (
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <RefulGauge percent={25} />
      </div>
    );
  }
}
