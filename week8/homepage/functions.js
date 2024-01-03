var options = {
    strings: ['Nigar Hajiyeva', '10th-Grade Student', 'CS50 Student'],
    typeSpeed: 110,
    backSpeed: 130,
    loop: true
  };

  var typed = new Typed('.typing1', options);

  // 2nd animation
  var options = {
    strings: ['10th-Grade Student', 'CS50 Student', 'Nigar Hajiyeva'],
    typeSpeed: 110,
    backSpeed: 130,
    loop: true
  };

  var typed = new Typed('.typing2', options);



  // 3rd animation
  var options = {
    strings: [ 'CS50 Student', 'Nigar Hajiyeva', '10th-Grade Student'],
    typeSpeed: 110,
    backSpeed: 130,
    loop: true
  };

  var typed = new Typed('.typing3', options);


function hi()
{
  var name = document.querySelector('#name').value;
  if (name !== "")
  {
    document.getElementById('text').innerHTML = 'Hi ' + name + '!';
    document.getElementById('text2').innerHTML = "<img src=\'https://cliply.co/wp-content/uploads/2019/06/391906110_WAVING_HAND_400px.gif\' width=\'40%\' height=\'auto\'>";
  }
}

function happy()
{
  document.getElementById('text3').innerHTML = "<img src=\'https://netlab-com.ru/assets/img/audit/thump-up.gif\' width=\'30%\' height=\'auto\'>";
}



function sad()
{
  document.getElementById('text3').innerHTML = "<img src=\'images/be-happy.jpg' width=\'40%\' height=\'auto\'>";
}


function changeColor(event)
{
  var color = document.getElementById('input1').value;
  var elements = document.querySelectorAll(".change-color");

  for (let i = 0; i < elements.length; i++)
  {
    if (i < 2)
    {
      elements[i].style.backgroundColor = color;
    }
    else
    {
      elements[i].style.color = color;
    }
  }
}