export default function getStudentsByLocation(datas, city) {
  if (datas && city && typeof datas === 'object') {
    return datas.filter((data) => data.location === city);
  }
  return [];
}
