import base_types
import ISO3NumericCurrencyCode
import CreditDebit3Code
import ISODate
import Number
import Max35Text
import ImpliedCurrencyAndAmount
import ISO3NumericCountryCode
import Max140Binary
import RecordMessage1Choice
import ClearingMethod2Code
import OtherAmount5

class Record3(base_types._BaseFieldType):

	__slots__ = ["_DstnId", "_IntrchngFeeCcy", "_DstnShrtNm", "_ClrAmt", "_DstnCtry", "_RcrdChcksmInptVal", "_OrgtrAssgnr", "_ClrPrty", "_ClrCdtDbt", "_AgtFeeCdtDbt", "_RcrdMsg", "_ClrCcy", "_IntrchngFeeCdtDbt", "_ClrMtd", "_ClrDt", "_IntrchngFeeAmt", "_AgtFeeCcy", "_OrgtrId", "_DstnAssgnr", "_OthrClrMtd", "_AgtFeeAmt", "_OthrAmt", "_OrgtrCtry", "_SeqCntr", "_OrgtrShrtNm"]
	@property
	def DstnId(self):
		return self._DstnId

	@DstnId.setter
	def DstnId(self, value):
		self._DstnId = value if type(value) != auto else self.make_default("DstnId")

	@DstnId.deleter
	def DstnId(self):
		del self._DstnId
		self._DstnId = None

	@property
	def IntrchngFeeCcy(self):
		return self._IntrchngFeeCcy

	@IntrchngFeeCcy.setter
	def IntrchngFeeCcy(self, value):
		self._IntrchngFeeCcy = value if type(value) != auto else self.make_default("IntrchngFeeCcy")

	@IntrchngFeeCcy.deleter
	def IntrchngFeeCcy(self):
		del self._IntrchngFeeCcy
		self._IntrchngFeeCcy = None

	@property
	def DstnShrtNm(self):
		return self._DstnShrtNm

	@DstnShrtNm.setter
	def DstnShrtNm(self, value):
		self._DstnShrtNm = value if type(value) != auto else self.make_default("DstnShrtNm")

	@DstnShrtNm.deleter
	def DstnShrtNm(self):
		del self._DstnShrtNm
		self._DstnShrtNm = None

	@property
	def ClrAmt(self):
		return self._ClrAmt

	@ClrAmt.setter
	def ClrAmt(self, value):
		self._ClrAmt = value if type(value) != auto else self.make_default("ClrAmt")

	@ClrAmt.deleter
	def ClrAmt(self):
		del self._ClrAmt
		self._ClrAmt = None

	@property
	def DstnCtry(self):
		return self._DstnCtry

	@DstnCtry.setter
	def DstnCtry(self, value):
		self._DstnCtry = value if type(value) != auto else self.make_default("DstnCtry")

	@DstnCtry.deleter
	def DstnCtry(self):
		del self._DstnCtry
		self._DstnCtry = None

	@property
	def RcrdChcksmInptVal(self):
		return self._RcrdChcksmInptVal

	@RcrdChcksmInptVal.setter
	def RcrdChcksmInptVal(self, value):
		self._RcrdChcksmInptVal = value if type(value) != auto else self.make_default("RcrdChcksmInptVal")

	@RcrdChcksmInptVal.deleter
	def RcrdChcksmInptVal(self):
		del self._RcrdChcksmInptVal
		self._RcrdChcksmInptVal = None

	@property
	def OrgtrAssgnr(self):
		return self._OrgtrAssgnr

	@OrgtrAssgnr.setter
	def OrgtrAssgnr(self, value):
		self._OrgtrAssgnr = value if type(value) != auto else self.make_default("OrgtrAssgnr")

	@OrgtrAssgnr.deleter
	def OrgtrAssgnr(self):
		del self._OrgtrAssgnr
		self._OrgtrAssgnr = None

	@property
	def ClrPrty(self):
		return self._ClrPrty

	@ClrPrty.setter
	def ClrPrty(self, value):
		self._ClrPrty = value if type(value) != auto else self.make_default("ClrPrty")

	@ClrPrty.deleter
	def ClrPrty(self):
		del self._ClrPrty
		self._ClrPrty = None

	@property
	def ClrCdtDbt(self):
		return self._ClrCdtDbt

	@ClrCdtDbt.setter
	def ClrCdtDbt(self, value):
		self._ClrCdtDbt = value if type(value) != auto else self.make_default("ClrCdtDbt")

	@ClrCdtDbt.deleter
	def ClrCdtDbt(self):
		del self._ClrCdtDbt
		self._ClrCdtDbt = None

	@property
	def AgtFeeCdtDbt(self):
		return self._AgtFeeCdtDbt

	@AgtFeeCdtDbt.setter
	def AgtFeeCdtDbt(self, value):
		self._AgtFeeCdtDbt = value if type(value) != auto else self.make_default("AgtFeeCdtDbt")

	@AgtFeeCdtDbt.deleter
	def AgtFeeCdtDbt(self):
		del self._AgtFeeCdtDbt
		self._AgtFeeCdtDbt = None

	@property
	def RcrdMsg(self):
		return self._RcrdMsg

	@RcrdMsg.setter
	def RcrdMsg(self, value):
		self._RcrdMsg = value if type(value) != auto else self.make_default("RcrdMsg")

	@RcrdMsg.deleter
	def RcrdMsg(self):
		del self._RcrdMsg
		self._RcrdMsg = None

	@property
	def ClrCcy(self):
		return self._ClrCcy

	@ClrCcy.setter
	def ClrCcy(self, value):
		self._ClrCcy = value if type(value) != auto else self.make_default("ClrCcy")

	@ClrCcy.deleter
	def ClrCcy(self):
		del self._ClrCcy
		self._ClrCcy = None

	@property
	def IntrchngFeeCdtDbt(self):
		return self._IntrchngFeeCdtDbt

	@IntrchngFeeCdtDbt.setter
	def IntrchngFeeCdtDbt(self, value):
		self._IntrchngFeeCdtDbt = value if type(value) != auto else self.make_default("IntrchngFeeCdtDbt")

	@IntrchngFeeCdtDbt.deleter
	def IntrchngFeeCdtDbt(self):
		del self._IntrchngFeeCdtDbt
		self._IntrchngFeeCdtDbt = None

	@property
	def ClrMtd(self):
		return self._ClrMtd

	@ClrMtd.setter
	def ClrMtd(self, value):
		self._ClrMtd = value if type(value) != auto else self.make_default("ClrMtd")

	@ClrMtd.deleter
	def ClrMtd(self):
		del self._ClrMtd
		self._ClrMtd = None

	@property
	def ClrDt(self):
		return self._ClrDt

	@ClrDt.setter
	def ClrDt(self, value):
		self._ClrDt = value if type(value) != auto else self.make_default("ClrDt")

	@ClrDt.deleter
	def ClrDt(self):
		del self._ClrDt
		self._ClrDt = None

	@property
	def IntrchngFeeAmt(self):
		return self._IntrchngFeeAmt

	@IntrchngFeeAmt.setter
	def IntrchngFeeAmt(self, value):
		self._IntrchngFeeAmt = value if type(value) != auto else self.make_default("IntrchngFeeAmt")

	@IntrchngFeeAmt.deleter
	def IntrchngFeeAmt(self):
		del self._IntrchngFeeAmt
		self._IntrchngFeeAmt = None

	@property
	def AgtFeeCcy(self):
		return self._AgtFeeCcy

	@AgtFeeCcy.setter
	def AgtFeeCcy(self, value):
		self._AgtFeeCcy = value if type(value) != auto else self.make_default("AgtFeeCcy")

	@AgtFeeCcy.deleter
	def AgtFeeCcy(self):
		del self._AgtFeeCcy
		self._AgtFeeCcy = None

	@property
	def OrgtrId(self):
		return self._OrgtrId

	@OrgtrId.setter
	def OrgtrId(self, value):
		self._OrgtrId = value if type(value) != auto else self.make_default("OrgtrId")

	@OrgtrId.deleter
	def OrgtrId(self):
		del self._OrgtrId
		self._OrgtrId = None

	@property
	def DstnAssgnr(self):
		return self._DstnAssgnr

	@DstnAssgnr.setter
	def DstnAssgnr(self, value):
		self._DstnAssgnr = value if type(value) != auto else self.make_default("DstnAssgnr")

	@DstnAssgnr.deleter
	def DstnAssgnr(self):
		del self._DstnAssgnr
		self._DstnAssgnr = None

	@property
	def OthrClrMtd(self):
		return self._OthrClrMtd

	@OthrClrMtd.setter
	def OthrClrMtd(self, value):
		self._OthrClrMtd = value if type(value) != auto else self.make_default("OthrClrMtd")

	@OthrClrMtd.deleter
	def OthrClrMtd(self):
		del self._OthrClrMtd
		self._OthrClrMtd = None

	@property
	def AgtFeeAmt(self):
		return self._AgtFeeAmt

	@AgtFeeAmt.setter
	def AgtFeeAmt(self, value):
		self._AgtFeeAmt = value if type(value) != auto else self.make_default("AgtFeeAmt")

	@AgtFeeAmt.deleter
	def AgtFeeAmt(self):
		del self._AgtFeeAmt
		self._AgtFeeAmt = None

	@property
	def OthrAmt(self):
		return self._OthrAmt

	@OthrAmt.setter
	def OthrAmt(self, value):
		self._OthrAmt = value if type(value) != auto else self.make_default("OthrAmt")

	@OthrAmt.deleter
	def OthrAmt(self):
		del self._OthrAmt
		self._OthrAmt = None

	@property
	def OrgtrCtry(self):
		return self._OrgtrCtry

	@OrgtrCtry.setter
	def OrgtrCtry(self, value):
		self._OrgtrCtry = value if type(value) != auto else self.make_default("OrgtrCtry")

	@OrgtrCtry.deleter
	def OrgtrCtry(self):
		del self._OrgtrCtry
		self._OrgtrCtry = None

	@property
	def SeqCntr(self):
		return self._SeqCntr

	@SeqCntr.setter
	def SeqCntr(self, value):
		self._SeqCntr = value if type(value) != auto else self.make_default("SeqCntr")

	@SeqCntr.deleter
	def SeqCntr(self):
		del self._SeqCntr
		self._SeqCntr = None

	@property
	def OrgtrShrtNm(self):
		return self._OrgtrShrtNm

	@OrgtrShrtNm.setter
	def OrgtrShrtNm(self, value):
		self._OrgtrShrtNm = value if type(value) != auto else self.make_default("OrgtrShrtNm")

	@OrgtrShrtNm.deleter
	def OrgtrShrtNm(self):
		del self._OrgtrShrtNm
		self._OrgtrShrtNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DstnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdChcksmInptVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrPrty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcrdMsg', type=RecordMessage1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeCdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMtd', type=ClearingMethod2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrchngFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstnAssgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrClrMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtFeeAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmt', type=OtherAmount5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrCtry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqCntr', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

