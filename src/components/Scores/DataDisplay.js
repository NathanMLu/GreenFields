import React, { useEffect, useState } from "react";
import { Grid, Box } from "@mui/material";
import YardOutlinedIcon from "@mui/icons-material/YardOutlined";
import useHttp from "../hooks/use-HTTP";
const DataDisplay = () => {
  const { tempLoading, tempError, sendRequest: getTempData } = useHttp();
  const [tempState, setTemp] = useState(null);
  const [dampState, setDamp] = useState(null);
  useEffect(() => {
    const transformData = (tempData) => {
      setTemp(tempData["temp"]);

      setDamp(tempData["dampness"]);
    };
    getTempData({ url: "/data" }, transformData);
  }, [getTempData]);

  return (
    <Grid container textAlign="center" justifyContent="center">
      <h1>Plant Info</h1>
      <Box component="span" sx={{ display: "flex", alignItems: "center" }}>
        <YardOutlinedIcon fontSize="large" />
      </Box>

      <Grid container justifyContent="center">
        <Grid item>Temperature</Grid>
        <Grid item>{tempState}</Grid>
      </Grid>
      <Grid container justifyContent="center">
        <Grid item>Dampness</Grid>
        <Grid item>{dampState}</Grid>
      </Grid>
    </Grid>
  );
};

export default DataDisplay;
