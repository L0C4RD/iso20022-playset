# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification132
from . import SubAccount5

class Account28(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctNm", "_Dsgnt", "_OwnrId", "_SubAcctDtls", "_Svcr"]
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
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if value is not None else base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = base_types.UninitialisedField(self, 'Dsgnt', Max35Text, False)

	@property
	def OwnrId(self):
		return self._OwnrId

	@OwnrId.setter
	def OwnrId(self, value):
		self._OwnrId = value if value is not None else base_types.UninitialisedField(self, 'OwnrId', PartyIdentification132, False)

	@OwnrId.deleter
	def OwnrId(self):
		del self._OwnrId
		self._OwnrId = base_types.UninitialisedField(self, 'OwnrId', PartyIdentification132, False)

	@property
	def SubAcctDtls(self):
		return self._SubAcctDtls

	@SubAcctDtls.setter
	def SubAcctDtls(self, value):
		self._SubAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount5, False)

	@SubAcctDtls.deleter
	def SubAcctDtls(self):
		del self._SubAcctDtls
		self._SubAcctDtls = base_types.UninitialisedField(self, 'SubAcctDtls', SubAccount5, False)

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if value is not None else base_types.UninitialisedField(self, 'Svcr', PartyIdentification132, False)

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = base_types.UninitialisedField(self, 'Svcr', PartyIdentification132, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrId', type=PartyIdentification132, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctDtls', type=SubAccount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification132, min=0, max=1, mutex_group=None, array=False),
	))