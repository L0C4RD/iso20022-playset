# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchData5 import BranchData5
from ._FinancialInstitutionIdentification23 import FinancialInstitutionIdentification23

class BranchAndFinancialInstitutionIdentification8(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='BrnchId', type=BranchData5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstnId', type=FinancialInstitutionIdentification23, min=1, max=1, mutex_group=None, array=False),
	))