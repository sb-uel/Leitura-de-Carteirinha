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
-- Table `RamoIEEE`.`Curso`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`Curso` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`Curso` (
  `ID_Curso` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Curso` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`ID_Curso`),
  UNIQUE INDEX `Curso_UNIQUE` (`Curso` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RamoIEEE`.`Usuário`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`Usuário` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`Usuário` (
  `ID_Usuário` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `N_Matricula` VARCHAR(45) NOT NULL,
  `Nome` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  `ID_Curso` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`ID_Usuário`),
  INDEX `fk_Usuário_Curso1_idx` (`ID_Curso` ASC) VISIBLE,
  CONSTRAINT `fk_Usuário_Curso1`
    FOREIGN KEY (`ID_Curso`)
    REFERENCES `RamoIEEE`.`Curso` (`ID_Curso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RamoIEEE`.`Reuniões`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`Reuniões` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`Reuniões` (
  `ID_Reuniões` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Data` DATE NOT NULL,
  PRIMARY KEY (`ID_Reuniões`),
  UNIQUE INDEX `Data_UNIQUE` (`Data` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `RamoIEEE`.`Presenças`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `RamoIEEE`.`Presenças` ;

CREATE TABLE IF NOT EXISTS `RamoIEEE`.`Presenças` (
  `ID_Presenças` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Presente` BIT NOT NULL,
  `ID_Reuniões` INT UNSIGNED NOT NULL,
  `ID_Usuário` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`ID_Presenças`),
  INDEX `fk_Presenças_Reuniões1_idx` (`ID_Reuniões` ASC) VISIBLE,
  INDEX `fk_Presenças_Usuário1_idx` (`ID_Usuário` ASC) VISIBLE,
  CONSTRAINT `fk_Presenças_Reuniões1`
    FOREIGN KEY (`ID_Reuniões`)
    REFERENCES `RamoIEEE`.`Reuniões` (`ID_Reuniões`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Presenças_Usuário1`
    FOREIGN KEY (`ID_Usuário`)
    REFERENCES `RamoIEEE`.`Usuário` (`ID_Usuário`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
