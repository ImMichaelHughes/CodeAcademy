weight = 7

# Ground Shipping

if weight <= 2:
  priceGround = (1.5 * weight) + 20
elif weight <= 6:
  priceGround = (3 * weight) + 20
elif weight <= 10:
  priceGround = (4 * weight) + 20
else:
  priceGround = (4.75 * weight) + 20

print("Ground Shipping for", weight, "pound package $", priceGround)

# Premium Shipping

priceGroundPrem = 125

print("Premium shipping for", weight, "pound package $", priceGroundPrem)

# Drone Shipping

if weight <= 2:
  priceDrone = (4.5 * weight)
elif weight <= 6:
  priceDrone = (9 * weight)
elif weight <= 10:
  priceDrone = (12 * weight)
else:
  priceDrone = (14.25 * weight)

print("Drone Shipping for", weight, "pound package $", priceDrone)