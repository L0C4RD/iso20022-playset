# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import CryptographicKey19
from . import DataSetIdentification11
from . import Max140Binary
from . import Max5000Binary

class DataSetRequest7(base_types._BaseFieldType):

	__slots__ = ["_DlgtnProof", "_Id", "_POIChllng", "_PrtctdDlgtnProof", "_SsnKey", "_TMChllng"]
	@property
	def DlgtnProof(self):
		return self._DlgtnProof

	@DlgtnProof.setter
	def DlgtnProof(self, value):
		self._DlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

	@DlgtnProof.deleter
	def DlgtnProof(self):
		del self._DlgtnProof
		self._DlgtnProof = base_types.UninitialisedField(self, 'DlgtnProof', Max5000Binary, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', DataSetIdentification11, False)

	@property
	def POIChllng(self):
		return self._POIChllng

	@POIChllng.setter
	def POIChllng(self, value):
		self._POIChllng = value if value is not None else base_types.UninitialisedField(self, 'POIChllng', Max140Binary, False)

	@POIChllng.deleter
	def POIChllng(self):
		del self._POIChllng
		self._POIChllng = base_types.UninitialisedField(self, 'POIChllng', Max140Binary, False)

	@property
	def PrtctdDlgtnProof(self):
		return self._PrtctdDlgtnProof

	@PrtctdDlgtnProof.setter
	def PrtctdDlgtnProof(self, value):
		self._PrtctdDlgtnProof = value if value is not None else base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@PrtctdDlgtnProof.deleter
	def PrtctdDlgtnProof(self):
		del self._PrtctdDlgtnProof
		self._PrtctdDlgtnProof = base_types.UninitialisedField(self, 'PrtctdDlgtnProof', ContentInformationType39, False)

	@property
	def SsnKey(self):
		return self._SsnKey

	@SsnKey.setter
	def SsnKey(self, value):
		self._SsnKey = value if value is not None else base_types.UninitialisedField(self, 'SsnKey', CryptographicKey19, False)

	@SsnKey.deleter
	def SsnKey(self):
		del self._SsnKey
		self._SsnKey = base_types.UninitialisedField(self, 'SsnKey', CryptographicKey19, False)

	@property
	def TMChllng(self):
		return self._TMChllng

	@TMChllng.setter
	def TMChllng(self, value):
		self._TMChllng = value if value is not None else base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	@TMChllng.deleter
	def TMChllng(self):
		del self._TMChllng
		self._TMChllng = base_types.UninitialisedField(self, 'TMChllng', Max140Binary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtnProof', type=Max5000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=DataSetIdentification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdDlgtnProof', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnKey', type=CryptographicKey19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMChllng', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
	))