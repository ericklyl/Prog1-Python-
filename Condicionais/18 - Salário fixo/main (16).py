def main():
  sf = int(input())
  vv = int(input())
  #vf = int(input())
  if (1500 >= vv ):
      sl = sf + (0.03*vv)
      print(sl)
  elif (1500 < vv):
      sl = sf + (0.03*1500) + ((vv - 1500)*0.05)
      print(sl)
if __name__ == "__main__":
    main()