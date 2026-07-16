# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ContractRegistrationReference2Choice
from . import ISODate
from . import Max1025Text

class TransactionCertificateContract2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CtrctRef", "_TxAmtInCtrctCcy", "_XpctdAdvncPmtRtrDt", "_XpctdShipmntDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max1025Text, False)

	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if value is not None else base_types.UninitialisedField(self, 'CtrctRef', ContractRegistrationReference2Choice, False)

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = base_types.UninitialisedField(self, 'CtrctRef', ContractRegistrationReference2Choice, False)

	@property
	def TxAmtInCtrctCcy(self):
		return self._TxAmtInCtrctCcy

	@TxAmtInCtrctCcy.setter
	def TxAmtInCtrctCcy(self, value):
		self._TxAmtInCtrctCcy = value if value is not None else base_types.UninitialisedField(self, 'TxAmtInCtrctCcy', ActiveCurrencyAndAmount, False)

	@TxAmtInCtrctCcy.deleter
	def TxAmtInCtrctCcy(self):
		del self._TxAmtInCtrctCcy
		self._TxAmtInCtrctCcy = base_types.UninitialisedField(self, 'TxAmtInCtrctCcy', ActiveCurrencyAndAmount, False)

	@property
	def XpctdAdvncPmtRtrDt(self):
		return self._XpctdAdvncPmtRtrDt

	@XpctdAdvncPmtRtrDt.setter
	def XpctdAdvncPmtRtrDt(self, value):
		self._XpctdAdvncPmtRtrDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdAdvncPmtRtrDt', ISODate, False)

	@XpctdAdvncPmtRtrDt.deleter
	def XpctdAdvncPmtRtrDt(self):
		del self._XpctdAdvncPmtRtrDt
		self._XpctdAdvncPmtRtrDt = base_types.UninitialisedField(self, 'XpctdAdvncPmtRtrDt', ISODate, False)

	@property
	def XpctdShipmntDt(self):
		return self._XpctdShipmntDt

	@XpctdShipmntDt.setter
	def XpctdShipmntDt(self, value):
		self._XpctdShipmntDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdShipmntDt', ISODate, False)

	@XpctdShipmntDt.deleter
	def XpctdShipmntDt(self):
		del self._XpctdShipmntDt
		self._XpctdShipmntDt = base_types.UninitialisedField(self, 'XpctdShipmntDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctRef', type=ContractRegistrationReference2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmtInCtrctCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdAdvncPmtRtrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdShipmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))