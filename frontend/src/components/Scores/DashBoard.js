import React, { useState, useEffect } from "react";
import { Container, Paper, Grid, Box, Button } from "@mui/material";
import ProgressBar from "./ProgressBar";
import BloodtypeOutlinedIcon from "@mui/icons-material/BloodtypeOutlined";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import useHttp from "../hooks/use-HTTP";
import DataDisplay from "./DataDisplay";
import { useCounter } from "./CountDown";

const DashBoard = (props) => {
  // console.log("Seconds from dash" + seconds);
  const [seconds, setSeconds] = useState();
  const [light, setLight] = useState(false);
  const [water, setWater] = useState(false);
  const [score, setScore] = useState(0);
  const { waterLoading, waterError, sendRequest: sendWater } = useHttp();
  const { lightLoading, lightError, sendRequest: sendLight } = useHttp();
  const { scoreLoading, scoreError, sendRequest: getScore } = useHttp();
  useEffect(() => {
    const transformData = (data) => {
      setScore(data["score"]);
    };
    getScore({ url: "/data" }, transformData);
  }, [getScore]);
  const lightHandler = async (event) => {
    console.log("light button clicked ");
    sendLight({
      url: "/light",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: { lightSet: !light },
    });
    setLight(!light);
  };

  const waterHandler = (event) => {
    setWater(true);

    console.log("water button clicked ");
    sendWater({
      url: "/water",
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: { water: true },
    });
  };
  const lightButtonVariant = light ? "contained" : "outlined";
  return (
    <Container>
      <Paper></Paper>
      <Grid container spacing={2} justifyContent="center">
        <Grid item xs={12} md={6} xl={10} textAlign="center" margin={2}>
          <Paper>
            <Box padding={4}>
              <Grid container spacing={2} justifyContent="center">
                <Grid item>
                  <h1>Score: </h1>
                </Grid>
                <Grid item>
                  <ProgressBar strokeWidth={10} percentage={score} />
                </Grid>
              </Grid>
            </Box>
          </Paper>
        </Grid>
      </Grid>
      <Grid container spacing={1} justifyContent="center">
        <Grid item xs={12} md={6} xl={4} textAlign="center" margin={0}>
          <Paper>
            <Box padding={2}>
              <h1>Interact</h1>
              <Grid container spacing={2} justifyContent="center">
                <Grid item xs={4} md={5} xl={4}>
                  <Button
                    variant="contained"
                    startIcon={<BloodtypeOutlinedIcon />}
                    onClick={waterHandler}
                  >
                    Water
                  </Button>
                </Grid>
                <Grid item xs={4} md={4} xl={4}>
                  <Button
                    variant={lightButtonVariant}
                    startIcon={<LightModeOutlinedIcon />}
                    style={{ backgroundColor: light && "#FFC900" }}
                    onClick={lightHandler}
                  >
                    Light
                  </Button>
                </Grid>
              </Grid>
            </Box>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6} xl={4} textAlign="center" margin={0}>
          <Paper>
            <Box padding={4}>
              <DataDisplay />
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default DashBoard;
