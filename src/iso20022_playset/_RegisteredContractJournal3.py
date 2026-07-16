# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ContractClosureReason1Choice
from . import DocumentIdentification28
from . import ISODate

class RegisteredContractJournal3(base_types._BaseFieldType):

	__slots__ = ["_ClsrDt", "_ClsrRsn", "_RegnAgt", "_UnqId"]
	@property
	def ClsrDt(self):
		return self._ClsrDt

	@ClsrDt.setter
	def ClsrDt(self, value):
		self._ClsrDt = value if value is not None else base_types.UninitialisedField(self, 'ClsrDt', ISODate, False)

	@ClsrDt.deleter
	def ClsrDt(self):
		del self._ClsrDt
		self._ClsrDt = base_types.UninitialisedField(self, 'ClsrDt', ISODate, False)

	@property
	def ClsrRsn(self):
		return self._ClsrRsn

	@ClsrRsn.setter
	def ClsrRsn(self, value):
		self._ClsrRsn = value if value is not None else base_types.UninitialisedField(self, 'ClsrRsn', ContractClosureReason1Choice, False)

	@ClsrRsn.deleter
	def ClsrRsn(self):
		del self._ClsrRsn
		self._ClsrRsn = base_types.UninitialisedField(self, 'ClsrRsn', ContractClosureReason1Choice, False)

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if value is not None else base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def UnqId(self):
		return self._UnqId

	@UnqId.setter
	def UnqId(self, value):
		self._UnqId = value if value is not None else base_types.UninitialisedField(self, 'UnqId', DocumentIdentification28, False)

	@UnqId.deleter
	def UnqId(self):
		del self._UnqId
		self._UnqId = base_types.UninitialisedField(self, 'UnqId', DocumentIdentification28, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsrRsn', type=ContractClosureReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqId', type=DocumentIdentification28, min=0, max=1, mutex_group=None, array=False),
	))