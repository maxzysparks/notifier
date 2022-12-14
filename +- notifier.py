def check_price(token: str, threshold: float):
  
  # Query current price of token
  current_price = get_current_price(token)
  
  # Check if current price is above or below threshold
  if current_price >= threshold:
    
    # Send notification that price has increased
    send_notification(f'{token} price has increased!')
  elif current_price <= threshold:
    
    # Send notification that price has decreased
    send_notification(f'{token} price has decreased!')
