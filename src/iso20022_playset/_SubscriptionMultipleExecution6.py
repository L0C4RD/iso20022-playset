from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CancellationRight1Choice import CancellationRight1Choice
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._IndividualPerson32 import IndividualPerson32
from ._InvestmentAccount78 import InvestmentAccount78
from ._Max35Text import Max35Text
from ._PaymentTransaction162 import PaymentTransaction162
from ._PlaceOfTradeIdentification4Choice import PlaceOfTradeIdentification4Choice
from ._SubscriptionExecution14 import SubscriptionExecution14
from ._YesNoIndicator import YesNoIndicator

class SubscriptionMultipleExecution6(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_BlkCshSttlmDtls", "_BnfcryDtls", "_CxlRght", "_IndvExctnDtls", "_InvstmtAcctDtls", "_MstrRef", "_OrdrDtTm", "_PlcOfTrad", "_RcvdDtTm", "_ReqdFutrTradDt", "_TtlSttlmAmt"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if type(value) != base_types.auto else self.make_default("AmdmntInd")

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = None

	@property
	def BlkCshSttlmDtls(self):
		return self._BlkCshSttlmDtls

	@BlkCshSttlmDtls.setter
	def BlkCshSttlmDtls(self, value):
		self._BlkCshSttlmDtls = value if type(value) != base_types.auto else self.make_default("BlkCshSttlmDtls")

	@BlkCshSttlmDtls.deleter
	def BlkCshSttlmDtls(self):
		del self._BlkCshSttlmDtls
		self._BlkCshSttlmDtls = None

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if type(value) != base_types.auto else self.make_default("BnfcryDtls")

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = None

	@property
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if type(value) != base_types.auto else self.make_default("CxlRght")

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = None

	@property
	def IndvExctnDtls(self):
		return self._IndvExctnDtls

	@IndvExctnDtls.setter
	def IndvExctnDtls(self, value):
		self._IndvExctnDtls = value if type(value) != base_types.auto else self.make_default("IndvExctnDtls")

	@IndvExctnDtls.deleter
	def IndvExctnDtls(self):
		del self._IndvExctnDtls
		self._IndvExctnDtls = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if type(value) != base_types.auto else self.make_default("OrdrDtTm")

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def RcvdDtTm(self):
		return self._RcvdDtTm

	@RcvdDtTm.setter
	def RcvdDtTm(self, value):
		self._RcvdDtTm = value if type(value) != base_types.auto else self.make_default("RcvdDtTm")

	@RcvdDtTm.deleter
	def RcvdDtTm(self):
		del self._RcvdDtTm
		self._RcvdDtTm = None

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if type(value) != base_types.auto else self.make_default("ReqdFutrTradDt")

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = None

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if type(value) != base_types.auto else self.make_default("TtlSttlmAmt")

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlkCshSttlmDtls', type=PaymentTransaction162, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvExctnDtls', type=SubscriptionExecution14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount78, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

