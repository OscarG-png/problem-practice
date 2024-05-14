function packageSort(
  width: number,
  height: number,
  length: number,
  mass: number
): string {
  const volume = width * height * length;
  const bulky =
    width >= 150 || height >= 150 || length >= 150 || volume >= 1000000;

  if (bulky && mass >= 20) {
    return "REJECTED";
  } else if (bulky || mass >= 20) {
    return "SPECIAL";
  } else {
    return "STANDARD";
  }
}
