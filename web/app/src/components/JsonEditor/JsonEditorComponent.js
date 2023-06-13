import { JSONEditor } from "react-json-editor-viewer";
import styles from "./JsonEditor.module.css";

function JsonEditorComponent(props) {
  return (
    <div className={styles.container}>
      <JSONEditor data={props.data} onChange={props.onChange} />
    </div>
  );
}

export default JsonEditorComponent;
