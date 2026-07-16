# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentType3Code
from . import EncryptedData2
from . import EnvelopedData12

class ProtectedData2(base_types._BaseFieldType):

	__slots__ = ["_CnttTp", "_EnvlpdData", "_NcrptdData"]
	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if value is not None else base_types.UninitialisedField(self, 'CnttTp', ContentType3Code, False)

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = base_types.UninitialisedField(self, 'CnttTp', ContentType3Code, False)

	@property
	def EnvlpdData(self):
		return self._EnvlpdData

	@EnvlpdData.setter
	def EnvlpdData(self, value):
		self._EnvlpdData = value if value is not None else base_types.UninitialisedField(self, 'EnvlpdData', EnvelopedData12, False)

	@EnvlpdData.deleter
	def EnvlpdData(self):
		del self._EnvlpdData
		self._EnvlpdData = base_types.UninitialisedField(self, 'EnvlpdData', EnvelopedData12, False)

	@property
	def NcrptdData(self):
		return self._NcrptdData

	@NcrptdData.setter
	def NcrptdData(self, value):
		self._NcrptdData = value if value is not None else base_types.UninitialisedField(self, 'NcrptdData', EncryptedData2, False)

	@NcrptdData.deleter
	def NcrptdData(self):
		del self._NcrptdData
		self._NcrptdData = base_types.UninitialisedField(self, 'NcrptdData', EncryptedData2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnttTp', type=ContentType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptdData', type=EncryptedData2, min=0, max=1, mutex_group=None, array=False),
	))