import React, { useState } from 'react';
import api from '../../api/api';
import './UOMForm.css';

const UOMForm = () => {
  const [uom_name, setUomName] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!uom_name.trim()) {
        alert('UOM Name is required');
        return;
      }
      await api.post('/insertUOM', { uom_name });
      setUomName('');
    } catch (err) {
      console.error('Error inserting UOM', err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="uom-form">
      <input placeholder="UOM Name" value={uom_name} onChange={e => setUomName(e.target.value)} />
      <button type="submit">Add UOM</button>
    </form>
  );
};

export default UOMForm;