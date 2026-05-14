# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._BenchmarkCurveName7Choice import BenchmarkCurveName7Choice
from ._DecimalNumber import DecimalNumber
from ._Max256Text import Max256Text
from ._Price8 import Price8
from ._SecurityIdentification39 import SecurityIdentification39

class BenchmarkCurve6(base_types._BaseFieldType):

	__slots__ = ["_BchmkCrvCcy", "_BchmkCrvNm", "_BchmkCrvPt", "_BchmkId", "_BchmkPric", "_Sprd"]
	@property
	def BchmkCrvCcy(self):
		return self._BchmkCrvCcy

	@BchmkCrvCcy.setter
	def BchmkCrvCcy(self, value):
		self._BchmkCrvCcy = value if type(value) != base_types.auto else self.make_default("BchmkCrvCcy")

	@BchmkCrvCcy.deleter
	def BchmkCrvCcy(self):
		del self._BchmkCrvCcy
		self._BchmkCrvCcy = None

	@property
	def BchmkCrvNm(self):
		return self._BchmkCrvNm

	@BchmkCrvNm.setter
	def BchmkCrvNm(self, value):
		self._BchmkCrvNm = value if type(value) != base_types.auto else self.make_default("BchmkCrvNm")

	@BchmkCrvNm.deleter
	def BchmkCrvNm(self):
		del self._BchmkCrvNm
		self._BchmkCrvNm = None

	@property
	def BchmkCrvPt(self):
		return self._BchmkCrvPt

	@BchmkCrvPt.setter
	def BchmkCrvPt(self, value):
		self._BchmkCrvPt = value if type(value) != base_types.auto else self.make_default("BchmkCrvPt")

	@BchmkCrvPt.deleter
	def BchmkCrvPt(self):
		del self._BchmkCrvPt
		self._BchmkCrvPt = None

	@property
	def BchmkId(self):
		return self._BchmkId

	@BchmkId.setter
	def BchmkId(self, value):
		self._BchmkId = value if type(value) != base_types.auto else self.make_default("BchmkId")

	@BchmkId.deleter
	def BchmkId(self):
		del self._BchmkId
		self._BchmkId = None

	@property
	def BchmkPric(self):
		return self._BchmkPric

	@BchmkPric.setter
	def BchmkPric(self, value):
		self._BchmkPric = value if type(value) != base_types.auto else self.make_default("BchmkPric")

	@BchmkPric.deleter
	def BchmkPric(self):
		del self._BchmkPric
		self._BchmkPric = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != base_types.auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BchmkCrvCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvNm', type=BenchmarkCurveName7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvPt', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))