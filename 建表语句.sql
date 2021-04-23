/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 8.0.18 : Database - coursedb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`coursedb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `coursedb`;

/*Table structure for table `animal` */

DROP TABLE IF EXISTS `animal`;

CREATE TABLE `animal` (
  `animalId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '宠物ID',
  `animalName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '宠物名称',
  `age` int(11) NOT NULL COMMENT '年龄',
  `temper` double DEFAULT NULL COMMENT '体温',
  `breathe` int(11) DEFAULT NULL COMMENT '呼吸',
  `heartRate` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '心率',
  PRIMARY KEY (`animalId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `animal` */

insert  into `animal`(`animalId`,`animalName`,`age`,`temper`,`breathe`,`heartRate`) values (1,'小王',10,10,10,'10'),(2,'小张',10,10,10,'10'),(3,'小赵',10,10,10,'10'),(4,'小孙',10,10,10,'10'),(5,'小李',10,10,10,'10');

/*Table structure for table `assay` */

DROP TABLE IF EXISTS `assay`;

CREATE TABLE `assay` (
  `assayId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '化验项目ID',
  `name` varchar(50) DEFAULT NULL COMMENT '项目名称',
  `pay` int(11) DEFAULT NULL COMMENT '费用',
  `intro` varchar(50) DEFAULT NULL COMMENT '简介',
  `imgUrl` varchar(100) DEFAULT NULL COMMENT '图片url',
  PRIMARY KEY (`assayId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `assay` */

insert  into `assay`(`assayId`,`name`,`pay`,`intro`,`imgUrl`) values (1,'拍片',10,'项目简介','test'),(2,'验血',10,'项目简介','test');

/*Table structure for table `case` */

DROP TABLE IF EXISTS `case`;

CREATE TABLE `case` (
  `caseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例ID',
  `caseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病例名称',
  `animalName` varchar(20) DEFAULT NULL COMMENT '宠物名称',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病种名称',
  `caseInfo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '文字简介',
  `videoUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '视频信息',
  `imageUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片信息',
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `case` */

insert  into `case`(`caseId`,`caseName`,`animalName`,`diseaseName`,`caseInfo`,`videoUrl`,`imageUrl`) values (21,'小李的案例','小李','炎症','发炎','test','testtest'),(23,'小明的案例','小明','狂犬病','怕水','test','testtest');

/*Table structure for table `caseassay` */

DROP TABLE IF EXISTS `caseassay`;

CREATE TABLE `caseassay` (
  `caseAId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例化验项目ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `assayId` int(10) unsigned NOT NULL COMMENT '化验项目ID',
  PRIMARY KEY (`caseAId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `caseassay` */

/*Table structure for table `casemedicine` */

DROP TABLE IF EXISTS `casemedicine`;

CREATE TABLE `casemedicine` (
  `caseMId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例药品ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `medicineId` int(10) unsigned NOT NULL COMMENT '药品ID',
  PRIMARY KEY (`caseMId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `casemedicine` */

insert  into `casemedicine`(`caseMId`,`caseId`,`medicineId`) values (1,21,18),(2,21,18),(3,21,19);

/*Table structure for table `casevaccine` */

DROP TABLE IF EXISTS `casevaccine`;

CREATE TABLE `casevaccine` (
  `caseVId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例疫苗ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `vaccineId` int(10) unsigned NOT NULL COMMENT '疫苗ID',
  PRIMARY KEY (`caseVId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `casevaccine` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `categoryID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `categoryName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`categoryName`) values (1,'传染病'),(20,'呼吸道疾病');

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `diseaseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病种ID',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '病种名称',
  `categoryName` varchar(50) NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`diseaseId`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `disease` */

insert  into `disease`(`diseaseId`,`diseaseName`,`categoryName`) values (5,'狂犬病1','传染病'),(7,'狂犬病3','传染病'),(8,'狂犬病4','传染病'),(9,'狂犬病5','传染病'),(10,'狂犬病6','传染病'),(11,'狂犬病7','传染病'),(12,'狂犬病8','传染病'),(13,'狂犬病9','传染病'),(14,'狂犬病10','传染病'),(15,'狂犬病11','传染病'),(16,'狂犬病12','传染病'),(17,'胃炎','炎症'),(18,'狂犬病','传染病');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `feeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '收费ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `count` int(10) unsigned NOT NULL COMMENT '全部费用',
  `caseName` varchar(50) NOT NULL COMMENT '病例名称',
  PRIMARY KEY (`feeId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `fee` */

insert  into `fee`(`feeId`,`caseId`,`count`,`caseName`) values (1,21,30,'小李的案例'),(2,23,0,'小明的案例');

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `itemId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物品ID',
  `roomId` int(11) DEFAULT NULL COMMENT '科室ID',
  `itemName` varchar(20) DEFAULT NULL COMMENT '物品名称',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '物品简介',
  `videoUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '视频信息',
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `item` */

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicineId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '药品ID',
  `name` varchar(50) DEFAULT NULL COMMENT '药品名称',
  `pay` int(11) DEFAULT NULL COMMENT '费用',
  `storage` int(11) DEFAULT NULL COMMENT '库存',
  `intro` varchar(50) DEFAULT NULL COMMENT '简介',
  `imgUrl` varchar(50) DEFAULT NULL COMMENT '药品图片',
  `roomName` varchar(50) DEFAULT NULL COMMENT '科室名称',
  `type` varchar(20) DEFAULT NULL COMMENT '药品种类',
  PRIMARY KEY (`medicineId`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `medicine` */

insert  into `medicine`(`medicineId`,`name`,`pay`,`storage`,`intro`,`imgUrl`,`roomName`,`type`) values (17,'疫苗2',10,10,'简介','test','科室1','疫苗'),(18,'药品1',10,10,'简介','test','科室2','药品'),(19,'药品2',10,10,'简介','test','科室2','药品');

/*Table structure for table `medicineroom` */

DROP TABLE IF EXISTS `medicineroom`;

CREATE TABLE `medicineroom` (
  `Id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `medicineId` int(10) unsigned NOT NULL COMMENT '药品ID',
  `roomId` int(10) unsigned NOT NULL COMMENT '科室ID',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `medicineroom` */

insert  into `medicineroom`(`Id`,`medicineId`,`roomId`) values (12,17,8),(13,18,7),(14,19,7);

/*Table structure for table `paper` */

DROP TABLE IF EXISTS `paper`;

CREATE TABLE `paper` (
  `paperId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '试卷ID',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `sum` int(11) DEFAULT NULL COMMENT '试卷总分',
  `num` int(11) DEFAULT NULL COMMENT '试卷题数',
  `diseaseName` varchar(50) DEFAULT NULL COMMENT '所属病种名称',
  PRIMARY KEY (`paperId`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

/*Data for the table `paper` */

insert  into `paper`(`paperId`,`paperName`,`sum`,`num`,`diseaseName`) values (1,'期末考试狂犬病试卷',10,2,'狂犬病'),(2,'入学考试狂犬病试卷',95,NULL,'狂犬病');

/*Table structure for table `paperquestion` */

DROP TABLE IF EXISTS `paperquestion`;

CREATE TABLE `paperquestion` (
  `paperQuestionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试试题ID',
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
  `questionId` int(11) DEFAULT NULL COMMENT '问题ID',
  PRIMARY KEY (`paperQuestionId`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

/*Data for the table `paperquestion` */

insert  into `paperquestion`(`paperQuestionId`,`paperId`,`questionId`) values (1,15,1),(2,15,3),(3,15,4),(4,38,1),(5,38,3),(6,38,4),(7,39,1),(8,39,3),(9,39,4),(10,40,1),(11,40,3),(12,40,4),(13,41,1),(14,41,3),(15,41,4),(16,42,1),(17,42,3),(18,42,4),(19,45,1),(20,45,4),(21,45,3);

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `questionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '问题ID',
  `questionInfo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '题干',
  `answer` int(11) DEFAULT NULL COMMENT '答案',
  `diseaseId` int(11) DEFAULT NULL COMMENT '所属病种ID',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '所属病种名称',
  `score` int(11) DEFAULT NULL COMMENT '分值',
  `choiceA` varchar(50) DEFAULT NULL COMMENT '选项A',
  `choiceB` varchar(50) DEFAULT NULL COMMENT '选项B',
  `choiceC` varchar(50) DEFAULT NULL COMMENT '选项C',
  `choiceD` varchar(50) DEFAULT NULL COMMENT '选项D',
  PRIMARY KEY (`questionId`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

/*Data for the table `question` */

insert  into `question`(`questionId`,`questionInfo`,`answer`,`diseaseId`,`diseaseName`,`score`,`choiceA`,`choiceB`,`choiceC`,`choiceD`) values (1,'题目1',1,1,'狂犬病',5,'选A','选B','选C','选D'),(3,'题干题干',1,NULL,'狂犬病',5,'选项','选项','选项','选项'),(4,'题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(5,'题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(6,'题干题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(7,'感染病题干',1,NULL,'感染病',5,'选项',' 选项','选项','选项'),(8,'凑数生成试卷1',1,NULL,'狂犬病',5,'选项','选项','选项','选项'),(9,'凑数2',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(10,'凑数3',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(11,'凑数4',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(12,'凑数5',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(13,'凑数6',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(14,'狂犬病第二页',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(15,'狂犬病第二页1',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(16,'狂犬病第二页2',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(17,'狂犬病第二页3',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(18,'狂犬病第二页4',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(19,'狂犬病第二页5',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(20,'狂犬病第二页6',1,NULL,'狂犬病',10,'选项','选项','选项','选项');

/*Table structure for table `room` */

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `roomId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '科室ID',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '介绍',
  `employee` varchar(20) DEFAULT NULL COMMENT '负责人姓名',
  `roomName` varchar(20) DEFAULT NULL COMMENT '科室名称',
  `imgUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '科室图片',
  PRIMARY KEY (`roomId`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

/*Data for the table `room` */

insert  into `room`(`roomId`,`intro`,`employee`,`roomName`,`imgUrl`) values (6,'科室简介啦啦啦','小王','新的科室','pictureTest'),(7,'科室简介','负责人小王','科室2','test'),(8,'科室简介','负责人小王','科室1','test'),(9,'科室简介啦啦啦','小王','新的科室111','pictureTest');

/*Table structure for table `task` */

DROP TABLE IF EXISTS `task`;

CREATE TABLE `task` (
  `taskId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '职能ID',
  `taskName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '职能名称',
  `role` int(11) DEFAULT NULL COMMENT '角色',
  PRIMARY KEY (`taskId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `task` */

/*Table structure for table `taskprocess` */

DROP TABLE IF EXISTS `taskprocess`;

CREATE TABLE `taskprocess` (
  `taskProcessId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '职能学习ID',
  `content` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '职能内容',
  `imgUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片信息',
  `taskId` int(11) DEFAULT NULL COMMENT '职能ID',
  `process` int(11) DEFAULT NULL COMMENT '流程阶段，0为begin，1为mid，2为end',
  PRIMARY KEY (`taskProcessId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `taskprocess` */

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `testId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试ID',
  `testName` varchar(50) DEFAULT NULL COMMENT '考试名称',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `beginTime` datetime DEFAULT NULL COMMENT '开始时间',
  `endTime` datetime DEFAULT NULL COMMENT '结束时间',
  `diseaseName` varchar(50) DEFAULT NULL COMMENT '相关病种',
  PRIMARY KEY (`testId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `test` */

insert  into `test`(`testId`,`testName`,`paperName`,`beginTime`,`endTime`,`diseaseName`) values (1,'期末考试','期末考试狂犬病试卷','2021-03-01 08:00:00','2021-03-01 10:00:00','狂犬病'),(2,'入学考试','入学考试狂犬病试卷','2021-03-01 08:00:00','2021-03-01 10:00:00','狂犬病');

/*Table structure for table `testpaper` */

DROP TABLE IF EXISTS `testpaper`;

CREATE TABLE `testpaper` (
  `testPaperId` int(11) NOT NULL AUTO_INCREMENT,
  `testId` int(11) DEFAULT NULL,
  `paperId` int(11) DEFAULT NULL,
  PRIMARY KEY (`testPaperId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `testpaper` */

insert  into `testpaper`(`testPaperId`,`testId`,`paperId`) values (1,1,1),(2,2,2);

/*Table structure for table `testuser` */

DROP TABLE IF EXISTS `testuser`;

CREATE TABLE `testuser` (
  `testUser` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试考生ID',
  `testId` int(11) DEFAULT NULL COMMENT '考试ID',
  `userId` int(11) DEFAULT NULL COMMENT '考试ID',
  PRIMARY KEY (`testUser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `testuser` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `userId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `userName` varchar(20) DEFAULT NULL COMMENT '用户名称',
  `passWord` varchar(20) DEFAULT NULL COMMENT '密码',
  `authority` int(11) DEFAULT NULL COMMENT '权限',
  `age` int(11) DEFAULT NULL COMMENT '年龄',
  `gender` varchar(10) DEFAULT NULL COMMENT '性别',
  `mail` varchar(50) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

/*Table structure for table `userrole` */

DROP TABLE IF EXISTS `userrole`;

CREATE TABLE `userrole` (
  `userRoleId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userName` varchar(20) NOT NULL,
  `role` varchar(20) NOT NULL COMMENT '前台，医助，医师',
  `content` varchar(500) DEFAULT NULL,
  `duty` varchar(500) DEFAULT NULL,
  `process` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`userRoleId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `userrole` */

insert  into `userrole`(`userRoleId`,`userName`,`role`,`content`,`duty`,`process`) values (1,'小王','医师','干活','什么的干活','流程1，2，3'),(5,'小王','前台','干活','什么的干活啦啦啦','流程3,2，1'),(6,'小张','前台','干活','什么的干活啦啦啦','流程3,2，1');

/*Table structure for table `vaccine` */

DROP TABLE IF EXISTS `vaccine`;

CREATE TABLE `vaccine` (
  `vaccineId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '疫苗ID',
  `name` varchar(50) DEFAULT NULL COMMENT '疫苗名称',
  `pay` int(11) DEFAULT NULL COMMENT '费用',
  `storage` int(11) DEFAULT NULL COMMENT '库存',
  `intro` varchar(50) DEFAULT NULL COMMENT '疫苗名称',
  `imgUrl` varchar(100) DEFAULT NULL COMMENT '疫苗图片',
  PRIMARY KEY (`vaccineId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `vaccine` */

insert  into `vaccine`(`vaccineId`,`name`,`pay`,`storage`,`intro`,`imgUrl`) values (1,'狂犬病疫苗',10,5,'药品简介','test');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
