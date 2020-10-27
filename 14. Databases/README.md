# 14. Databases

## Basic SQL

```sql
SELECT CITY FROM STATION WHERE CODE = '123'
```

Get distinct cities:

```sql
SELECT DISTINCT CITY FROM STATION WHERE CODE = '123'
```

Count number of distinct cities

```sql
SELECT count(DISTINCT CITY) FROM STATION WHERE CODE = '123'
```

Apart from count, there is also `sum`, `avg`, `ceil`, `floor`.

Get the shortest city name and longest city name

```sql
SELECT CITY, LENGTH(CITY) FROM STATION
ORDER BY LENGTH(CITY), CITY asc 
limit 1;

SELECT CITY, LENGTH(CITY) FROM STATION
ORDER BY LENGTH(CITY), CITY desc 
limit 1;

```

Get cities ending with vowels

```sql
SELECT DISTINCT CITY FROM STATION WHERE city REGEXP "[aeiou]$"
```

Select substring of column. The first two characters. 1 means first character, 2 means length. SQL has an index system starting from 1. To get the last ones, use -X.

```sql
SELECT SUBSTR(NAME, 1, 2) FROM TABLE
```

Output a string for each case

```sql
SELECT
    CASE
        WHEN A >= (B + C) OR B >= (A + C) OR C >= (A + B) THEN 'Not A Triangle'
        WHEN A = B AND A = C THEN 'Equilateral'
        WHEN A = B OR B = C OR A = C THEN 'Isosceles'
        ELSE 'Scalene'
    END
FROM TRIANGLES;
```

Get the list of top earning employees, and the number of employees that earn this amount

```sql
SELECT earnings, count(*) FROM Employee
GROUP BY earnings
ORDER BY earnings desc
limit 1;
```

```sql
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) 
FROM CITY INNER JOIN COUNTRY 
ON CITY.CountryCode=COUNTRY.Code
GROUP BY COUNTRY.Continent;
```

## Book SQL

```sql
SELECT CourseName, TeacherName FROM Courses, Teachers WHERE Courses.TeacherID = Teachers.TeacherID
```

Normalized databases are designed to minimize redundancy, while denormalized databases are designed to optimize read time. We can denormalize the databases by storing redundant data and avoid doing many joins.

As an example, we have this database. * indicates a primary key.

```sql
Courses: CourseID*, CourseName, TeacherID
Teachers: TeacherID*, TeacherName
Students: StudentID*, StudentName
StudentCourses: CourseID*, StudentID*
```

### Query 1: student enrollment

> Get a list of all students and how many courses each student is enrolled in

```sql
SELECT StudentName, Students.StudentID, count(StudentCourses.CourseID) as [Cnt]
FROM Students LEFT JOIN StudentCourses
ON Students.StudentID = StudentCourses.StudentID
GROUP BY Students.StudentID, Students.StudentName
```

For reasons and incorrect implementations and their justification, see chaper 14 in book.

### Query 2: Teacher class size

> Get a list of all teachers and how many students they teach. If a teacher teaches the same student in two courses, double count the student. Sort the list in descending order of the number of students a teacher teaches

```sql
SELECT TeacherName, isnull(StudentSize.Number, 0)
FROM Teachers LEFT JOIN 
    (SELECT TeacherID, count(StudentCourses.CourseID) AS [Number]
    FROM Courses INNER JOIN StudentCourses
    ON Courses.CourseID = StudentCourses.CourseID
    GROUP BY Courses.TeacherID) StudentSize
ON Teachers.TeacherID = StudentSize.TeacherID
ORDER BY StudentSize.Number DESC
```

## Small database design

How to design a small database

1. Handle ambiguity: understand exactly what you need to design, consult with the interviewer
2. Define the core objects: typically each core object translates into a table
3. Analyze relationships: how tables are connected to each other
4. Investigate actions: walk through the common actions that will be taken and understand how to store and retrieve the relevant data.

## Large database design

When designing a large, scalable database, joins are generally very slow. You must *denormalize* your data. Duplicate the relevant data in many tables.

