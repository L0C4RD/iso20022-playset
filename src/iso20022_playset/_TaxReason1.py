# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max105Text
from . import Max10Text

class TaxReason1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Expltn"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', Max10Text, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', Max10Text, False)

	@property
	def Expltn(self):
		return self._Expltn

	@Expltn.setter
	def Expltn(self, value):
		self._Expltn = value if value is not None else base_types.UninitialisedField(self, 'Expltn', Max105Text, False)

	@Expltn.deleter
	def Expltn(self):
		del self._Expltn
		self._Expltn = base_types.UninitialisedField(self, 'Expltn', Max105Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Expltn', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
	))