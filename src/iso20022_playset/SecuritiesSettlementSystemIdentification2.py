from . import base_types
import CountryCode
import Max140Text
import Contact9
import Max35Text
import LEIIdentifier

class SecuritiesSettlementSystemIdentification2(base_types._BaseFieldType):

	__slots__ = ["_CSDLglNm", "_RspnsblPty", "_LEI", "_SysNm", "_CtryOfJursdctn", "_SysId"]
	@property
	def CSDLglNm(self):
		return self._CSDLglNm

	@CSDLglNm.setter
	def CSDLglNm(self, value):
		self._CSDLglNm = value if type(value) != auto else self.make_default("CSDLglNm")

	@CSDLglNm.deleter
	def CSDLglNm(self):
		del self._CSDLglNm
		self._CSDLglNm = None

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if type(value) != auto else self.make_default("RspnsblPty")

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if type(value) != auto else self.make_default("SysNm")

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = None

	@property
	def CtryOfJursdctn(self):
		return self._CtryOfJursdctn

	@CtryOfJursdctn.setter
	def CtryOfJursdctn(self, value):
		self._CtryOfJursdctn = value if type(value) != auto else self.make_default("CtryOfJursdctn")

	@CtryOfJursdctn.deleter
	def CtryOfJursdctn(self):
		del self._CtryOfJursdctn
		self._CtryOfJursdctn = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSDLglNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=Contact9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfJursdctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

