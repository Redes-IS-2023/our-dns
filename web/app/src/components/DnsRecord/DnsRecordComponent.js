import styles from "./DnsRecordComponent.module.css";

import React, { useState, useEffect } from "react";
import JsonEditorComponent from "../JsonEditor/JsonEditorComponent";
import { Button } from "react-bootstrap";

function DnsRecordComponent(props) {
  const [data, setData] = useState({});

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      var endpoint = props.endpointGet;
      if (props.code) endpoint += props.code;
      const response = await fetch(endpoint);
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const updateData = async () => {
    try {
      await fetch(props.endpointPost, {
        method: "POST",
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((json) => console.log(json));
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const editorChanged = (key, value, parent, data) => {
    setData(data);
  };

  return (
    <div className={styles.container}>
      <JsonEditorComponent data={data} onChange={editorChanged} />
      <div className={styles.submit}>
        <Button variant="success" onClick={updateData}>
          Push changes
        </Button>{" "}
        <Button variant="info" onClick={fetchData}>
          Fetch data
        </Button>{" "}
      </div>
    </div>
  );
}

export default DnsRecordComponent;
