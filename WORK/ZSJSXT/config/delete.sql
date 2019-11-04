DELETE tbTotalScore where PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')
DELETE tbDTScoreDetail where DTScoreID IN(SELECT tbDTScore.DTScoreID FROM tbDTScore where PersonnelID IN (SELECT tbDTScore.PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%'))
DELETE tbDTScore where PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')
DELETE tbSJScore WHERE PersonnelID IN (SELECT PersonnelID from tbSigTeamPersonnel where TrueName like '%tsh_%')
DELETE tbKCPersonnel WHERE PersonnelID IN(SELECT PersonnelID FROM tbSigTeamPersonnel where IsAccount=1 and TrueName LIKE'%tsh_%')
DELETE tbSigTeamPersonnel where TrueName like '%tsh_%'
DELETE tbSigTeam where TeamName LIKE '%tsh团队_%'
DELETE tbSigSchool where SchoolName LIKE '%tsh院校_%'
DELETE tbKC where KCTitle='tsh考场'