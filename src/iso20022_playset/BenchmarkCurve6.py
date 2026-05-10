import base_types
import ActiveOrHistoricCurrencyCode
import DecimalNumber
import BenchmarkCurveName7Choice
import SecurityIdentification39
import Price8
import Max256Text

class BenchmarkCurve6(base_types._BaseFieldType):

	__slots__ = ["_BchmkCrvNm", "_Sprd", "_BchmkCrvCcy", "_BchmkId", "_BchmkPric", "_BchmkCrvPt"]
	@property
	def BchmkCrvNm(self):
		return self._BchmkCrvNm

	@BchmkCrvNm.setter
	def BchmkCrvNm(self, value):
		self._BchmkCrvNm = value if type(value) != auto else self.make_default("BchmkCrvNm")

	@BchmkCrvNm.deleter
	def BchmkCrvNm(self):
		del self._BchmkCrvNm
		self._BchmkCrvNm = None

	@property
	def Sprd(self):
		return self._Sprd

	@Sprd.setter
	def Sprd(self, value):
		self._Sprd = value if type(value) != auto else self.make_default("Sprd")

	@Sprd.deleter
	def Sprd(self):
		del self._Sprd
		self._Sprd = None

	@property
	def BchmkCrvCcy(self):
		return self._BchmkCrvCcy

	@BchmkCrvCcy.setter
	def BchmkCrvCcy(self, value):
		self._BchmkCrvCcy = value if type(value) != auto else self.make_default("BchmkCrvCcy")

	@BchmkCrvCcy.deleter
	def BchmkCrvCcy(self):
		del self._BchmkCrvCcy
		self._BchmkCrvCcy = None

	@property
	def BchmkId(self):
		return self._BchmkId

	@BchmkId.setter
	def BchmkId(self, value):
		self._BchmkId = value if type(value) != auto else self.make_default("BchmkId")

	@BchmkId.deleter
	def BchmkId(self):
		del self._BchmkId
		self._BchmkId = None

	@property
	def BchmkPric(self):
		return self._BchmkPric

	@BchmkPric.setter
	def BchmkPric(self, value):
		self._BchmkPric = value if type(value) != auto else self.make_default("BchmkPric")

	@BchmkPric.deleter
	def BchmkPric(self):
		del self._BchmkPric
		self._BchmkPric = None

	@property
	def BchmkCrvPt(self):
		return self._BchmkCrvPt

	@BchmkCrvPt.setter
	def BchmkCrvPt(self, value):
		self._BchmkCrvPt = value if type(value) != auto else self.make_default("BchmkCrvPt")

	@BchmkCrvPt.deleter
	def BchmkCrvPt(self):
		del self._BchmkCrvPt
		self._BchmkCrvPt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BchmkCrvNm', type=BenchmarkCurveName7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sprd', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BchmkCrvPt', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

