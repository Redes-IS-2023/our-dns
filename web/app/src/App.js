import styles from "./App.module.css";
import DnsRecord from "./components/DnsRecord/DnsRecordComponent";

function App() {
  const host = "http://127.0.0.1:5000/api/";
  const endpointDnsGet = `${host}records/`;
  const endpointDnsPost = `${host}record/`;
  const endpointGlobal = host + "global";

  return (
    <div className={styles.App}>
      <body className={styles.container}>
        <DnsRecord
          endpointGet={endpointDnsGet}
          endpointPost={endpointDnsPost}
        ></DnsRecord>
        <DnsRecord
          endpointGet={endpointGlobal}
          endpointPost={endpointGlobal}
        ></DnsRecord>
      </body>
    </div>
  );
}

export default App;
