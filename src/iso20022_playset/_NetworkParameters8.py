# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NetworkParameters7
from . import NetworkType2Code

class NetworkParameters8(base_types._BaseFieldType):

	__slots__ = ["_Accs", "_Tp"]
	@property
	def Accs(self):
		return self._Accs

	@Accs.setter
	def Accs(self, value):
		self._Accs = value if value is not None else base_types.UninitialisedField(self, 'Accs', NetworkParameters7, False)

	@Accs.deleter
	def Accs(self):
		del self._Accs
		self._Accs = base_types.UninitialisedField(self, 'Accs', NetworkParameters7, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', NetworkType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', NetworkType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accs', type=NetworkParameters7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=NetworkType2Code, min=1, max=1, mutex_group=None, array=False),
	))