# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max350Text

class RegulatoryStipulations1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Stiptns"]
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
	def Stiptns(self):
		return self._Stiptns

	@Stiptns.setter
	def Stiptns(self, value):
		self._Stiptns = value if value is not None else base_types.UninitialisedField(self, 'Stiptns', Max350Text, True)

	@Stiptns.deleter
	def Stiptns(self):
		del self._Stiptns
		self._Stiptns = base_types.UninitialisedField(self, 'Stiptns', Max350Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stiptns', type=Max350Text, min=1, max=None, mutex_group=None, array=True),
	))