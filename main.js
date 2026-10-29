(function(){
  var items=[].slice.call(document.querySelectorAll('.g-item')),lb=document.getElementById('lb'),img=document.getElementById('lb-img'),
      webp=document.getElementById('lb-webp'),cap=document.getElementById('lb-cap'),cur=0,last=null;
  function show(i){cur=(i+items.length)%items.length;var a=items[cur];webp.srcset=a.dataset.webp;img.src=a.getAttribute('href');img.alt=a.dataset.cap;cap.textContent=a.dataset.cap+'  ('+(cur+1)+' / '+items.length+')';}
  function open(i){last=document.activeElement;show(i);lb.hidden=false;document.body.style.overflow='hidden';lb.querySelector('.lb-close').focus();}
  function close(){lb.hidden=true;document.body.style.overflow='';if(last)last.focus();}
  items.forEach(function(a,i){a.addEventListener('click',function(e){e.preventDefault();open(i);});});
  lb.querySelector('.lb-close').onclick=close;lb.querySelector('.lb-prev').onclick=function(){show(cur-1)};lb.querySelector('.lb-next').onclick=function(){show(cur+1)};
  lb.addEventListener('click',function(e){if(e.target===lb||e.target.tagName==='FIGURE')close();});
  document.addEventListener('keydown',function(e){if(lb.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowLeft')show(cur-1);if(e.key==='ArrowRight')show(cur+1);});
  var sx=null;lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>40)show(cur+(dx<0?1:-1));sx=null;});
})();
document.querySelectorAll('.copy-code').forEach(function(b){b.addEventListener('click',function(){var c=b.dataset.code;(navigator.clipboard?navigator.clipboard.writeText(c):Promise.reject()).then(function(){b.textContent='Copied: '+c},function(){b.textContent='Code: '+c});});});
