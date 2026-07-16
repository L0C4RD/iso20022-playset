# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20000Text
from . import NarrativeType1Choice

class Narrative1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Txt"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', NarrativeType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', NarrativeType1Choice, False)

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if value is not None else base_types.UninitialisedField(self, 'Txt', Max20000Text, True)

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = base_types.UninitialisedField(self, 'Txt', Max20000Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=NarrativeType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max20000Text, min=1, max=5, mutex_group=None, array=True),
	))