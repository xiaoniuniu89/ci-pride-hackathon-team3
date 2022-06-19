from event.models import Event, Donation


def payment_confirmation(pk, amount):
    """ post webhook payment confirmation view """
    # find event and make a donation 
    event = Event.objects.get(pk=pk)
    amount = amount // 100
    Donation.objects.create(total=amount, event=event)
    print('donation created')
    # Order.objects.filter(order_key=data).update(billing_status=True)
    # # find order items and send confirmation email containing links
    # order = Order.objects.get(order_key=data)
    # order_items = OrderItem.objects.filter(order=order)
    # order_items_url = [item.product.pdf.url for item in order_items]
    # subject = 'Your E-biblio books'
    # from_email = settings.EMAIL_HOST_USER
    # to = order.email
    # text_message = f'''
    #     Hi there, {order.full_name}. Your payment with E-biblio was successful.
    #     Here are your books,{"".join(order_items_url)} Enjoy 30% off your next
    #     purchase with the discount code EBIBLIO30.'''
    # html_message = get_template(("email.html")).render({
    #     'order': order,
    #     'order_items': order_items
    # })
    # message = EmailMultiAlternatives(subject, text_message, from_email, [to])
    # message.attach_alternative(html_message, "text/html")
    # message.send()