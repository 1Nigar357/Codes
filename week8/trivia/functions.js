var count = 0;
function error(color, order)
{
    document.getElementsByTagName("button")[order].style.backgroundColor = color;

    if (color === 'red')
    {
        document.getElementById('text').innerHTML = 'Incorrect';
    }
    else
    {
        document.getElementById('text').innerHTML = 'Correct!';
    }
}




function check()
{

        var name = document.querySelector('.name').value.toLowerCase();
	    var input = document.querySelector('.name');

        if (name === 'scratch')
        {
            document.getElementById('text2').innerHTML = 'Correct!';
            input.style.backgroundColor = 'green';
        }
        else
        {
            document.getElementById('text2').innerHTML = 'Incorrect';
            input.style.backgroundColor = 'red';
        }
}

