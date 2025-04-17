
export function trimToLength(str, length) {
  if (!str) {
    return "";
  }
  if (str.length > length) {
    return str.substring(0, length) + '...';
  }
  return str;
}