# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Priority1Code
from . import YesNoIndicator

class InformationQualifierType1(base_types._BaseFieldType):

	__slots__ = ["_IsFrmtd", "_Prty"]
	@property
	def IsFrmtd(self):
		return self._IsFrmtd

	@IsFrmtd.setter
	def IsFrmtd(self, value):
		self._IsFrmtd = value if value is not None else base_types.UninitialisedField(self, 'IsFrmtd', YesNoIndicator, False)

	@IsFrmtd.deleter
	def IsFrmtd(self):
		del self._IsFrmtd
		self._IsFrmtd = base_types.UninitialisedField(self, 'IsFrmtd', YesNoIndicator, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority1Code, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IsFrmtd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority1Code, min=0, max=1, mutex_group=None, array=False),
	))