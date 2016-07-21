from system.core.router import routes

routes['default_controller'] = 'Trackr'
routes["POST"]["/signup"] = "Trackr#register"
routes["POST"]["/signin"] = "Trackr#login"
routes["POST"]["/addrecord"] = "Trackr#createRecord"
routes["POST"]["/getall"] = "Trackr#getAllRecords"
routes["POST"]["/delete"] = "Trackr#deleteRecord"
