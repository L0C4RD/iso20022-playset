# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentType2Code
from . import EnvelopedData11

class ContentInformationType40(base_types._BaseFieldType):

	__slots__ = ["_CnttTp", "_EnvlpdData"]
	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if value is not None else base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = base_types.UninitialisedField(self, 'CnttTp', ContentType2Code, False)

	@property
	def EnvlpdData(self):
		return self._EnvlpdData

	@EnvlpdData.setter
	def EnvlpdData(self, value):
		self._EnvlpdData = value if value is not None else base_types.UninitialisedField(self, 'EnvlpdData', EnvelopedData11, False)

	@EnvlpdData.deleter
	def EnvlpdData(self):
		del self._EnvlpdData
		self._EnvlpdData = base_types.UninitialisedField(self, 'EnvlpdData', EnvelopedData11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData11, min=1, max=1, mutex_group=None, array=False),
	))