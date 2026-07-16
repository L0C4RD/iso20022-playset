# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact3NumericText
from . import OptionNumber1Code

class OptionNumber1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Nb"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', OptionNumber1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', OptionNumber1Code, False)

	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if value is not None else base_types.UninitialisedField(self, 'Nb', Exact3NumericText, False)

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = base_types.UninitialisedField(self, 'Nb', Exact3NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=OptionNumber1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Nb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))