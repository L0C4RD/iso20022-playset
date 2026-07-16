# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ChargeBasis2Choice
from . import ChargeOrCommissionDiscount1
from . import ChargeType10Choice
from . import Max35Text
from . import PartyIdentification139
from . import PercentageRate

class Fee9(base_types._BaseFieldType):

	__slots__ = ["_Bsis", "_DscntDtls", "_NonStdSLARef", "_RcptId", "_ReqdAmt", "_ReqdRate", "_StdAmt", "_StdRate", "_Tp"]
	@property
	def Bsis(self):
		return self._Bsis

	@Bsis.setter
	def Bsis(self, value):
		self._Bsis = value if value is not None else base_types.UninitialisedField(self, 'Bsis', ChargeBasis2Choice, False)

	@Bsis.deleter
	def Bsis(self):
		del self._Bsis
		self._Bsis = base_types.UninitialisedField(self, 'Bsis', ChargeBasis2Choice, False)

	@property
	def DscntDtls(self):
		return self._DscntDtls

	@DscntDtls.setter
	def DscntDtls(self, value):
		self._DscntDtls = value if value is not None else base_types.UninitialisedField(self, 'DscntDtls', ChargeOrCommissionDiscount1, False)

	@DscntDtls.deleter
	def DscntDtls(self):
		del self._DscntDtls
		self._DscntDtls = base_types.UninitialisedField(self, 'DscntDtls', ChargeOrCommissionDiscount1, False)

	@property
	def NonStdSLARef(self):
		return self._NonStdSLARef

	@NonStdSLARef.setter
	def NonStdSLARef(self, value):
		self._NonStdSLARef = value if value is not None else base_types.UninitialisedField(self, 'NonStdSLARef', Max35Text, False)

	@NonStdSLARef.deleter
	def NonStdSLARef(self):
		del self._NonStdSLARef
		self._NonStdSLARef = base_types.UninitialisedField(self, 'NonStdSLARef', Max35Text, False)

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if value is not None else base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = base_types.UninitialisedField(self, 'RcptId', PartyIdentification139, False)

	@property
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'ReqdAmt', ActiveCurrencyAndAmount, False)

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = base_types.UninitialisedField(self, 'ReqdAmt', ActiveCurrencyAndAmount, False)

	@property
	def ReqdRate(self):
		return self._ReqdRate

	@ReqdRate.setter
	def ReqdRate(self, value):
		self._ReqdRate = value if value is not None else base_types.UninitialisedField(self, 'ReqdRate', PercentageRate, False)

	@ReqdRate.deleter
	def ReqdRate(self):
		del self._ReqdRate
		self._ReqdRate = base_types.UninitialisedField(self, 'ReqdRate', PercentageRate, False)

	@property
	def StdAmt(self):
		return self._StdAmt

	@StdAmt.setter
	def StdAmt(self, value):
		self._StdAmt = value if value is not None else base_types.UninitialisedField(self, 'StdAmt', ActiveCurrencyAndAmount, False)

	@StdAmt.deleter
	def StdAmt(self):
		del self._StdAmt
		self._StdAmt = base_types.UninitialisedField(self, 'StdAmt', ActiveCurrencyAndAmount, False)

	@property
	def StdRate(self):
		return self._StdRate

	@StdRate.setter
	def StdRate(self, value):
		self._StdRate = value if value is not None else base_types.UninitialisedField(self, 'StdRate', PercentageRate, False)

	@StdRate.deleter
	def StdRate(self):
		del self._StdRate
		self._StdRate = base_types.UninitialisedField(self, 'StdRate', PercentageRate, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType10Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType10Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bsis', type=ChargeBasis2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntDtls', type=ChargeOrCommissionDiscount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSLARef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StdRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType10Choice, min=1, max=1, mutex_group=None, array=False),
	))