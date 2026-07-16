# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ExposureType13Code
from . import ISODate
from . import ISODateTime
from . import ShortLong1Code
from . import SummaryAmounts2

class Summary3(base_types._BaseFieldType):

	__slots__ = ["_NetXcssDfcit", "_NetXcssDfcitInd", "_ReqdSttlmDt", "_SummryDtls", "_TtlValOfColl", "_ValtnDtTm", "_XpsdAmtPtyA", "_XpsdAmtPtyB", "_XpsrTp"]
	@property
	def NetXcssDfcit(self):
		return self._NetXcssDfcit

	@NetXcssDfcit.setter
	def NetXcssDfcit(self, value):
		self._NetXcssDfcit = value if value is not None else base_types.UninitialisedField(self, 'NetXcssDfcit', ActiveCurrencyAndAmount, False)

	@NetXcssDfcit.deleter
	def NetXcssDfcit(self):
		del self._NetXcssDfcit
		self._NetXcssDfcit = base_types.UninitialisedField(self, 'NetXcssDfcit', ActiveCurrencyAndAmount, False)

	@property
	def NetXcssDfcitInd(self):
		return self._NetXcssDfcitInd

	@NetXcssDfcitInd.setter
	def NetXcssDfcitInd(self, value):
		self._NetXcssDfcitInd = value if value is not None else base_types.UninitialisedField(self, 'NetXcssDfcitInd', ShortLong1Code, False)

	@NetXcssDfcitInd.deleter
	def NetXcssDfcitInd(self):
		del self._NetXcssDfcitInd
		self._NetXcssDfcitInd = base_types.UninitialisedField(self, 'NetXcssDfcitInd', ShortLong1Code, False)

	@property
	def ReqdSttlmDt(self):
		return self._ReqdSttlmDt

	@ReqdSttlmDt.setter
	def ReqdSttlmDt(self, value):
		self._ReqdSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@ReqdSttlmDt.deleter
	def ReqdSttlmDt(self):
		del self._ReqdSttlmDt
		self._ReqdSttlmDt = base_types.UninitialisedField(self, 'ReqdSttlmDt', ISODate, False)

	@property
	def SummryDtls(self):
		return self._SummryDtls

	@SummryDtls.setter
	def SummryDtls(self, value):
		self._SummryDtls = value if value is not None else base_types.UninitialisedField(self, 'SummryDtls', SummaryAmounts2, False)

	@SummryDtls.deleter
	def SummryDtls(self):
		del self._SummryDtls
		self._SummryDtls = base_types.UninitialisedField(self, 'SummryDtls', SummaryAmounts2, False)

	@property
	def TtlValOfColl(self):
		return self._TtlValOfColl

	@TtlValOfColl.setter
	def TtlValOfColl(self, value):
		self._TtlValOfColl = value if value is not None else base_types.UninitialisedField(self, 'TtlValOfColl', ActiveCurrencyAndAmount, False)

	@TtlValOfColl.deleter
	def TtlValOfColl(self):
		del self._TtlValOfColl
		self._TtlValOfColl = base_types.UninitialisedField(self, 'TtlValOfColl', ActiveCurrencyAndAmount, False)

	@property
	def ValtnDtTm(self):
		return self._ValtnDtTm

	@ValtnDtTm.setter
	def ValtnDtTm(self, value):
		self._ValtnDtTm = value if value is not None else base_types.UninitialisedField(self, 'ValtnDtTm', ISODateTime, False)

	@ValtnDtTm.deleter
	def ValtnDtTm(self):
		del self._ValtnDtTm
		self._ValtnDtTm = base_types.UninitialisedField(self, 'ValtnDtTm', ISODateTime, False)

	@property
	def XpsdAmtPtyA(self):
		return self._XpsdAmtPtyA

	@XpsdAmtPtyA.setter
	def XpsdAmtPtyA(self, value):
		self._XpsdAmtPtyA = value if value is not None else base_types.UninitialisedField(self, 'XpsdAmtPtyA', ActiveCurrencyAndAmount, False)

	@XpsdAmtPtyA.deleter
	def XpsdAmtPtyA(self):
		del self._XpsdAmtPtyA
		self._XpsdAmtPtyA = base_types.UninitialisedField(self, 'XpsdAmtPtyA', ActiveCurrencyAndAmount, False)

	@property
	def XpsdAmtPtyB(self):
		return self._XpsdAmtPtyB

	@XpsdAmtPtyB.setter
	def XpsdAmtPtyB(self, value):
		self._XpsdAmtPtyB = value if value is not None else base_types.UninitialisedField(self, 'XpsdAmtPtyB', ActiveCurrencyAndAmount, False)

	@XpsdAmtPtyB.deleter
	def XpsdAmtPtyB(self):
		del self._XpsdAmtPtyB
		self._XpsdAmtPtyB = base_types.UninitialisedField(self, 'XpsdAmtPtyB', ActiveCurrencyAndAmount, False)

	@property
	def XpsrTp(self):
		return self._XpsrTp

	@XpsrTp.setter
	def XpsrTp(self, value):
		self._XpsrTp = value if value is not None else base_types.UninitialisedField(self, 'XpsrTp', ExposureType13Code, False)

	@XpsrTp.deleter
	def XpsrTp(self):
		del self._XpsrTp
		self._XpsrTp = base_types.UninitialisedField(self, 'XpsrTp', ExposureType13Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetXcssDfcit', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXcssDfcitInd', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryDtls', type=SummaryAmounts2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlValOfColl', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrTp', type=ExposureType13Code, min=1, max=1, mutex_group=None, array=False),
	))