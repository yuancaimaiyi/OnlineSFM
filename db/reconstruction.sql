CREATE TABLE RECONSTRUCTIONS(
    ID CHAR(36) NOT NULL PRIMARY KEY,
    PATH VARCHAR(200) NOT NULL
);
CREATE TABLE VIEWS(
    ID CHAR(36) NOT NULL PRIMARY KEY,
    RECONSTRUCTION_ID CHAR(36) NOT NULL REFERENCES RECONSTRUCTIONS,
    PATH VARCHAR(200) NOT NULL,
    FORMAT VARCHAR(20) NOT NULL
);
CREATE TABLE SPARSE(
    ID CHAR(36) NOT NULL PRIMARY KEY,
    RECONSTRUCTION_ID CHAR(36) NOT NULL REFERENCES RECONSTRUCTIONS,
    PLY_PATH VARCHAR(200) NOT NULL,
    MVS_PATH VARCHAR(200) NOT NULL
);
CREATE TABLE OBJ(
    ID CHAR(36) NOT NULL PRIMARY KEY,
    RECONSTRUCTION_ID CHAR(36) NOT NULL REFERENCES RECONSTRUCTIONS,
    PATH VARCHAR(200) NOT NULL,
    TEXTURE_PATH VARCHAR(200) NOT NULL,
    MTL_PATH VARCHAR(200) NOT NULL
);
CREATE TABLE CAMERA_INTRINSICS(
    MODEL VARCHAR(50) NOT NULL PRIMARY KEY,
    FOCAL_LENGTH FLOAT,
    FOCUS_MODE VARCHAR(40),
    HORIZONTAL_VIEW_ANGLE FLOAT,
    JPEG_QUALITY INT
);