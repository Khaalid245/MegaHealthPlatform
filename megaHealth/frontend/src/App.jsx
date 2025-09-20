import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/patients/")
      .then(res => setPatients(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Patients</h1>
      <ul>
        {patients.map((p) => (
          <li key={p.id} className="border p-2">{p.name} - {p.age}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
