export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberofDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
}
