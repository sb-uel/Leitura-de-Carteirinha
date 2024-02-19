-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema RamoIEEE
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `RamoIEEE` ;

-- -----------------------------------------------------
-- Schema RamoIEEE
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `RamoIEEE` DEFAULT CHARACTER SET utf8 ;
USE `RamoIEEE` ;

-- -----------------------------------------------------
-- Table `RamoIEEE`.`cursos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`cursos` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`cursos` (
  `id_curso` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `curso` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id_curso`),
  UNIQUE INDEX `Curso_UNIQUE` (`curso` ASC) VISIBLE)
ENGINE = InnoDB;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'COMPUTAÇÃO'),(2,'ELÉTRICA');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `RamoIEEE`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`usuarios` (
  `id_usuario` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `n_carteirinha` CHAR(14) NOT NULL,
  `n_matricula` CHAR(12) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(45) NULL,
  `id_curso` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_usuario`),
  INDEX `fk_Usuário_Curso1_idx` (`id_curso` ASC) VISIBLE,
  UNIQUE INDEX `N_Carteirinha_UNIQUE` (`n_carteirinha` ASC) VISIBLE,
  UNIQUE INDEX `N_Matricula_UNIQUE` (`n_matricula` ASC) VISIBLE,
  CONSTRAINT `fk_Usuário_Curso1`
    FOREIGN KEY (`id_curso`)
    REFERENCES `RamoIEEE`.`cursos` (`id_curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RamoIEEE`.`reunioes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`reunioes` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`reunioes` (
  `id_reuniao` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `data` DATE NOT NULL,
  PRIMARY KEY (`id_reuniao`),
  UNIQUE INDEX `Data_UNIQUE` (`data` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RamoIEEE`.`presencas`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`presencas` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`presencas` (
  `id_presenca` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `presente` BIT NOT NULL,
  `id_reuniao` INT UNSIGNED NOT NULL,
  `id_usuario` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_presenca`),
  INDEX `fk_Presenças_Reuniões1_idx` (`id_reuniao` ASC) VISIBLE,
  INDEX `fk_Presenças_Usuário1_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_Presenças_Reuniões1`
    FOREIGN KEY (`id_reuniao`)
    REFERENCES `RamoIEEE`.`reunioes` (`id_reuniao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Presenças_Usuário1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `RamoIEEE`.`usuarios` (`id_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
