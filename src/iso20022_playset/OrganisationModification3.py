from . import base_types
import ISODate
import OrganisationIdentification39
import CountryCode
import PartyModification3
import FullLegalNameModification1
import TradingNameModification1
import AddressModification3

class OrganisationModification3(base_types._BaseFieldType):

	__slots__ = ["_RegnDt", "_MainMndtHldr", "_BllgAdr", "_TrsrMgr", "_RprtvOffcr", "_OprlAdr", "_LglAdr", "_OrgId", "_TradgNm", "_LglRprtv", "_FullLglNm", "_BizAdr", "_CtryOfOpr", "_Sndr"]
	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if type(value) != auto else self.make_default("RegnDt")

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = None

	@property
	def MainMndtHldr(self):
		return self._MainMndtHldr

	@MainMndtHldr.setter
	def MainMndtHldr(self, value):
		self._MainMndtHldr = value if type(value) != auto else self.make_default("MainMndtHldr")

	@MainMndtHldr.deleter
	def MainMndtHldr(self):
		del self._MainMndtHldr
		self._MainMndtHldr = None

	@property
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if type(value) != auto else self.make_default("BllgAdr")

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = None

	@property
	def TrsrMgr(self):
		return self._TrsrMgr

	@TrsrMgr.setter
	def TrsrMgr(self, value):
		self._TrsrMgr = value if type(value) != auto else self.make_default("TrsrMgr")

	@TrsrMgr.deleter
	def TrsrMgr(self):
		del self._TrsrMgr
		self._TrsrMgr = None

	@property
	def RprtvOffcr(self):
		return self._RprtvOffcr

	@RprtvOffcr.setter
	def RprtvOffcr(self, value):
		self._RprtvOffcr = value if type(value) != auto else self.make_default("RprtvOffcr")

	@RprtvOffcr.deleter
	def RprtvOffcr(self):
		del self._RprtvOffcr
		self._RprtvOffcr = None

	@property
	def OprlAdr(self):
		return self._OprlAdr

	@OprlAdr.setter
	def OprlAdr(self, value):
		self._OprlAdr = value if type(value) != auto else self.make_default("OprlAdr")

	@OprlAdr.deleter
	def OprlAdr(self):
		del self._OprlAdr
		self._OprlAdr = None

	@property
	def LglAdr(self):
		return self._LglAdr

	@LglAdr.setter
	def LglAdr(self, value):
		self._LglAdr = value if type(value) != auto else self.make_default("LglAdr")

	@LglAdr.deleter
	def LglAdr(self):
		del self._LglAdr
		self._LglAdr = None

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

	@property
	def TradgNm(self):
		return self._TradgNm

	@TradgNm.setter
	def TradgNm(self, value):
		self._TradgNm = value if type(value) != auto else self.make_default("TradgNm")

	@TradgNm.deleter
	def TradgNm(self):
		del self._TradgNm
		self._TradgNm = None

	@property
	def LglRprtv(self):
		return self._LglRprtv

	@LglRprtv.setter
	def LglRprtv(self, value):
		self._LglRprtv = value if type(value) != auto else self.make_default("LglRprtv")

	@LglRprtv.deleter
	def LglRprtv(self):
		del self._LglRprtv
		self._LglRprtv = None

	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if type(value) != auto else self.make_default("FullLglNm")

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = None

	@property
	def BizAdr(self):
		return self._BizAdr

	@BizAdr.setter
	def BizAdr(self, value):
		self._BizAdr = value if type(value) != auto else self.make_default("BizAdr")

	@BizAdr.deleter
	def BizAdr(self):
		del self._BizAdr
		self._BizAdr = None

	@property
	def CtryOfOpr(self):
		return self._CtryOfOpr

	@CtryOfOpr.setter
	def CtryOfOpr(self, value):
		self._CtryOfOpr = value if type(value) != auto else self.make_default("CtryOfOpr")

	@CtryOfOpr.deleter
	def CtryOfOpr(self):
		del self._CtryOfOpr
		self._CtryOfOpr = None

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if type(value) != auto else self.make_default("Sndr")

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainMndtHldr', type=PartyModification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgAdr', type=AddressModification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrsrMgr', type=PartyModification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprtvOffcr', type=PartyModification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OprlAdr', type=AddressModification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglAdr', type=AddressModification3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgNm', type=TradingNameModification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRprtv', type=PartyModification3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FullLglNm', type=FullLegalNameModification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizAdr', type=AddressModification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfOpr', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sndr', type=PartyModification3, min=0, max=None, mutex_group=None, array=True),
	))

