import styles from "./App.module.css";
import DnsRecord from "./components/DnsRecord";

function App() {
  const host = "http://127.0.0.1:5000/api/";
  const endpointDns = `${host}records`;
  const endpointGlobal = host + "global";

  return (
    <div className={styles.App}>
      <body className={styles.container}>
        <DnsRecord endpoint={endpointDns}></DnsRecord>
        <DnsRecord endpoint={endpointGlobal}></DnsRecord>
      </body>
    </div>
  );
}

export default App;
