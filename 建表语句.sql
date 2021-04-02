<<<<<<< HEAD
<<<<<<< HEAD
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
  `heartRate` int(11) DEFAULT NULL COMMENT '心率',
  PRIMARY KEY (`animalId`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Data for the table `animal` */

insert  into `animal`(`animalId`,`animalName`,`age`,`temper`,`breathe`,`heartRate`) values (1,'小王',10,10,10,10),(2,'小张',10,10,10,10);

/*Table structure for table `case` */

DROP TABLE IF EXISTS `case`;

CREATE TABLE `case` (
  `caseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例ID',
  `caseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病例名称',
  `animalName` varchar(20) DEFAULT NULL COMMENT '宠物名称',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病种名称',
  `diseaseinfo` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '文字简介',
  `videoUrl` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '视频信息',
  `imageUrl` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片信息',
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `case` */

insert  into `case`(`caseId`,`caseName`,`animalName`,`diseaseName`,`diseaseinfo`,`videoUrl`,`imageUrl`) values (1,NULL,'小明\n',NULL,'怕水','test\n','test');

/*Table structure for table `caseconsumable` */

DROP TABLE IF EXISTS `caseconsumable`;

CREATE TABLE `caseconsumable` (
  `caseCId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例-收费项目ID',
  `caseId` int(11) DEFAULT NULL COMMENT '病例ID',
  `consumableId` int(11) DEFAULT NULL COMMENT '收费项目ID',
  PRIMARY KEY (`caseCId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `caseconsumable` */

/*Table structure for table `caseexecute` */

DROP TABLE IF EXISTS `caseexecute`;

CREATE TABLE `caseexecute` (
  `caseEId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例-收费项目ID',
  `caseId` int(11) NOT NULL COMMENT '病例ID',
  `executeId` int(11) NOT NULL COMMENT '收费项目ID',
  PRIMARY KEY (`caseEId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `caseexecute` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `categoryID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `categoryName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`categoryName`) values (1,'分类一');

/*Table structure for table `consumables` */

DROP TABLE IF EXISTS `consumables`;

CREATE TABLE `consumables` (
  `consumableId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '收费项目ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目名称',
  `type` int(11) NOT NULL COMMENT '药品1 疫苗2',
  `storage` int(11) NOT NULL COMMENT '库存',
  `pay` int(11) NOT NULL COMMENT '费用',
  PRIMARY KEY (`consumableId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `consumables` */

insert  into `consumables`(`consumableId`,`name`,`type`,`storage`,`pay`) values (1,'新冠疫苗',2,10,10);

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `diseaseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病种ID',
  `categoryId` int(11) DEFAULT NULL COMMENT '分类ID',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '病种名称',
  PRIMARY KEY (`diseaseId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `disease` */

insert  into `disease`(`diseaseId`,`categoryId`,`diseaseName`) values (1,NULL,'狂犬病');

/*Table structure for table `executes` */

DROP TABLE IF EXISTS `executes`;

CREATE TABLE `executes` (
  `executeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '执行类ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目名称',
  `type` int(11) NOT NULL COMMENT '收费种类',
  `pay` int(11) NOT NULL COMMENT '费用',
  PRIMARY KEY (`executeId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `executes` */

insert  into `executes`(`executeId`,`name`,`type`,`pay`) values (1,'X光',2,10);

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `itemId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物品ID',
  `roomId` int(11) DEFAULT NULL COMMENT '科室ID',
  `itemName` varchar(20) DEFAULT NULL COMMENT '物品名称',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '物品简介',
  `videoUrl` varchar(50) DEFAULT NULL COMMENT '视频信息',
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `item` */

/*Table structure for table `paper` */

DROP TABLE IF EXISTS `paper`;

CREATE TABLE `paper` (
  `paperId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '试卷ID',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `sum` int(11) DEFAULT NULL COMMENT '试卷总分',
  `num` int(11) DEFAULT NULL COMMENT '试卷题数',
  `diseaseId` int(11) DEFAULT NULL COMMENT '所属病种ID',
  `deseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '所属病种名称',
  PRIMARY KEY (`paperId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `paper` */

insert  into `paper`(`paperId`,`paperName`,`sum`,`num`,`diseaseId`,`deseaseName`) values (1,'期中考试',10,2,1,'狂犬病');

/*Table structure for table `paperquestion` */

DROP TABLE IF EXISTS `paperquestion`;

CREATE TABLE `paperquestion` (
  `paperQuestionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试试题ID',
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
  `questionId` int(11) DEFAULT NULL COMMENT '问题ID',
  PRIMARY KEY (`paperQuestionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `paperquestion` */

/*Table structure for table `testModule` */

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Data for the table `testModule` */

insert  into `question`(`questionId`,`questionInfo`,`answer`,`diseaseId`,`diseaseName`,`score`,`choiceA`,`choiceB`,`choiceC`,`choiceD`) values (1,'题目1',1,1,'狂犬病',5,'选A','选B','选C','选D'),(2,'题目1',1,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,'题干题干',1,NULL,'狂犬病',NULL,'选项','选项','选项','选项');

/*Table structure for table `room` */

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `roomId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '科室ID',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '介绍',
  `employee` varchar(20) DEFAULT NULL COMMENT '负责人姓名',
  `medicine` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '药品',
  PRIMARY KEY (`roomId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `room` */

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
  `imgUrl` varchar(50) DEFAULT NULL COMMENT '图片信息',
  `taskId` int(11) DEFAULT NULL COMMENT '职能ID',
  `process` int(11) DEFAULT NULL COMMENT '流程阶段，0为begin，1为mid，2为end',
  PRIMARY KEY (`taskProcessId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `taskprocess` */

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `testId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试ID',
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
  `testName` varchar(50) DEFAULT NULL COMMENT '考试名称',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `beginTime` datetime DEFAULT NULL COMMENT '开始时间',
  `endTime` datetime DEFAULT NULL COMMENT '结束时间',
  PRIMARY KEY (`testId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `test` */

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
  `gender` int(11) DEFAULT NULL COMMENT '性别',
  `mail` varchar(50) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
=======
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
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
  `heartRate` int(11) DEFAULT NULL COMMENT '心率',
  PRIMARY KEY (`animalId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `animal` */

insert  into `animal`(`animalId`,`animalName`,`age`,`temper`,`breathe`,`heartRate`) values (1,'小王',10,10,10,10),(2,'小张',10,10,10,10),(3,'小赵',10,10,10,10),(4,'小孙',10,10,10,10),(5,'小李',10,10,10,10);

/*Table structure for table `case` */

DROP TABLE IF EXISTS `case`;

CREATE TABLE `case` (
  `caseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例ID',
  `caseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病例名称',
  `animalName` varchar(20) DEFAULT NULL COMMENT '宠物名称',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '病种名称',
  `diseaseInfo` varchar(500) DEFAULT NULL COMMENT '文字简介',
  `videoUrl` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '视频信息',
  `imageUrl` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '图片信息',
  PRIMARY KEY (`caseId`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `case` */

/*Table structure for table `caseconsumable` */

DROP TABLE IF EXISTS `caseconsumable`;

CREATE TABLE `caseconsumable` (
  `caseCId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例-收费项目ID',
  `caseId` int(11) DEFAULT NULL COMMENT '病例ID',
  `consumableId` int(11) DEFAULT NULL COMMENT '收费项目ID',
  PRIMARY KEY (`caseCId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `caseconsumable` */

/*Table structure for table `caseexecute` */

DROP TABLE IF EXISTS `caseexecute`;

CREATE TABLE `caseexecute` (
  `caseEId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '病例-收费项目ID',
  `caseId` int(11) NOT NULL COMMENT '病例ID',
  `executeId` int(11) NOT NULL COMMENT '收费项目ID',
  PRIMARY KEY (`caseEId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `caseexecute` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `categoryID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `categoryName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`categoryID`)
<<<<<<< HEAD
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`categoryName`) values (19,'分类111');
=======
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

/*Data for the table `category` */

insert  into `category`(`categoryID`,`categoryName`) values (1,'传染病'),(20,'呼吸道疾病');
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

/*Table structure for table `consumables` */

DROP TABLE IF EXISTS `consumables`;

CREATE TABLE `consumables` (
  `consumableId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '收费项目ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目名称',
  `type` int(11) NOT NULL COMMENT '药品1 疫苗2',
  `storage` int(11) NOT NULL COMMENT '库存',
  `pay` int(11) NOT NULL COMMENT '费用',
  PRIMARY KEY (`consumableId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `consumables` */

insert  into `consumables`(`consumableId`,`name`,`type`,`storage`,`pay`) values (1,'新冠疫苗',2,10,10);

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `diseaseId` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '病种ID',
  `diseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '病种名称',
  `categoryName` varchar(50) NOT NULL COMMENT '分类名称',
  PRIMARY KEY (`diseaseId`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `disease` */

/*Table structure for table `executes` */

DROP TABLE IF EXISTS `executes`;

CREATE TABLE `executes` (
  `executeId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '执行类ID',
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '项目名称',
  `type` int(11) NOT NULL COMMENT '收费种类',
  `pay` int(11) NOT NULL COMMENT '费用',
  PRIMARY KEY (`executeId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `executes` */

insert  into `executes`(`executeId`,`name`,`type`,`pay`) values (1,'X光',2,10);

/*Table structure for table `item` */

DROP TABLE IF EXISTS `item`;

CREATE TABLE `item` (
  `itemId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '物品ID',
  `roomId` int(11) DEFAULT NULL COMMENT '科室ID',
  `itemName` varchar(20) DEFAULT NULL COMMENT '物品名称',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '物品简介',
  `videoUrl` varchar(50) DEFAULT NULL COMMENT '视频信息',
  PRIMARY KEY (`itemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `item` */

/*Table structure for table `paper` */

DROP TABLE IF EXISTS `paper`;

CREATE TABLE `paper` (
  `paperId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '试卷ID',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `sum` int(11) DEFAULT NULL COMMENT '试卷总分',
  `num` int(11) DEFAULT NULL COMMENT '试卷题数',
  `diseaseId` int(11) DEFAULT NULL COMMENT '所属病种ID',
<<<<<<< HEAD
  `deseaseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '所属病种名称',
=======
  `diseaseName` varchar(50) DEFAULT NULL COMMENT '所属病种名称',
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
  PRIMARY KEY (`paperId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `paper` */

<<<<<<< HEAD
insert  into `paper`(`paperId`,`paperName`,`sum`,`num`,`diseaseId`,`deseaseName`) values (1,'期中考试',10,2,1,'狂犬病');
=======
insert  into `paper`(`paperId`,`paperName`,`sum`,`num`,`diseaseId`,`diseaseName`) values (1,'期中考试',10,2,1,'狂犬病');
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

/*Table structure for table `paperquestion` */

DROP TABLE IF EXISTS `paperquestion`;

CREATE TABLE `paperquestion` (
  `paperQuestionId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试试题ID',
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
  `questionId` int(11) DEFAULT NULL COMMENT '问题ID',
  PRIMARY KEY (`paperQuestionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `paperquestion` */

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
<<<<<<< HEAD
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `question` */

insert  into `question`(`questionId`,`questionInfo`,`answer`,`diseaseId`,`diseaseName`,`score`,`choiceA`,`choiceB`,`choiceC`,`choiceD`) values (1,'题目1',1,1,'狂犬病',5,'选A','选B','选C','选D'),(2,'题目1',1,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,'题干题干',1,NULL,'狂犬病',NULL,'选项','选项','选项','选项'),(4,'题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(5,'题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(6,'题干题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项');
=======
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

/*Data for the table `question` */

insert  into `question`(`questionId`,`questionInfo`,`answer`,`diseaseId`,`diseaseName`,`score`,`choiceA`,`choiceB`,`choiceC`,`choiceD`) values (1,'题目1',1,1,'狂犬病',5,'选A','选B','选C','选D'),(3,'题干题干',1,NULL,'狂犬病',NULL,'选项','选项','选项','选项'),(4,'题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(5,'题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(6,'题干题干题干题干题干',1,NULL,'狂犬病',10,'选项','选项','选项','选项'),(7,'感染病题干',1,NULL,'感染病',5,'选项',' 选项','选项','选项');
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

/*Table structure for table `room` */

DROP TABLE IF EXISTS `room`;

CREATE TABLE `room` (
  `roomId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '科室ID',
  `intro` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '介绍',
  `employee` varchar(20) DEFAULT NULL COMMENT '负责人姓名',
  `medicine` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '药品',
  PRIMARY KEY (`roomId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `room` */

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
  `imgUrl` varchar(50) DEFAULT NULL COMMENT '图片信息',
  `taskId` int(11) DEFAULT NULL COMMENT '职能ID',
  `process` int(11) DEFAULT NULL COMMENT '流程阶段，0为begin，1为mid，2为end',
  PRIMARY KEY (`taskProcessId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `taskprocess` */

/*Table structure for table `test` */

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `testId` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '考试ID',
<<<<<<< HEAD
  `paperId` int(11) DEFAULT NULL COMMENT '试卷ID',
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
  `testName` varchar(50) DEFAULT NULL COMMENT '考试名称',
  `paperName` varchar(50) DEFAULT NULL COMMENT '试卷名称',
  `beginTime` datetime DEFAULT NULL COMMENT '开始时间',
  `endTime` datetime DEFAULT NULL COMMENT '结束时间',
<<<<<<< HEAD
  PRIMARY KEY (`testId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `test` */

=======
  `diseaseName` varchar(50) DEFAULT NULL COMMENT '相关病种',
  PRIMARY KEY (`testId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `test` */

insert  into `test`(`testId`,`testName`,`paperName`,`beginTime`,`endTime`,`diseaseName`) values (1,'期中考试','期中考试狂犬病试卷','2021-03-01 08:00:00','2021-03-01 10:00:00','狂犬病');

>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
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
  `gender` int(11) DEFAULT NULL COMMENT '性别',
  `mail` varchar(50) DEFAULT NULL COMMENT '邮箱',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
<<<<<<< HEAD
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
