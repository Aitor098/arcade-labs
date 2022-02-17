import arcade
arcade.open_window(800, 600, "Mi dibujo")

arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

#farito
arcade.draw_circle_filled(375,250,30, arcade.color.YELLOW)
arcade.draw_circle_filled(45,250,30, arcade.color.YELLOW)

#chasis coche
arcade.draw_lrtb_rectangle_filled(30, 380, 300, 170, arcade.color.RED)

#La calzada
arcade.draw_rectangle_filled(400,110,800,100, arcade.color.GRAY)

#El coche
arcade.draw_circle_filled(100, 170,50, arcade.color.BLACK)
arcade.draw_circle_filled(300, 170,50, arcade.color.BLACK)
arcade.draw_rectangle_filled(195, 350, 260,110, arcade.color.RED)
arcade.draw_rectangle_filled(195, 350, 230,100, arcade.color.PAPAYA_WHIP)

#Conductor
arcade.draw_circle_filled(260, 350, 23,arcade.color.BLACK)
arcade.draw_rectangle_filled(260, 325, 12, 50, arcade.color.BLACK)

#lineas discontinuas de suelo
arcade.draw_rectangle_filled(400,110,150,20,arcade.color.WHITE)
arcade.draw_rectangle_filled(200,110,150,20,arcade.color.WHITE)
arcade.draw_rectangle_filled(600,110,150,20,arcade.color.WHITE)
arcade.draw_rectangle_filled(800,110,150,20,arcade.color.WHITE)
arcade.draw_rectangle_filled(0,110,150,20,arcade.color.WHITE)

#SOl
arcade.draw_circle_filled(700,500,70, arcade.color.YELLOW)

#Nube
arcade.draw_rectangle_filled(420, 500, 290, 30, arcade.color.WHITE)
arcade.draw_circle_filled(300,520,35,arcade.color.WHITE)
arcade.draw_circle_filled(360,540,40,arcade.color.WHITE)
arcade.draw_circle_filled(420,540,40,arcade.color.WHITE)
arcade.draw_circle_filled(480,540,40,arcade.color.WHITE)
arcade.draw_circle_filled(540,520,35,arcade.color.WHITE)






arcade.finish_render()

arcade.run()