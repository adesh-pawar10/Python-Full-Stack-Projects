import React, { useEffect, useState } from 'react';
import api from '../../api/api';
import './UOMList.css';

const UOMList = () => {
  const [uoms, setUoms] = useState([]);

  const fetchUOMs = async () => {
    try {
      const res = await api.get('/getUOMs');
      setUoms(res.data.data);
    } catch (err) {
      console.error('Error fetching UOMs', err);
    }
  };

  useEffect(() => {
    fetchUOMs();
  }, []);

  const deleteUOM = async (id) => {
    try {
      await api.post('/deleteUOM', { uom_id: id });
      fetchUOMs();
    } catch (err) {
      console.error('Error deleting UOM', err);
    }
  };

  return (
    <div className="uom-list">
      <h2>UOM List</h2>
      <ul>
        {uoms.map(u => (
          <li key={u.uom_id} className="uom-item">
            {u.uom_name}
            <button onClick={() => deleteUOM(u.uom_id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UOMList;