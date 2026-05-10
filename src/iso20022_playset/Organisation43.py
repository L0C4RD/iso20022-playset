from . import base_types
from .Max350Text import Max350Text
from .PartyIdentification272 import PartyIdentification272
from .Max35Text import Max35Text
from .Max70Text import Max70Text
from .PostalAddress27 import PostalAddress27
from .OrganisationLegalStatus1Code import OrganisationLegalStatus1Code
from .ISODate import ISODate
from .TrueFalseIndicator import TrueFalseIndicator
from .CountryCode import CountryCode

class Organisation43(base_types._BaseFieldType):

	__slots__ = ["_Sndr", "_BrdRsltnInd", "_OrgLglSts", "_MainMndtHldr", "_RegnDt", "_RegnNb", "_TaxtnIdNb", "_LglAdr", "_TradgNm", "_TrsrMgr", "_EstblishdDt", "_FullLglNm", "_BizAdr", "_OprlAdr", "_RprtvOffcr", "_CtryOfOpr", "_TaxtnCtry", "_RegnCtry"]
	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != base_types.auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	@property
	def BrdRsltnInd(self):
		return self._BrdRsltnInd

	@BrdRsltnInd.setter
	def BrdRsltnInd(self, value):
		self._BrdRsltnInd = value if type(value) != base_types.auto else self.make_default("BrdRsltnInd")

	@BrdRsltnInd.deleter
	def BrdRsltnInd(self):
		del self._BrdRsltnInd
		self._BrdRsltnInd = None

	@property
	def OrgLglSts(self):
		return self._OrgLglSts

	@OrgLglSts.setter
	def OrgLglSts(self, value):
		self._OrgLglSts = value if type(value) != base_types.auto else self.make_default("OrgLglSts")

	@OrgLglSts.deleter
	def OrgLglSts(self):
		del self._OrgLglSts
		self._OrgLglSts = None

	@property
	def MainMndtHldr(self):
		return self._MainMndtHldr

	@MainMndtHldr.setter
	def MainMndtHldr(self, value):
		self._MainMndtHldr = value if type(value) != base_types.auto else self.make_default("MainMndtHldr")

	@MainMndtHldr.deleter
	def MainMndtHldr(self):
		del self._MainMndtHldr
		self._MainMndtHldr = None

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if type(value) != base_types.auto else self.make_default("RegnDt")

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = None

	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if type(value) != base_types.auto else self.make_default("RegnNb")

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = None

	@property
	def TaxtnIdNb(self):
		return self._TaxtnIdNb

	@TaxtnIdNb.setter
	def TaxtnIdNb(self, value):
		self._TaxtnIdNb = value if type(value) != base_types.auto else self.make_default("TaxtnIdNb")

	@TaxtnIdNb.deleter
	def TaxtnIdNb(self):
		del self._TaxtnIdNb
		self._TaxtnIdNb = None

	@property
	def LglAdr(self):
		return self._LglAdr

	@LglAdr.setter
	def LglAdr(self, value):
		self._LglAdr = value if type(value) != base_types.auto else self.make_default("LglAdr")

	@LglAdr.deleter
	def LglAdr(self):
		del self._LglAdr
		self._LglAdr = None

	@property
	def TradgNm(self):
		return self._TradgNm

	@TradgNm.setter
	def TradgNm(self, value):
		self._TradgNm = value if type(value) != base_types.auto else self.make_default("TradgNm")

	@TradgNm.deleter
	def TradgNm(self):
		del self._TradgNm
		self._TradgNm = None

	@property
	def TrsrMgr(self):
		return self._TrsrMgr

	@TrsrMgr.setter
	def TrsrMgr(self, value):
		self._TrsrMgr = value if type(value) != base_types.auto else self.make_default("TrsrMgr")

	@TrsrMgr.deleter
	def TrsrMgr(self):
		del self._TrsrMgr
		self._TrsrMgr = None

	@property
	def EstblishdDt(self):
		return self._EstblishdDt

	@EstblishdDt.setter
	def EstblishdDt(self, value):
		self._EstblishdDt = value if type(value) != base_types.auto else self.make_default("EstblishdDt")

	@EstblishdDt.deleter
	def EstblishdDt(self):
		del self._EstblishdDt
		self._EstblishdDt = None

	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if type(value) != base_types.auto else self.make_default("FullLglNm")

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = None

	@property
	def BizAdr(self):
		return self._BizAdr

	@BizAdr.setter
	def BizAdr(self, value):
		self._BizAdr = value if type(value) != base_types.auto else self.make_default("BizAdr")

	@BizAdr.deleter
	def BizAdr(self):
		del self._BizAdr
		self._BizAdr = None

	@property
	def OprlAdr(self):
		return self._OprlAdr

	@OprlAdr.setter
	def OprlAdr(self, value):
		self._OprlAdr = value if type(value) != base_types.auto else self.make_default("OprlAdr")

	@OprlAdr.deleter
	def OprlAdr(self):
		del self._OprlAdr
		self._OprlAdr = None

	@property
	def RprtvOffcr(self):
		return self._RprtvOffcr

	@RprtvOffcr.setter
	def RprtvOffcr(self, value):
		self._RprtvOffcr = value if type(value) != base_types.auto else self.make_default("RprtvOffcr")

	@RprtvOffcr.deleter
	def RprtvOffcr(self):
		del self._RprtvOffcr
		self._RprtvOffcr = None

	@property
	def CtryOfOpr(self):
		return self._CtryOfOpr

	@CtryOfOpr.setter
	def CtryOfOpr(self, value):
		self._CtryOfOpr = value if type(value) != base_types.auto else self.make_default("CtryOfOpr")

	@CtryOfOpr.deleter
	def CtryOfOpr(self):
		del self._CtryOfOpr
		self._CtryOfOpr = None

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if type(value) != base_types.auto else self.make_default("TaxtnCtry")

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = None

	@property
	def RegnCtry(self):
		return self._RegnCtry

	@RegnCtry.setter
	def RegnCtry(self, value):
		self._RegnCtry = value if type(value) != base_types.auto else self.make_default("RegnCtry")

	@RegnCtry.deleter
	def RegnCtry(self):
		del self._RegnCtry
		self._RegnCtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sndr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrdRsltnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgLglSts', type=OrganisationLegalStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainMndtHldr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrsrMgr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprlAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprtvOffcr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtryOfOpr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))

