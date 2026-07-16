# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeSearch5Choice
from . import IntraBalanceStatusType2

class IntraBalanceQueryStatus3(base_types._BaseFieldType):

	__slots__ = ["_DtPrd", "_Tp"]
	@property
	def DtPrd(self):
		return self._DtPrd

	@DtPrd.setter
	def DtPrd(self, value):
		self._DtPrd = value if value is not None else base_types.UninitialisedField(self, 'DtPrd', DateAndDateTimeSearch5Choice, False)

	@DtPrd.deleter
	def DtPrd(self):
		del self._DtPrd
		self._DtPrd = base_types.UninitialisedField(self, 'DtPrd', DateAndDateTimeSearch5Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', IntraBalanceStatusType2, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', IntraBalanceStatusType2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtPrd', type=DateAndDateTimeSearch5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IntraBalanceStatusType2, min=1, max=1, mutex_group=None, array=False),
	))