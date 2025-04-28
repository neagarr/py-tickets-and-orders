from datetime import datetime
from db.models import Order, Ticket, User, MovieSession


def create_order(
        tickets: list,
        username: str,
        date: str=None,
) -> None:

    order = Order.objects.create(
        user_id=User.objects.get(username=username).id
    )

    if date:
        not_str_date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        order.created_at = not_str_date
        order.save()



    for ticket in tickets:
        movie_session = MovieSession.objects.get(
            id=ticket["movie_session"]
        )

        Ticket.objects.create(
            movie_session=movie_session,
            order=order,
            row=ticket["row"],
            seat=ticket.get("seat"),
        )