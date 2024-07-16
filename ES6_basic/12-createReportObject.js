import createEmployeesObject from './11-createEmployeesObject';

export default function createReportObject(employeesList = createEmployeesObject()) {
  let newObject = {
    allEmployees: employeesList,
  };
  newObject = {
    ...newObject,
    getNumberOfDepartments(employeesList) {
      return Object.entries((employeesList)).length;
    },
  };
  return newObject;
}
