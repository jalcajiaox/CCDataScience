import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

visits_cart= pd.merge(visits,cart,how="left")


x=len(visits_cart)



cart_null=len(visits_cart[visits_cart.cart_time.isnull()])


y= float(cart_null)/x

print(y)

cart_checkout= pd.merge(cart,checkout,how="left")

print(cart_checkout)

total_checkouts=len(cart_checkout)

leave_checkouts=len(cart_checkout[cart_checkout.checkout_time.isnull()])

percentaje_of_cart_butnotchecks= float(leave_checkouts)/total_checkouts

print(percentaje_of_cart_butnotchecks)

print("\n")
print("step_7")

four_steps_funnel= visits.merge(cart, how="left").merge(checkout,how="left").merge(purchase,how="left")

total_x_steps= len(four_steps_funnel)


not_purchase= len(four_steps_funnel[four_steps_funnel.purchase_time.isnull()])

print(float(not_purchase)/total_x_steps)

four_steps_funnel['time_to_purchase'] = four_steps_funnel.purchase_time - four_steps_funnel.visit_time

print("\n")
print(four_steps_funnel.time_to_purchase)
print("\n")
print(four_steps_funnel.time_to_purchase.mean())