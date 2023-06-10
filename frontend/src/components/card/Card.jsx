import React, { useState, useEffect } from 'react';
import './card.css';
import q0 from '../../assets/q0.png';
import q1 from '../../assets/q1.png';
import q2 from '../../assets/q2.png';
import q3 from '../../assets/q3.png';
import q4 from '../../assets/q4.png';
import q5 from '../../assets/q5.png';
import q6 from '../../assets/q6.png';
import q7 from '../../assets/q7.png';
import q8 from '../../assets/q8.png';
import q9 from '../../assets/q9.png';
import q10 from '../../assets/q10.png';
import q11 from '../../assets/q11.png';
import { motion } from 'framer-motion';

const Card = (props) => {
const { id } = props;
const [data, setData] = useState(null);

useEffect(() => {
fetch('http://localhost:8000')
.then(response => response.json())
.then(data => setData(data));
}, []);

const images = [q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11];

if (!data) {
return (
<motion.div 
className='notcard'
initial={{ opacity: 0, y: 50 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.5, delay: id * 0.1 }}>
<img src={images[id]} />
<h2>درحال بارگزاری</h2>
</motion.div>
);
}

const item = data[id];

return (
<motion.div
className='card'
initial={{ opacity: 0, y: 50 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 0.5, delay: id * 0.1 }}
>
<img src={images[id]} />
<h2>{item.name}</h2>
<p>تومان {item.price}</p>

<a href={item.link}>
<div className='link'>خـــریــــد</div>
</a>
</motion.div>
);
};

export default Card;