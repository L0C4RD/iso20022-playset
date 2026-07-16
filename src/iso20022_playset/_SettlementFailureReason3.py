# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2Fraction1NonNegativeNumber
from . import SettlementFailureReason2

class SettlementFailureReason3(base_types._BaseFieldType):

	__slots__ = ["_AvrgDrtn", "_Desc"]
	@property
	def AvrgDrtn(self):
		return self._AvrgDrtn

	@AvrgDrtn.setter
	def AvrgDrtn(self, value):
		self._AvrgDrtn = value if value is not None else base_types.UninitialisedField(self, 'AvrgDrtn', Max2Fraction1NonNegativeNumber, False)

	@AvrgDrtn.deleter
	def AvrgDrtn(self):
		del self._AvrgDrtn
		self._AvrgDrtn = base_types.UninitialisedField(self, 'AvrgDrtn', Max2Fraction1NonNegativeNumber, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', SettlementFailureReason2, True)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', SettlementFailureReason2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvrgDrtn', type=Max2Fraction1NonNegativeNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=SettlementFailureReason2, min=1, max=None, mutex_group=None, array=True),
	))