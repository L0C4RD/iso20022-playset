# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification38Choice
from . import DatePeriod2
from . import Max35Text
from . import PartyIdentification136
from . import SystemAndCurrency1

class BillingSearchCriteria3(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BllgId", "_BllgPrd", "_PtyId", "_RspnsblPtyId", "_Svc"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification38Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification38Choice, False)

	@property
	def BllgId(self):
		return self._BllgId

	@BllgId.setter
	def BllgId(self, value):
		self._BllgId = value if value is not None else base_types.UninitialisedField(self, 'BllgId', Max35Text, False)

	@BllgId.deleter
	def BllgId(self):
		del self._BllgId
		self._BllgId = base_types.UninitialisedField(self, 'BllgId', Max35Text, False)

	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if value is not None else base_types.UninitialisedField(self, 'BllgPrd', DatePeriod2, False)

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = base_types.UninitialisedField(self, 'BllgPrd', DatePeriod2, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = base_types.UninitialisedField(self, 'RspnsblPtyId', PartyIdentification136, False)

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if value is not None else base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = base_types.UninitialisedField(self, 'Svc', SystemAndCurrency1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))