from . import base_types
import ISODate
import PlaceOfTradeIdentification1Choice
import IndividualPerson32
import RedemptionOrder14
import ISODateTime
import InvestmentAccount58
import DateAndDateTimeChoice
import Max35Text
import ActiveCurrencyAndAmount
import PaymentTransaction72
import CancellationRight1Choice

class RedemptionMultipleOrder6(base_types._BaseFieldType):

	__slots__ = ["_CxlRght", "_BlkCshSttlmDtls", "_MstrRef", "_InvstmtAcctDtls", "_TtlSttlmAmt", "_OrdrDtTm", "_ReqdFutrTradDt", "_XpryDtTm", "_PlcOfTrad", "_BnfcryDtls", "_IndvOrdrDtls"]
	@property
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if type(value) != auto else self.make_default("CxlRght")

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = None

	@property
	def BlkCshSttlmDtls(self):
		return self._BlkCshSttlmDtls

	@BlkCshSttlmDtls.setter
	def BlkCshSttlmDtls(self, value):
		self._BlkCshSttlmDtls = value if type(value) != auto else self.make_default("BlkCshSttlmDtls")

	@BlkCshSttlmDtls.deleter
	def BlkCshSttlmDtls(self):
		del self._BlkCshSttlmDtls
		self._BlkCshSttlmDtls = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if type(value) != auto else self.make_default("TtlSttlmAmt")

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = None

	@property
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if type(value) != auto else self.make_default("OrdrDtTm")

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = None

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if type(value) != auto else self.make_default("ReqdFutrTradDt")

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = None

	@property
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if type(value) != auto else self.make_default("XpryDtTm")

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if type(value) != auto else self.make_default("BnfcryDtls")

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = None

	@property
	def IndvOrdrDtls(self):
		return self._IndvOrdrDtls

	@IndvOrdrDtls.setter
	def IndvOrdrDtls(self, value):
		self._IndvOrdrDtls = value if type(value) != auto else self.make_default("IndvOrdrDtls")

	@IndvOrdrDtls.deleter
	def IndvOrdrDtls(self):
		del self._IndvOrdrDtls
		self._IndvOrdrDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BlkCshSttlmDtls', type=PaymentTransaction72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlSttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvOrdrDtls', type=RedemptionOrder14, min=1, max=None, mutex_group=None, array=True),
	))

