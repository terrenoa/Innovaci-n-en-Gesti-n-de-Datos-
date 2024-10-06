-- MySQL Script generated by MySQL Workbench
-- Mon Jun 10 22:27:53 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`ObraS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ObraS` (
  `idOS` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idOS`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Pacientes` (
  `dni` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `ObraS_idObraS` INT NOT NULL,
  PRIMARY KEY (`dni`, `ObraS_idObraS`),
  UNIQUE INDEX `DNI_UNIQUE` (`dni` ASC) VISIBLE,
  INDEX `fk_Pacientes_ObraS1_idx` (`ObraS_idObraS` ASC) VISIBLE,
  CONSTRAINT `fk_Pacientes_ObraS1`
    FOREIGN KEY (`ObraS_idObraS`)
    REFERENCES `mydb`.`ObraS` (`idOS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Profesionales`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Profesionales` (
  `idProfesionales` INT NOT NULL AUTO_INCREMENT,
  `cuil` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProfesionales`),
  UNIQUE INDEX `idProfesionales_UNIQUE` (`idProfesionales` ASC) VISIBLE,
  UNIQUE INDEX `cuil_UNIQUE` (`cuil` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Especialidad` (
  `idEspecialidad` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `idServicios Medicos_UNIQUE` (`idEspecialidad` ASC) VISIBLE,
  UNIQUE INDEX `especialidad_UNIQUE` (`nombre` ASC) VISIBLE,
  PRIMARY KEY (`idEspecialidad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Turno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Turno` (
  `idTurno` INT NOT NULL AUTO_INCREMENT,
  `estado` ENUM('pendiente', 'aceptado', 'cancelado') NOT NULL,
  `fecha` DATE NOT NULL,
  `f_hora` DATETIME NOT NULL,
  `Profesionales_idProfesionales` INT NOT NULL,
  `Pacientes_dni` INT NOT NULL,
  `Especialidad_idEspecialidad` INT NOT NULL,
  PRIMARY KEY (`idTurno`, `Profesionales_idProfesionales`, `Pacientes_dni`, `Especialidad_idEspecialidad`),
  INDEX `fk_Turno_Profesionales1_idx` (`Profesionales_idProfesionales` ASC) VISIBLE,
  INDEX `fk_Turno_Pacientes1_idx` (`Pacientes_dni` ASC) VISIBLE,
  INDEX `fk_Turno_Especialidad1_idx` (`Especialidad_idEspecialidad` ASC) VISIBLE,
  CONSTRAINT `fk_Turno_Profesionales1`
    FOREIGN KEY (`Profesionales_idProfesionales`)
    REFERENCES `mydb`.`Profesionales` (`idProfesionales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turno_Pacientes1`
    FOREIGN KEY (`Pacientes_dni`)
    REFERENCES `mydb`.`Pacientes` (`dni`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Turno_Especialidad1`
    FOREIGN KEY (`Especialidad_idEspecialidad`)
    REFERENCES `mydb`.`Especialidad` (`idEspecialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Profesionales_has_Especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Profesionales_has_Especialidad` (
  `Profesionales_idProfesionales` INT NOT NULL,
  `Especialidad_idEspecialidad` INT NOT NULL,
  PRIMARY KEY (`Profesionales_idProfesionales`, `Especialidad_idEspecialidad`),
  INDEX `fk_Profesionales_has_Especialidad_Especialidad1_idx` (`Especialidad_idEspecialidad` ASC) VISIBLE,
  INDEX `fk_Profesionales_has_Especialidad_Profesionales1_idx` (`Profesionales_idProfesionales` ASC) VISIBLE,
  CONSTRAINT `fk_Profesionales_has_Especialidad_Profesionales1`
    FOREIGN KEY (`Profesionales_idProfesionales`)
    REFERENCES `mydb`.`Profesionales` (`idProfesionales`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Profesionales_has_Especialidad_Especialidad1`
    FOREIGN KEY (`Especialidad_idEspecialidad`)
    REFERENCES `mydb`.`Especialidad` (`idEspecialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ObraS_has_Especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ObraS_has_Especialidad` (
  `ObraS_idOS` INT NOT NULL AUTO_INCREMENT,
  `Especialidad_idEspecialidad` INT NOT NULL,
  PRIMARY KEY (`ObraS_idOS`, `Especialidad_idEspecialidad`),
  INDEX `fk_ObraS_has_Especialidad_Especialidad1_idx` (`Especialidad_idEspecialidad` ASC) VISIBLE,
  INDEX `fk_ObraS_has_Especialidad_ObraS1_idx` (`ObraS_idOS` ASC) VISIBLE,
  CONSTRAINT `fk_ObraS_has_Especialidad_ObraS1`
    FOREIGN KEY (`ObraS_idOS`)
    REFERENCES `mydb`.`ObraS` (`idOS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ObraS_has_Especialidad_Especialidad1`
    FOREIGN KEY (`Especialidad_idEspecialidad`)
    REFERENCES `mydb`.`Especialidad` (`idEspecialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`historias_clinicas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`historias_clinicas` (
  `idhistorias_clinicas` INT NOT NULL,
  `Pacientes_dni` INT NOT NULL,
  `Pacientes_ObraS_idObraS` INT NOT NULL,
  `fecha_primera_atencion` DATE NULL,
  `altura` FLOAT NULL,
  `peso` FLOAT NULL,
  `alergias` TINYINT(1) NOT NULL,
  `medicacion_diaria` TINYINT(1) NOT NULL,
  `hipertenso` TINYINT(1) NULL,
  `fue_operado` TINYINT(1) NULL,
  PRIMARY KEY (`idhistorias_clinicas`, `Pacientes_dni`, `Pacientes_ObraS_idObraS`),
  INDEX `fk_historias_clinicas_Pacientes1_idx` (`Pacientes_dni` ASC, `Pacientes_ObraS_idObraS` ASC) VISIBLE,
  CONSTRAINT `fk_historias_clinicas_Pacientes1`
    FOREIGN KEY (`Pacientes_dni` , `Pacientes_ObraS_idObraS`)
    REFERENCES `mydb`.`Pacientes` (`dni` , `ObraS_idObraS`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
