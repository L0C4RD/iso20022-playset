# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticatedData10
from . import ContentType2Code
from . import SignedData9

class ContentInformationType38(base_types._BaseFieldType):

	__slots__ = ["_AuthntcdData", "_CnttTp", "_SgndData"]
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
		base_types.FieldEntry(name='SgndData', type=SignedData9, min=0, max=1, mutex_group=None, array=False),
	))