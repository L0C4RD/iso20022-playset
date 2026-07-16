# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection29
from . import AmountOrRate2Choice
from . import BaseOneRate
from . import CommissionType6Choice
from . import ISODate
from . import PartyIdentification117

class Commission24(base_types._BaseFieldType):

	__slots__ = ["_ClctnDt", "_Comssn", "_RcptId", "_Tp", "_TtlComssn", "_TtlVATAmt", "_VATRate"]
	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@property
	def Comssn(self):
		return self._Comssn

	@Comssn.setter
	def Comssn(self, value):
		self._Comssn = value if value is not None else base_types.UninitialisedField(self, 'Comssn', AmountOrRate2Choice, False)

	@Comssn.deleter
	def Comssn(self):
		del self._Comssn
		self._Comssn = base_types.UninitialisedField(self, 'Comssn', AmountOrRate2Choice, False)

	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if value is not None else base_types.UninitialisedField(self, 'RcptId', PartyIdentification117, False)

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = base_types.UninitialisedField(self, 'RcptId', PartyIdentification117, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CommissionType6Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CommissionType6Choice, False)

	@property
	def TtlComssn(self):
		return self._TtlComssn

	@TtlComssn.setter
	def TtlComssn(self, value):
		self._TtlComssn = value if value is not None else base_types.UninitialisedField(self, 'TtlComssn', AmountAndDirection29, False)

	@TtlComssn.deleter
	def TtlComssn(self):
		del self._TtlComssn
		self._TtlComssn = base_types.UninitialisedField(self, 'TtlComssn', AmountAndDirection29, False)

	@property
	def TtlVATAmt(self):
		return self._TtlVATAmt

	@TtlVATAmt.setter
	def TtlVATAmt(self, value):
		self._TtlVATAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlVATAmt', ActiveCurrencyAndAmount, False)

	@TtlVATAmt.deleter
	def TtlVATAmt(self):
		del self._TtlVATAmt
		self._TtlVATAmt = base_types.UninitialisedField(self, 'TtlVATAmt', ActiveCurrencyAndAmount, False)

	@property
	def VATRate(self):
		return self._VATRate

	@VATRate.setter
	def VATRate(self, value):
		self._VATRate = value if value is not None else base_types.UninitialisedField(self, 'VATRate', BaseOneRate, False)

	@VATRate.deleter
	def VATRate(self):
		del self._VATRate
		self._VATRate = base_types.UninitialisedField(self, 'VATRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Comssn', type=AmountOrRate2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptId', type=PartyIdentification117, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CommissionType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVATAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))