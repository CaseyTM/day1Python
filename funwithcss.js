var html = "";
$(document).ready(()=>{
	for(let i = 0; i < 6000; i++){
		if(i % 2 == 0){
			html += '<div class="tile2"></div>';
		}else
			html += '<div class="tile"></div>';
	}
	$('#wrapper').html(html)
});
