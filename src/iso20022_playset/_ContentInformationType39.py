# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AuthenticatedData10 import AuthenticatedData10
from ._ContentType2Code import ContentType2Code
from ._DigestedData6 import DigestedData6
from ._EnvelopedData11 import EnvelopedData11
from ._SignedData9 import SignedData9

class ContentInformationType39(base_types._BaseFieldType):

	__slots__ = ["_AuthntcdData", "_CnttTp", "_DgstdData", "_EnvlpdData", "_SgndData"]
	@property
	def AuthntcdData(self):
		return self._AuthntcdData

	@AuthntcdData.setter
	def AuthntcdData(self, value):
		self._AuthntcdData = value if type(value) != base_types.auto else self.make_default("AuthntcdData")

	@AuthntcdData.deleter
	def AuthntcdData(self):
		del self._AuthntcdData
		self._AuthntcdData = None

	@property
	def CnttTp(self):
		return self._CnttTp

	@CnttTp.setter
	def CnttTp(self, value):
		self._CnttTp = value if type(value) != base_types.auto else self.make_default("CnttTp")

	@CnttTp.deleter
	def CnttTp(self):
		del self._CnttTp
		self._CnttTp = None

	@property
	def DgstdData(self):
		return self._DgstdData

	@DgstdData.setter
	def DgstdData(self, value):
		self._DgstdData = value if type(value) != base_types.auto else self.make_default("DgstdData")

	@DgstdData.deleter
	def DgstdData(self):
		del self._DgstdData
		self._DgstdData = None

	@property
	def EnvlpdData(self):
		return self._EnvlpdData

	@EnvlpdData.setter
	def EnvlpdData(self, value):
		self._EnvlpdData = value if type(value) != base_types.auto else self.make_default("EnvlpdData")

	@EnvlpdData.deleter
	def EnvlpdData(self):
		del self._EnvlpdData
		self._EnvlpdData = None

	@property
	def SgndData(self):
		return self._SgndData

	@SgndData.setter
	def SgndData(self, value):
		self._SgndData = value if type(value) != base_types.auto else self.make_default("SgndData")

	@SgndData.deleter
	def SgndData(self):
		del self._SgndData
		self._SgndData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthntcdData', type=AuthenticatedData10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnttTp', type=ContentType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstdData', type=DigestedData6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EnvlpdData', type=EnvelopedData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgndData', type=SignedData9, min=0, max=1, mutex_group=None, array=False),
	))