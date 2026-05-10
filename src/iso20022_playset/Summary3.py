from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .SummaryAmounts2 import SummaryAmounts2
from .ISODateTime import ISODateTime
from .ISODate import ISODate
from .ExposureType13Code import ExposureType13Code
from .ShortLong1Code import ShortLong1Code

class Summary3(base_types._BaseFieldType):

	__slots__ = ["_SummryDtls", "_NetXcssDfcitInd", "_NetXcssDfcit", "_XpsdAmtPtyA", "_XpsrTp", "_XpsdAmtPtyB", "_ReqdSttlmDt", "_ValtnDtTm", "_TtlValOfColl"]
	@property
	def SummryDtls(self):
		return self._SummryDtls

	@SummryDtls.setter
	def SummryDtls(self, value):
		self._SummryDtls = value if type(value) != base_types.auto else self.make_default("SummryDtls")

	@SummryDtls.deleter
	def SummryDtls(self):
		del self._SummryDtls
		self._SummryDtls = None

	@property
	def NetXcssDfcitInd(self):
		return self._NetXcssDfcitInd

	@NetXcssDfcitInd.setter
	def NetXcssDfcitInd(self, value):
		self._NetXcssDfcitInd = value if type(value) != base_types.auto else self.make_default("NetXcssDfcitInd")

	@NetXcssDfcitInd.deleter
	def NetXcssDfcitInd(self):
		del self._NetXcssDfcitInd
		self._NetXcssDfcitInd = None

	@property
	def NetXcssDfcit(self):
		return self._NetXcssDfcit

	@NetXcssDfcit.setter
	def NetXcssDfcit(self, value):
		self._NetXcssDfcit = value if type(value) != base_types.auto else self.make_default("NetXcssDfcit")

	@NetXcssDfcit.deleter
	def NetXcssDfcit(self):
		del self._NetXcssDfcit
		self._NetXcssDfcit = None

	@property
	def XpsdAmtPtyA(self):
		return self._XpsdAmtPtyA

	@XpsdAmtPtyA.setter
	def XpsdAmtPtyA(self, value):
		self._XpsdAmtPtyA = value if type(value) != base_types.auto else self.make_default("XpsdAmtPtyA")

	@XpsdAmtPtyA.deleter
	def XpsdAmtPtyA(self):
		del self._XpsdAmtPtyA
		self._XpsdAmtPtyA = None

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if type(value) != base_types.auto else self.make_default("XpsrTp")

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = None

	@property
	def XpsdAmtPtyB(self):
		return self._XpsdAmtPtyB

	@XpsdAmtPtyB.setter
	def XpsdAmtPtyB(self, value):
		self._XpsdAmtPtyB = value if type(value) != base_types.auto else self.make_default("XpsdAmtPtyB")

	@XpsdAmtPtyB.deleter
	def XpsdAmtPtyB(self):
		del self._XpsdAmtPtyB
		self._XpsdAmtPtyB = None

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if type(value) != base_types.auto else self.make_default("ReqdSttlmDt")

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = None

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if type(value) != base_types.auto else self.make_default("ValtnDtTm")

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = None

	@property
	def TtlValOfColl(self):
		return self._TtlValOfColl

	@TtlValOfColl.setter
	def TtlValOfColl(self, value):
		self._TtlValOfColl = value if type(value) != base_types.auto else self.make_default("TtlValOfColl")

	@TtlValOfColl.deleter
	def TtlValOfColl(self):
		del self._TtlValOfColl
		self._TtlValOfColl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SummryDtls', type=SummaryAmounts2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXcssDfcitInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXcssDfcit', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType13Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfColl', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

