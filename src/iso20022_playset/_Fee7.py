# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ChargeBasis2Choice
from . import ChargeBearer1Code
from . import ChargeOrCommissionDiscount2
from . import ChargeType6Choice
from . import PartyIdentification139

class Fee7(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Bsis", "_ChrgBr", "_DscntDtls", "_RcptId", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

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
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if value is not None else base_types.UninitialisedField(self, 'ChrgBr', ChargeBearer1Code, False)

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = base_types.UninitialisedField(self, 'ChrgBr', ChargeBearer1Code, False)

	@property
	def DscntDtls(self):
		return self._DscntDtls

	@DscntDtls.setter
	def DscntDtls(self, value):
		self._DscntDtls = value if value is not None else base_types.UninitialisedField(self, 'DscntDtls', ChargeOrCommissionDiscount2, False)

	@DscntDtls.deleter
	def DscntDtls(self):
		del self._DscntDtls
		self._DscntDtls = base_types.UninitialisedField(self, 'DscntDtls', ChargeOrCommissionDiscount2, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType6Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bsis', type=ChargeBasis2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearer1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DscntDtls', type=ChargeOrCommissionDiscount2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification139, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ChargeType6Choice, min=1, max=1, mutex_group=None, array=False),
	))