/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.5.8-log : Database - exam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`exam` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `exam`;

/*Table structure for table `applications` */

DROP TABLE IF EXISTS `applications`;

CREATE TABLE `applications` (
  `application_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `candidate_id` int(11) DEFAULT NULL,
  `application_date` varchar(100) DEFAULT NULL,
  `qrimage` varchar(500) DEFAULT NULL,
  `application_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`application_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `applications` */

insert  into `applications`(`application_id`,`exam_id`,`candidate_id`,`application_date`,`qrimage`,`application_status`) values (4,10,1,'2022-01-29 13:47:23','static/qrcode/7ddb8199-8d59-4ee3-8f13-b7e9b63ad2e6.png','pending'),(5,10,4,'2022-01-29 14:55:45','static/qrcode/ea195915-7a21-4084-9987-433aba9ee843.png','pending'),(6,10,5,'2022-01-29 15:19:58','static/qrcode/39a69fe5-5340-4dbf-9fda-524dd0a413bc.png','pending');

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `assign_id` int(10) NOT NULL AUTO_INCREMENT,
  `institute_id` int(10) DEFAULT NULL,
  `application_id` int(10) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `assign` */

insert  into `assign`(`assign_id`,`institute_id`,`application_id`,`date`,`status`) values (12,4,1,'2022-01-22','pending'),(13,2,3,'2022-01-22','pending'),(14,7,4,'2022-01-29','pending'),(15,7,5,'2022-01-29','pending'),(16,7,6,'2022-01-29','pending');

/*Table structure for table `block` */

DROP TABLE IF EXISTS `block`;

CREATE TABLE `block` (
  `block_id` int(11) NOT NULL AUTO_INCREMENT,
  `institute_id` int(11) DEFAULT NULL,
  `block_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`block_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `block` */

insert  into `block`(`block_id`,`institute_id`,`block_name`) values (1,1,'block A1'),(2,1,'block B'),(3,4,'block AA'),(4,4,'block AB'),(5,2,'block sngA'),(6,2,'block sngB'),(7,6,'block cha1'),(8,6,'block cha2');

/*Table structure for table `candidates` */

DROP TABLE IF EXISTS `candidates`;

CREATE TABLE `candidates` (
  `candidate_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `house_name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `pincode` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`candidate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `candidates` */

insert  into `candidates`(`candidate_id`,`login_id`,`first_name`,`last_name`,`gender`,`dob`,`house_name`,`place`,`pincode`,`phone`,`email`,`photo`) values (1,16,'anakha','T A','Female','1/1/2000','jkbb','mudikkalayi','685312','8281940635','anu@gmail.com','static/38071e6c-f887-4fab-b45e-ddb79c65ec14abc.jpg'),(2,17,'krishna','k s','Female','29/4/1999','guhf','thamarachal','652833','958428366','krishna@gmail.com','static/cc282d71-3b83-4e43-a3d9-67143496d742abc.jpg'),(3,18,'darsanahhg','prasad','Female','27/11/1999','jjvghhh','vhdhsh','685422','9856324187','darsana@gmail.com','static/f8084597-98d5-4878-aa67-8acc4ebf60ecabc.jpg'),(4,22,'sanchana','sunny','Female','04/11/1998','koodathil ','manakkapady','683511','7034249935','sanchanasunny@gmail.com','static/5dea9290-28b5-4dcb-8b35-0af27fff7e2dabc.jpg'),(5,23,'hsb','vhsb','Female','6/8/200','vshv','vhsb','8468','964854865','ss@gmail.com','static/cc95e9c7-05bb-4346-ab10-06f2ff8cffc2abc.jpg');

/*Table structure for table `classroom` */

DROP TABLE IF EXISTS `classroom`;

CREATE TABLE `classroom` (
  `classroom_id` int(11) NOT NULL AUTO_INCREMENT,
  `block_id` int(11) DEFAULT NULL,
  `class_name` varchar(100) DEFAULT NULL,
  `strength` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`classroom_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `classroom` */

insert  into `classroom`(`classroom_id`,`block_id`,`class_name`,`strength`) values (1,NULL,'s1 bsc maths','26'),(2,2,'s5 bsc botany','20'),(3,3,'S2 MCA','39'),(4,4,'S4 MBA','20'),(5,5,'S6 Btech civil','2'),(6,6,'S5 MCA','25'),(7,8,'s1 bsc it','20'),(8,7,'s6 hm','15'),(9,6,'s1 btsp','10'),(10,7,'s3 bcom ca','10'),(11,8,'s5 bba','20');

/*Table structure for table `exam_institutes` */

DROP TABLE IF EXISTS `exam_institutes`;

CREATE TABLE `exam_institutes` (
  `exam_institute_id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_id` int(11) DEFAULT NULL,
  `institute_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`exam_institute_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `exam_institutes` */

insert  into `exam_institutes`(`exam_institute_id`,`exam_id`,`institute_id`) values (1,1,1),(4,1,2),(6,2,3),(7,3,4),(8,3,1),(9,1,4),(10,3,2),(11,3,3),(12,3,6),(13,2,6),(14,2,4),(15,2,2),(16,5,1),(17,5,3),(18,5,2),(19,6,4),(20,6,6),(21,5,6),(22,7,1),(23,7,3),(24,8,7),(25,8,6),(26,8,4),(27,8,3),(28,8,2),(29,9,7),(30,9,4),(31,10,7),(32,10,6),(33,10,2);

/*Table structure for table `exam_master` */

DROP TABLE IF EXISTS `exam_master`;

CREATE TABLE `exam_master` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `exam_date` varchar(100) DEFAULT NULL,
  `exam_time` varchar(100) DEFAULT NULL,
  `exam_duration` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `no_of_post` varchar(100) DEFAULT NULL,
  `exam_mode` varchar(100) DEFAULT NULL,
  `exam_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `exam_master` */

insert  into `exam_master`(`exam_id`,`title`,`exam_date`,`exam_time`,`exam_duration`,`description`,`no_of_post`,`exam_mode`,`exam_status`) values (1,'aaa','2021-12-28','13:00','1 hr','kksejknwhef','20',NULL,'Hall Tickets Generated'),(2,'bbb','2021-12-27','15:00','2 hrs','yyyy','10',NULL,'Hall Tickets Generated'),(3,'pp','2021-12-29','10:00','1 hr','mmmsdyy','15',NULL,'Hall Tickets Generated'),(4,'ldgkhfn','2022-01-14','13:53','1 hr','wkhdf','5',NULL,'Hall Tickets Generated'),(5,'test','2022-01-21','10:46','1 hr','wrg','6',NULL,'Hall Tickets Generated'),(6,'min','2022-01-28','23:00','1 hr','jSRF','4',NULL,'Hall Tickets Generated'),(7,'yyy','2022-01-21','09:15','1 hr','hghg','20',NULL,'Hall Tickets Generated'),(8,'rr','2022-01-22','10:33','1 hr','srg','20','Online','Hall Tickets Generated'),(9,'qwerty','2022-01-29','17:30','2 hrs','wsgfr','','Offline','Hall Tickets Generated'),(10,'pqrst','2022-01-31','10:00','3 hrs','hgjwgefu','20','Online','Hall Tickets Generated');

/*Table structure for table `facialdetails` */

DROP TABLE IF EXISTS `facialdetails`;

CREATE TABLE `facialdetails` (
  `fdetail_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) DEFAULT NULL,
  `exam_id` int(11) DEFAULT NULL,
  `details` varchar(10000) DEFAULT NULL,
  PRIMARY KEY (`fdetail_id`)
) ENGINE=MyISAM AUTO_INCREMENT=68 DEFAULT CHARSET=latin1;

/*Data for the table `facialdetails` */

insert  into `facialdetails`(`fdetail_id`,`candidate_id`,`exam_id`,`details`) values (65,1,10,'[array([-0.15697195,  0.08120228,  0.07535551, -0.09527653, -0.15319023,\n       -0.01586966, -0.08717355, -0.07632425,  0.09821992, -0.15984547,\n        0.1183337 , -0.05771517, -0.15849587,  0.06046333, -0.06074326,\n        0.15337899, -0.12902088, -0.15617546, -0.04478769, -0.07029557,\n        0.00588352,  0.01567913, -0.05229088,  0.07721972, -0.16800486,\n       -0.38455272, -0.07048173, -0.08376787,  0.00597632, -0.04819362,\n       -0.09277966,  0.06806447, -0.21399729, -0.00717013,  0.04177449,\n        0.13168879,  0.02416873, -0.00289608,  0.14412241,  0.01765561,\n       -0.24162766,  0.05621995,  0.15395258,  0.25980607,  0.16603035,\n        0.05931056,  0.03261615, -0.07959139,  0.14478616, -0.19670786,\n       -0.01603254,  0.11415387,  0.05400116,  0.02878786,  0.0673734 ,\n       -0.16693494,  0.06570372,  0.06083961, -0.18558609,  0.0255594 ,\n        0.05712397, -0.02238147, -0.04390225, -0.0535828 ,  0.29045498,\n        0.10419393, -0.09438045, -0.1526123 ,  0.24217415, -0.16832279,\n       -0.01890001,  0.04334292, -0.10192007, -0.13387513, -0.25966945,\n        0.01434509,  0.42884254,  0.20562685, -0.13592634,  0.11414444,\n       -0.0816604 , -0.04670458,  0.06629105,  0.08905669, -0.10765898,\n        0.0756406 , -0.0421249 ,  0.08146724,  0.24786979,  0.06755559,\n        0.04470994,  0.1496263 ,  0.0531904 ,  0.05942415,  0.02707091,\n        0.03522943, -0.23082066, -0.0629893 , -0.21715754, -0.06723854,\n       -0.02472944, -0.01516838,  0.01992988,  0.22727059, -0.25384563,\n        0.17621726, -0.05965468, -0.07747527, -0.07500324,  0.13463733,\n       -0.02447541, -0.0309705 ,  0.07312338, -0.21331416,  0.10117677,\n        0.17858881,  0.05588998,  0.10276237,  0.11844526, -0.02502396,\n        0.01126128,  0.00902764, -0.23954187, -0.08996159,  0.07168616,\n       -0.14491189,  0.08104283,  0.0438764 ])]'),(66,4,10,'[array([-1.88825205e-01,  5.14653511e-02,  2.76524834e-02, -7.79882967e-02,\n       -9.89643186e-02,  1.67624541e-02, -9.14257169e-02, -1.05224758e-01,\n        2.02299163e-01, -1.35663658e-01,  2.13310838e-01, -6.97802603e-02,\n       -1.58116847e-01, -4.18482907e-03, -3.80804911e-02,  1.45536929e-01,\n       -1.48457050e-01, -1.45222560e-01, -8.98117013e-03, -5.82472198e-02,\n        1.04442704e-04, -1.53552741e-02, -2.88985856e-02,  1.08669870e-01,\n       -2.10592449e-01, -4.11687106e-01, -2.78349593e-02, -1.42075151e-01,\n       -8.08758587e-02, -8.77210870e-02,  4.75224219e-02,  7.92350546e-02,\n       -2.44712353e-01,  4.69835568e-03, -1.58448424e-03,  1.85465857e-01,\n       -4.41824533e-02,  4.31652181e-02,  1.63022086e-01,  5.76085672e-02,\n       -2.63694108e-01, -1.88414231e-02,  3.28616388e-02,  2.73638606e-01,\n        1.31722525e-01,  8.59553292e-02, -1.26503091e-02, -7.01174587e-02,\n        1.24373183e-01, -2.08630621e-01,  2.75865234e-02,  1.18871562e-01,\n        9.23356339e-02, -1.72140189e-02,  8.53572786e-03, -1.49075598e-01,\n        2.99808495e-02,  1.00626469e-01, -2.07982421e-01,  3.32284383e-02,\n        4.56897691e-02, -1.34096906e-01, -5.27326874e-02, -5.54549210e-02,\n        2.87801445e-01,  1.21150300e-01, -1.06920741e-01, -5.89497313e-02,\n        1.80899322e-01, -1.22299090e-01, -2.28717662e-02,  8.82227570e-02,\n       -8.16340968e-02, -2.38120407e-01, -3.21669310e-01,  4.93110251e-03,\n        4.12107885e-01,  8.74536484e-02, -1.23338066e-01,  4.26845364e-02,\n       -6.70710057e-02, -2.74153240e-03,  1.44771999e-02,  1.25638559e-01,\n       -7.38700032e-02,  3.32132727e-02, -6.51886407e-03,  1.92353949e-02,\n        2.14517996e-01,  4.53128107e-02,  1.59786791e-02,  1.78593174e-01,\n       -6.52097240e-02,  2.42886394e-02, -9.27363150e-03, -1.13047939e-02,\n       -1.35753617e-01, -3.35834734e-02, -9.45922658e-02, -9.22970846e-02,\n       -2.48548519e-02, -4.06997167e-02,  1.81955341e-02,  8.89398679e-02,\n       -3.46696943e-01,  1.72211304e-01, -7.29232375e-03, -5.82319424e-02,\n        4.39401008e-02,  8.24900195e-02, -4.55324128e-02, -6.14335835e-02,\n        1.81437269e-01, -2.98467308e-01,  1.58464566e-01,  2.02645987e-01,\n        8.11444297e-02,  2.12225229e-01,  9.96315256e-02,  9.08905640e-03,\n       -4.40541282e-02,  4.02840041e-03, -2.45438740e-01, -2.47730557e-02,\n        6.52235672e-02, -9.08955857e-02,  8.60440880e-02,  1.93243474e-02]), array([-9.68270227e-02,  9.68414769e-02,  5.78335375e-02, -4.99678329e-02,\n       -6.60522878e-02, -5.13806567e-02, -1.24985464e-02, -9.86363143e-02,\n        7.54374564e-02, -7.04724900e-03,  1.60623759e-01, -3.19888741e-02,\n       -2.57708400e-01, -4.96471189e-02, -1.19945006e-02,  8.56241882e-02,\n       -7.39210099e-02, -1.04106590e-01, -1.37081802e-01, -1.38991296e-01,\n        1.89952422e-02,  1.18111148e-01,  4.43139896e-02, -1.28764529e-02,\n       -7.66930282e-02, -2.41460994e-01, -6.60606027e-02, -6.04641140e-02,\n        7.11201057e-02, -1.40255049e-01,  4.47073616e-02,  4.06663753e-02,\n       -1.74631491e-01, -1.26131214e-02,  2.13411637e-04,  6.68482184e-02,\n       -5.78664988e-02, -1.03161238e-01,  1.94311887e-01,  2.57307049e-02,\n       -1.59142107e-01,  1.54701788e-02,  1.09151259e-01,  2.62832761e-01,\n        2.03080624e-01, -1.19907763e-02, -6.16238825e-03, -1.37589844e-02,\n        5.40957004e-02, -2.23021179e-01,  5.41332960e-02,  1.51871383e-01,\n        1.14311256e-01,  9.91533622e-02,  7.41216168e-02, -1.74378514e-01,\n        2.03026105e-02,  8.07850733e-02, -1.19706266e-01,  8.31146762e-02,\n        1.02002420e-01, -1.17802486e-01, -2.97898240e-02, -7.13938251e-02,\n        1.40737116e-01,  5.37193716e-02, -9.67297927e-02, -1.28323987e-01,\n        5.61789721e-02, -1.82653010e-01, -7.12844729e-02,  1.03977472e-01,\n       -9.51133370e-02, -9.99102592e-02, -2.23028302e-01,  7.03426749e-02,\n        3.40959817e-01,  1.42262742e-01, -1.66772351e-01,  1.39303952e-02,\n       -5.95157705e-02, -3.02027129e-02,  1.70191098e-02,  5.61277308e-02,\n       -7.44205564e-02, -3.46454941e-02, -1.30897030e-01, -1.68880075e-03,\n        1.84776455e-01, -2.23646108e-02, -2.60343216e-02,  1.94064081e-01,\n        6.11988362e-03,  1.33150797e-02, -5.27007133e-03,  3.35673317e-02,\n       -1.37909055e-01, -1.99454352e-02, -2.00412609e-02, -2.82822177e-02,\n        2.61457451e-02, -1.80100098e-01,  4.41381987e-03,  1.00818649e-01,\n       -1.49775386e-01,  2.10900381e-01, -2.39642896e-03,  6.36854861e-03,\n        4.22332482e-03,  3.67172770e-02, -3.81690916e-03, -3.31035303e-03,\n        1.38718262e-01, -1.98044494e-01,  2.12064758e-01,  1.80031091e-01,\n       -8.53928179e-03,  1.23468958e-01,  6.26928955e-02,  1.68100879e-01,\n       -4.13939618e-02,  6.04977943e-02, -9.46742594e-02, -1.21301875e-01,\n       -4.08783928e-02, -5.37607819e-04,  3.93576622e-02,  7.55025372e-02])]'),(67,5,10,'[array([-0.16855307,  0.06124786,  0.07007675, -0.08450843, -0.07655689,\n        0.02473873, -0.07355301, -0.09213076,  0.21911536, -0.16846098,\n        0.16395421, -0.01861543, -0.17809431,  0.06107242, -0.01087826,\n        0.19280942, -0.14377643, -0.16365367, -0.0191657 , -0.06944636,\n       -0.02221105,  0.02407182, -0.01389211,  0.10560868, -0.20795499,\n       -0.41599238, -0.04537876, -0.08351763, -0.04180425, -0.06220279,\n        0.02767155,  0.03571364, -0.22902578,  0.03773102,  0.0612472 ,\n        0.22640358, -0.05114625, -0.06338802,  0.17128961,  0.05692349,\n       -0.2553485 , -0.00408833,  0.05981321,  0.2556915 ,  0.10056846,\n        0.07116935,  0.05112489, -0.13018759,  0.17541052, -0.18277514,\n       -0.01894737,  0.08866429,  0.07539179,  0.00199206,  0.06178185,\n       -0.19220887,  0.08085928,  0.10554587, -0.2186846 , -0.00172711,\n        0.02109201, -0.08982226, -0.00366505, -0.05208299,  0.24745436,\n        0.07029833, -0.10140607, -0.09059262,  0.21437591, -0.13070075,\n       -0.00677322,  0.07344068, -0.08199615, -0.25453407, -0.32090902,\n       -0.00303872,  0.40325594,  0.16417699, -0.10178366,  0.09119338,\n        0.00217018,  0.01837387,  0.02760665,  0.17694417, -0.08798146,\n        0.05522501, -0.02672579,  0.04285134,  0.24578348,  0.04723969,\n        0.01203828,  0.12313927, -0.02891487,  0.04339775, -0.02617187,\n        0.00216027, -0.20376612, -0.00481411, -0.13642563, -0.08313587,\n       -0.04255391,  0.03071811,  0.04773324,  0.13506758, -0.32591528,\n        0.17290415, -0.03072297, -0.12861766, -0.01197718,  0.13312499,\n       -0.06131414, -0.05009227,  0.11619285, -0.31027505,  0.13636799,\n        0.25002313,  0.03595727,  0.21377274,  0.09711519,  0.02074729,\n       -0.01099252,  0.02771191, -0.23641838, -0.07412345,  0.04829019,\n       -0.07033919,  0.10239355,  0.00988497])]');

/*Table structure for table `hall_ticket` */

DROP TABLE IF EXISTS `hall_ticket`;

CREATE TABLE `hall_ticket` (
  `hall_ticket_id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) DEFAULT NULL,
  `institute_id` int(11) DEFAULT NULL,
  `issued_date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hall_ticket_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `hall_ticket` */

insert  into `hall_ticket`(`hall_ticket_id`,`application_id`,`institute_id`,`issued_date`,`status`) values (2,1,2,'2021-12-28','pending'),(3,3,2,'2022-01-10','pending'),(4,2,4,'2022-01-10','pending'),(5,5,2,'2022-01-10','pending'),(6,3,1,'2022-01-13','pending'),(7,3,1,'2022-01-13','pending'),(8,1,4,'2022-01-13','pending'),(9,2,1,'2022-01-13','pending'),(10,4,3,'2022-01-13','pending'),(11,3,1,'2022-01-13','pending');

/*Table structure for table `institutes` */

DROP TABLE IF EXISTS `institutes`;

CREATE TABLE `institutes` (
  `institute_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `landmark` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `internet` varchar(100) DEFAULT NULL,
  `no_classroom` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`institute_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `institutes` */

insert  into `institutes`(`institute_id`,`login_id`,`name`,`place`,`landmark`,`phone`,`email`,`latitude`,`longitude`,`internet`,`no_classroom`) values (1,2,'bmc','aluva','choondy','9447371935','bmc@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50'),(2,3,'sngce','kolencherry','kadayiruppu','7034249935','sngce@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50'),(3,4,'fisat','angamaly','mookkannoor','9471213650','fisat@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50'),(4,8,'mes','n.paravoor','kunnukara','9388702046','mes@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50'),(6,15,'chavara','sdf','sdf','8551472036','chavara@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50'),(7,19,'riss','mg road','ernakulam','8542175236','riss@gmail.com','9.976712251779837','76.28459930419922','Yes','Above 50');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'bmc','bmc','institute'),(3,'sngce','sngce','institute'),(4,'fisat','fisat','institute'),(5,'ammu','ammu','staff'),(6,'arun','arun','staff'),(7,'neha','nehas','staff'),(8,'mes','mes','institute'),(9,'anu','anu','staff'),(10,'','','pending'),(11,'sonnu','sonnu','candidates'),(12,'arun','arun1','candidates'),(13,'saanju','saanju123','candidates'),(14,'darsana','darsana1','staff'),(15,'chavara','Chavara1','institute'),(16,'anu','anu1','candidates'),(17,'krishna','Krishna ','candidates'),(18,'darsana','darsana','candidates'),(19,'riss','Riss@123','pending'),(20,'harsha','Harsha1','staff'),(21,'neha','neha','staff'),(22,'sanchana','sanchana','candidates'),(23,'saa','saa','candidates');

/*Table structure for table `seats` */

DROP TABLE IF EXISTS `seats`;

CREATE TABLE `seats` (
  `seat_id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) DEFAULT NULL,
  `classroom_id` int(11) DEFAULT NULL,
  `seat_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`seat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `seats` */

insert  into `seats`(`seat_id`,`application_id`,`classroom_id`,`seat_no`) values (1,3,5,1);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `institute_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`institute_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`) values (1,1,5,'ammu','p b','8451236796','ammu@gmail.com'),(2,1,6,'arun','kumar','9874125632','arun@gmail.com'),(3,1,7,'neha','sarah','9647215843','neha@gmail.com'),(4,4,9,'anagha',' T A','9875123642','anu@gmail.com'),(5,2,14,'darsana','prasad','8963467256','darsana@gmail.com'),(6,4,20,'harsha','P','7548236195','harsha@gmail.com'),(7,7,21,'neha','sara','9524813657','neha@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
