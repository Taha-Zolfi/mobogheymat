import React, { useState, useEffect } from 'react';
import './fpage.css'
import logo from '../../assets/logo.png'

const Fpage = () => {

return (
<div className='fpage'> 
    <img src={logo}/>
    <div className='texts'>
    <h1>قیمت روز موبایل</h1>
    <p>نکته : تمامی قیمت ها از <a href="https://torob.com">سایت ترب</a> کراول شده و صرفا این سایت پروژه ای برای رزومه است . <a href="https://eloquent-ramanujan-aplcwxfu9.iran.liara.run/">ارتباط با برنامه نویس</a> </p>
    <p>اگر قیمت ها برای شما نمایش داده نشد قندشکن خودتونو خاموش کنید و رفرش کنید</p>
    </div>
</div> 

  );
}

export default Fpage;