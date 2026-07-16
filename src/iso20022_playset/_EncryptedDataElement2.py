# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EncryptedData2Choice
from . import EncryptedDataFormat1Code
from . import Max35Text

class EncryptedDataElement2(base_types._BaseFieldType):

	__slots__ = ["_ClearTxtFrmt", "_Data", "_Id", "_OthrClearTxtFrmt"]
	@property
	def ClearTxtFrmt(self):
		return self._ClearTxtFrmt

	@ClearTxtFrmt.setter
	def ClearTxtFrmt(self, value):
		self._ClearTxtFrmt = value if value is not None else base_types.UninitialisedField(self, 'ClearTxtFrmt', EncryptedDataFormat1Code, False)

	@ClearTxtFrmt.deleter
	def ClearTxtFrmt(self):
		del self._ClearTxtFrmt
		self._ClearTxtFrmt = base_types.UninitialisedField(self, 'ClearTxtFrmt', EncryptedDataFormat1Code, False)

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if value is not None else base_types.UninitialisedField(self, 'Data', EncryptedData2Choice, False)

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = base_types.UninitialisedField(self, 'Data', EncryptedData2Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def OthrClearTxtFrmt(self):
		return self._OthrClearTxtFrmt

	@OthrClearTxtFrmt.setter
	def OthrClearTxtFrmt(self, value):
		self._OthrClearTxtFrmt = value if value is not None else base_types.UninitialisedField(self, 'OthrClearTxtFrmt', Max35Text, False)

	@OthrClearTxtFrmt.deleter
	def OthrClearTxtFrmt(self):
		del self._OthrClearTxtFrmt
		self._OthrClearTxtFrmt = base_types.UninitialisedField(self, 'OthrClearTxtFrmt', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClearTxtFrmt', type=EncryptedDataFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=EncryptedData2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrClearTxtFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))