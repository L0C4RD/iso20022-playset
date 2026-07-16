# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max35Text

class IdentificationSource1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dmst", "_Prtry"]
	@property
	def Dmst(self):
		return self._Dmst

	@Dmst.setter
	def Dmst(self, value):
		self._Dmst = value if value is not None else base_types.UninitialisedField(self, 'Dmst', CountryCode, False)

	@Dmst.deleter
	def Dmst(self):
		del self._Dmst
		self._Dmst = base_types.UninitialisedField(self, 'Dmst', CountryCode, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dmst', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))