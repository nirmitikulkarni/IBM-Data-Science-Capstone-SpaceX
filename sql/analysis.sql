-- SQLite: load the dataset as table spacex
SELECT LaunchSite,COUNT(*) AS TotalLaunches,SUM(Class) AS SuccessfulLandings,
       ROUND(100.0*AVG(Class),1) AS SuccessRatePct
FROM spacex GROUP BY LaunchSite ORDER BY TotalLaunches DESC;
SELECT Class,COUNT(*) AS Launches,ROUND(AVG(PayloadMass),1) AS AvgPayloadKg,
       MIN(PayloadMass) AS MinPayloadKg,MAX(PayloadMass) AS MaxPayloadKg
FROM spacex GROUP BY Class ORDER BY Class;
SELECT CAST(substr(Date,1,4) AS INTEGER) AS Year,COUNT(*) AS Launches,
       SUM(Class) AS SuccessfulLandings,ROUND(100.0*AVG(Class),1) AS SuccessRatePct
FROM spacex GROUP BY Year ORDER BY Year;
SELECT Orbit,COUNT(*) AS Launches,ROUND(100.0*AVG(Class),1) AS SuccessRatePct
FROM spacex GROUP BY Orbit HAVING COUNT(*)>=3 ORDER BY SuccessRatePct DESC;
SELECT LaunchSite,Class,COUNT(*) AS Records FROM spacex
GROUP BY LaunchSite,Class ORDER BY LaunchSite,Class;
