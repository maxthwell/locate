--
-- PostgreSQL database dump
--

-- Dumped from database version 10.0
-- Dumped by pg_dump version 10.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: device; Type: TABLE; Schema: public; Owner: locate
--

CREATE TABLE device (
    dev_id integer NOT NULL,
    dev_addr bytea NOT NULL,
    usage text,
    power integer DEFAULT 0,
    last_locate_id bigint DEFAULT 0,
    user_id integer DEFAULT 0 NOT NULL
);


ALTER TABLE device OWNER TO locate;

--
-- Name: device_dev_id_seq; Type: SEQUENCE; Schema: public; Owner: locate
--

CREATE SEQUENCE device_dev_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE device_dev_id_seq OWNER TO locate;

--
-- Name: device_dev_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: locate
--

ALTER SEQUENCE device_dev_id_seq OWNED BY device.dev_id;


--
-- Name: locate_data; Type: TABLE; Schema: public; Owner: locate
--

CREATE TABLE locate_data (
    locate_id bigint NOT NULL,
    lat real,
    lon real,
    dev_id integer,
    time_s timestamp without time zone DEFAULT (now())::timestamp without time zone
);


ALTER TABLE locate_data OWNER TO locate;

--
-- Name: locate_data_locate_id_seq; Type: SEQUENCE; Schema: public; Owner: locate
--

CREATE SEQUENCE locate_data_locate_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE locate_data_locate_id_seq OWNER TO locate;

--
-- Name: locate_data_locate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: locate
--

ALTER SEQUENCE locate_data_locate_id_seq OWNED BY locate_data.locate_id;


--
-- Name: user_info; Type: TABLE; Schema: public; Owner: locate
--

CREATE TABLE user_info (
    user_id integer NOT NULL,
    name text
);


ALTER TABLE user_info OWNER TO locate;

--
-- Name: user_info_user_id_seq; Type: SEQUENCE; Schema: public; Owner: locate
--

CREATE SEQUENCE user_info_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE user_info_user_id_seq OWNER TO locate;

--
-- Name: user_info_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: locate
--

ALTER SEQUENCE user_info_user_id_seq OWNED BY user_info.user_id;


--
-- Name: device dev_id; Type: DEFAULT; Schema: public; Owner: locate
--

ALTER TABLE ONLY device ALTER COLUMN dev_id SET DEFAULT nextval('device_dev_id_seq'::regclass);


--
-- Name: locate_data locate_id; Type: DEFAULT; Schema: public; Owner: locate
--

ALTER TABLE ONLY locate_data ALTER COLUMN locate_id SET DEFAULT nextval('locate_data_locate_id_seq'::regclass);


--
-- Name: user_info user_id; Type: DEFAULT; Schema: public; Owner: locate
--

ALTER TABLE ONLY user_info ALTER COLUMN user_id SET DEFAULT nextval('user_info_user_id_seq'::regclass);


--
-- Name: device device_pkey; Type: CONSTRAINT; Schema: public; Owner: locate
--

ALTER TABLE ONLY device
    ADD CONSTRAINT device_pkey PRIMARY KEY (dev_id);


--
-- Name: locate_data locate_data_pkey; Type: CONSTRAINT; Schema: public; Owner: locate
--

ALTER TABLE ONLY locate_data
    ADD CONSTRAINT locate_data_pkey PRIMARY KEY (locate_id);


--
-- Name: user_info user_info_pkey; Type: CONSTRAINT; Schema: public; Owner: locate
--

ALTER TABLE ONLY user_info
    ADD CONSTRAINT user_info_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

