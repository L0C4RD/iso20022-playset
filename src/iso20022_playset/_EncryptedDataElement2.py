# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EncryptedData2Choice import EncryptedData2Choice
from ._EncryptedDataFormat1Code import EncryptedDataFormat1Code
from ._Max35Text import Max35Text

class EncryptedDataElement2(base_types._BaseFieldType):

	__slots__ = ["_ClearTxtFrmt", "_Data", "_Id", "_OthrClearTxtFrmt"]
	@property
	def ClearTxtFrmt(self):
		return self._ClearTxtFrmt

	@ClearTxtFrmt.setter
	def ClearTxtFrmt(self, value):
		self._ClearTxtFrmt = value if type(value) != base_types.auto else self.make_default("ClearTxtFrmt")

	@ClearTxtFrmt.deleter
	def ClearTxtFrmt(self):
		del self._ClearTxtFrmt
		self._ClearTxtFrmt = None

	@property
	def Data(self):
		return self._Data

	@Data.setter
	def Data(self, value):
		self._Data = value if type(value) != base_types.auto else self.make_default("Data")

	@Data.deleter
	def Data(self):
		del self._Data
		self._Data = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def OthrClearTxtFrmt(self):
		return self._OthrClearTxtFrmt

	@OthrClearTxtFrmt.setter
	def OthrClearTxtFrmt(self, value):
		self._OthrClearTxtFrmt = value if type(value) != base_types.auto else self.make_default("OthrClearTxtFrmt")

	@OthrClearTxtFrmt.deleter
	def OthrClearTxtFrmt(self):
		del self._OthrClearTxtFrmt
		self._OthrClearTxtFrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClearTxtFrmt', type=EncryptedDataFormat1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Data', type=EncryptedData2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrClearTxtFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))