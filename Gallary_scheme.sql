-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Gallery
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Gallery` ;

-- -----------------------------------------------------
-- Schema Gallery
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Gallery` DEFAULT CHARACTER SET utf8 ;
USE `Gallery` ;

-- -----------------------------------------------------
-- Table `Gallery`.`Photographer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gallery`.`Photographer` (
  `idPhotographer` INT NOT NULL AUTO_INCREMENT,
  `PhotographerName` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPhotographer`),
  UNIQUE INDEX `idPhotographer_UNIQUE` (`idPhotographer` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gallery`.`Album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gallery`.`Album` (
  `idAlbum` INT NOT NULL AUTO_INCREMENT,
  `AlbumName` VARCHAR(45) NOT NULL,
  `CreationDate` DATE NOT NULL,
  PRIMARY KEY (`idAlbum`),
  UNIQUE INDEX `idAlbum_UNIQUE` (`idAlbum` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gallery`.`Photo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gallery`.`Photo` (
  `idPhoto` INT NOT NULL AUTO_INCREMENT,
  `Photodate` DATE NOT NULL,
  `idPhotographer` INT NOT NULL,
  `idAlbum` INT NOT NULL,
  PRIMARY KEY (`idPhoto`),
  UNIQUE INDEX `idPhoto_UNIQUE` (`idPhoto` ASC) VISIBLE,
  INDEX `fk_photo_photographer_idPhotographer_idx` (`idPhotographer` ASC) VISIBLE,
  INDEX `fk_photo_album_idAlbum_idx` (`idAlbum` ASC) VISIBLE,
  CONSTRAINT `fk_photo_photographer_idPhotographer`
    FOREIGN KEY (`idPhotographer`)
    REFERENCES `Gallery`.`Photographer` (`idPhotographer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_photo_album_idAlbum`
    FOREIGN KEY (`idAlbum`)
    REFERENCES `Gallery`.`Album` (`idAlbum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Gallery`.`AlbumPhotographer_xref`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gallery`.`AlbumPhotographer_xref` (
  `idAlbumPhotographer_xref` INT NOT NULL AUTO_INCREMENT,
  `idAlbum` INT NOT NULL,
  `idPhotographer` INT NOT NULL,
  PRIMARY KEY (`idAlbumPhotographer_xref`),
  UNIQUE INDEX `idAlbumPhotographer_xref_UNIQUE` (`idAlbumPhotographer_xref` ASC) VISIBLE,
  INDEX `fk_albumphotographer_photographer_idPhotographer_idx` (`idPhotographer` ASC) VISIBLE,
  INDEX `fk_albumphotographer_album_idAlbum_idx` (`idAlbum` ASC) VISIBLE,
  CONSTRAINT `fk_albumphotographer_photographer_idPhotographer`
    FOREIGN KEY (`idPhotographer`)
    REFERENCES `Gallery`.`Photographer` (`idPhotographer`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_albumphotographer_album_idAlbum`
    FOREIGN KEY (`idAlbum`)
    REFERENCES `Gallery`.`Album` (`idAlbum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
