from . import base_types
from ._AccountIdentification38Choice import AccountIdentification38Choice
from ._DatePeriod2 import DatePeriod2
from ._Max35Text import Max35Text
from ._PartyIdentification136 import PartyIdentification136
from ._SystemAndCurrency1 import SystemAndCurrency1

class BillingSearchCriteria3(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_BllgId", "_BllgPrd", "_PtyId", "_RspnsblPtyId", "_Svc"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def BllgId(self):
		return self._BllgId

	@BllgId.setter
	def BllgId(self, value):
		self._BllgId = value if type(value) != base_types.auto else self.make_default("BllgId")

	@BllgId.deleter
	def BllgId(self):
		del self._BllgId
		self._BllgId = None

	@property
	def BllgPrd(self):
		return self._BllgPrd

	@BllgPrd.setter
	def BllgPrd(self, value):
		self._BllgPrd = value if type(value) != base_types.auto else self.make_default("BllgPrd")

	@BllgPrd.deleter
	def BllgPrd(self):
		del self._BllgPrd
		self._BllgPrd = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def RspnsblPtyId(self):
		return self._RspnsblPtyId

	@RspnsblPtyId.setter
	def RspnsblPtyId(self, value):
		self._RspnsblPtyId = value if type(value) != base_types.auto else self.make_default("RspnsblPtyId")

	@RspnsblPtyId.deleter
	def RspnsblPtyId(self):
		del self._RspnsblPtyId
		self._RspnsblPtyId = None

	@property
	def Svc(self):
		return self._Svc

	@Svc.setter
	def Svc(self, value):
		self._Svc = value if type(value) != base_types.auto else self.make_default("Svc")

	@Svc.deleter
	def Svc(self):
		del self._Svc
		self._Svc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgPrd', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPtyId', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svc', type=SystemAndCurrency1, min=0, max=1, mutex_group=None, array=False),
	))

