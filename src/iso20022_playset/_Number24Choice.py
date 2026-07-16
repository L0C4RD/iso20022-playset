# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification36
from . import Max4NumericText

class Number24Choice(base_types._BaseFieldType):

	__slots__ = ["_NbId", "_Prtry"]
	@property
	def NbId(self):
		return self._NbId

	@NbId.setter
	def NbId(self, value):
		self._NbId = value if value is not None else base_types.UninitialisedField(self, 'NbId', Max4NumericText, False)

	@NbId.deleter
	def NbId(self):
		del self._NbId
		self._NbId = base_types.UninitialisedField(self, 'NbId', Max4NumericText, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification36, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbId', type=Max4NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))