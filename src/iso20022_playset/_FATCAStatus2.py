# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FATCASource1Choice
from . import FATCAStatus2Choice

class FATCAStatus2(base_types._BaseFieldType):

	__slots__ = ["_Src", "_Tp"]
	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if value is not None else base_types.UninitialisedField(self, 'Src', FATCASource1Choice, False)

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = base_types.UninitialisedField(self, 'Src', FATCASource1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FATCAStatus2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FATCAStatus2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Src', type=FATCASource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FATCAStatus2Choice, min=1, max=1, mutex_group=None, array=False),
	))