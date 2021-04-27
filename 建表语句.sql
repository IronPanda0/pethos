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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `animal` */

insert  into `animal`(`animalId`,`animalName`,`age`,`temper`,`breathe`,`heartRate`) values (1,'小王',10,10,10,'10'),(2,'小张',10,10,10,'10'),(3,'小明',10,10,10,'10'),(4,'小孙',10,10,10,'10'),(5,'小李',10,10,10,'10');

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
  `processUrl1` varchar(100) DEFAULT NULL COMMENT '流程图片信息1',
  `processUrl2` varchar(100) DEFAULT NULL COMMENT '流程图片信息2',
  `processUrl3` varchar(100) DEFAULT NULL COMMENT '流程图片信息3',
  `info1` varchar(100) DEFAULT NULL COMMENT '流程简介1',
  `info2` varchar(100) DEFAULT NULL COMMENT '流程简介2',
  `info3` varchar(100) DEFAULT NULL COMMENT '流程简介3',
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `case` */

insert  into `case`(`caseId`,`caseName`,`animalName`,`diseaseName`,`caseInfo`,`videoUrl`,`imageUrl`,`processUrl1`,`processUrl2`,`processUrl3`,`info1`,`info2`,`info3`) values (1,'小李的案例改','小李','犬瘟','111','111','111','111','111','111','111','111','111'),(2,'小明的案例','小明','发热','体温升高','test','testtest',NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table `casemedicine` */

DROP TABLE IF EXISTS `casemedicine`;

CREATE TABLE `casemedicine` (
  `caseMId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例药品ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `medicineId` int(10) unsigned NOT NULL COMMENT '药品ID',
  PRIMARY KEY (`caseMId`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Data for the table `casemedicine` */

insert  into `casemedicine`(`caseMId`,`caseId`,`medicineId`) values (1,21,18),(2,21,18),(3,21,19),(4,1,18),(5,1,18),(6,1,18),(7,1,18),(8,1,18);

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `categoryID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `categoryName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`categoryName`) values (1,'传染病'),(2,'内科病'),(3,'外科病');

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `diseaseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病种ID',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '病种名称',
  `categoryName` varchar(50) NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`diseaseId`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `disease` */

insert  into `disease`(`diseaseId`,`diseaseName`,`categoryName`) values (1,'犬瘟热','传染病'),(2,'细小','传染病'),(3,'发热','内科病'),(4,'咳嗽','内科病'),(5,'呕吐','内科病'),(6,'腹泻','内科病'),(7,'骨折','外科病'),(8,'外伤','外科病');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `feeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '收费ID',
  `caseId` int(10) unsigned NOT NULL COMMENT '病例ID',
  `count` int(10) unsigned NOT NULL COMMENT '全部费用',
  `caseName` varchar(50) NOT NULL COMMENT '病例名称',
  PRIMARY KEY (`feeId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `fee` */

insert  into `fee`(`feeId`,`caseId`,`count`,`caseName`) values (10,21,230,'小李的案例改'),(11,23,100,'小明的案例');

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hospitalId` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `caseName` varchar(50) DEFAULT NULL COMMENT '病例名称',
  `day` int(11) DEFAULT NULL COMMENT '住院天数',
  `pay` int(11) DEFAULT NULL COMMENT '住院费用',
  PRIMARY KEY (`hospitalId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `hospital` */

insert  into `hospital`(`hospitalId`,`caseName`,`day`,`pay`) values (1,'小明的案例',3,100),(2,'小李的案例改',3,200);

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

/*Data for the table `medicine` */

insert  into `medicine`(`medicineId`,`name`,`pay`,`storage`,`intro`,`imgUrl`,`roomName`,`type`) values (17,'最新药品',10,5,'药品简介','test','科室1','药品'),(18,'药品1',10,10,'简介','test','科室2','药品'),(19,'药品2',10,10,'简介','test','科室2','药品'),(20,'药品3',10,10,'简介','test','科室1','药品');

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
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

/*Data for the table `paper` */

/*Table structure for table `paperquestion` */

DROP TABLE IF EXISTS `paperquestion`;

CREATE TABLE `paperquestion` (
  `paperQuestionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试试题ID',
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
  `questionId` int(11) DEFAULT NULL COMMENT '问题ID',
  PRIMARY KEY (`paperQuestionId`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

/*Data for the table `paperquestion` */

/*Table structure for table `question` */

DROP TABLE IF EXISTS `question`;

CREATE TABLE `question` (
  `questionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '问题ID',
  `questionInfo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '题干',
  `answer` int(11) DEFAULT NULL COMMENT '答案',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '所属病种名称',
  `score` int(11) DEFAULT NULL COMMENT '分值',
  `choiceA` varchar(50) DEFAULT NULL COMMENT '选项A',
  `choiceB` varchar(50) DEFAULT NULL COMMENT '选项B',
  `choiceC` varchar(50) DEFAULT NULL COMMENT '选项C',
  `choiceD` varchar(50) DEFAULT NULL COMMENT '选项D',
  PRIMARY KEY (`questionId`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

/*Data for the table `question` */

insert  into `question`(`questionId`,`questionInfo`,`answer`,`diseaseName`,`score`,`choiceA`,`choiceB`,`choiceC`,`choiceD`) values (1,'题目1',1,'狂犬病',5,'选A','选B','选C','选D'),(3,'题干题干',1,'狂犬病',5,'选项','选项','选项','选项'),(4,'题干题干题干',1,'狂犬病',10,'选项','选项','选项','选项'),(5,'题干题干题干题干',1,'狂犬病',10,'选项','选项','选项','选项'),(6,'题干题干题干题干题干',1,'狂犬病',10,'选项','选项','选项','选项'),(7,'感染病题干',1,'感染病',5,'选项',' 选项','选项','选项'),(8,'凑数生成试卷1',1,'狂犬病',5,'选项','选项','选项','选项'),(9,'凑数2',1,'狂犬病',10,'选项','选项','选项','选项'),(10,'凑数3',1,'狂犬病',10,'选项','选项','选项','选项'),(11,'凑数4',1,'狂犬病',10,'选项','选项','选项','选项'),(12,'凑数5',1,'狂犬病',10,'选项','选项','选项','选项'),(13,'凑数6',1,'狂犬病',10,'选项','选项','选项','选项'),(14,'狂犬病第二页',1,'狂犬病',10,'选项','选项','选项','选项'),(15,'狂犬病第二页1',1,'狂犬病',10,'选项','选项','选项','选项'),(16,'狂犬病第二页2',1,'狂犬病',10,'选项','选项','选项','选项'),(17,'狂犬病第二页3',1,'狂犬病',10,'选项','选项','选项','选项'),(18,'狂犬病第二页4',1,'狂犬病',10,'选项','选项','选项','选项'),(19,'狂犬病第二页5',1,'狂犬病',10,'选项','选项','选项','选项'),(23,'测试添加问题',2,'传染病',5,'选项','选项','选项','选项');

/*Table structure for table `room` */

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `roomId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '科室ID',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '介绍',
  `employee` varchar(20) DEFAULT NULL COMMENT '负责人姓名',
  `roomName` varchar(20) DEFAULT NULL COMMENT '科室名称',
  `imgUrl` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '科室图片',
  PRIMARY KEY (`roomId`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

/*Data for the table `room` */

insert  into `room`(`roomId`,`intro`,`employee`,`roomName`,`imgUrl`) values (6,'科室简介啦啦啦','小王','新的科室','pictureTest'),(7,'科室简介','负责人小王','科室2','test'),(8,'科室简介','负责人小王','科室1','test'),(9,'科室简介啦啦啦','小王','新的科室111','pictureTest'),(11,'科室简介','小张','化验科','test');

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `test` */

insert  into `test`(`testId`,`testName`,`paperName`,`beginTime`,`endTime`,`diseaseName`) values (1,'入学考试','入学考试试卷','2021-03-01 08:00:00','2021-03-01 10:00:00','发热'),(2,'期中考试','期中考试试卷','2021-03-01 08:00:00','2021-03-01 10:00:00','犬瘟热'),(3,'期末考试','期末考试试卷','2021-04-01 10:00:00','2021-04-01 12:00:00','犬瘟热');

/*Table structure for table `testpaper` */

DROP TABLE IF EXISTS `testpaper`;

CREATE TABLE `testpaper` (
  `testPaperId` int(11) unsigned NOT NULL AUTO_INCREMENT,
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

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
