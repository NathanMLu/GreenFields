import React, { useEffect, useState } from "react";
import { Grid, Box } from "@mui/material";
import YardOutlinedIcon from "@mui/icons-material/YardOutlined";
import useHttp from "../hooks/use-HTTP";
import ProgressBar from "./ProgressBar";
import { margin } from "@mui/system";
import AcUnitOutlinedIcon from "@mui/icons-material/AcUnitOutlined";
import LocalFireDepartmentOutlinedIcon from "@mui/icons-material/LocalFireDepartmentOutlined";
import WhatshotOutlinedIcon from "@mui/icons-material/WhatshotOutlined";
import InsertEmoticonOutlinedIcon from "@mui/icons-material/InsertEmoticonOutlined";
const DataDisplay = () => {
  const { tempLoading, tempError, sendRequest: getTempData } = useHttp();
  const [tempState, setTemp] = useState(null);
  const [dampState, setDamp] = useState(false);
  useEffect(() => {
    const transformData = (tempData) => {
      setTemp(tempData["temp"]);

      setDamp(tempData["dampness"]);
    };
    getTempData({ url: "/data" }, transformData);
  }, [getTempData]);
  let tempColor = "black";
  let tempIcon = null;
  if (tempState > 100) {
    tempColor = "red";
    tempIcon = <LocalFireDepartmentOutlinedIcon />;
  } else if (tempState > 85) {
    tempColor = "orange";
    tempIcon = <WhatshotOutlinedIcon />;
  } else if (tempState > 60) {
    tempColor = "green";
    tempIcon = <InsertEmoticonOutlinedIcon />;
  } else {
    tempColor = "light blue";
    tempIcon = <AcUnitOutlinedIcon />;
  }

  return (
    <Grid container textAlign="center" justifyContent="center">
      <h1>Plant Info </h1>
      <Box
        component="span"
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
        }}
      >
        <YardOutlinedIcon fontSize="large" />
      </Box>

      <Grid container justifyContent="center" spacing={1}>
        <Grid item>
          <h2>Temperature:</h2>
        </Grid>
        <Grid item>
          <h2 style={{ color: tempColor }}>
            {tempState}f {tempIcon}
          </h2>
        </Grid>
      </Grid>
      <Grid container justifyContent="center" spacing={1}>
        <Grid item>
          <h2>Moisture:</h2>
        </Grid>
        <Grid item>
          {dampState ? (
            <h3 style={{ color: "green", marginTop: 25 }}>Healthy</h3>
          ) : (
            <h3 style={{ color: "Red", marginTop: 25 }}>Dry</h3>
          )}
        </Grid>
      </Grid>
    </Grid>
  );
};

export default DataDisplay;
