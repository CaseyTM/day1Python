onClick = this.makePayment

makePayment(){
	console.log("test");
	var handler = window.StripeCheckout.configure({
		key: 'pk_test_mlCpXfDbzXH68AMM0ABqTQ8x',
		locale: 'auto',
		token: function(tokenFromStripe){
			console.log(tokenFromStripe);
			var theData = {
				amount: 10 * 100,
				stripeToken: tokenFromStripe.id,
				token: localStorage.getItem('token')
			}
			$.ajax({
				method: 'POST',
				url: "http://localhost:3000/stripe",
				data: theData
			}).done((data)=>{
				console.log(data);
				// the data will represent the res.json sent to express
			})
		}
	});
	handler.open({
		name:"buy stuff from my auction site",
		description: "Pay for your auction",
		amount: 10 * 100
	});
}