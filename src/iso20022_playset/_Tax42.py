from . import base_types
from ._CountryCode import CountryCode
from ._ExemptionReason1Choice import ExemptionReason1Choice
from ._PartyIdentification139 import PartyIdentification139
from ._TaxAmountOrRate4Choice import TaxAmountOrRate4Choice
from ._TaxCalculationInformation9 import TaxCalculationInformation9
from ._TaxType3Choice import TaxType3Choice
from ._YesNoIndicator import YesNoIndicator

class Tax42(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_RcptId", "_Tax", "_TaxClctnDtls", "_Tp", "_XmptnInd", "_XmptnRsn"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != base_types.auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if type(value) != base_types.auto else self.make_default("RcptId")

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def TaxClctnDtls(self):
		return self._TaxClctnDtls

	@TaxClctnDtls.setter
	def TaxClctnDtls(self, value):
		self._TaxClctnDtls = value if type(value) != base_types.auto else self.make_default("TaxClctnDtls")

	@TaxClctnDtls.deleter
	def TaxClctnDtls(self):
		del self._TaxClctnDtls
		self._TaxClctnDtls = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def XmptnInd(self):
		return self._XmptnInd

	@XmptnInd.setter
	def XmptnInd(self, value):
		self._XmptnInd = value if type(value) != base_types.auto else self.make_default("XmptnInd")

	@XmptnInd.deleter
	def XmptnInd(self):
		del self._XmptnInd
		self._XmptnInd = None

	@property
	def XmptnRsn(self):
		return self._XmptnRsn

	@XmptnRsn.setter
	def XmptnRsn(self, value):
		self._XmptnRsn = value if type(value) != base_types.auto else self.make_default("XmptnRsn")

	@XmptnRsn.deleter
	def XmptnRsn(self):
		del self._XmptnRsn
		self._XmptnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxAmountOrRate4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxClctnDtls', type=TaxCalculationInformation9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptnRsn', type=ExemptionReason1Choice, min=0, max=1, mutex_group=None, array=False),
	))

