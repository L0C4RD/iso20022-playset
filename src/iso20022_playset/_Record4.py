# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingMethod3Code
from . import CreditDebit3Code
from . import ISO3NumericCountryCode
from . import ISO3NumericCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max140Binary
from . import Max35Text
from . import Number
from . import OtherAmount5
from . import RecordMessage2Choice

class Record4(base_types._BaseFieldType):

	__slots__ = ["_AgtFeeAmt", "_AgtFeeCcy", "_AgtFeeCdtDbt", "_ClrAmt", "_ClrCcy", "_ClrCdtDbt", "_ClrDt", "_ClrMtd", "_ClrPrty", "_DstnAssgnr", "_DstnCtry", "_DstnId", "_DstnShrtNm", "_IntrchngFeeAmt", "_IntrchngFeeCcy", "_IntrchngFeeCdtDbt", "_OrgtrAssgnr", "_OrgtrCtry", "_OrgtrId", "_OrgtrShrtNm", "_OthrAmt", "_RcrdChcksmInptVal", "_RcrdMsg", "_SeqCntr"]
	@property
	def AgtFeeAmt(self):
		return self._AgtFeeAmt

	@AgtFeeAmt.setter
	def AgtFeeAmt(self, value):
		self._AgtFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeAmt', ImpliedCurrencyAndAmount, False)

	@AgtFeeAmt.deleter
	def AgtFeeAmt(self):
		del self._AgtFeeAmt
		self._AgtFeeAmt = base_types.UninitialisedField(self, 'AgtFeeAmt', ImpliedCurrencyAndAmount, False)

	@property
	def AgtFeeCcy(self):
		return self._AgtFeeCcy

	@AgtFeeCcy.setter
	def AgtFeeCcy(self, value):
		self._AgtFeeCcy = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeCcy', ISO3NumericCurrencyCode, False)

	@AgtFeeCcy.deleter
	def AgtFeeCcy(self):
		del self._AgtFeeCcy
		self._AgtFeeCcy = base_types.UninitialisedField(self, 'AgtFeeCcy', ISO3NumericCurrencyCode, False)

	@property
	def AgtFeeCdtDbt(self):
		return self._AgtFeeCdtDbt

	@AgtFeeCdtDbt.setter
	def AgtFeeCdtDbt(self, value):
		self._AgtFeeCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'AgtFeeCdtDbt', CreditDebit3Code, False)

	@AgtFeeCdtDbt.deleter
	def AgtFeeCdtDbt(self):
		del self._AgtFeeCdtDbt
		self._AgtFeeCdtDbt = base_types.UninitialisedField(self, 'AgtFeeCdtDbt', CreditDebit3Code, False)

	@property
	def ClrAmt(self):
		return self._ClrAmt

	@ClrAmt.setter
	def ClrAmt(self, value):
		self._ClrAmt = value if value is not None else base_types.UninitialisedField(self, 'ClrAmt', ImpliedCurrencyAndAmount, False)

	@ClrAmt.deleter
	def ClrAmt(self):
		del self._ClrAmt
		self._ClrAmt = base_types.UninitialisedField(self, 'ClrAmt', ImpliedCurrencyAndAmount, False)

	@property
	def ClrCcy(self):
		return self._ClrCcy

	@ClrCcy.setter
	def ClrCcy(self, value):
		self._ClrCcy = value if value is not None else base_types.UninitialisedField(self, 'ClrCcy', ISO3NumericCurrencyCode, False)

	@ClrCcy.deleter
	def ClrCcy(self):
		del self._ClrCcy
		self._ClrCcy = base_types.UninitialisedField(self, 'ClrCcy', ISO3NumericCurrencyCode, False)

	@property
	def ClrCdtDbt(self):
		return self._ClrCdtDbt

	@ClrCdtDbt.setter
	def ClrCdtDbt(self, value):
		self._ClrCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'ClrCdtDbt', CreditDebit3Code, False)

	@ClrCdtDbt.deleter
	def ClrCdtDbt(self):
		del self._ClrCdtDbt
		self._ClrCdtDbt = base_types.UninitialisedField(self, 'ClrCdtDbt', CreditDebit3Code, False)

	@property
	def ClrDt(self):
		return self._ClrDt

	@ClrDt.setter
	def ClrDt(self, value):
		self._ClrDt = value if value is not None else base_types.UninitialisedField(self, 'ClrDt', ISODate, False)

	@ClrDt.deleter
	def ClrDt(self):
		del self._ClrDt
		self._ClrDt = base_types.UninitialisedField(self, 'ClrDt', ISODate, False)

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if value is not None else base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod3Code, False)

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = base_types.UninitialisedField(self, 'ClrMtd', ClearingMethod3Code, False)

	@property
	def ClrPrty(self):
		return self._ClrPrty

	@ClrPrty.setter
	def ClrPrty(self, value):
		self._ClrPrty = value if value is not None else base_types.UninitialisedField(self, 'ClrPrty', Max35Text, False)

	@ClrPrty.deleter
	def ClrPrty(self):
		del self._ClrPrty
		self._ClrPrty = base_types.UninitialisedField(self, 'ClrPrty', Max35Text, False)

	@property
	def DstnAssgnr(self):
		return self._DstnAssgnr

	@DstnAssgnr.setter
	def DstnAssgnr(self, value):
		self._DstnAssgnr = value if value is not None else base_types.UninitialisedField(self, 'DstnAssgnr', Max35Text, False)

	@DstnAssgnr.deleter
	def DstnAssgnr(self):
		del self._DstnAssgnr
		self._DstnAssgnr = base_types.UninitialisedField(self, 'DstnAssgnr', Max35Text, False)

	@property
	def DstnCtry(self):
		return self._DstnCtry

	@DstnCtry.setter
	def DstnCtry(self, value):
		self._DstnCtry = value if value is not None else base_types.UninitialisedField(self, 'DstnCtry', ISO3NumericCountryCode, False)

	@DstnCtry.deleter
	def DstnCtry(self):
		del self._DstnCtry
		self._DstnCtry = base_types.UninitialisedField(self, 'DstnCtry', ISO3NumericCountryCode, False)

	@property
	def DstnId(self):
		return self._DstnId

	@DstnId.setter
	def DstnId(self, value):
		self._DstnId = value if value is not None else base_types.UninitialisedField(self, 'DstnId', Max35Text, False)

	@DstnId.deleter
	def DstnId(self):
		del self._DstnId
		self._DstnId = base_types.UninitialisedField(self, 'DstnId', Max35Text, False)

	@property
	def DstnShrtNm(self):
		return self._DstnShrtNm

	@DstnShrtNm.setter
	def DstnShrtNm(self, value):
		self._DstnShrtNm = value if value is not None else base_types.UninitialisedField(self, 'DstnShrtNm', Max35Text, False)

	@DstnShrtNm.deleter
	def DstnShrtNm(self):
		del self._DstnShrtNm
		self._DstnShrtNm = base_types.UninitialisedField(self, 'DstnShrtNm', Max35Text, False)

	@property
	def IntrchngFeeAmt(self):
		return self._IntrchngFeeAmt

	@IntrchngFeeAmt.setter
	def IntrchngFeeAmt(self, value):
		self._IntrchngFeeAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeAmt', ImpliedCurrencyAndAmount, False)

	@IntrchngFeeAmt.deleter
	def IntrchngFeeAmt(self):
		del self._IntrchngFeeAmt
		self._IntrchngFeeAmt = base_types.UninitialisedField(self, 'IntrchngFeeAmt', ImpliedCurrencyAndAmount, False)

	@property
	def IntrchngFeeCcy(self):
		return self._IntrchngFeeCcy

	@IntrchngFeeCcy.setter
	def IntrchngFeeCcy(self, value):
		self._IntrchngFeeCcy = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeCcy', ISO3NumericCurrencyCode, False)

	@IntrchngFeeCcy.deleter
	def IntrchngFeeCcy(self):
		del self._IntrchngFeeCcy
		self._IntrchngFeeCcy = base_types.UninitialisedField(self, 'IntrchngFeeCcy', ISO3NumericCurrencyCode, False)

	@property
	def IntrchngFeeCdtDbt(self):
		return self._IntrchngFeeCdtDbt

	@IntrchngFeeCdtDbt.setter
	def IntrchngFeeCdtDbt(self, value):
		self._IntrchngFeeCdtDbt = value if value is not None else base_types.UninitialisedField(self, 'IntrchngFeeCdtDbt', CreditDebit3Code, False)

	@IntrchngFeeCdtDbt.deleter
	def IntrchngFeeCdtDbt(self):
		del self._IntrchngFeeCdtDbt
		self._IntrchngFeeCdtDbt = base_types.UninitialisedField(self, 'IntrchngFeeCdtDbt', CreditDebit3Code, False)

	@property
	def OrgtrAssgnr(self):
		return self._OrgtrAssgnr

	@OrgtrAssgnr.setter
	def OrgtrAssgnr(self, value):
		self._OrgtrAssgnr = value if value is not None else base_types.UninitialisedField(self, 'OrgtrAssgnr', Max35Text, False)

	@OrgtrAssgnr.deleter
	def OrgtrAssgnr(self):
		del self._OrgtrAssgnr
		self._OrgtrAssgnr = base_types.UninitialisedField(self, 'OrgtrAssgnr', Max35Text, False)

	@property
	def OrgtrCtry(self):
		return self._OrgtrCtry

	@OrgtrCtry.setter
	def OrgtrCtry(self, value):
		self._OrgtrCtry = value if value is not None else base_types.UninitialisedField(self, 'OrgtrCtry', ISO3NumericCountryCode, False)

	@OrgtrCtry.deleter
	def OrgtrCtry(self):
		del self._OrgtrCtry
		self._OrgtrCtry = base_types.UninitialisedField(self, 'OrgtrCtry', ISO3NumericCountryCode, False)

	@property
	def OrgtrId(self):
		return self._OrgtrId

	@OrgtrId.setter
	def OrgtrId(self, value):
		self._OrgtrId = value if value is not None else base_types.UninitialisedField(self, 'OrgtrId', Max35Text, False)

	@OrgtrId.deleter
	def OrgtrId(self):
		del self._OrgtrId
		self._OrgtrId = base_types.UninitialisedField(self, 'OrgtrId', Max35Text, False)

	@property
	def OrgtrShrtNm(self):
		return self._OrgtrShrtNm

	@OrgtrShrtNm.setter
	def OrgtrShrtNm(self, value):
		self._OrgtrShrtNm = value if value is not None else base_types.UninitialisedField(self, 'OrgtrShrtNm', Max35Text, False)

	@OrgtrShrtNm.deleter
	def OrgtrShrtNm(self):
		del self._OrgtrShrtNm
		self._OrgtrShrtNm = base_types.UninitialisedField(self, 'OrgtrShrtNm', Max35Text, False)

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if value is not None else base_types.UninitialisedField(self, 'OthrAmt', OtherAmount5, False)

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = base_types.UninitialisedField(self, 'OthrAmt', OtherAmount5, False)

	@property
	def RcrdChcksmInptVal(self):
		return self._RcrdChcksmInptVal

	@RcrdChcksmInptVal.setter
	def RcrdChcksmInptVal(self, value):
		self._RcrdChcksmInptVal = value if value is not None else base_types.UninitialisedField(self, 'RcrdChcksmInptVal', Max140Binary, False)

	@RcrdChcksmInptVal.deleter
	def RcrdChcksmInptVal(self):
		del self._RcrdChcksmInptVal
		self._RcrdChcksmInptVal = base_types.UninitialisedField(self, 'RcrdChcksmInptVal', Max140Binary, False)

	@property
	def RcrdMsg(self):
		return self._RcrdMsg

	@RcrdMsg.setter
	def RcrdMsg(self, value):
		self._RcrdMsg = value if value is not None else base_types.UninitialisedField(self, 'RcrdMsg', RecordMessage2Choice, False)

	@RcrdMsg.deleter
	def RcrdMsg(self):
		del self._RcrdMsg
		self._RcrdMsg = base_types.UninitialisedField(self, 'RcrdMsg', RecordMessage2Choice, False)

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if value is not None else base_types.UninitialisedField(self, 'SeqCntr', Number, False)

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = base_types.UninitialisedField(self, 'SeqCntr', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMtd', type=ClearingMethod3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrPrty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdChcksmInptVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdMsg', type=RecordMessage2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Number, min=1, max=1, mutex_group=None, array=False),
	))