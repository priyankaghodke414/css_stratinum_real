$("#container").PageScroll({
		selectors : {
			sections : ".sections",
			section : ".section",
			insection : ".insection",
			page : ".pages",
			active : ".active",
			controlPrev : ".control-prev",
			controlNext : ".control-next"
		},
		index : 0,
		easing : "ease",
		duration : 500,
		loop : false,
		pagination : true,
		keyboard :true,
		direction : "vertical",
		callback : ""
	});