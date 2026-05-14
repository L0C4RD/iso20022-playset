# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Contact9 import Contact9
from ._CountryCode import CountryCode
from ._LEIIdentifier import LEIIdentifier
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text

class SecuritiesSettlementSystemIdentification2(base_types._BaseFieldType):

	__slots__ = ["_CSDLglNm", "_CtryOfJursdctn", "_LEI", "_RspnsblPty", "_SysId", "_SysNm"]
	@property
	def CSDLglNm(self):
		return self._CSDLglNm

	@CSDLglNm.setter
	def CSDLglNm(self, value):
		self._CSDLglNm = value if type(value) != base_types.auto else self.make_default("CSDLglNm")

	@CSDLglNm.deleter
	def CSDLglNm(self):
		del self._CSDLglNm
		self._CSDLglNm = None

	@property
	def CtryOfJursdctn(self):
		return self._CtryOfJursdctn

	@CtryOfJursdctn.setter
	def CtryOfJursdctn(self, value):
		self._CtryOfJursdctn = value if type(value) != base_types.auto else self.make_default("CtryOfJursdctn")

	@CtryOfJursdctn.deleter
	def CtryOfJursdctn(self):
		del self._CtryOfJursdctn
		self._CtryOfJursdctn = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if type(value) != base_types.auto else self.make_default("RspnsblPty")

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if type(value) != base_types.auto else self.make_default("SysNm")

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSDLglNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfJursdctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=Contact9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))