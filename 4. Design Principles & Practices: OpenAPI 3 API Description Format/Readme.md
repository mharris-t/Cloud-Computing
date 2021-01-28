# Design Principles & Practices: OpenAPI 3 API Description Format

The task is to create an OpenAPI 3 specification in YAML format that serves basic CRUD (**C**reate, **R**ead, **U**pdate, **D**elete) for course management via HTTP requests.

The specification should be able to process each request and provide the output in JSON format. The paths and schemes required for the specification are described below.

**Schema name: Course**

  Attribute|Type|Conditions
  | ------------- | ------------- | ------------- |
  | id | string | readOnly:true |
  | code | string | readOnly:true - maxlength:10 |
  | name | string | required:true - maxlength:20 |
  | description | string | maxlength:30 |
  | course_type | string | required:true - enum:[compulsory, optional] | 
  | semester | string | required:true - enum:[autumn, spring] |
  | starting_date | string | required:true - format:date-time |
  | ending_date | string | required:true - format:date-time |
  
**Schema name: Courses**

  Attribute|Type|Description
  | ------------- | ------------- | ------------- |
  | [course] | array | An array of courses |
  
**Schema name: Success**

  Attribute|Type|Conditions
  | ------------- | ------------- | ------------- |
  | message | string | - |
  | id | string | - |
  
**Schema name: Error**
  Attribute|Type|Conditions
  | ------------- | ------------- | ------------- |
  | message | string | - | - |
  
**Paths**  

  Request|Type|Route|Request Body|Response Body
  | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Create | POST | /course | Course | Success: {message: ‘Course successfully created’, id: course_id} - Status code: 201 (Created) |
  | READ | GET | /courses | course_type OR semester(*) | Courses: [{Course}, ..] - Status code: 200 \| Error: {message: err} - Status code: 404 (Not Found) |
  | READ | GET | /course or /{course_id} | - | Course: {id: id, code: code, name: name, type: course_type, semester: semester, starting_date: starting_date, ending_date: ending_date} - Status code: 200 \| Error: {message: err} - Status code: 404 (Not Found) |
  | UPDATE | PUT | /course or /{course_id} | Course | Success: {message: ‘Course successfully updated’, id: course_id} - Status code: 200 \| Error: {message: err} - Status code: 404 (Not Found) \| Error: {message: err} - Status code: 422 (Unprocessable entity) |
  | DELETE | DELETE | /course or /{course_id} | - | Status code: 204 (No Content) \| Error: {message: err} - Status code: 404 (Not Found) |
  
  (*) The requestBody in the GET statements will be sent as parameters
