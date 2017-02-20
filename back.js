// backend
// will need to npm install stripe on the back end
router.post('/stripe', (req, res, next)=>{
	res.json(req.body);
});
