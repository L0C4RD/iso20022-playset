from . import base_types
from ._FinancialInstitutionIdentification18 import FinancialInstitutionIdentification18
from ._BranchData3 import BranchData3

class BranchAndFinancialInstitutionIdentification6(base_types._BaseFieldType):

	__slots__ = ["_BrnchId", "_FinInstnId"]
	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != base_types.auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

	@property
	def FinInstnId(self):
		return self._FinInstnId

	@FinInstnId.setter
	def FinInstnId(self, value):
		self._FinInstnId = value if type(value) != base_types.auto else self.make_default("FinInstnId")

	@FinInstnId.deleter
	def FinInstnId(self):
		del self._FinInstnId
		self._FinInstnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrnchId', type=BranchData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstnId', type=FinancialInstitutionIdentification18, min=1, max=1, mutex_group=None, array=False),
	))

