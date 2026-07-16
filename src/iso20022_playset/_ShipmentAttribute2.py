# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import ShipmentCondition1Choice

class ShipmentAttribute2(base_types._BaseFieldType):

	__slots__ = ["_Conds", "_CtryOfCntrPty", "_XpctdDt"]
	@property
	def Conds(self):
		return self._Conds

	@Conds.setter
	def Conds(self, value):
		self._Conds = value if value is not None else base_types.UninitialisedField(self, 'Conds', ShipmentCondition1Choice, False)

	@Conds.deleter
	def Conds(self):
		del self._Conds
		self._Conds = base_types.UninitialisedField(self, 'Conds', ShipmentCondition1Choice, False)

	@property
	def CtryOfCntrPty(self):
		return self._CtryOfCntrPty

	@CtryOfCntrPty.setter
	def CtryOfCntrPty(self, value):
		self._CtryOfCntrPty = value if value is not None else base_types.UninitialisedField(self, 'CtryOfCntrPty', CountryCode, False)

	@CtryOfCntrPty.deleter
	def CtryOfCntrPty(self):
		del self._CtryOfCntrPty
		self._CtryOfCntrPty = base_types.UninitialisedField(self, 'CtryOfCntrPty', CountryCode, False)

	@property
	def XpctdDt(self):
		return self._XpctdDt

	@XpctdDt.setter
	def XpctdDt(self, value):
		self._XpctdDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	@XpctdDt.deleter
	def XpctdDt(self):
		del self._XpctdDt
		self._XpctdDt = base_types.UninitialisedField(self, 'XpctdDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Conds', type=ShipmentCondition1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfCntrPty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))