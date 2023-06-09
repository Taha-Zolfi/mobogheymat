import React, { useState, useEffect } from 'react';
import './cards.css'
import Card from '../card/Card';

const Cards = () => {
  const cards = [];
  for (let i = 0; i < 12; i++) {
    cards.push(<Card key={i} id={i} />);
  }
return (
  <div className='con'>
<div className='cards'> 

  {cards}
</div> 
</div>
  );
}

export default Cards;