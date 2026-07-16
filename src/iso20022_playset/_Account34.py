# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification132
from . import PostalAddress1

class Account34(base_types._BaseFieldType):

	__slots__ = ["_AcctDsgnt", "_AcctId", "_AcctNm", "_AcctSvcr", "_RegnAdr"]
	@property
	def AcctDsgnt(self):
		return self._AcctDsgnt

	@AcctDsgnt.setter
	def AcctDsgnt(self, value):
		self._AcctDsgnt = value if value is not None else base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

	@AcctDsgnt.deleter
	def AcctDsgnt(self):
		del self._AcctDsgnt
		self._AcctDsgnt = base_types.UninitialisedField(self, 'AcctDsgnt', Max35Text, False)

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if value is not None else base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = base_types.UninitialisedField(self, 'AcctNm', Max35Text, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification132, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', PartyIdentification132, False)

	@property
	def RegnAdr(self):
		return self._RegnAdr

	@RegnAdr.setter
	def RegnAdr(self, value):
		self._RegnAdr = value if value is not None else base_types.UninitialisedField(self, 'RegnAdr', PostalAddress1, False)

	@RegnAdr.deleter
	def RegnAdr(self):
		del self._RegnAdr
		self._RegnAdr = base_types.UninitialisedField(self, 'RegnAdr', PostalAddress1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=PartyIdentification132, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
	))