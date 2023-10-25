export default function cleanSet(set, startString) {
  let string = '';

  if (!set || !startString || typeof (startString) !== 'string') return '';

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      string += `${item.slice(startString.length)}-`;
    }
  }
  return string.slice(0, -1);
}
