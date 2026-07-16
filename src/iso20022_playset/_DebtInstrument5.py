# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BondType1Code
from . import ISODate

class DebtInstrument5(base_types._BaseFieldType):

	__slots__ = ["_IssncDt", "_Tp"]
	@property
	def IssncDt(self):
		return self._IssncDt

	@IssncDt.setter
	def IssncDt(self, value):
		self._IssncDt = value if value is not None else base_types.UninitialisedField(self, 'IssncDt', ISODate, False)

	@IssncDt.deleter
	def IssncDt(self):
		del self._IssncDt
		self._IssncDt = base_types.UninitialisedField(self, 'IssncDt', ISODate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BondType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BondType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssncDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BondType1Code, min=1, max=1, mutex_group=None, array=False),
	))