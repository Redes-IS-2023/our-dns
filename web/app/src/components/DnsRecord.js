import styles from "./DnsRecord.module.css";

import React, { useState, useEffect } from "react";
import JsonEditor from "./JsonEditor";
import { Button } from "react-bootstrap";

function DnsRecord(props) {
  const [data, setData] = useState({});

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch(props.endpoint);
      const data = await response.json();
      setData(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const updateData = async () => {
    try {
      //const response = await push("http://127.0.0.1:5000/api/records");
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div className={styles.container}>
      <JsonEditor data={data}></JsonEditor>
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

export default DnsRecord;
