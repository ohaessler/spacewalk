--
-- Copyright (c) 2009 Red Hat, Inc.
--
-- This software is licensed to you under the GNU General Public License,
-- version 2 (GPLv2). There is NO WARRANTY for this software, express or
-- implied, including the implied warranties of MERCHANTABILITY or FITNESS
-- FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
-- along with this software; if not, see
-- http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
-- 
-- Red Hat trademarks are not licensed under GPLv2. No permission is
-- granted to use or replicate Red Hat trademarks that are incorporated
-- in this software or its documentation. 
--
--
--
--

create sequence rhn_checksum_id_seq;

create table
rhnChecksumType
(
	id			number
				constraint rhn_checksumtype_id_nn not null,
	label			varchar2(32)
				constraint rhn_checksumtype_label_nn not null,
	description		varchar2(64)
				constraint rhn_checksumtype_desc_nn not null,
	created			date default(sysdate)
				constraint rhn_checksumtype_creat_nn not null,
	modified		date default(sysdate)
				constraint rhn_checksumtype_mod_nn not null
)
	enable row movement
  ;

create index rhn_checksumtype_label_id_idx
	on rhnChecksumType( label, id )
	tablespace [[64k_tbs]]
  ;
alter table rhnChecksumType add constraint rhn_checksumtype_id_pk 
        primary key ( id );
alter table rhnChecksumType add constraint rhn_checksumtype_label_uq
	unique ( label );

create or replace trigger
rhn_checksumtype_mod_trig
before insert or update on rhnChecksumType
for each row
begin
	:new.modified := sysdate;
end;
/
show errors

--
--
-- Revision 1.1  2009/06/26 10:39:17  pkilambi
--  add schema to hold checksum types
--
