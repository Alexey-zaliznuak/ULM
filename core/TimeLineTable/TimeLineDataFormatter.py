import flet.canvas as cv
from peewee import Model

CELL_HEIGHT = 40


class TimeLineDataFormatter():
    def __init__(
            self,
            bookings,
            places
        ) -> list:
        self.bookings = sorted(bookings, key=lambda x: x['start_booking_time'])
        self.places = places

    def time_to_pixels(self, start_booking_time, end_booking_time):
        start = start_booking_time.hour * 60 + start_booking_time.minute
        end = end_booking_time.hour * 60 + end_booking_time.minute - start
        return {
            'start': start,
            'end': end,
        }

    def get_row(self, bookings):
        books = []
        prev_on_top = False

        for i in range(len(bookings)):
            booking = bookings[i]

            start = booking['start_booking_time']
            end = booking['end_booking_time']
            height = CELL_HEIGHT if booking['book_full'] else CELL_HEIGHT / 2

            top = prev_on_top

            if (
                i != 0 and
                start < bookings[i-1]['end_booking_time']
            ):
                top = not top

            floor = CELL_HEIGHT / 2 if top else 0
            prev_on_top = top
            coordinates = self.time_to_pixels(start, end)

            books.append(
                {
                    'start':  coordinates['start'],
                    'end':  coordinates['end'],
                    'floor':  floor,
                    'height':  height,
                }
            )

        return books

    def get_rows(self):
        rows = []
        for place in self.places:
            Book:Model = None
            books = Book.select().where(Book.place == place)
            rows.append(
                { 
                    'data': [*self.get_row(books)], 
                    'name': place.name
                }
            )
        return rows
  