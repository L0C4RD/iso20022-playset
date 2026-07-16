# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticatedData10
from . import ContentType2Code
from . import DigestedData6
from . import EnvelopedData11
from . import SignedData9

class ContentInformationType39(base_types._BaseFieldType):

	__slots__ = ["_AuthntcdData", "_CnttTp", "_DgstdData", "_EnvlpdData", "_SgndData"]
	@property
	def AuthntcdData(self):
		return self._AuthntcdData

	@AuthntcdData.setter
	def AuthntcdData(self, value):
		self._AuthntcdData = value if value is not None else base_types.UninitialisedField(self, 'AuthntcdData', AuthenticatedData10, False)

	@AuthntcdData.deleter
	def AuthntcdData(self):
		del self._AuthntcdData
		self._AuthntcdData = base_types.UninitialisedField(self, 'AuthntcdData', AuthenticatedData10, False)

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
	def DgstdData(self):
		return self._DgstdData

	@DgstdData.setter
	def DgstdData(self, value):
		self._DgstdData = value if value is not None else base_types.UninitialisedField(self, 'DgstdData', DigestedData6, False)

	@DgstdData.deleter
	def DgstdData(self):
		del self._DgstdData
		self._DgstdData = base_types.UninitialisedField(self, 'DgstdData', DigestedData6, False)

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

	@property
	def SgndData(self):
		return self._SgndData

	@SgndData.setter
	def SgndData(self, value):
		self._SgndData = value if value is not None else base_types.UninitialisedField(self, 'SgndData', SignedData9, False)

	@SgndData.deleter
	def SgndData(self):
		del self._SgndData
		self._SgndData = base_types.UninitialisedField(self, 'SgndData', SignedData9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcdData', type=AuthenticatedData10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstdData', type=DigestedData6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndData', type=SignedData9, min=0, max=1, mutex_group=None, array=False),
	))