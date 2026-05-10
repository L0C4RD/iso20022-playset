from . import base_types
from .DocumentIdentification28 import DocumentIdentification28
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .ContractClosureReason1Choice import ContractClosureReason1Choice
from .ISODate import ISODate

class RegisteredContractJournal3(base_types._BaseFieldType):

	__slots__ = ["_RegnAgt", "_ClsrRsn", "_ClsrDt", "_UnqId"]
	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != base_types.auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

	@property
	def ClsrRsn(self):
		return self._ClsrRsn

	@ClsrRsn.setter
	def ClsrRsn(self, value):
		self._ClsrRsn = value if type(value) != base_types.auto else self.make_default("ClsrRsn")

	@ClsrRsn.deleter
	def ClsrRsn(self):
		del self._ClsrRsn
		self._ClsrRsn = None

	@property
	def ClsrDt(self):
		return self._ClsrDt

	@ClsrDt.setter
	def ClsrDt(self, value):
		self._ClsrDt = value if type(value) != base_types.auto else self.make_default("ClsrDt")

	@ClsrDt.deleter
	def ClsrDt(self):
		del self._ClsrDt
		self._ClsrDt = None

	@property
	def UnqId(self):
		return self._UnqId

	@UnqId.setter
	def UnqId(self, value):
		self._UnqId = value if type(value) != base_types.auto else self.make_default("UnqId")

	@UnqId.deleter
	def UnqId(self):
		del self._UnqId
		self._UnqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrRsn', type=ContractClosureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqId', type=DocumentIdentification28, min=0, max=1, mutex_group=None, array=False),
	))

