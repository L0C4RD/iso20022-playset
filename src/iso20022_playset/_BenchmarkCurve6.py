# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BenchmarkCurveName7Choice
from . import DecimalNumber
from . import Max256Text
from . import Price8
from . import SecurityIdentification39

class BenchmarkCurve6(base_types._BaseFieldType):

	__slots__ = ["_BchmkCrvCcy", "_BchmkCrvNm", "_BchmkCrvPt", "_BchmkId", "_BchmkPric", "_Sprd"]
	@property
	def BchmkCrvCcy(self):
		return self._BchmkCrvCcy

	@BchmkCrvCcy.setter
	def BchmkCrvCcy(self, value):
		self._BchmkCrvCcy = value if value is not None else base_types.UninitialisedField(self, 'BchmkCrvCcy', ActiveOrHistoricCurrencyCode, False)

	@BchmkCrvCcy.deleter
	def BchmkCrvCcy(self):
		del self._BchmkCrvCcy
		self._BchmkCrvCcy = base_types.UninitialisedField(self, 'BchmkCrvCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def BchmkCrvNm(self):
		return self._BchmkCrvNm

	@BchmkCrvNm.setter
	def BchmkCrvNm(self, value):
		self._BchmkCrvNm = value if value is not None else base_types.UninitialisedField(self, 'BchmkCrvNm', BenchmarkCurveName7Choice, False)

	@BchmkCrvNm.deleter
	def BchmkCrvNm(self):
		del self._BchmkCrvNm
		self._BchmkCrvNm = base_types.UninitialisedField(self, 'BchmkCrvNm', BenchmarkCurveName7Choice, False)

	@property
	def BchmkCrvPt(self):
		return self._BchmkCrvPt

	@BchmkCrvPt.setter
	def BchmkCrvPt(self, value):
		self._BchmkCrvPt = value if value is not None else base_types.UninitialisedField(self, 'BchmkCrvPt', Max256Text, False)

	@BchmkCrvPt.deleter
	def BchmkCrvPt(self):
		del self._BchmkCrvPt
		self._BchmkCrvPt = base_types.UninitialisedField(self, 'BchmkCrvPt', Max256Text, False)

	@property
	def BchmkId(self):
		return self._BchmkId

	@BchmkId.setter
	def BchmkId(self, value):
		self._BchmkId = value if value is not None else base_types.UninitialisedField(self, 'BchmkId', SecurityIdentification39, False)

	@BchmkId.deleter
	def BchmkId(self):
		del self._BchmkId
		self._BchmkId = base_types.UninitialisedField(self, 'BchmkId', SecurityIdentification39, False)

	@property
	def BchmkPric(self):
		return self._BchmkPric

	@BchmkPric.setter
	def BchmkPric(self, value):
		self._BchmkPric = value if value is not None else base_types.UninitialisedField(self, 'BchmkPric', Price8, False)

	@BchmkPric.deleter
	def BchmkPric(self):
		del self._BchmkPric
		self._BchmkPric = base_types.UninitialisedField(self, 'BchmkPric', Price8, False)

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if value is not None else base_types.UninitialisedField(self, 'Sprd', DecimalNumber, False)

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = base_types.UninitialisedField(self, 'Sprd', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BchmkCrvCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvNm', type=BenchmarkCurveName7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvPt', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))