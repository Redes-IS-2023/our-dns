import React, { useState } from "react";
import styles from "./App.module.css";
import DnsRecord from "./components/DnsRecord/DnsRecordComponent";

function App() {
  const host = "http://127.0.0.1:5000/api/";
  const endpointDnsGet = `${host}records/`;
  const endpointDnsPost = `${host}record/`;
  const endpointGlobal = host + "global/";

  const [code, setCode] = useState("DE");

  const handleInputChange = (e) => setCode(e.target.value.toUpperCase());

  return (
    <div className={styles.App}>
      <body className={styles.container}>
        <section className={styles.section} style={{ marginTop: 32 }}>
          <DnsRecord
            endpointGet={endpointDnsGet}
            endpointPost={endpointDnsPost}
          ></DnsRecord>
        </section>
        <section className={styles.section}>
          <input
            className={styles.label}
            type="text"
            value={"DE"}
            onChange={handleInputChange}
          ></input>
          <DnsRecord
            endpointGet={endpointGlobal}
            endpointPost={endpointGlobal}
            code={code}
          ></DnsRecord>
        </section>
      </body>
    </div>
  );
}

export default App;
