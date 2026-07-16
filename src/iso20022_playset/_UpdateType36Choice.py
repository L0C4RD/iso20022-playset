# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityAttributes12
from . import UpdateType35Choice

class UpdateType36Choice(base_types._BaseFieldType):

	__slots__ = ["_Rplc", "_UpdTp"]
	@property
	def Rplc(self):
		return self._Rplc

	@Rplc.setter
	def Rplc(self, value):
		self._Rplc = value if value is not None else base_types.UninitialisedField(self, 'Rplc', SecurityAttributes12, False)

	@Rplc.deleter
	def Rplc(self):
		del self._Rplc
		self._Rplc = base_types.UninitialisedField(self, 'Rplc', SecurityAttributes12, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', UpdateType35Choice, True)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', UpdateType35Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rplc', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UpdTp', type=UpdateType35Choice, min=1, max=3, mutex_group=1, array=True),
	))