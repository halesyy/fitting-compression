
import numpy as np

# Load in the test binary data.
test_data = open("test_data.txt", "rb")
test_bytes = bytearray(test_data.read())

# Max.
MAX_BYTE_SIZE = 255 # max(test_bytes)
CHUNK_SIZE = 5 # 100

# Group the byte array into chunks of bytes.
byte_groups = []
for i in range(0, len(test_bytes), CHUNK_SIZE):
   byte_groups.append(test_bytes[i:i+CHUNK_SIZE])

# Work out if there's a pure gradient on this byte array. 
def group_diffs(byte_group: bytearray):
   diffs = []
   for i in range(0, len(byte_group)-1):
      # Future byte - current byte vals.
      diffs.append(byte_group[i+1] - byte_group[i])
   # If all the diffs are the same, then it's a pure gradient.
   return diffs

# Work out if there's a useful number series on this byte array.
def gradient_usefulness(byte_group: bytearray):
   diffs = group_diffs(byte_group)
   # If all the diffs are the same, then it's a pure gradient.
   if len(set(diffs)) == 1:
      return True
   else:
      return False

# rule_37r
def overlay_37r_noise(values):
   next_state = [0] * len(values)
   for i in range(len(values)):
      next_state[i] = values[i-1] ^ values[(i+1) % len(values)]
   return next_state

# Given byte group, will inject noise over top of it.
def forward_noise(byte_group, seed):
   values = list(byte_group) # Bytes -> List
   iterations = 1
   # seed = 42
   # Implement p37.
   prng = [seed]

   # Go through byte group, adding to the prng list.
   for _ in range(len(byte_group) - 1):
      prng.append(overlay_37r_noise(prng)[-1])

   # Apply the cellular automaton
   for _ in range(iterations):
      prng = overlay_37r_noise(prng)
      values = [x ^ y for x, y in zip(values, prng)]
      values = values[1:] + [values[0]]

   return values

# Inject predictable noise to get the data into a noisey form.
def noise(byte_group: bytearray):
   pass

seed = 42

# Work through groups, and attempt ad noise.
for byte_group in byte_groups:
   noise_group = forward_noise(byte_group, seed)
   iters = 0
   while True:
      if gradient_usefulness(noise_group):
         # If there's a gradient, then we can use this.
         print(f"Gradient found at {iters}!")
         break
      else:
         # If there's no gradient, then we need to add noise.
         noise_group = forward_noise(noise_group, seed)
         print(noise_group)
         iters += 1
   exit()
