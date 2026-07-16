# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Exact2UpperCaseAlphaText
from . import LEIIdentifier

class IssuerCSDIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_FrstTwoCharsInstrmId", "_LEI"]
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
	def FrstTwoCharsInstrmId(self):
		return self._FrstTwoCharsInstrmId

	@FrstTwoCharsInstrmId.setter
	def FrstTwoCharsInstrmId(self, value):
		self._FrstTwoCharsInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FrstTwoCharsInstrmId', Exact2UpperCaseAlphaText, False)

	@FrstTwoCharsInstrmId.deleter
	def FrstTwoCharsInstrmId(self):
		del self._FrstTwoCharsInstrmId
		self._FrstTwoCharsInstrmId = base_types.UninitialisedField(self, 'FrstTwoCharsInstrmId', Exact2UpperCaseAlphaText, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstTwoCharsInstrmId', type=Exact2UpperCaseAlphaText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))