# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Contact9
from . import CountryCode
from . import LEIIdentifier
from . import Max140Text
from . import Max35Text

class SecuritiesSettlementSystemIdentification2(base_types._BaseFieldType):

	__slots__ = ["_CSDLglNm", "_CtryOfJursdctn", "_LEI", "_RspnsblPty", "_SysId", "_SysNm"]
	@property
	def CSDLglNm(self):
		return self._CSDLglNm

	@CSDLglNm.setter
	def CSDLglNm(self, value):
		self._CSDLglNm = value if value is not None else base_types.UninitialisedField(self, 'CSDLglNm', Max140Text, False)

	@CSDLglNm.deleter
	def CSDLglNm(self):
		del self._CSDLglNm
		self._CSDLglNm = base_types.UninitialisedField(self, 'CSDLglNm', Max140Text, False)

	@property
	def CtryOfJursdctn(self):
		return self._CtryOfJursdctn

	@CtryOfJursdctn.setter
	def CtryOfJursdctn(self, value):
		self._CtryOfJursdctn = value if value is not None else base_types.UninitialisedField(self, 'CtryOfJursdctn', CountryCode, False)

	@CtryOfJursdctn.deleter
	def CtryOfJursdctn(self):
		del self._CtryOfJursdctn
		self._CtryOfJursdctn = base_types.UninitialisedField(self, 'CtryOfJursdctn', CountryCode, False)

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPty', Contact9, True)

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = base_types.UninitialisedField(self, 'RspnsblPty', Contact9, True)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', Max35Text, False)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', Max35Text, False)

	@property
	def SysNm(self):
		return self._SysNm

	@SysNm.setter
	def SysNm(self, value):
		self._SysNm = value if value is not None else base_types.UninitialisedField(self, 'SysNm', Max140Text, False)

	@SysNm.deleter
	def SysNm(self):
		del self._SysNm
		self._SysNm = base_types.UninitialisedField(self, 'SysNm', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSDLglNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfJursdctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=Contact9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))