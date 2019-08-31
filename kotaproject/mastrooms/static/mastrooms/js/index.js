$(document).ready(function()
{
	"use strict";
	/* 1. Vars and Inits */
	var header = $('.header');
	var menuActive = false;
	var menu = $('.menu');
	var burger = $('.hamburger');
	var ctrl = new ScrollMagic.Controller();
	setHeader();
	$(window).on('resize', function()
	{
		setHeader();
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initMenu();
	initMilestones();
	initTabs();
	initColorbox();
	

	/* 2. Set Header */
	function setHeader()
	{
		if($(window).scrollTop() > 100)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/* 3. Init Menu */
	function initMenu()
	{
		if($('.menu').length)
		{
			var menu = $('.menu');
			if($('.hamburger').length)
			{
				burger.on('click', function()
				{
					if(menuActive)
					{
						closeMenu();
					}
					else
					{
						openMenu();

						$(document).one('click', function cls(e)
						{
							if($(e.target).hasClass('menu_mm'))
							{
								$(document).one('click', cls);
							}
							else
							{
								closeMenu();
							}
						});
					}
				});
			}
		}
	}

	function openMenu()
	{
		menu.addClass('active');
		menuActive = true;
	}

	function closeMenu()
	{
		menu.removeClass('active');
		menuActive = false;
	}

	function initMilestones()
	{
		if($('.milestone_counter').length)
		{
			var milestoneItems = $('.milestone_counter');

	    	milestoneItems.each(function(i)
	    	{
	    		var ele = $(this);
	    		var endValue = ele.data('end-value');
	    		var eleValue = ele.text();

	    		/* Use data-sign-before and data-sign-after to add signs
	    		infront or behind the counter number */
	    		var signBefore = "";
	    		var signAfter = "";

	    		if(ele.attr('data-sign-before'))
	    		{
	    			signBefore = ele.attr('data-sign-before');
	    		}

	    		if(ele.attr('data-sign-after'))
	    		{
	    			signAfter = ele.attr('data-sign-after');
	    		}

	    		var milestoneScene = new ScrollMagic.Scene({
		    		triggerElement: this,
		    		triggerHook: 'onEnter',
		    		reverse:false
		    	})
		    	.on('start', function()
		    	{
		    		var counter = {value:eleValue};
		    		var counterTween = TweenMax.to(counter, 4,
		    		{
		    			value: endValue,
		    			roundProps:"value", 
						ease: Circ.easeOut, 
						onUpdate:function()
						{
							document.getElementsByClassName('milestone_counter')[i].innerHTML = signBefore + counter.value + signAfter;
						}
		    		});
		    	})
			    .addTo(ctrl);
	    	});
		}
	}
	function initTabs()
	{
		if($('.tab').length)
		{
			$('.tab').on('click', function()
			{
				$('.tab').removeClass('active');
				$(this).addClass('active');
				var clickedIndex = $('.tab').index(this);

				var panels = $('.tab_panel');
				panels.removeClass('active');
				$(panels[clickedIndex]).addClass('active');
			});
		}
	}
	function initColorbox()
	{
		if($('.gallery_item').length)
		{
			$('.colorbox').colorbox(
			{
				rel:'colorbox',
				photo: true,
				maxWidth: '90%'
			});
		}
	}

}
)
;