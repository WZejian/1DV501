# computes how many boxes of candles a person needs to buy each year
# for her\his birthday cake

left = 0             # Candle left
needed = 0           # Candle needed
total_candles = 0
boxes = 0            # Number of boxes of candles each year
total_boxes = 0

for i in range(1, 101):   # Birthday between 1 to 100
    needed += 1      # Add 1 candle per year
    total_candles += needed    # Add all candles each year needed
    if left < needed:
        if (needed - left) % 24 != 0:
            boxes = (needed - left)//24 + 1   # 24 candles in one box
        else:
            boxes = (needed - left)//24
        total_boxes = total_boxes + boxes  # Add all boxes each year
        print(f"Before birthday {i}, buy {boxes} boxes")
        left = total_boxes * 24 - total_candles
    else:          # left >= needed
        left = total_boxes * 24 - total_candles
        continue

print("Total number of boxes:", 1 + total_candles//24, ", remaining candles:",
      round(24*(1 + total_candles // 24 - total_candles/24)))
