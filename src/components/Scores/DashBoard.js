import React from "react";
import { Container, Paper, Grid } from "@mui/material";
import ProgressBar from "./ProgressBar";

const DashBoard = () => {
  return (
    <Container>
      <Grid container spacing={2} justifyContent="center">
        <Grid item xs={12} md={6} xl={10} textAlign="center">
          <ProgressBar strokeWidth={10} percentage={70} />
        </Grid>
      </Grid>
      <Grid container>
        <Grid item>
          <Paper style={{ height: 100, width: 50 }}></Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default DashBoard;
