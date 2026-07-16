# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CancellationRight1Choice
from . import ISODate
from . import ISODateTime
from . import IndividualPerson32
from . import InvestmentAccount78
from . import Max35Text
from . import PaymentTransaction162
from . import PlaceOfTradeIdentification4Choice
from . import SubscriptionExecution14
from . import YesNoIndicator

class SubscriptionMultipleExecution6(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_BlkCshSttlmDtls", "_BnfcryDtls", "_CxlRght", "_IndvExctnDtls", "_InvstmtAcctDtls", "_MstrRef", "_OrdrDtTm", "_PlcOfTrad", "_RcvdDtTm", "_ReqdFutrTradDt", "_TtlSttlmAmt"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if value is not None else base_types.UninitialisedField(self, 'AmdmntInd', YesNoIndicator, False)

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = base_types.UninitialisedField(self, 'AmdmntInd', YesNoIndicator, False)

	@property
	def BlkCshSttlmDtls(self):
		return self._BlkCshSttlmDtls

	@BlkCshSttlmDtls.setter
	def BlkCshSttlmDtls(self, value):
		self._BlkCshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'BlkCshSttlmDtls', PaymentTransaction162, False)

	@BlkCshSttlmDtls.deleter
	def BlkCshSttlmDtls(self):
		del self._BlkCshSttlmDtls
		self._BlkCshSttlmDtls = base_types.UninitialisedField(self, 'BlkCshSttlmDtls', PaymentTransaction162, False)

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson32, True)

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson32, True)

	@property
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if value is not None else base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

	@property
	def IndvExctnDtls(self):
		return self._IndvExctnDtls

	@IndvExctnDtls.setter
	def IndvExctnDtls(self, value):
		self._IndvExctnDtls = value if value is not None else base_types.UninitialisedField(self, 'IndvExctnDtls', SubscriptionExecution14, True)

	@IndvExctnDtls.deleter
	def IndvExctnDtls(self):
		del self._IndvExctnDtls
		self._IndvExctnDtls = base_types.UninitialisedField(self, 'IndvExctnDtls', SubscriptionExecution14, True)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount78, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount78, False)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification4Choice, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification4Choice, False)

	@property
	def RcvdDtTm(self):
		return self._RcvdDtTm

	@RcvdDtTm.setter
	def RcvdDtTm(self, value):
		self._RcvdDtTm = value if value is not None else base_types.UninitialisedField(self, 'RcvdDtTm', ISODateTime, False)

	@RcvdDtTm.deleter
	def RcvdDtTm(self):
		del self._RcvdDtTm
		self._RcvdDtTm = base_types.UninitialisedField(self, 'RcvdDtTm', ISODateTime, False)

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

	@property
	def TtlSttlmAmt(self):
		return self._TtlSttlmAmt

	@TtlSttlmAmt.setter
	def TtlSttlmAmt(self, value):
		self._TtlSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlSttlmAmt', ActiveCurrencyAndAmount, False)

	@TtlSttlmAmt.deleter
	def TtlSttlmAmt(self):
		del self._TtlSttlmAmt
		self._TtlSttlmAmt = base_types.UninitialisedField(self, 'TtlSttlmAmt', ActiveCurrencyAndAmount, False)

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