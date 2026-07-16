# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactDetails4
from . import CountryCode
from . import Exact2UpperCaseAlphaText
from . import LEIIdentifier

class SettlementInternaliserIdentification1(base_types._BaseFieldType):

	__slots__ = ["_BrnchId", "_Ctry", "_LEI", "_RspnsblPrsn"]
	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if value is not None else base_types.UninitialisedField(self, 'BrnchId', Exact2UpperCaseAlphaText, False)

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = base_types.UninitialisedField(self, 'BrnchId', Exact2UpperCaseAlphaText, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

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
	def RspnsblPrsn(self):
		return self._RspnsblPrsn

	@RspnsblPrsn.setter
	def RspnsblPrsn(self, value):
		self._RspnsblPrsn = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPrsn', ContactDetails4, False)

	@RspnsblPrsn.deleter
	def RspnsblPrsn(self):
		del self._RspnsblPrsn
		self._RspnsblPrsn = base_types.UninitialisedField(self, 'RspnsblPrsn', ContactDetails4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrnchId', type=Exact2UpperCaseAlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPrsn', type=ContactDetails4, min=1, max=1, mutex_group=None, array=False),
	))