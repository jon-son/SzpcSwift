/*
MySQL Data Transfer
Source Host: 10.1.5.26
Source Database: szpc-swift
Target Host: 10.1.5.26
Target Database: szpc-swift
Date: 2018/11/2 16:53:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user_list
-- ----------------------------
CREATE TABLE `user_list` (
  `user_name` varchar(255) NOT NULL,
  `user_type` int(1) NOT NULL COMMENT '0:超级管理员\r\n1:管理员\r\n2:普通用户',
  `account` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `user_list` VALUES ('jonson', '1', '16240620', 'e10adc3949ba59abbe56e057f20f883e');
