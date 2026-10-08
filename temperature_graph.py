from graphics import *

def main(args: list[str]) -> int:

    w: GraphWin = GraphWin('Daily High Temperatures', 800, 800)
    w.setCoords(-1, -10, 8, 110)

    # Source: Open-Meteo Historical Weather API, Spartanburg, SC, accessed Sep. 4, 2026.
    # https://archive-api.open-meteo.com/v1/archive?latitude=34.9496&longitude=-81.9320&start_date=2026-08-28&end_date=2026-09-03&daily=temperature_2m_max&temperature_unit=fahrenheit&timezone=America%2FNew_York

    # Draw the axes with temperature increasing upward.
    x_axis: Line = Line(Point(0, 0), Point(8, 0))
    x_axis.setOutline('black')
    x_axis.draw(w)

    y_axis: Line = Line(Point(0, 0), Point(0, 100))
    y_axis.setOutline('black')
    y_axis.draw(w)

    # Add labels to the temperature axis.
    zero_label: Text = Text(Point(-0.3, 0), '0')
    zero_label.setFill('black')
    zero_label.draw(w)

    twenty_label: Text = Text(Point(-0.3, 20), '20')
    twenty_label.setFill('black')
    twenty_label.draw(w)

    forty_label: Text = Text(Point(-0.3, 40), '40')
    forty_label.setFill('black')
    forty_label.draw(w)

    sixty_label: Text = Text(Point(-0.3, 60), '60')
    sixty_label.setFill('black')
    sixty_label.draw(w)

    eighty_label: Text = Text(Point(-0.3, 80), '80')
    eighty_label.setFill('black')
    eighty_label.draw(w)

    one_hundred_label: Text = Text(Point(-0.4, 100), '100')
    one_hundred_label.setFill('black')
    one_hundred_label.draw(w)

    # Draw the bars for Spartanburg's daily high temperatures in degrees F.
    august_28_bar: Rectangle = Rectangle(Point(0.7, 0), Point(1.3, 87.6))
    august_28_bar.setFill('sky blue')
    august_28_bar.setOutline('sky blue')
    august_28_bar.draw(w)

    august_29_bar: Rectangle = Rectangle(Point(1.7, 0), Point(2.3, 84.7))
    august_29_bar.setFill('sky blue')
    august_29_bar.setOutline('sky blue')
    august_29_bar.draw(w)

    august_30_bar: Rectangle = Rectangle(Point(2.7, 0), Point(3.3, 85.1))
    august_30_bar.setFill('sky blue')
    august_30_bar.setOutline('sky blue')
    august_30_bar.draw(w)

    august_31_bar: Rectangle = Rectangle(Point(3.7, 0), Point(4.3, 89.9))
    august_31_bar.setFill('sky blue')
    august_31_bar.setOutline('sky blue')
    august_31_bar.draw(w)

    september_1_bar: Rectangle = Rectangle(Point(4.7, 0), Point(5.3, 92.9))
    september_1_bar.setFill('sky blue')
    september_1_bar.setOutline('sky blue')
    september_1_bar.draw(w)

    september_2_bar: Rectangle = Rectangle(Point(5.7, 0), Point(6.3, 94.8))
    september_2_bar.setFill('sky blue')
    september_2_bar.setOutline('sky blue')
    september_2_bar.draw(w)

    september_3_bar: Rectangle = Rectangle(Point(6.7, 0), Point(7.3, 94.8))
    september_3_bar.setFill('sky blue')
    september_3_bar.setOutline('sky blue')
    september_3_bar.draw(w)

    # Label every date on the X axis.
    august_28_date: Text = Text(Point(1, -5), 'Aug 28')
    august_28_date.setFill('black')
    august_28_date.draw(w)

    august_29_date: Text = Text(Point(2, -5), 'Aug 29')
    august_29_date.setFill('black')
    august_29_date.draw(w)

    august_30_date: Text = Text(Point(3, -5), 'Aug 30')
    august_30_date.setFill('black')
    august_30_date.draw(w)

    august_31_date: Text = Text(Point(4, -5), 'Aug 31')
    august_31_date.setFill('black')
    august_31_date.draw(w)

    september_1_date: Text = Text(Point(5, -5), 'Sep 1')
    september_1_date.setFill('black')
    september_1_date.draw(w)

    september_2_date: Text = Text(Point(6, -5), 'Sep 2')
    september_2_date.setFill('black')
    september_2_date.draw(w)

    september_3_date: Text = Text(Point(7, -5), 'Sep 3')
    september_3_date.setFill('black')
    september_3_date.draw(w)

    # Label the high temperature for each bar.
    august_28_temperature: Text = Text(Point(1, 90), '87.6 F')
    august_28_temperature.setFill('black')
    august_28_temperature.draw(w)

    august_29_temperature: Text = Text(Point(2, 87), '84.7 F')
    august_29_temperature.setFill('black')
    august_29_temperature.draw(w)

    august_30_temperature: Text = Text(Point(3, 88), '85.1 F')
    august_30_temperature.setFill('black')
    august_30_temperature.draw(w)

    august_31_temperature: Text = Text(Point(4, 92), '89.9 F')
    august_31_temperature.setFill('black')
    august_31_temperature.draw(w)

    september_1_temperature: Text = Text(Point(5, 96), '92.9 F')
    september_1_temperature.setFill('black')
    september_1_temperature.draw(w)

    september_2_temperature: Text = Text(Point(6, 98), '94.8 F')
    september_2_temperature.setFill('black')
    september_2_temperature.draw(w)

    september_3_temperature: Text = Text(Point(7, 98), '94.8 F')
    september_3_temperature.setFill('black')
    september_3_temperature.draw(w)

    # Add a title for the graph.
    graph_title: Text = Text(Point(4, 106), 'Spartanburg, SC Daily High Temperatures')
    graph_title.setFill('black')
    graph_title.setSize(16)
    graph_title.draw(w)

    # Wait for a mouse click and then close the window
    w.getMouse()
    w.close()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
