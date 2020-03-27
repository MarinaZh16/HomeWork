--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
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


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    actor_id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: actor_film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor_film (
    actor_id integer NOT NULL,
    film_id integer NOT NULL
);


ALTER TABLE public.actor_film OWNER TO postgres;

--
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    film_id integer NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.film OWNER TO postgres;

--
-- Name: producer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer (
    producer_id integer NOT NULL,
    name text NOT NULL,
    surname text NOT NULL
);


ALTER TABLE public.producer OWNER TO postgres;

--
-- Name: producer_film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producer_film (
    producer_id integer NOT NULL,
    film_id integer NOT NULL
);


ALTER TABLE public.producer_film OWNER TO postgres;

--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (actor_id, name, surname) FROM stdin;
\.


--
-- Data for Name: actor_film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor_film (actor_id, film_id) FROM stdin;
\.


--
-- Data for Name: film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.film (film_id, title) FROM stdin;
\.


--
-- Data for Name: producer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer (producer_id, name, surname) FROM stdin;
\.


--
-- Data for Name: producer_film; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producer_film (producer_id, film_id) FROM stdin;
\.


--
-- Name: actor_film actor_film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_pkey PRIMARY KEY (actor_id, film_id);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (actor_id);


--
-- Name: film film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film
    ADD CONSTRAINT film_pkey PRIMARY KEY (film_id);


--
-- Name: producer_film producer_film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_pkey PRIMARY KEY (producer_id, film_id);


--
-- Name: producer producer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer
    ADD CONSTRAINT producer_pkey PRIMARY KEY (producer_id);


--
-- Name: actor_film actor_film_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actor(actor_id);


--
-- Name: actor_film actor_film_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor_film
    ADD CONSTRAINT actor_film_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id);


--
-- Name: producer_film producer_film_film_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_film_id_fkey FOREIGN KEY (film_id) REFERENCES public.film(film_id);


--
-- Name: producer_film producer_film_producer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producer_film
    ADD CONSTRAINT producer_film_producer_id_fkey FOREIGN KEY (producer_id) REFERENCES public.producer(producer_id);


--
-- PostgreSQL database dump complete
--

