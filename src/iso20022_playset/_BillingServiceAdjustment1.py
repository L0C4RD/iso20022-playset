# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingSubServiceIdentification1
from . import DecimalNumber
from . import ISODate
from . import Max140Text
from . import Max35Text
from . import ServiceAdjustmentType1Code

class BillingServiceAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_AdjstmntId", "_Amt", "_BalReqrdAmt", "_Desc", "_ErrDt", "_NewChrgAmt", "_NewPric", "_NewVol", "_OrgnlChrgAmt", "_OrgnlPric", "_OrgnlVol", "_PricChng", "_SubSvc", "_Tp", "_VolChng"]
	@property
	def AdjstmntId(self):
		return self._AdjstmntId

	@AdjstmntId.setter
	def AdjstmntId(self, value):
		self._AdjstmntId = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntId', Max35Text, False)

	@AdjstmntId.deleter
	def AdjstmntId(self):
		del self._AdjstmntId
		self._AdjstmntId = base_types.UninitialisedField(self, 'AdjstmntId', Max35Text, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountAndDirection34, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountAndDirection34, False)

	@property
	def BalReqrdAmt(self):
		return self._BalReqrdAmt

	@BalReqrdAmt.setter
	def BalReqrdAmt(self, value):
		self._BalReqrdAmt = value if value is not None else base_types.UninitialisedField(self, 'BalReqrdAmt', AmountAndDirection34, False)

	@BalReqrdAmt.deleter
	def BalReqrdAmt(self):
		del self._BalReqrdAmt
		self._BalReqrdAmt = base_types.UninitialisedField(self, 'BalReqrdAmt', AmountAndDirection34, False)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def ErrDt(self):
		return self._ErrDt

	@ErrDt.setter
	def ErrDt(self, value):
		self._ErrDt = value if value is not None else base_types.UninitialisedField(self, 'ErrDt', ISODate, False)

	@ErrDt.deleter
	def ErrDt(self):
		del self._ErrDt
		self._ErrDt = base_types.UninitialisedField(self, 'ErrDt', ISODate, False)

	@property
	def NewChrgAmt(self):
		return self._NewChrgAmt

	@NewChrgAmt.setter
	def NewChrgAmt(self, value):
		self._NewChrgAmt = value if value is not None else base_types.UninitialisedField(self, 'NewChrgAmt', AmountAndDirection34, False)

	@NewChrgAmt.deleter
	def NewChrgAmt(self):
		del self._NewChrgAmt
		self._NewChrgAmt = base_types.UninitialisedField(self, 'NewChrgAmt', AmountAndDirection34, False)

	@property
	def NewPric(self):
		return self._NewPric

	@NewPric.setter
	def NewPric(self, value):
		self._NewPric = value if value is not None else base_types.UninitialisedField(self, 'NewPric', AmountAndDirection34, False)

	@NewPric.deleter
	def NewPric(self):
		del self._NewPric
		self._NewPric = base_types.UninitialisedField(self, 'NewPric', AmountAndDirection34, False)

	@property
	def NewVol(self):
		return self._NewVol

	@NewVol.setter
	def NewVol(self, value):
		self._NewVol = value if value is not None else base_types.UninitialisedField(self, 'NewVol', DecimalNumber, False)

	@NewVol.deleter
	def NewVol(self):
		del self._NewVol
		self._NewVol = base_types.UninitialisedField(self, 'NewVol', DecimalNumber, False)

	@property
	def OrgnlChrgAmt(self):
		return self._OrgnlChrgAmt

	@OrgnlChrgAmt.setter
	def OrgnlChrgAmt(self, value):
		self._OrgnlChrgAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlChrgAmt', AmountAndDirection34, False)

	@OrgnlChrgAmt.deleter
	def OrgnlChrgAmt(self):
		del self._OrgnlChrgAmt
		self._OrgnlChrgAmt = base_types.UninitialisedField(self, 'OrgnlChrgAmt', AmountAndDirection34, False)

	@property
	def OrgnlPric(self):
		return self._OrgnlPric

	@OrgnlPric.setter
	def OrgnlPric(self, value):
		self._OrgnlPric = value if value is not None else base_types.UninitialisedField(self, 'OrgnlPric', AmountAndDirection34, False)

	@OrgnlPric.deleter
	def OrgnlPric(self):
		del self._OrgnlPric
		self._OrgnlPric = base_types.UninitialisedField(self, 'OrgnlPric', AmountAndDirection34, False)

	@property
	def OrgnlVol(self):
		return self._OrgnlVol

	@OrgnlVol.setter
	def OrgnlVol(self, value):
		self._OrgnlVol = value if value is not None else base_types.UninitialisedField(self, 'OrgnlVol', DecimalNumber, False)

	@OrgnlVol.deleter
	def OrgnlVol(self):
		del self._OrgnlVol
		self._OrgnlVol = base_types.UninitialisedField(self, 'OrgnlVol', DecimalNumber, False)

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if value is not None else base_types.UninitialisedField(self, 'PricChng', AmountAndDirection34, False)

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = base_types.UninitialisedField(self, 'PricChng', AmountAndDirection34, False)

	@property
	def SubSvc(self):
		return self._SubSvc

	@SubSvc.setter
	def SubSvc(self, value):
		self._SubSvc = value if value is not None else base_types.UninitialisedField(self, 'SubSvc', BillingSubServiceIdentification1, False)

	@SubSvc.deleter
	def SubSvc(self):
		del self._SubSvc
		self._SubSvc = base_types.UninitialisedField(self, 'SubSvc', BillingSubServiceIdentification1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ServiceAdjustmentType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ServiceAdjustmentType1Code, False)

	@property
	def VolChng(self):
		return self._VolChng

	@VolChng.setter
	def VolChng(self, value):
		self._VolChng = value if value is not None else base_types.UninitialisedField(self, 'VolChng', DecimalNumber, False)

	@VolChng.deleter
	def VolChng(self):
		del self._VolChng
		self._VolChng = base_types.UninitialisedField(self, 'VolChng', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalReqrdAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewChrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewVol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlVol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubSvc', type=BillingSubServiceIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ServiceAdjustmentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolChng', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))