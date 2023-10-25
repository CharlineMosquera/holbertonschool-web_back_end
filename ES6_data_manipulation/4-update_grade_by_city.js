import getStudentsByLocation from './2-get_students_by_loc';

export default function updateStudentGradeByCity(datas, city, newGrades) {
  const filterByCity = getStudentsByLocation(datas, city);
  return filterByCity.map((student) => ({
    ...student,
    grade:
      newGrades.filter((gradeInfo) => gradeInfo.studentId === student.id)[0]?.grade || "N/A",
  }));
}
