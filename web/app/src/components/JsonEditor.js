import JSONInput from "react-json-editor-ajrm";
import locale from "react-json-editor-ajrm/locale/en";

function JsonEditor(props) {
  return <JSONInput placeholder={props.data} locale={locale} height="500px" />;
}

export default JsonEditor;
