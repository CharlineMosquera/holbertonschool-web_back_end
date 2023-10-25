export default function getStudentIdsSum(datas) {
  if (datas) {
    return datas.reduce((sum, data) => sum + data.id, 0);
  }
  return 0;
}
