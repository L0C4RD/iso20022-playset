# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import Max350Text
from . import Max35Text
from . import Max70Text
from . import OrganisationLegalStatus1Code
from . import PartyIdentification272
from . import PostalAddress27
from . import TrueFalseIndicator

class Organisation43(base_types._BaseFieldType):

	__slots__ = ["_BizAdr", "_BrdRsltnInd", "_CtryOfOpr", "_EstblishdDt", "_FullLglNm", "_LglAdr", "_MainMndtHldr", "_OprlAdr", "_OrgLglSts", "_RegnCtry", "_RegnDt", "_RegnNb", "_RprtvOffcr", "_Sndr", "_TaxtnCtry", "_TaxtnIdNb", "_TradgNm", "_TrsrMgr"]
	@property
	def BizAdr(self):
		return self._BizAdr

	@BizAdr.setter
	def BizAdr(self, value):
		self._BizAdr = value if value is not None else base_types.UninitialisedField(self, 'BizAdr', PostalAddress27, False)

	@BizAdr.deleter
	def BizAdr(self):
		del self._BizAdr
		self._BizAdr = base_types.UninitialisedField(self, 'BizAdr', PostalAddress27, False)

	@property
	def BrdRsltnInd(self):
		return self._BrdRsltnInd

	@BrdRsltnInd.setter
	def BrdRsltnInd(self, value):
		self._BrdRsltnInd = value if value is not None else base_types.UninitialisedField(self, 'BrdRsltnInd', TrueFalseIndicator, False)

	@BrdRsltnInd.deleter
	def BrdRsltnInd(self):
		del self._BrdRsltnInd
		self._BrdRsltnInd = base_types.UninitialisedField(self, 'BrdRsltnInd', TrueFalseIndicator, False)

	@property
	def CtryOfOpr(self):
		return self._CtryOfOpr

	@CtryOfOpr.setter
	def CtryOfOpr(self, value):
		self._CtryOfOpr = value if value is not None else base_types.UninitialisedField(self, 'CtryOfOpr', CountryCode, False)

	@CtryOfOpr.deleter
	def CtryOfOpr(self):
		del self._CtryOfOpr
		self._CtryOfOpr = base_types.UninitialisedField(self, 'CtryOfOpr', CountryCode, False)

	@property
	def EstblishdDt(self):
		return self._EstblishdDt

	@EstblishdDt.setter
	def EstblishdDt(self, value):
		self._EstblishdDt = value if value is not None else base_types.UninitialisedField(self, 'EstblishdDt', ISODate, False)

	@EstblishdDt.deleter
	def EstblishdDt(self):
		del self._EstblishdDt
		self._EstblishdDt = base_types.UninitialisedField(self, 'EstblishdDt', ISODate, False)

	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if value is not None else base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

	@property
	def LglAdr(self):
		return self._LglAdr

	@LglAdr.setter
	def LglAdr(self, value):
		self._LglAdr = value if value is not None else base_types.UninitialisedField(self, 'LglAdr', PostalAddress27, False)

	@LglAdr.deleter
	def LglAdr(self):
		del self._LglAdr
		self._LglAdr = base_types.UninitialisedField(self, 'LglAdr', PostalAddress27, False)

	@property
	def MainMndtHldr(self):
		return self._MainMndtHldr

	@MainMndtHldr.setter
	def MainMndtHldr(self, value):
		self._MainMndtHldr = value if value is not None else base_types.UninitialisedField(self, 'MainMndtHldr', PartyIdentification272, True)

	@MainMndtHldr.deleter
	def MainMndtHldr(self):
		del self._MainMndtHldr
		self._MainMndtHldr = base_types.UninitialisedField(self, 'MainMndtHldr', PartyIdentification272, True)

	@property
	def OprlAdr(self):
		return self._OprlAdr

	@OprlAdr.setter
	def OprlAdr(self, value):
		self._OprlAdr = value if value is not None else base_types.UninitialisedField(self, 'OprlAdr', PostalAddress27, False)

	@OprlAdr.deleter
	def OprlAdr(self):
		del self._OprlAdr
		self._OprlAdr = base_types.UninitialisedField(self, 'OprlAdr', PostalAddress27, False)

	@property
	def OrgLglSts(self):
		return self._OrgLglSts

	@OrgLglSts.setter
	def OrgLglSts(self, value):
		self._OrgLglSts = value if value is not None else base_types.UninitialisedField(self, 'OrgLglSts', OrganisationLegalStatus1Code, False)

	@OrgLglSts.deleter
	def OrgLglSts(self):
		del self._OrgLglSts
		self._OrgLglSts = base_types.UninitialisedField(self, 'OrgLglSts', OrganisationLegalStatus1Code, False)

	@property
	def RegnCtry(self):
		return self._RegnCtry

	@RegnCtry.setter
	def RegnCtry(self, value):
		self._RegnCtry = value if value is not None else base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@RegnCtry.deleter
	def RegnCtry(self):
		del self._RegnCtry
		self._RegnCtry = base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if value is not None else base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if value is not None else base_types.UninitialisedField(self, 'RegnNb', Max70Text, False)

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = base_types.UninitialisedField(self, 'RegnNb', Max70Text, False)

	@property
	def RprtvOffcr(self):
		return self._RprtvOffcr

	@RprtvOffcr.setter
	def RprtvOffcr(self, value):
		self._RprtvOffcr = value if value is not None else base_types.UninitialisedField(self, 'RprtvOffcr', PartyIdentification272, True)

	@RprtvOffcr.deleter
	def RprtvOffcr(self):
		del self._RprtvOffcr
		self._RprtvOffcr = base_types.UninitialisedField(self, 'RprtvOffcr', PartyIdentification272, True)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', PartyIdentification272, True)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', PartyIdentification272, True)

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if value is not None else base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	@property
	def TaxtnIdNb(self):
		return self._TaxtnIdNb

	@TaxtnIdNb.setter
	def TaxtnIdNb(self, value):
		self._TaxtnIdNb = value if value is not None else base_types.UninitialisedField(self, 'TaxtnIdNb', Max35Text, False)

	@TaxtnIdNb.deleter
	def TaxtnIdNb(self):
		del self._TaxtnIdNb
		self._TaxtnIdNb = base_types.UninitialisedField(self, 'TaxtnIdNb', Max35Text, False)

	@property
	def TradgNm(self):
		return self._TradgNm

	@TradgNm.setter
	def TradgNm(self, value):
		self._TradgNm = value if value is not None else base_types.UninitialisedField(self, 'TradgNm', Max350Text, False)

	@TradgNm.deleter
	def TradgNm(self):
		del self._TradgNm
		self._TradgNm = base_types.UninitialisedField(self, 'TradgNm', Max350Text, False)

	@property
	def TrsrMgr(self):
		return self._TrsrMgr

	@TrsrMgr.setter
	def TrsrMgr(self, value):
		self._TrsrMgr = value if value is not None else base_types.UninitialisedField(self, 'TrsrMgr', PartyIdentification272, False)

	@TrsrMgr.deleter
	def TrsrMgr(self):
		del self._TrsrMgr
		self._TrsrMgr = base_types.UninitialisedField(self, 'TrsrMgr', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrdRsltnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfOpr', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MainMndtHldr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OprlAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgLglSts', type=OrganisationLegalStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprtvOffcr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification272, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrsrMgr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))