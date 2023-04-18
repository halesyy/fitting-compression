
import numpy as np
import json

# Load in the test binary data.
test_data = open("test_data.txt", "rb")
test_bytes = bytearray(test_data.read())

# Max.
MAX_BYTE_SIZE = 255 # max(test_bytes)
CHUNK_SIZE = 3 # 100

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
      return True, diffs[0]
   else:
      return False, False

# Forward noise movement.
def forward_noise(byte_array, seed):
   prng = np.random.default_rng(seed)
   while True:
      noise = prng.integers(0, 256, size=len(byte_array), dtype=np.uint8)
      byte_array = np.bitwise_xor(byte_array, noise)
      yield byte_array

# Backward noise movement.
def reverse_noise(byte_array, seed, iters=1):
   prng = np.random.default_rng(seed)
   for _ in range(iters):
      noise = prng.integers(0, 256, size=len(byte_array), dtype=np.uint8)
      byte_array = np.bitwise_xor(byte_array, noise)
   return byte_array

# Seed used.
seed = 42

# Add in: 
reversible_data = {
   "seed": seed,
   "iters": [],
   "csize": CHUNK_SIZE
}

# Work through groups, and attempt ad noise.
for byte_group in byte_groups:
   iters = 0
   for noise_group in forward_noise(byte_group, seed):
      # Useful, done.
      useful, gradient = gradient_usefulness(noise_group)
      if useful:
         print(f"Gradient found at {iters}!")
         reversible_data["iters"].append([iters, gradient])
         break
      iters += 1

print(reversible_data)
# print(json.dumps(reversible_data, indent=4))
