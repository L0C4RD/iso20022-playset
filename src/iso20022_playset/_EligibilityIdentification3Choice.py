# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISINOct2015Identifier
from . import SystemPartyIdentification2Choice

class EligibilityIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_FinInstrmId", "_IssrCSDId"]
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
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', ISINOct2015Identifier, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', ISINOct2015Identifier, False)

	@property
	def IssrCSDId(self):
		return self._IssrCSDId

	@IssrCSDId.setter
	def IssrCSDId(self, value):
		self._IssrCSDId = value if value is not None else base_types.UninitialisedField(self, 'IssrCSDId', SystemPartyIdentification2Choice, False)

	@IssrCSDId.deleter
	def IssrCSDId(self):
		del self._IssrCSDId
		self._IssrCSDId = base_types.UninitialisedField(self, 'IssrCSDId', SystemPartyIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrCSDId', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
	))