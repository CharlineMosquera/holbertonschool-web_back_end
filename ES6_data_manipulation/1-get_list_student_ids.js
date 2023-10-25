export default function getListStudentIds(datas) {
  if (typeof datas === 'object' && datas !== null) {
    return datas.map((data) => data.id);
  }
  return [];
}
