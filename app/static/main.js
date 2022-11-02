// const bookBtn = document.querySelector('.bookmark-btt');
// const section = document.querySelector('section');
// const label = document.querySelector('label');

// bookBtn.addEventListener('click', function() {
//     section.style.left = 0;
//     label.style.opacity = 0;
// })

// bookBtn.addEventListener('blur', function() {
//     section.style.left = '-200px';
//     label.style.opacity = 1;
// })

//메뉴 상태 변경 버튼을 누르면 .container 상태를 변경하도록 처리
window.addEventListener("load", function(){
    document.querySelector(".toggle1").addEventListener("click", function(){
      document.querySelector(".container1").classList.toggle("collapse1");
    });
  });