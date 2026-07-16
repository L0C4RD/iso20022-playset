# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import Max350Text
from . import OrganisationIdentification39
from . import PartyIdentification274
from . import PostalAddress27

class Organisation42(base_types._BaseFieldType):

	__slots__ = ["_BizAdr", "_BllgAdr", "_CtryOfOpr", "_FullLglNm", "_LglAdr", "_LglRprtv", "_MainMndtHldr", "_OprlAdr", "_OrgId", "_RegnDt", "_RprtvOffcr", "_Sndr", "_TradgNm", "_TrsrMgr"]
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
	def BllgAdr(self):
		return self._BllgAdr

	@BllgAdr.setter
	def BllgAdr(self, value):
		self._BllgAdr = value if value is not None else base_types.UninitialisedField(self, 'BllgAdr', PostalAddress27, False)

	@BllgAdr.deleter
	def BllgAdr(self):
		del self._BllgAdr
		self._BllgAdr = base_types.UninitialisedField(self, 'BllgAdr', PostalAddress27, False)

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
	def LglRprtv(self):
		return self._LglRprtv

	@LglRprtv.setter
	def LglRprtv(self, value):
		self._LglRprtv = value if value is not None else base_types.UninitialisedField(self, 'LglRprtv', PartyIdentification274, True)

	@LglRprtv.deleter
	def LglRprtv(self):
		del self._LglRprtv
		self._LglRprtv = base_types.UninitialisedField(self, 'LglRprtv', PartyIdentification274, True)

	@property
	def MainMndtHldr(self):
		return self._MainMndtHldr

	@MainMndtHldr.setter
	def MainMndtHldr(self, value):
		self._MainMndtHldr = value if value is not None else base_types.UninitialisedField(self, 'MainMndtHldr', PartyIdentification274, True)

	@MainMndtHldr.deleter
	def MainMndtHldr(self):
		del self._MainMndtHldr
		self._MainMndtHldr = base_types.UninitialisedField(self, 'MainMndtHldr', PartyIdentification274, True)

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
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if value is not None else base_types.UninitialisedField(self, 'OrgId', OrganisationIdentification39, False)

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = base_types.UninitialisedField(self, 'OrgId', OrganisationIdentification39, False)

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
	def RprtvOffcr(self):
		return self._RprtvOffcr

	@RprtvOffcr.setter
	def RprtvOffcr(self, value):
		self._RprtvOffcr = value if value is not None else base_types.UninitialisedField(self, 'RprtvOffcr', PartyIdentification274, True)

	@RprtvOffcr.deleter
	def RprtvOffcr(self):
		del self._RprtvOffcr
		self._RprtvOffcr = base_types.UninitialisedField(self, 'RprtvOffcr', PartyIdentification274, True)

	@property
	def Sndr(self):
		return self._Sndr

	@Sndr.setter
	def Sndr(self, value):
		self._Sndr = value if value is not None else base_types.UninitialisedField(self, 'Sndr', PartyIdentification274, True)

	@Sndr.deleter
	def Sndr(self):
		del self._Sndr
		self._Sndr = base_types.UninitialisedField(self, 'Sndr', PartyIdentification274, True)

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
		self._TrsrMgr = value if value is not None else base_types.UninitialisedField(self, 'TrsrMgr', PartyIdentification274, False)

	@TrsrMgr.deleter
	def TrsrMgr(self):
		del self._TrsrMgr
		self._TrsrMgr = base_types.UninitialisedField(self, 'TrsrMgr', PartyIdentification274, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfOpr', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglAdr', type=PostalAddress27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglRprtv', type=PartyIdentification274, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MainMndtHldr', type=PartyIdentification274, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OprlAdr', type=PostalAddress27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprtvOffcr', type=PartyIdentification274, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sndr', type=PartyIdentification274, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradgNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrsrMgr', type=PartyIdentification274, min=0, max=1, mutex_group=None, array=False),
	))