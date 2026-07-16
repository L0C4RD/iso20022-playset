# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchData3
from . import FinancialInstitutionIdentification18

class BranchAndFinancialInstitutionIdentification6(base_types._BaseFieldType):

	__slots__ = ["_BrnchId", "_FinInstnId"]
	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if value is not None else base_types.UninitialisedField(self, 'BrnchId', BranchData3, False)

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = base_types.UninitialisedField(self, 'BrnchId', BranchData3, False)

	@property
	def FinInstnId(self):
		return self._FinInstnId

	@FinInstnId.setter
	def FinInstnId(self, value):
		self._FinInstnId = value if value is not None else base_types.UninitialisedField(self, 'FinInstnId', FinancialInstitutionIdentification18, False)

	@FinInstnId.deleter
	def FinInstnId(self):
		del self._FinInstnId
		self._FinInstnId = base_types.UninitialisedField(self, 'FinInstnId', FinancialInstitutionIdentification18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrnchId', type=BranchData3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstnId', type=FinancialInstitutionIdentification18, min=1, max=1, mutex_group=None, array=False),
	))