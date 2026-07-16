# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import IdentificationType42Choice
from . import Max35Text

class AlternatePartyIdentification7(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_Ctry", "_IdTp"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if value is not None else base_types.UninitialisedField(self, 'AltrnId', Max35Text, False)

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = base_types.UninitialisedField(self, 'AltrnId', Max35Text, False)

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
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if value is not None else base_types.UninitialisedField(self, 'IdTp', IdentificationType42Choice, False)

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = base_types.UninitialisedField(self, 'IdTp', IdentificationType42Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=IdentificationType42Choice, min=1, max=1, mutex_group=None, array=False),
	))